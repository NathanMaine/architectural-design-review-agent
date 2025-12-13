from fastapi import FastAPI
from pydantic import BaseModel
from .llm_client import LLMClient

app = FastAPI(title="Architectural Design Review Agent")

llm_client = LLMClient()


class ReviewRequest(BaseModel):
    document: str


@app.post("/review")
async def review_architecture(request: ReviewRequest):
    """
    Placeholder endpoint for architecture doc review.
    Wire in sub-skills (anti-pattern detection, risk scoring, suggestions)
    using the generic LLM client.
    """
    # TODO: call separate "skills" modules using llm_client.
    return {
        "summary": "Not implemented yet. Add skills to generate a real review.",
        "issues": [],
        "risk_overall": "UNKNOWN"
    }
