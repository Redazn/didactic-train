import re

class UncertaintyAnalyzer:
    @staticmethod
    def analyze_uncertainty(text):
        """Analisis ketidakpastian dengan metode yang lebih sederhana"""
        tokens = re.findall(r'\b\w+\b', text.lower())
        
        if not tokens:
            return 0.0
            
        unique_count = len(set(tokens))
        total_count = len(tokens)
        uncertainty = unique_count / total_count
        
        return uncertainty

    @staticmethod
    def normalize_uncertainty(uncertainty):
        """Normalisasi nilai ketidakpastian ke range 0-1"""
        return min(max(uncertainty, 0.0), 1.0)