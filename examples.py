############## CONTOH PENGGUNAAN ############

```
# ===========================================
# ENTROPY FRAMEWORK - SIMPLIFIED GEMINI INTEGRATION
# ===========================================

# Clone repo asli Anda
!git clone -q https://github.com/Redazn/didactic-train.git
%cd didactic-train

# Install hanya dependensi penting
!pip install -q google-generativeai

import os
import google.generativeai as genai
from ECalculator import EntropyCalculator
from RSelector import RoleSelector
from DAnalyzer import DimensionAnalyzer
import time

# ===== SETUP GEMINI =====
GEMINI_API_KEY = "!!!!!!!!"  # Ganti dengan API key Anda
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# ===== FUNGSI UTAMA YANG DIPERBAIKI =====
def generate_output(input_text, role, cognitive_style, processing_style):
    """Fungsi output yang dioptimalkan dengan Gemini"""
    # Buat prompt berdasarkan konfigurasi
    prompt = f"""
Anda adalah AI yang berperan sebagai {role}. 
Gunakan gaya {cognitive_style} dan pendekatan {processing_style}.

Pertanyaan: {input_text}

Jawablah dengan:
- Sesuai peran dan gaya yang ditentukan
- Fokus pada aspek utility dari jawaban
- Sertakan analisis singkat tentang keterbatasan pendekatan ini
"""
    
    # Generate response
    response = model.generate_content(prompt)
    return response.text

def entropy_framework_demo(questions):
    """Demo framework dengan perbandingan langsung"""
    print("="*60)
    print("ENTROPY FRAMEWORK DEMO - PERBANDINGAN OUTPUT")
    print("="*60)
    
    for i, question in enumerate(questions, 1):
        print(f"\n🔍 PERTANYAAN {i}: {question}")
        
        # Hitung entropy
        entropy = EntropyCalculator.calculate_text_entropy(question)
        norm_entropy = EntropyCalculator.normalize_entropy(entropy)
        entropy_level = EntropyCalculator.get_entropy_level(norm_entropy)
        
        # Pilih role dan dimensi
        selector = RoleSelector()
        role = selector.select_role(entropy_level)
        cognitive, processing = selector.select_dimensions(entropy_level)
        
        # Analisis keterbatasan
        analyzer = DimensionAnalyzer(cognitive, processing)
        limitations = analyzer.limitations
        
        print(f"\n📊 ANALISIS:")
        print(f"- Entropy: {entropy:.2f} ({entropy_level})")
        print(f"- Role: {role}")
        print(f"- Gaya: {cognitive}/{processing}")
        print(f"- Keterbatasan: {', '.join(limitations)}")
        
        # Hasilkan output dengan framework
        print("\n🤖 OUTPUT DENGAN FRAMEWORK:")
        framework_output = generate_output(question, role, cognitive, processing)
        print(framework_output)
        
        # Output tanpa framework (baseline)
        print("\n🔄 OUTPUT TANPA FRAMEWORK (BASELINE):")
        baseline_response = model.generate_content(question).text
        print(baseline_response)
        
        print("\n" + "="*60)

# ===== CONTOH PENGGUNAAN =====
if __name__ == "__main__":
    # Contoh pertanyaan dengan kompleksitas berbeda
    demo_questions = [
        "Apa gejala diabetes?",
        "Bagaimana cara mencegah diabetes?",
        "Apa dampak filosofis dari penyakit kronis seperti diabetes terhadap kehidupan manusia?"
    ]
    
    entropy_framework_demo(demo_questions)
    print("\n✅ DEMO SELESAI - PERBANDINGAN JELAS TERLIHAT")
```