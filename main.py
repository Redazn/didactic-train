from ECalculator import EntropyCalculator
from RSelector import RoleSelector
from OGenerator import OutputGenerator
import google.generativeai as genai
import json
import os
import numpy as np

# ===================================================
# MODEL INTEGRATION BRIDGE (Fully Modular)
# ===================================================
class ModelGenerator:
    @staticmethod
    def setup_generator(model_type, **kwargs):
        """Factory method untuk membuat model generator"""
        if model_type == "gemini":
            return ModelGenerator.create_gemini_generator(
                kwargs.get("api_key"),
                kwargs.get("model_name", "gemini-1.5-flash")
            )
        elif model_type == "openai":
            return ModelGenerator.create_openai_generator(
                kwargs.get("api_key"),
                kwargs.get("model_name", "gpt-4-turbo")
            )
        elif model_type == "transformers":
            return ModelGenerator.create_transformers_generator(
                kwargs.get("model_name", "gpt2"),
                kwargs.get("device", -1)
            )
        elif model_type == "rest_api":
            return ModelGenerator.create_restapi_generator(
                kwargs.get("api_url"),
                kwargs.get("headers", {}),
                kwargs.get("payload_template", {"prompt": "{prompt}"})
            )
        elif model_type == "echo":
            return lambda prompt: f"ECHO: {prompt}"
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

    @staticmethod
    def create_gemini_generator(api_key, model_name):
        import google.generativeai as genai
        if not api_key:
            raise ValueError("Gemini API key not provided")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        def generator(prompt):
            response = model.generate_content(prompt)
            if response.candidates and response.candidates[0].content.parts:
                return response.candidates[0].content.parts[0].text.strip()
            return "Maaf, tidak dapat menghasilkan respons."
        return generator

    @staticmethod
    def create_openai_generator(api_key, model_name):
        from openai import OpenAI
        if not api_key:
            raise ValueError("OpenAI API key not provided")
        client = OpenAI(api_key=api_key)

        def generator(prompt):
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=600,
                temperature=0.5
            )
            return response.choices[0].message.content.strip()
        return generator

    @staticmethod
    def create_transformers_generator(model_name, device):
        from transformers import pipeline
        generator = pipeline(
            "text-generation",
            model=model_name,
            device=device
        )

        def generate_func(prompt):
            output = generator(
                prompt,
                max_length=300,
                num_return_sequences=1,
                temperature=0.7
            )
            return output[0]['generated_text'].strip()
        return generate_func

    @staticmethod
    def create_restapi_generator(api_url, headers, payload_template):
        import requests

        def generator(prompt):
            payload = {}
            for key, value in payload_template.items():
                if isinstance(value, str):
                    payload[key] = value.format(prompt=prompt)
                else:
                    payload[key] = value

            response = requests.post(
                api_url,
                headers=headers,
                json=payload
            )

            if response.status_code != 200:
                return f"⚠️ API error: {response.status_code} - {response.text}"

            return response.text
        return generator

# ===================================================
# MAIN APPLICATION
# ===================================================
def load_config():
    try:
        with open('config.json') as f:
            return json.load(f)
    except:
        print("⚠️ Using default configuration")
        return {
            "roles": ["Assistance"],
            "role_weights": {"low": [1], "medium": [1], "high": [1]},
            "dimension_weights": {"low": {}, "medium": {}, "high": {}}
        }

def print_header():
    print("🤖 " + "="*50)
    print("    SISTEM AI DENGAN ANALISIS KETIDAKPASTIAN")
    print("    Framework Entropy-Utility Modular")
    print("="*52)

def print_analysis(entropy, entropy_level, role, cognitive_style, processing_style):
    print("\n🔬 ANALISIS INPUT:")
    print(f"   Entropy: {entropy:.2f} ({entropy_level.upper()})")
    print(f"   Role: {role}")
    print(f"   Gaya Kognitif: {cognitive_style}")
    print(f"   Gaya Pemrosesan: {processing_style}")

def select_model_type():
    """Interaktif pemilihan model"""
    print("\n🔧 Pilih jenis model:")
    print("1. Gemini (Google AI)")
    print("2. OpenAI")
    print("3. Transformers (Hugging Face)")
    print("4. REST API")
    print("5. Echo (Test Mode)")

    choice = input("Masukkan pilihan (1-5): ").strip()
    options = {
        "1": "gemini",
        "2": "openai",
        "3": "transformers",
        "4": "rest_api",
        "5": "echo"
    }
    return options.get(choice, "echo")

