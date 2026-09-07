import re
from typing import Dict, Any, List

class OSProfiler:
    """Extracts cognitive-structural signals from raw tokenised text[cite: 3]."""
    def profile(self, text: str) -> Dict[str, Any]:
        # Measure recursion via nested clauses or multi-step conjunctions
        recursion_markers = len(re.findall(r'\b(because|if|therefore|however|nested|meanwhile)\b', text, re.IGNORECASE))
        recursion_depth = min(float(recursion_markers) / 5.0, 1.0)
        
        # Determine compression based on average word length and sentence density
        words = text.split()
        avg_word_len = sum(len(w) for w in words) / max(len(words), 1)
        compression_factor = min(avg_word_len / 7.0, 1.0)
        
        # Measure tangent probability via conceptual branching punctuation (dashes, parentheses)
        branching_marks = text.count('—') + text.count('(') + text.count(';')
        tangent_probability = min(float(branching_marks) / 3.0, 1.0)
        
        return {
            "recursion_depth": recursion_depth,
            "compression_factor": compression_factor,
            "tangent_probability": tangent_probability,
            "analytical_tempo": "dense" if compression_factor > 0.6 else "stepwise"
        }

class OSStabiliser:
    """Maintains a rolling session window to prevent drift without identity tracking[cite: 3]."""
    def __init__(self, window_size: int = 3):
        self.window_size = window_size
        self.history: List[Dict[str, Any]] = []

    def update(self, os_map: Dict[str, Any]) -> Dict[str, Any]:
        self.history.append(os_map)
        if len(self.history) > self.window_size:
            self.history.pop(0)
            
        # Compute stable rolling averages
        avg_recursion = sum(h["recursion_depth"] for h in self.history) / len(self.history)
        avg_compression = sum(h["compression_factor"] for h in self.history) / len(self.history)
        
        return {
            "stable_recursion": avg_recursion,
            "stable_compression": avg_compression,
            "drift_correction_flag": False
        }

class MindFirstEngine:
    """Core M1E orchestrator implementing the post-identity pipeline[cite: 3]."""
    def __init__(self):
        self.profiler = OSProfiler()
        self.stabiliser = OSStabiliser()

    def process_turn(self, user_text: str) -> Dict[str, Any]:
        os_map = self.profiler.profile(user_text)
        stability_envelope = self.stabiliser.update(os_map)
        
        return {
            "os_map": os_map,
            "stability_envelope": stability_envelope,
            "identity_null_enforced": True
        }
