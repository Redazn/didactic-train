import openai  # Untuk implementasi nyata

class OutputGenerator:
    def __init__(self, role, cognitive_style, processing_style):
        self.role = role
        self.cognitive_style = cognitive_style
        self.processing_style = processing_style
        
    def generate_prompt(self, input_text):
        """Buat prompt berdasarkan role dan dimensi"""
        role_context = {
            "Governance": "Anda adalah pakar tata kelola dan kebijakan",
            "Artist": "Anda adalah seniman kreatif",
            "Doctor": "Anda adalah dokter medis profesional",
            "Teacher": "Anda adalah pendidik berpengalaman",
            "Philosopher": "Anda adalah filsuf kontemplatif",
            "Engineer": "Anda adalah insinyur teknis",
            "Scientific": "Anda adalah ilmuwan riset",
            "Assistance": "Anda adalah asisten penolong"
        }
        
        style_context = {
            "Analytical": "Gunakan pendekatan logis dan berbasis data",
            "Emotive": "Sertakan pertimbangan emosional dan empati",
            "Structured": "Respons terstruktur dan sistematis (step by step)",
            "Exploratory": "Eksplorasi berbagai kemungkinan kreatif"
        }
        
        prompt = f"{role_context[self.role]}. {style_context[self.cognitive_style]}. "
        prompt += f"{style_context[self.processing_style]}. "
        prompt += f"Pertanyaan: {input_text}\nJawaban:"
        
        return prompt
    
    def generate_output(self, input_text):
        """Hasilkan output (simulasi untuk MVP)"""
        # Dalam implementasi nyata: ganti dengan panggilan ke LLM
        prompt = self.generate_prompt(input_text)
        
        # Simulasi output berdasarkan role
        responses = {
            "Governance": "Kebijakan yang efektif memerlukan pendekatan berbasis bukti...",
            "Artist": "Karya seni ini mengungkapkan emosi mendalam melalui...",
            "Doctor": "Dari perspektif medis, gejala tersebut menunjukkan...",
            "Teacher": "Konsep ini dapat diajarkan melalui tiga pendekatan utama...",
            "Philosopher": "Pertanyaan ini menyentuh hakikat eksistensi manusia...",
            "Engineer": "Solusi teknis optimal memerlukan analisis parameter berikut...",
            "Scientific": "Berdasarkan penelitian terbaru, hipotesis yang mungkin...",
            "Assistance": "Saya dapat membantu dengan beberapa opsi solusi..."
        }
        
        return responses.get(self.role, "Saya akan mencoba menjawab pertanyaan Anda.")