def get_model_config(model_type):
    """Dapatkan konfigurasi berdasarkan jenis model"""
    config = {}

    if model_type == "gemini":
        config["api_key"] = input("Masukkan Gemini API key: ").strip()
        config["model_name"] = input("Model name [gemini-1.5-flash]: ").strip() or "gemini-1.5-flash"

    elif model_type == "openai":
        config["api_key"] = input("Masukkan OpenAI API key: ").strip()
        config["model_name"] = input("Model name [gpt-4-turbo]: ").strip() or "gpt-4-turbo"

    elif model_type == "transformers":
        config["model_name"] = input("Model name [gpt2]: ").strip() or "gpt2"
        config["device"] = int(input("Device (-1=CPU, 0=GPU) [-1]: ").strip() or -1)

    elif model_type == "rest_api":
        config["api_url"] = input("Masukkan API URL: ").strip()

        headers = {}
        print("\nMasukkan headers (format: key:value, kosongkan untuk selesai)")
        while True:
            header = input("Header: ").strip()
            if not header: break
            if ":" in header:
                key, value = header.split(":", 1)
                headers[key.strip()] = value.strip()

        config["headers"] = headers
        config["payload_template"] = {"prompt": "{prompt}"}  # Default

    return config

def main():
    config = load_config()
    print_header()

    model_type = select_model_type()
    model_config = get_model_config(model_type)

    try:
        model_generator = ModelGenerator.setup_generator(model_type, **model_config)
        print(f"✅ Model {model_type.upper()} berhasil diinisialisasi")
    except Exception as e:
        print(f"❌ Failed to setup model: {str(e)}")
        print("🔄 Using fallback echo generator")
        model_generator = lambda prompt: f"ECHO: {prompt}"

    # =============================================
    # 🔥 Inisialisasi PFT Fusion Controller
    # =============================================
    pft_controller = EntropyCalculator.PFTFusion(
        temperature=0.65,
        window_size=5
    )

    while True:
        try:
            print("\n" + "="*50)
            input_text = input("🤔 Masukkan pertanyaan/pernyataan (atau 'quit' untuk keluar): ")

            if input_text.lower() in ['quit', 'exit', 'keluar', 'q']:
                print("\n👋 Terima kasih telah menggunakan sistem AI ini!")
                break

            if not input_text.strip():
                print("❌ Input tidak boleh kosong!")
                continue

            print("\n🔄 Menganalisis struktur dan ketidakpastian...")

            # Hitung entropy dasar
            entropy = EntropyCalculator.calculate_text_entropy(input_text)
            normalized_entropy = EntropyCalculator.normalize_entropy(entropy)
            entropy_level = EntropyCalculator.get_entropy_level(normalized_entropy)

            # =============================================
            # 🧠 ANALISIS KOMPLEKSITAS TINGKAT LANJUT
            # =============================================
            cognitive_depth = EntropyCalculator.estimate_cognitive_depth(input_text)
            abstraction_level = EntropyCalculator.detect_abstraction_level(input_text)

            # Update PFT controller dengan nilai kompleksitas
            fusion_value = pft_controller.fuse(cognitive_depth, abstraction_level)

            # Deteksi risiko reasoning collapse
            collapse_risk = cognitive_depth > 0.7 and abstraction_level > 0.6

            # Pilih role dan dimensi
            selector = RoleSelector(config)
            selected_role = selector.select_role(entropy_level)
            cognitive_style, processing_style = selector.select_dimensions(entropy_level)

            # =============================================
            # 🚀 ADAPTIVE PROMPT ENGINEERING
            # =============================================
            # Tambahkan instruksi khusus berdasarkan analisis fusion
            system_note = ""
            if fusion_value > 0.4:
                system_note = " [Gunakan pendekatan terstruktur dan solusi konkret]"
            elif fusion_value < -0.4:
                system_note = " [Eksplorasi berbagai perspektif dan kemungkinan solusi]"

            if collapse_risk:
                system_note += " ⚠️[HINDARI HALUSINASI - FAKTA SAJA]"

            input_text += system_note

            # Print analysis (ditambah info baru)
            print("\n🔬 ANALISIS INPUT LANJUTAN:")
            print(f"   Entropy: {entropy:.2f} ({entropy_level.upper()})")
            print(f"   Kedalaman Kognitif: {cognitive_depth:.2f}")
            print(f"   Level Abstraksi: {abstraction_level:.2f}")
            print(f"   Nilai Fusion: {fusion_value:.2f}")
            print(f"   Risiko Reasoning Collapse: {'YA' if collapse_risk else 'TIDAK'}")
            print(f"   Role: {selected_role}")
            print(f"   Gaya Kognitif: {cognitive_style}")
            print(f"   Gaya Pemrosesan: {processing_style}")

            print("\n🤖 Membuat respons...")

            # Hasilkan output seperti biasa
            generator = OutputGenerator(selected_role, cognitive_style, processing_style)
            output = generator.generate_output(input_text, model_generator)

            print("\n💬 " + "="*50)
            print(output)
            print("="*52)

            # =============================================
            # 📈 POST-RESPONSE ANALYSIS
            # =============================================
            # Hitung uncertainty dari output
            output_uncertainty = EntropyCalculator.calculate_text_entropy(output)
            print(f"\n📊 POST-ANALYSIS:")
            print(f"   Output Entropy: {output_uncertainty:.2f}")
            print(f"   Meta-Entropy Window: {pft_controller.entropy_window[-3:]}")

        except KeyboardInterrupt:
            print("\n\n👋 Program dihentikan. Sampai jumpa!")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {str(e)}")
            print("🔄 Silakan coba lagi...")
            continue

if __name__ == "__main__":
    main()