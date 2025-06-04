from UncertaintyAnalyszer import UncertaintyAnalyzer

class OutputGenerator:
    """Modular output generator framework"""
    def __init__(self, role, cognitive_style, processing_style):
        self.role = role
        self.cognitive_style = cognitive_style
        self.processing_style = processing_style
    
    def create_prompt(self, input_text):
        """Create standardized prompt template"""
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
        
        return f"""{role_context.get(self.role, 'Anda adalah asisten AI')}

GAYA RESPONS:
- {style_context.get(self.cognitive_style, 'Gunakan pendekatan logis')}
- {style_context.get(self.processing_style, 'Berikan respons yang informatif')}

Pertanyaan: {input_text}

Jawablah dalam bahasa Indonesia yang natural dan:
1. Berikan jawaban utama yang informatif
2. Akhiri dengan analisis ketidakpastian jika perlu
"""
    
    def generate_output(self, input_text, model_generator):
        """
        Generate output using external model generator
        
        Parameters:
        input_text (str): User input
        model_generator (callable): Function that takes prompt and returns response
        
        Returns:
        str: Complete output with uncertainty analysis
        """
        # Create prompt
        prompt = self.create_prompt(input_text)
        
        # Generate response using external model
        try:
            response = model_generator(prompt)
        except Exception as e:
            response = f"⚠️ Error in model generation: {str(e)}"
        
        # Add uncertainty analysis
        uncertainty_analyzer = UncertaintyAnalyzer(input_text)
        uncertainty_report = uncertainty_analyzer.get_uncertainty_report()
        
        return f"{response}\n\n{uncertainty_report}"