import numpy as np
from scipy.spatial.distance import cosine

class PFTCognitiveMemory:
    def __init__(self):
        self.short_term = {}  # Memori jangka pendek (konteks saat ini)
        self.long_term = {}   # Memori jangka panjang (pengalaman)
        self.theta_params = {'weight_STM': 0.6, 'weight_LTM': 0.4}
        self.phi_threshold = 0.65  # Ambang integrasi
    
    def store_experience(self, key, experience):
        """Menyimpan pengalaman ke memori jangka panjang"""
        self.long_term[key] = {
            'state': experience['state'],
            'meaning': experience['meaning'],
            'performance': experience['performance']
        }
    
    def activate_context(self, context):
        """Mengaktifkan konteks saat ini di memori jangka pendek"""
        self.short_term = context
    
    def pft_fusion_operator(self):
        """
        Mengaplikasikan operator fusi PFT pada memori
        Mengembalikan keadaan emergent
        """
        if not self.short_term or not self.long_term:
            return None
        
        # Temukan pengalaman paling relevan di LTM
        ltm_key, ltm_experience = self.find_most_relevant()
        
        # Hitung keselarasan semantik
        alignment_score = self.calculate_semantic_alignment(
            self.short_term['meaning'],
            ltm_experience['meaning']
        )
        
        # Hitung kekuatan interaksi
        interaction_strength = 1 - cosine(
            self.short_term['state'],
            ltm_experience['state']
        )
        
        # Hitung bobot fusi
        alpha_STM = self.theta_params['weight_STM'] * alignment_score
        alpha_LTM = self.theta_params['weight_LTM'] * alignment_score
        beta = self.phi_threshold * interaction_strength
        
        # Normalisasi
        total_weight = alpha_STM + alpha_LTM + beta
        weights = {
            'STM': alpha_STM / total_weight,
            'LTM': alpha_LTM / total_weight,
            'emergence': beta / total_weight
        }
        
        # Fusi keadaan
        fused_state = (
            weights['STM'] * np.array(self.short_term['state']) +
            weights['LTM'] * np.array(ltm_experience['state']) +
            weights['emergence'] * self.semantic_interaction(
                self.short_term['state'],
                ltm_experience['state']
            )
        )
        
        return {
            'state': fused_state.tolist(),
            'meaning': self.coherent_meaning(
                self.short_term['meaning'],
                ltm_experience['meaning']
            ),
            'weights': weights,
            'source': (id(self.short_term), ltm_key)
        }
    
    def calculate_emergence_index(self, fused_state):
        """
        Menghitung indeks emergensi berdasarkan performa
        """
        stm_perf = self.evaluate_performance(self.short_term['state'])
        ltm_perf = self.evaluate_performance(
            self.long_term[self.find_most_relevant()[0]]['state']
        )
        fused_perf = self.evaluate_performance(fused_state['state'])
        
        max_individual = max(stm_perf, ltm_perf)
        emergence_index = (fused_perf - max_individual) / max_individual
        
        # Simpan pengalaman emergen jika cukup signifikan
        if emergence_index > 0.15:
            self.store_experience(
                key=f"emergent_{int(time.time())}",
                experience={
                    'state': fused_state['state'],
                    'meaning': fused_state['meaning'],
                    'performance': fused_perf
                }
            )
        
        return emergence_index
    
    def find_most_relevant(self):
        """Mencari pengalaman paling relevan di LTM"""
        best_key = None
        best_score = -1
        
        for key, exp in self.long_term.items():
            score = self.calculate_semantic_alignment(
                self.short_term['meaning'],
                exp['meaning']
            )
            if score > best_score:
                best_score = score
                best_key = key
        
        return best_key, self.long_term[best_key]
    
    def calculate_semantic_alignment(self, meaning_A, meaning_B):
        """Menghitung keselarasan semantik antara dua makna"""
        # Implementasi sederhana: cosine similarity dari embedding
        return 1 - cosine(
            self.get_embedding(meaning_A),
            self.get_embedding(meaning_B)
        )
    
    def semantic_interaction(self, state_A, state_B):
        """Interaksi semantik menciptakan keadaan baru"""
        # Operasi khusus domain - contoh untuk NLP
        return (np.array(state_A) * np.array(state_B)) / (np.linalg.norm(state_A) * np.linalg.norm(state_B))
    
    def coherent_meaning(self, meaning_A, meaning_B):
        """Menciptakan makna koheren dari dua input"""
        # Gabungkan elemen unik dari kedua makna
        combined = list(set(meaning_A.split() + meaning_B.split()))
        return " ".join(sorted(combined))
    
    def get_embedding(self, text):
        """Embedding teks sederhana (bisa diganti dengan model canggih)"""
        # Implementasi dummy - dalam praktek gunakan model embedding
        return np.random.rand(100)
    
    def evaluate_performance(self, state):
        """Evaluasi performa keadaan (domain spesifik)"""
        # Contoh: norm dari keadaan sebagai proxy performa
        return np.linalg.norm(state)