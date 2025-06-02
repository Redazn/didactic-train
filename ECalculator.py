import math
from collections import Counter

class EntropyCalculator:
    @staticmethod
    def calculate_text_entropy(text):
        """Menghitung entropy Shannon untuk teks input"""
        if not text:
            return 0.0
        
        char_counts = Counter(text)
        text_length = len(text)
        entropy = 0.0
        
        for count in char_counts.values():
            probability = count / text_length
            entropy -= probability * math.log2(probability)
            
        return entropy
    
    @staticmethod
    def normalize_entropy(entropy, max_possible=8):
        """Normalisasi entropy ke skala 0-1"""
        normalized = entropy / max_possible
        return min(normalized, 1.0)
    
    @staticmethod
    def get_entropy_level(normalized_entropy):
        """Kategorikan entropy ke dalam level"""
        if normalized_entropy < 0.3:
            return "low"
        elif normalized_entropy < 0.7:
            return "medium"
        else:
            return "high"
