import os
from UncertaintyAnalyzer import UncertaintyAnalyzer

class OutputGenerator:
    def __init__(self, role, cognitive_style, processing_style):
        self.role = role
        self.cognitive_style = cognitive_style
        self.processing_style = processing_style
        
 
    def generate_prompt(self, input_text):
        """Generate system prompt untuk Gemini"""
        role_context = {
            "Governance": "Anda adalah pakar tata kelola dan kebijakan publik",
            "Artist": "Anda adalah seniman kreatif",
            "Doctor": "Anda adalah dokter medis profesional",
            "Teacher": "Anda adalah pendidik berpengalaman",
            "Philosopher": "Anda adalah filsuf kontemplatif",
            "Engineer": "Anda adalah insinyur teknis",
            "Scientific": "Anda adalah ilmuwan riset",
            "Assistance": "Anda adalah asisten AI yang membantu"
        }
        
        style_context = {
            "Analytical": "Gunakan pendekatan logis dan berbasis data",
            "Emotive": "Sertakan pertimbangan emosional dan empati",
            "Structured": "Berikan respons yang terstruktur dan sistematis",
            "Exploratory": "Eksplorasi berbagai kemungkinan dan perspektif"
        }
        
        system_prompt = f"""{role_context[self.role]}

GAYA RESPONS:
- {style_context[self.cognitive_style]}
- {style_context[self.processing_style]}

Pertanyaan: {input_text}

Jawablah dalam bahasa Indonesia yang natural dan:
1. Berikan jawaban utama yang informatif
2. Akhiri dengan analisis ketidakpastian dan permintaan klarifikasi jika perlu
"""
        
        return system_prompt
        
    def generate_output(self, input_text):
        """Generate output menggunakan Gemini atau fallback"""
        # Analisis ketidakpastian
        uncertainty_analyzer = UncertaintyAnalyzer(input_text)
        uncertainty_report = uncertainty_analyzer.get_uncertainty_report()
        
        if self.use_generator:
            try:
                prompt = self.generate_prompt(input_text)
                response = self.model.generate_content(
                    prompt,
                    generation_config=self.generation_config
                )
                
                if response.candidates and response.candidates[0].content.parts:
                    output = response.candidates[0].content.parts[0].text.strip()
                    return f"{output}\n\n{uncertainty_report}"
                else:
                    return f"Maaf, tidak dapat menghasilkan respons.\n\n{uncertainty_report}"
                    
            except Exception as e:
                print(f"⚠️ Gemini API Error: {e}")
                return self._fallback_response(input_text, uncertainty_report)
        else:
            return self._fallback_response(input_text, uncertainty_report)
    
    def _fallback_response(self, input_text, uncertainty_report):
        """Fallback responses jika Gemini tidak tersedia"""
        responses = {
            "Governance": f"Sebagai pakar tata kelola, saya akan menganalisis '{input_text}'...",
            "Artist": f"Dari sudut pandang artistik, '{input_text}'...",
            "Doctor": f"Secara medis, pertanyaan tentang '{input_text}'...",
            "Teacher": f"Sebagai pendidik, saya akan menjelaskan '{input_text}'...",
            "Philosopher": f"Pertanyaan '{input_text}' membawa kita pada refleksi...",
            "Engineer": f"Dari perspektif teknis, '{input_text}'...",
            "Scientific": f"Berdasarkan pendekatan ilmiah, '{input_text}'...",
            "Assistance": f"Saya akan membantu menjawab '{input_text}'..."
        }
        
        base_response = responses.get(self.role, f"Terima kasih atas pertanyaan tentang '{input_text}'.")
        
        # Add style-specific elements
        if self.cognitive_style == 'Analytical':
            base_response += " Mari kita analisis secara sistematis."
        elif self.cognitive_style == 'Emotive':
            base_response += " Mari kita pertimbangkan aspek emosionalnya."
            
        if self.processing_style == 'Structured':
            base_response += " Saya akan menyajikan informasi secara terstruktur."
        elif self.processing_style == 'Exploratory':
            base_response += " Mari kita eksplorasi berbagai kemungkinan."
            
        return f"{base_response}\n\n{uncertainty_report}"