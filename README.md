# Declarative Prompt Compilation, Cognitive Memory & Quantitative Volume Profile Engine

**Author:** Mehrdad Poorhassan (`Dr. Metal`)  
**ORCID:** `0009-0004-9269-3912`  
**CERN Zenodo DOI:** `10.5281/zenodo.23762055`  
**License:** Apache License 2.0  

## 1. Overview
This repository provides the reference implementation for **Declarative Prompt Compilation**, **Discrete Automated Prompt Optimization (APO)** across structural framing schemas (`PICCO`, `COAST`, `CARE`, `GCT`, `KERNEL`), the **5-Tier Cognitive Memory Hierarchy**, and a vectorized **Quantitative Volume Profile & Wilder's RMA Engine**.

## 2. Repository Structure (Root)
- `declarative_prompt_compiler.py`: Implements `FieldSpec`, `DeclarativeSignature`, `DeclarativePromptCompiler` (deterministic schema compilation & discrete APO trajectory evaluation), and `FiveTierCognitiveMemory` (FIFO working buffer, archival eviction, entity-relation knowledge graph triples, and SHA-256 governed truth anchors).
- `quantitative_volume_profile_engine.py`: Implements `QuantitativeVolumeProfileEngine` for range-distributed contiguous Volume Profile (`POC`, `VAH`, `VAL`, and Value Area share) alongside Wilder's RMA (`ATR`, `RSI`, and `MACD`).

## 3. Reproducible Empirical Execution Benchmarks (Python 3.11 & `tracemalloc`)

All figures below are deterministic and directly reproducible by executing `declarative_prompt_compiler.py` and `quantitative_volume_profile_engine.py`:

### 3.1. Declarative Schema Compilation (`1,000` Iterations per Framework)
| Framing Schema | 1,000-Call Total Latency | Per-Call Latency | Compiled Output Size | Deterministic SHA-256 Prefix | Peak Heap RAM (`tracemalloc`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PICCO** | `35.66 ms` | `0.0357 ms` | `437 bytes` | `0f6743b34bd5` | `1.81 KB` |
| **COAST** | `36.25 ms` | `0.0362 ms` | `437 bytes` | `b694aa7815c4` | `1.67 KB` |
| **CARE** | `42.53 ms` | `0.0425 ms` | `436 bytes` | `2505424e034e` | `1.67 KB` |
| **GCT** | `32.77 ms` | `0.0328 ms` | `435 bytes` | `4334a9659885` | `1.67 KB` |
| **KERNEL** | `34.96 ms` | `0.0350 ms` | `438 bytes` | `07f9e416694c` | `1.68 KB` |

### 3.2. Quantitative Volume Profile Engine (`N = 10,000` OHLCV Bars, `np.random.seed(42)`, `50` Bins, `70%` Value Area)
| Metric / Output | Measured Value | Verification Notes |
| :--- | :--- | :--- |
| **Point of Control (`POC`)** | `96.2197` | Maximum volume density bin center |
| **Value Area High (`VAH`)** | `127.4552` | Upper contiguous 70% volume boundary |
| **Value Area Low (`VAL`)** | `72.1238` | Lower contiguous 70% volume boundary |
| **Captured Value Area Share** | `0.7060` (`70.60%`) | Satisfies `>= 0.70` contiguous threshold |
| **Peak Heap Memory (`tracemalloc`)** | `82.71 KB` | Bounded $O(\text{bins})$ allocation |

## 4. Citation
- Poorhassan, M. (2026). *Declarative Prompt Compilation, 5-Tier Cognitive Memory, and Vectorized Quantitative Volume Profile Engine*. Zenodo (CERN). DOI: `10.5281/zenodo.23762055`. ORCID: `0009-0004-9269-3912`.
