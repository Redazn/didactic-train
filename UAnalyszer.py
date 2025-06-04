import spacy
from ECalculator import EntropyCalculator

class UncertaintyAnalyzer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.nlp = spacy.load("id_core_news_sm")
        self.doc = self.nlp(input_text)
        self.entropy = EntropyCalculator.calculate_text_entropy(input_text)
        self.normalized_entropy = EntropyCalculator.normalize_entropy(self.entropy)
        self.entropy_level = EntropyCalculator.get_entropy_level(self.normalized_entropy)
        self.missing_elements = []
        
    def analyze_spok(self):
        """Analisis struktur SPOK dan identifikasi elemen yang hilang"""
        sentences = list(self.doc.sents)
        spok_reports = []
        
        for sent in sentences:
            elements = {"S": None, "P": None, "O": None, "K": None}
            for token in sent:
                if token.dep_ in ("nsubj", "nsubj:pass", "nsubj:outer"):
                    elements["S"] = token.text
                elif token.dep_ == "ROOT":
                    elements["P"] = token.text
                elif token.dep_ in ("obj", "iobj", "obl", "obj:outer"):
                    elements["O"] = token.text
                elif token.dep_ in ("advmod", "obl", "advcl", "compound"):
                    if not elements["K"]:
                        elements["K"] = []
                    elements["K"].append(token.text)
            
            # Ubah K menjadi string jika ada
            if elements["K"]:
                elements["K"] = " ".join(elements["K"])
            
            spok_reports.append(elements)
            
            # Deteksi elemen yang hilang
            missing = []
            if not elements["S"]:
                missing.append("Subjek")
            if not elements["P"]:
                missing.append("Predikat")
            if not elements["O"]:
                missing.append("Objek")
            if missing:
                self.missing_elements.append({
                    "sentence": sent.text,
                    "missing": missing
                })
            
        return spok_reports
    
    def generate_clarification_question(self):
        """Buat pertanyaan klarifikasi berdasarkan elemen yang hilang"""
        if not self.missing_elements:
            return ""
        
        questions = []
        for issue in self.missing_elements:
            missing_str = ", ".join(issue["missing"])
            questions.append(
                f"Pertanyaan '{issue['sentence']}' kurang {missing_str}. " +
                "Bisakah Anda memberikan detail lebih lanjut?"
            )
        
        return "\n\n".join(questions)
    
    def get_uncertainty_report(self):
        """Hasilkan laporan ketidakpastian untuk output"""
        report = f"🔍 ANALISIS KETIDAKPASTIAN (Entropy: {self.entropy:.2f} - {self.entropy_level.upper()})\n"
        
        if self.missing_elements:
            report += "Saya mendeteksi beberapa area yang membutuhkan klarifikasi:\n"
            for issue in self.missing_elements:
                report += f"- Kalimat: '{issue['sentence']}'\n"
                report += f"  Elemen kurang: {', '.join(issue['missing'])}\n"
        else:
            report += "Struktur pertanyaan cukup jelas, tapi ada beberapa aspek yang perlu dipertimbangkan:\n"
            
        # Tambahkan pertanyaan klarifikasi
        clarification = self.generate_clarification_question()
        if clarification:
            report += "\n❓ KLARIFIKASI DIBUTUHKAN:\n" + clarification
        
        return report