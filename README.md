# Declarative Prompt Compilation, Type Validation & Bounded Memory

**Author:** Mehrdad Poorhassan (Dr. Metal)  
**ORCID:** 0009-0004-9269-3912  
**DOI:** 10.5281/zenodo.23762055  
**Status:** Experimental reference implementation.

## Compiler pipeline

`declarative_prompt_compiler.py` implements:
1. Typed `DeclarativeSignature` to AST conversion.
2. Field-name, duplicate-name, required-field and exact runtime type checks.
3. Deterministic JSON-quoted prompt blocks and a full SHA-256 IR fingerprint.
4. A discrete selection loop over five **framing profiles** (PICCO, COAST, CARE, GCT, KERNEL).
5. Exact-record split-overlap checks for train/validation/test data.

The five profile labels currently render the same canonical prompt grammar with a profile identifier. They are not independent external framework backends or runtime adapters.

## APO / evaluation limits

The optimizer verifies exact canonical-record disjointness. This does not detect paraphrase-level, source-level, temporal or semantic leakage. The evaluator is user-supplied; the optimizer does not establish that the metric is scientifically valid. The small main-program evaluator is only an execution smoke test and its score must not be interpreted as model performance.

## Bounded five-tier memory prototype

Working, episodic, archival, knowledge-graph and governed-policy stores each have explicit capacity limits; governed policies use FIFO eviction at the configured cap. Tier 5 governed facts are surfaced in the effective context. A narrow conflict filter suppresses explicit numeric key/value conflicts (for example, `max_tokens=4096` against a policy specifying `max_tokens=1024`). This is not general contradiction reasoning, cryptographic certification, durable storage or multi-user isolation.

## Reproduce

Python 3.11+; no third-party runtime dependencies:

```bash
python -m py_compile declarative_prompt_compiler.py
python -m unittest discover -s tests -v
python declarative_prompt_compiler.py
```

## Security

Treat all prompt fields, demonstration records and retrieved memories as untrusted input. JSON quoting prevents raw newline/section-boundary injection in the rendered representation; it does not prevent semantic prompt injection or guarantee safe behavior by a downstream model.

## Licensing

Code is Apache-2.0. Documentation/survey text is CC BY 4.0 only where explicitly identified. Check the applicable license for each file.
