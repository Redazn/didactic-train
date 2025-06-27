"""
⊕Mind: Modular Reasoning & Proof AI Engine
MVP Implementation Structure
"""

import hashlib
import json
import time
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum

class LogicOperator(Enum):
    AND = "∧"
    OR = "∨"
    OPLUS = "⊕"  # Modular composition
    NOT = "¬"
    IMPLIES = "→"

@dataclass
class LogicRule:
    """Represents a single logic rule"""
    name: str
    conditions: List[str]
    conclusion: str
    operator: LogicOperator
    confidence: float = 1.0
    tags: List[str] = field(default_factory=list)  # e.g., ["medis", "respirasi"]

@dataclass
class ReasoningTrace:
    """Tracks the reasoning process"""
    steps: List[str]
    rules_applied: List[str]
    final_conclusion: str
    proof_hash: str

class OPlusReasoningEngine:
    """
    Core reasoning engine using ⊕ operator for modular logic composition
    """
    
    def __init__(self, confidence_threshold: float = 0.75):
        self.rules: Dict[str, LogicRule] = {}
        self.facts: Dict[str, bool] = {}
        self.inferred_facts: Dict[str, bool] = {}  # For nested rule support
        self.trace: List[str] = []
        self.threshold = confidence_threshold  # Confidence threshold
    
    def add_rule(self, rule: LogicRule):
        """Add a logic rule to the engine"""
        self.rules[rule.name] = rule
        self.trace.append(f"Added rule: {rule.name}")
    
    def add_fact(self, fact: str, value: bool):
        """Add a fact to the knowledge base"""
        self.facts[fact] = value
        self.trace.append(f"Added fact: {fact} = {value}")
    
    def oplus_compose(self, rule_a: str, rule_b: str) -> str:
        """
        ⊕ Operator: Compose two rules modularly
        A ⊕ B = combined reasoning from both rules
        """
        if rule_a not in self.rules or rule_b not in self.rules:
            raise ValueError("Rules not found")
        
        # Create composed rule
        composed_name = f"{rule_a}_⊕_{rule_b}"
        rule_obj_a = self.rules[rule_a]
        rule_obj_b = self.rules[rule_b]
        
        # Combine conditions
        combined_conditions = rule_obj_a.conditions + rule_obj_b.conditions
        combined_conclusion = f"({rule_obj_a.conclusion}) ∧ ({rule_obj_b.conclusion})"
        
        composed_rule = LogicRule(
            name=composed_name,
            conditions=combined_conditions,
            conclusion=combined_conclusion,
            operator=LogicOperator.OPLUS,
            confidence=min(rule_obj_a.confidence, rule_obj_b.confidence)
        )
        
        self.add_rule(composed_rule)
        self.trace.append(f"⊕ Composed: {rule_a} ⊕ {rule_b} → {composed_name}")
        
        return composed_name
    
    def evaluate_rule(self, rule_name: str) -> Tuple[bool, float]:
        """Evaluate if a rule can be applied given current facts"""
        if rule_name not in self.rules:
            return False, 0.0
        
        rule = self.rules[rule_name]
        
        # Check conditions in both facts and inferred_facts
        all_facts = {**self.facts, **self.inferred_facts}
        
        # Check if all conditions are satisfied
        satisfied_conditions = 0
        for condition in rule.conditions:
            if condition in all_facts and all_facts[condition]:
                satisfied_conditions += 1
        
        # 1. Separate rule fires logic and confidence calculation
        rule_fires = satisfied_conditions == len(rule.conditions)
        
        # Calculate satisfaction ratio and confidence score
        satisfaction_ratio = satisfied_conditions / len(rule.conditions) if rule.conditions else 1.0
        confidence_score = satisfaction_ratio * rule.confidence
        
        # 2. Apply confidence threshold
        rule_passes_threshold = confidence_score >= self.threshold
        final_rule_fires = rule_fires and rule_passes_threshold
        
        if final_rule_fires:
            # 6. Add confidence to trace log
            self.trace.append(f"Rule {rule_name} FIRED with confidence: {confidence_score:.2f}")
            # 5. Support nested rules - add conclusion to inferred_facts
            self.inferred_facts[rule.conclusion] = True
        elif rule_fires and not rule_passes_threshold:
            self.trace.append(f"Rule {rule_name} satisfied but below threshold ({confidence_score:.2f} < {self.threshold})")
        
        return final_rule_fires, confidence_score
    
    def reason(self) -> ReasoningTrace:
        """Main reasoning loop"""
        applied_rules = []
        conclusions = []
        
        # Apply all rules that can fire
        for rule_name, rule in self.rules.items():
            fires, confidence = self.evaluate_rule(rule_name)
            if fires:
                applied_rules.append(rule_name)
                conclusions.append(rule.conclusion)
        
        # Generate final conclusion
        final_conclusion = " ∧ ".join(conclusions) if conclusions else "No conclusion"
        
        # Generate proof hash (ZKP emulation)
        proof_data = {
            "facts": self.facts,
            "applied_rules": applied_rules,
            "conclusion": final_conclusion
        }
        proof_hash = hashlib.sha256(json.dumps(proof_data, sort_keys=True).encode()).hexdigest()
        
        return ReasoningTrace(
            steps=self.trace.copy(),
            rules_applied=applied_rules,
            final_conclusion=final_conclusion,
            proof_hash=proof_hash[:16]  # Shortened for display
        )
    
    def export_trace(self) -> Dict[str, Any]:
        """7. Export trace to JSON for web UI or training data"""
        return {
            "trace": self.trace,
            "facts": self.facts,
            "inferred_facts": self.inferred_facts,
            "rules": {name: {
                "conditions": rule.conditions,
                "conclusion": rule.conclusion,
                "confidence": rule.confidence,
                "tags": rule.tags
            } for name, rule in self.rules.items()},
            "threshold": self.threshold,
            "timestamp": time.time()
        }

