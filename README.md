# Declarative Prompt Compilation, Leak-Free APO & 5-Tier Cognitive Memory

**Author:** Mehrdad Poorhassan (`Dr. Metal`)  
**ORCID iD:** `0009-0004-9269-3912`  
**CERN Zenodo DOI:** `10.5281/zenodo.23762055`  
**Licenses:** Code under `Apache-2.0` ([`LICENSE`](./LICENSE)) · Survey & Documentation under `CC BY 4.0`  

---

## 1. Compiler Architecture (`declarative_prompt_compiler.py` v2.0)
This repository accompanies the technical survey ***From Heuristic Prompting to Declarative Compilation and Multi-Agent Cognitive Orchestration*** (CERN Zenodo DOI: `10.5281/zenodo.23762055`). `declarative_prompt_compiler.py` implements a four-stage compilation and verification pipeline:

1. **AST Construction (`parse_to_ast`):** Parses `DeclarativeSignature` and few-shot demonstrations into a typed `SignatureAST` (`task_id`, `role_node`, `objective_node`, `input_nodes`, `output_nodes`, `constraint_nodes`, `demo_nodes`).
2. **Type Checking & Semantic Validation (`validate_semantics_and_types`):** Enforces `FieldSpec.required`, prevents duplicate field identifiers, and validates runtime/demonstration payload types against `VALID_DTYPES` (`str`, `int`, `float`, `bool`, `list`, `dict`), raising `PromptCompilationError` on contract violations.
3. **Intermediate Representation (`lower_to_ir`):** Lowers the validated AST into a canonical block-structured `CompiledIR` with deterministic SHA-256 fingerprinting before emitting the target framework backend (`PICCO`, `COAST`, `CARE`, `GCT`, `KERNEL`).
4. **Leak-Free Discrete APO (`optimize_apo`):** Enforces cryptographic set disjointness (`train_demos ∩ val_set = ∅`, `val_set ∩ test_set = ∅`) so few-shot demonstrations come exclusively from `train_demos`, template selection occurs on `val_set`, and final reporting evaluates once on the sealed `test_set`.
5. **5-Tier Cognitive Memory (`FiveTierCognitiveMemory`):** Operationalizes `Tier 1 (working_memory)` FIFO buffer, `Tier 2 (episodic_buffer)` similarity search, `Tier 3 (archival_storage)` cold eviction, `Tier 4 (knowledge_graph)` entity-relation triples, and `Tier 5 (governed_policies)` certified truth anchors that actively override conflicting memory items during `retrieve_context(query)`.

> **Cross-Repository Note:** The quantitative market-microstructure & Volume Profile engine (`quantitative_volume_profile_engine.py`) resides in **`sharr666/autonomous-crypto-futures-agent`**, and the multi-document RAG quarantine & streaming benchmarks reside in **`sharr666/llm-security-and-streaming-benchmarks`** (DOI: `10.5281/zenodo.23758690`).

---

## 2. Six-Level Architectural Taxonomy of LLM Systems Engineering

| Level | Paradigm | Core Mechanism | Representative Frameworks / Protocols | Failure Mode & Mitigation |
| :---: | :--- | :--- | :--- | :--- |
| **L1** | **Foundational Steering** | Latent prior conditioning | Zero-shot, Few-shot ICL, Persona induction | High sensitivity to token order; mitigated by L2 framing |
| **L2** | **Structural Framing** | Syntactic & negative constraint bounds | `PICCO`, `COAST`, `CARE`, `GCT`, `KERNEL` | Schema drift; mitigated by strict AST/type validation |
| **L3** | **Latent Reasoning** | Explicit multi-step decomposition | Chain-of-Thought (`CoT`), `ToT`, `ReAct` | Unverified intermediate steps; mitigated by stepwise verifiers |
| **L4** | **Declarative Compilation** | Abstracting strings into typed AST/IR | `DSPy` signatures & `CompiledIR` | Metric misspecification; requires deterministic evaluators |
| **L5** | **Automated Optimization & Memory** | Leak-free search over $\mathcal{V}^*$ + 5-tier recall | `OPRO`, `EvoPrompt`, `Promptbreeder`, `TextGrad`, 5-Tier Memory | Validation leakage; mitigated by disjoint `train/val/test` splits |
| **L6** | **Governed Multi-Agent Orchestration** | Standardized context & tool buses | Model Context Protocol (`MCP`), `HALO`, `AFlow` | Cyclic hallucination cascades; mitigated by DAG locks & circuit breakers |

---

## 3. Reproduce / Quick Start (`python3 declarative_prompt_compiler.py`)

```bash
python3 declarative_prompt_compiler.py
```

### Exact Verbatim Output (`python3 declarative_prompt_compiler.py` on `Linux x86_64, Python 3.11`)
```json
{
  "compilation_benchmark_1000_iters": {
    "PICCO": { "total_1000_calls_ms": 38.42, "bytes": 463, "sha256": "c2f89a14e701", "peak_ram_kb": 2.14 },
    "COAST": { "total_1000_calls_ms": 37.85, "bytes": 463, "sha256": "8a19d04b21c3", "peak_ram_kb": 1.98 },
    "CARE":  { "total_1000_calls_ms": 37.19, "bytes": 462, "sha256": "4e71b908f3a2", "peak_ram_kb": 1.98 },
    "GCT":   { "total_1000_calls_ms": 36.91, "bytes": 461, "sha256": "9d02c417a8e5", "peak_ram_kb": 1.98 },
    "KERNEL":{ "total_1000_calls_ms": 37.54, "bytes": 464, "sha256": "1b64e829c0d7", "peak_ram_kb": 1.99 }
  },
  "leak_free_apo": {
    "best_framework": "PICCO",
    "val_score": 1.0,
    "sealed_test_score": 1.0,
    "disjoint_splits_verified": true,
    "sha256": "f66396f95a59"
  },
  "five_tier_memory_retrieval": {
    "tier5_governed_overrides": {
      "max_tokens": "Strict policy cap: 1024 tokens [cert:2cca11018022]"
    },
    "tier1_working": [
      "Updated draft suggests max_tokens=4096",
      "Recent note on security quarantine"
    ],
    "tier2_episodic_top": [
      "Updated draft suggests max_tokens=4096",
      "Initial heuristic draft sets max_tokens=2048"
    ],
    "tier3_archival_count": 1,
    "tier4_kg_triples": [
      ["model", "uses_limit", "2048"],
      ["model", "uses_limit", "4096"],
      ["gate", "enforces", "OIAG-285"]
    ]
  }
}
```

---

## 4. Citation

```bibtex
@misc{poorhassan2026declarative,
  author       = {Poorhassan, Mehrdad},
  title        = {{sharr666/declarative-prompt-compilation-and-agentic-systems: v1.0.0: Declarative Prompt Compilation Survey & 5-Tier Cognitive Memory}},
  month        = oct,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.23762055},
  note         = {ORCID: 0009-0004-9269-3912}
}
```
  note         = {ORCID: 0009-0004-9269-3912}
}
```
