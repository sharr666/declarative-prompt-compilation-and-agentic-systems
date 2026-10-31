"""
Author: Mehrdad Poorhassan (Dr. Metal) — ORCID: 0009-0004-9269-3912
Declarative Prompt Compiler, Discrete APO Optimizer, and 5-Tier Cognitive Memory Substrate
"""
import hashlib, json
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Tuple
import numpy as np

@dataclass
class FieldSpec:
    name: str
    dtype: str
    description: str
    required: bool = True

@dataclass
class DeclarativeSignature:
    task_name: str
    role: str
    objective: str
    inputs: List[FieldSpec]
    outputs: List[FieldSpec]
    constraints: List[str]
    framework: str = "KERNEL"

class DeclarativePromptCompiler:
    SUPPORTED_FRAMEWORKS = ("PICCO", "COAST", "CARE", "GCT", "KERNEL")

    def compile(self, sig: DeclarativeSignature, demonstrations: Optional[List[Dict[str, str]]] = None) -> str:
        if sig.framework not in self.SUPPORTED_FRAMEWORKS:
            raise ValueError(f"Unsupported framing framework: {sig.framework}")
        in_schema = "\n".join(f"  - {f.name} ({f.dtype}): {f.description}" for f in sig.inputs)
        out_schema = "\n".join(f"  - {f.name} ({f.dtype}): {f.description}" for f in sig.outputs)
        rules = "\n".join(f"  {i+1}. {c}" for i, c in enumerate(sig.constraints))
        demo_block = ""
        if demonstrations:
            demo_block = "\n[Bootstrapped Demonstrations]\n" + "\n".join(json.dumps(d) for d in demonstrations) + "\n"
        return (
            f"[{sig.framework} DECLARATIVE SPECIFICATION — {sig.task_name}]\n"
            f"[Role]: {sig.role}\n[Objective]: {sig.objective}\n"
            f"[Input Schema]:\n{in_schema}\n[Constraints]:\n{rules}\n"
            f"{demo_block}[Output Contract]:\n{out_schema}"
        )

    def optimize_apo(self, base_sig: DeclarativeSignature, val_set: List[Dict[str, str]], evaluator: Callable[[str, Dict[str, str]], float]) -> Dict[str, object]:
        best_score, best_fw, best_prompt = -1.0, base_sig.framework, ""
        trajectory = []
        for fw in self.SUPPORTED_FRAMEWORKS:
            cand = DeclarativeSignature(base_sig.task_name, base_sig.role, base_sig.objective, base_sig.inputs, base_sig.outputs, base_sig.constraints + [f"Enforce {fw} determinism."], fw)
            prompt = self.compile(cand, val_set[:2])
            score = float(np.mean([evaluator(prompt, x) for x in val_set]))
            trajectory.append({"framework": fw, "score": round(score, 4)})
            if score > best_score:
                best_score, best_fw, best_prompt = score, fw, prompt
        return {"best_framework": best_fw, "best_score": round(best_score, 4), "trajectory": trajectory, "sha256": hashlib.sha256(best_prompt.encode()).hexdigest()[:16]}

class FiveTierCognitiveMemory:
    def __init__(self, working_capacity: int = 8) -> None:
        self.working_capacity = working_capacity
        self.working_memory: List[str] = []
        self.archival_storage: List[str] = []
        self.knowledge_graph: List[Tuple[str, str, str]] = []
        self.governed_policies: Dict[str, str] = {}

    def insert_observation(self, text: str, triple: Optional[Tuple[str, str, str]] = None) -> None:
        self.working_memory.append(text)
        if len(self.working_memory) > self.working_capacity:
            self.archival_storage.append(self.working_memory.pop(0))
        if tri            self.knowledge_graph.append(triple)ple:
            self.knowledge_graph.append(triple)
