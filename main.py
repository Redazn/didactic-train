from ECalculator import EntropyCalculator
from RSelector import RoleSelector
from DAnalyzer import DimensionAnalyzer
from OGenerator import OutputGenerator

def main():
    # Dapatkan input pengguna
    input_text = input("Masukkan pertanyaan/pernyataan: ")
    
    # Hitung entropy
    entropy = EntropyCalculator.calculate_text_entropy(input_text)
    normalized_entropy = EntropyCalculator.normalize_entropy(entropy)
    entropy_level = EntropyCalculator.get_entropy_level(normalized_entropy)
    
    print(f"\nEntropy Input: {entropy:.4f} (Level: {entropy_level})")
    
    # Pilih role dan dimensi
    selector = RoleSelector()
    selected_role = selector.select_role(entropy_level)
    cognitive_style, processing_style = selector.select_dimensions(entropy_level)
    
    print(f"Selected Role: {selected_role}")
    print(f"Cognitive Style: {cognitive_style}, Processing Style: {processing_style}")
    
    # Analisis dimensi dan keterbatasan
    dimension_analyzer = DimensionAnalyzer(cognitive_style, processing_style)
    print(dimension_analyzer.get_constraint_description())
    
    # Hasilkan output
    generator = OutputGenerator(selected_role, cognitive_style, processing_style)
    output = generator.generate_output(input_text)
    
    # Terapkan keterbatasan
    constrained_output = dimension_analyzer.apply_constraints(output)
    
    print("\n--- OUTPUT UTILITY ---")
    print(constrained_output)
    
    # Tampilkan transparansi
    print("\n--- TRANSPARANSI ---")
    print(f"Utility: Output dioptimalkan untuk {selected_role} dengan fokus {cognitive_style}-{processing_style}")
    print(f"Trade-off: Kapasitas terbatas pada {', '.join(dimension_analyzer.limitations)}")

if __name__ == "__main__":
    main()
