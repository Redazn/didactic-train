class DimensionAnalyzer:
    def __init__(self, cognitive_style, processing_style):
        self.cognitive_style = cognitive_style
        self.processing_style = processing_style
        
    @property
    def limitations(self):
        """Tentukan keterbatasan berdasarkan dimensi yang dipilih"""
        limitations = []
        
        if self.cognitive_style == 'Analytical':
            limitations.append("Feeling (Emosi subjektif)")
        else:
            limitations.append("Thinking (Analisis logis)")
            
        if self.processing_style == 'Structured':
            limitations.append("Perceiving (Eksplorasi terbuka)")
        else:
            limitations.append("Judging (Penilaian terstruktur)")
            
        return limitations
    
    def get_constraint_description(self):
        """Deskripsi keterbatasan untuk output"""
        return f"Keterbatasan AI: Kapasitas {', '.join(self.limitations)} berkurang"
    
    def apply_constraints(self, output_text):
        """Terapkan keterbatasan pada output (simulasi)"""
        # Dalam implementasi nyata, ini akan memengaruhi distribusi token LLM
        if self.cognitive_style == 'Analytical':
            return output_text.replace("saya merasa", "analisis menunjukkan")
        else:
            return output_text.replace("data menunjukkan", "saya merasakan")
