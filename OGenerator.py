from UAnalyszer import UncertaintyAnalyzer

class OutputGenerator:
    def __init__(self, role, cognitive_style, processing_style):
        self.role = role
        self.cognitive_style = cognitive_style
        self.processing_style = processing_style
        self.memory = PFTCognitiveMemory()
        self.uncertainty_analyzer = UncertaintyAnalyzer()
    
    def generate_output(self, input_text, model_generator):
        # Analisis input
        uncertainty = self.uncertainty_analyzer.analyze_uncertainty(input_text)
        
        # Aktifkan konteks saat ini di STM
        current_context = self.create_context(input_text, uncertainty)
        self.memory.activate_context(current_context)
        
        # Lakukan fusi memori
        fused_state = self.memory.pft_fusion_operator()
        
        if fused_state:
            emergence_index = self.memory.calculate_emergence_index(fused_state)
            
            # Bangun prompt dengan pengetahuan emergen
            prompt = self.create_prompt(
                input_text, 
                fused_state['meaning'], 
                emergence_index
            )
        else:
            # Fallback jika tidak ada memori yang relevan
            prompt = self.create_prompt(input_text, "", 0)
        
        response = model_generator(prompt)
        
        # Evaluasi dan simpan pengalaman
        performance = self.evaluate_response(response, input_text)
        self.memory.store_experience(
            key=f"exp_{int(time.time())}",
            experience={
                'state': current_context['state'],
                'meaning': current_context['meaning'],
                'performance': performance
            }
        )
        
        return response + f"\n\n[Emergence Index: {emergence_index:.2f}]"
    
    def create_context(self, input_text, uncertainty):
        """Membuat representasi konteks saat ini"""
        return {
            'state': self.text_to_vector(input_text),
            'meaning': self.extract_key_meaning(input_text),
            'uncertainty': uncertainty
        }
    
    def text_to_vector(self, text):
        """Konversi teks ke vektor keadaan (sederhana)"""
        # Dalam implementasi nyata, gunakan embedding
        return [len(text), text.count('?'), len(text.split())]
    
    def extract_key_meaning(self, text):
        """Ekstraksi makna kunci (sederhana)"""
        # Bisa ditingkatkan dengan teknik NLP
        keywords = ["apa", "siapa", "kenapa", "mengapa", "bagaimana", "kapan"]
        return " ".join([word for word in text.split() if word in keywords])
    
    def create_prompt(self, input_text, fused_meaning, emergence_index):
        """Membuat prompt dengan integrasi pengetahuan emergen"""
        base_prompt = f"Pertanyaan: {input_text}\n\n"
        
        if emergence_index > 0.1:
            knowledge_integration = (
                "PENGETAHUAN TERINTEGRASI:\n"
                f"{fused_meaning}\n\n"
                f"Gunakan pengetahuan di atas untuk memberikan jawaban yang lebih mendalam."
            )
        else:
            knowledge_integration = ""
        
        return (
            f"Anda adalah {self.role}. {self.get_role_context()}\n\n"
            f"{knowledge_integration}\n\n"
            "Jawablah pertanyaan berikut dengan gaya:\n"
            f"- {self.cognitive_style}\n"
            f"- {self.processing_style}\n\n"
            f"{base_prompt}"
        )
    
    def evaluate_response(self, response, input_text):
        """Evaluasi kualitas respons (sederhana)"""
        # Metrik: panjang respons, kesesuaian dengan pertanyaan
        relevance = 1 - cosine(
            self.get_embedding(input_text),
            self.get_embedding(response)
        )
        return len(response) * relevance