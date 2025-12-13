# Architectural Design Review Agent

Like a spell-checker, but for building software.
Before engineers start building, this AI reads their blueprints and points out mistakes so expert human architects do not have to grade every single paper.

## What This Is

A service that:

- Accepts an architecture document (plain text / Markdown).
- Runs simple "skills":
  - detect common architecture anti-patterns
  - rate risk
  - propose improvements
- Returns a structured JSON review.

## IP-Safety Boundaries

- Uses generic, well-known anti-patterns (for example tight coupling, no caching, missing observability).
- No organization-specific scoring or proprietary patterns.
- Not tied to any particular product or customer designs.

## Suggested Architecture

- `src/main.py` -- FastAPI with `/review`.
- `src/llm_client.py` -- stub LLM client.
- (Later, add modules like:)
  - `src/skills/anti_pattern_detector.py`
  - `src/skills/risk_classifier.py`
  - `src/skills/suggestion_generator.py`

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export LLM_API_KEY="your-key-here"

uvicorn src.main:app --reload
```

Example call:

```bash
curl -X POST http://localhost:8000/review \
  -H "Content-Type: application/json" \
  -d '{"document": "Your architecture doc text here."}'
```