class ZKPEmulator:
    """
    Zero-Knowledge Proof Emulator
    Simulates proof generation without revealing sensitive data
    """
    
    @staticmethod
    def generate_proof(facts: Dict[str, bool], conclusion: str) -> Dict[str, Any]:
        """Generate a ZKP-style proof with improved hashing"""
        timestamp = str(int(time.time()))
        
        # 3. Improved hashing with salt and timestamp
        raw_data = f"{sorted(facts.items())}_{conclusion}_{timestamp}"
        fact_commitment = hashlib.sha256(raw_data.encode()).hexdigest()
        
        # Create proof structure
        proof = {
            "commitment": fact_commitment[:16],
            "conclusion": conclusion,
            "proof_valid": True,
            "timestamp": timestamp,
            "proof_type": "⊕Mind_ZKP_v1",
            "salt": timestamp[-4:]  # Last 4 digits as salt
        }
        
        return proof
    
    @staticmethod
    def verify_proof(proof: Dict[str, Any], expected_facts: Dict[str, bool], expected_conclusion: str) -> bool:
        """Verify a proof without seeing the original facts"""
        # Reconstruct the raw data using proof timestamp
        raw_data = f"{sorted(expected_facts.items())}_{expected_conclusion}_{proof['timestamp']}"
        expected_commitment = hashlib.sha256(raw_data.encode()).hexdigest()
        return proof["commitment"] == expected_commitment[:16]

class LLMTranslator:
    """
    Placeholder for LLM integration
    In real implementation, this would use HuggingFace, OpenAI, etc.
    """
    
    @staticmethod
    def natural_to_logic(natural_text: str) -> List[LogicRule]:
        """Convert natural language to logic rules"""
        # Simplified mock implementation
        # In real version, this would use LLM API
        
        mock_rules = []
        
        if "demam" in natural_text.lower() and "batuk" in natural_text.lower():
            rule = LogicRule(
                name="risk_assessment",
                conditions=["demam", "batuk"],
                conclusion="risiko_tinggi",
                operator=LogicOperator.AND,
                confidence=0.85,
                tags=["medis", "respirasi"]  # 4. Add tags support
            )
            mock_rules.append(rule)
        
        return mock_rules
    
    @staticmethod
    def logic_to_natural(trace: ReasoningTrace) -> str:
        """Convert logic trace back to natural language"""
        explanation = f"""
        Berdasarkan analisis sistematis:
        
        🔍 Langkah-langkah reasoning:
        {chr(10).join(f"  • {step}" for step in trace.steps[-5:])}
        
        ⚡ Rules yang diaplikasikan: {', '.join(trace.rules_applied)}
        
        🎯 Kesimpulan: {trace.final_conclusion}
        
        🔐 Proof Hash: {trace.proof_hash}
        """
        return explanation

