import math
import numpy as np
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
    
    # =============================================
    # 🔥 PFT FUSION INTEGRATION
    # =============================================
    class PFTFusion:
        def __init__(self, temperature=0.5, window_size=10):
            self.T = temperature  # Parameter kontrol "exploration vs exploitation"
            self.entropy_window = []  # Penyimpanan histori entropy
            self.window_size = window_size  # Ukuran moving window

        def update_entropy(self, value):
            """Update window dengan nilai entropy baru"""
            self.entropy_window.append(value)
            if len(self.entropy_window) > self.window_size:
                self.entropy_window.pop(0)

        def compute_window_entropy(self):
            """Hitung entropy dari histori entropy (meta-entropy)"""
            if len(self.entropy_window) < 2:
                return 0
            
            # Normalisasi nilai absolut
            abs_values = np.abs(self.entropy_window)
            total = np.sum(abs_values)
            if total == 0:
                return 0
                
            p = abs_values / total
            return -np.sum(p * np.log(p + 1e-10))  # Shannon entropy + stabilizer

        def fuse(self, a, b):
            """
            Fusion dua nilai dengan pertimbangan entropy historis.
            Formula: F = (a - b) - T * H(histori)
            """
            self.update_entropy(a)
            meta_entropy = self.compute_window_entropy()
            F = (a - b) - self.T * meta_entropy
            return np.tanh(F)  # Normalisasi [-1, 1]
        
        def dynamic_threshold(self):
            """Threshold adaptif berdasarkan moving average"""
            if len(self.entropy_window) < 3:
                return 0.5
            return np.mean(self.entropy_window) * 0.7

    # =============================================
    # 🧠 ADVANCED COMPLEXITY ESTIMATORS
    # =============================================
    @staticmethod
    def estimate_cognitive_depth(text):
        """Estimasi kedalaman kognitif teks"""
        # Heuristik: hitung density kata kunci kompleksitas
        complexity_indicators = ["mengapa", "bagaimana", "solusi", "analisis",
                                "perbandingan", "dampak", "strategi"]
        words = text.lower().split()
        
        if not words:
            return 0
            
        count = sum(1 for word in words if word in complexity_indicators)
        return min(count / len(words), 1.0)
    
    @staticmethod
    def detect_abstraction_level(text):
        """Deteksi level abstraksi berdasarkan indikator linguistik"""
        abstract_indicators = ["secara umum", "prinsipnya", "pada dasarnya",
                              "konsep", "filosofi", "paradigma"]
        concrete_indicators = ["contoh", "langkah", "praktek", "implementasi",
                              "teknis", "instruksi"]
        
        abstract_count = sum(text.lower().count(phrase) for phrase in abstract_indicators)
        concrete_count = sum(text.lower().count(phrase) for phrase in concrete_indicators)
        
        total = abstract_count + concrete_count
        if total == 0:
            return 0.5  # Netral
            
        return abstract_count / total  # 0=konkret, 1=abstrak