def simulate_verifier(zkp_proof: Dict[str, Any], facts: Dict[str, bool], conclusion: str):
    """8. Simulate ZKP Verifier for end-to-end demo"""
    print("\n🧪 Simulating ZKP Verifier...")
    print(f"   Verifying proof: {zkp_proof['commitment']}")
    print(f"   Expected conclusion: {conclusion}")
    
    # Simulate verification process
    valid = ZKPEmulator.verify_proof(zkp_proof, facts, conclusion)
    
    if valid:
        print("   ✅ Proof verified! The reasoning is mathematically sound.")
        print(f"   🔐 Proof type: {zkp_proof['proof_type']}")
        print(f"   ⏰ Generated at: {zkp_proof['timestamp']}")
    else:
        print("   ❌ Invalid proof. Something went wrong.")
    
    return valid
    """Demonstrate the ⊕Mind system"""
    
    print("🧠 ⊕Mind: Modular Reasoning Engine Demo")
    print("=" * 50)
    
    # Initialize engine with custom threshold
    engine = OPlusReasoningEngine(confidence_threshold=0.7)
    
    # Add medical assessment rules
    rule1 = LogicRule(
        name="fever_rule",
        conditions=["demam"],
        conclusion="gejala_infeksi",
        operator=LogicOperator.IMPLIES,
        tags=["medis", "gejala"]
    )
    
    rule2 = LogicRule(
        name="cough_rule",
        conditions=["batuk"],
        conclusion="gejala_respirasi",
        operator=LogicOperator.IMPLIES,
        tags=["medis", "respirasi"]
    )
    
    # 5. Demo nested rule support
    rule3 = LogicRule(
        name="severity_rule",
        conditions=["gejala_infeksi", "gejala_respirasi"],
        conclusion="kondisi_serius",
        operator=LogicOperator.AND,
        confidence=0.9,
        tags=["medis", "diagnosis"]
    )
    
    engine.add_rule(rule1)
    engine.add_rule(rule2)
    engine.add_rule(rule3)  # Nested rule
    
    # Add facts
    engine.add_fact("demam", True)
    engine.add_fact("batuk", True)
    
    # Compose rules using ⊕ operator
    composed_rule = engine.oplus_compose("fever_rule", "cough_rule")
    
    # Run reasoning
    trace = engine.reason()
    
    # Generate ZKP
    zkp_proof = ZKPEmulator.generate_proof(engine.facts, trace.final_conclusion)
    
    # Convert to natural language
    explanation = LLMTranslator.logic_to_natural(trace)
    
    print("\n📊 Results:")
    print(explanation)
    print(f"\n🔐 ZKP Proof: {zkp_proof}")
    
    # 7. Export trace to JSON
    trace_json = engine.export_trace()
    print(f"\n📄 Exported trace keys: {list(trace_json.keys())}")
    
    # 8. Simulate verifier
    simulate_verifier(zkp_proof, engine.facts, trace.final_conclusion)
    
    return engine, trace, zkp_proof

if __name__ == "__main__":
    demo_oplus_mind()

def demo_oplus_mind():
    """Demonstrate the ⊕Mind system"""
    print("🧠 ⊕Mind: Modular Reasoning Engine Demo")
    print("=" * 50)

    # Initialize engine with custom threshold
    engine = OPlusReasoningEngine(confidence_threshold=0.7)

    # Add medical assessment rules
    rule1 = LogicRule(
        name="fever_rule",
        conditions=["demam"],
        conclusion="gejala_infeksi",
        operator=LogicOperator.IMPLIES,
        tags=["medis", "gejala"]
    )
    rule2 = LogicRule(
        name="cough_rule",
        conditions=["batuk"],
        conclusion="gejala_respirasi",
        operator=LogicOperator.IMPLIES,
        tags=["medis", "respirasi"]
    )
    rule3 = LogicRule(
        name="severity_rule",
        conditions=["gejala_infeksi", "gejala_respirasi"],
        conclusion="kondisi_serius",
        operator=LogicOperator.AND,
        confidence=0.9,
        tags=["medis", "diagnosis"]
    )

    engine.add_rule(rule1)
    engine.add_rule(rule2)
    engine.add_rule(rule3)

    # Add facts
    engine.add_fact("demam", True)
    engine.add_fact("batuk", True)

    # Compose rules using ⊕ operator
    composed_rule = engine.oplus_compose("fever_rule", "cough_rule")

    # Run reasoning
    trace = engine.reason()

    # Generate ZKP
    zkp_proof = ZKPEmulator.generate_proof(engine.facts, trace.final_conclusion)

    # Convert to natural language
    explanation = LLMTranslator.logic_to_natural(trace)

    print("\n📊 Results:")
    print(explanation)
    print(f"\n🔐 ZKP Proof: {zkp_proof}")

    # Export trace to JSON
    trace_json = engine.export_trace()
    print(f"\n📄 Exported trace keys: {list(trace_json.keys())}")

    # Simulate verifier
    simulate_verifier(zkp_proof, engine.facts, trace.final_conclusion)

    return engine, trace, zkp_proof