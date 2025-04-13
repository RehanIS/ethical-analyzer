
from pydantic import BaseModel
from typing import List, Dict

class ScenarioRequest(BaseModel):
    scenario: str

class AnalysisResponse(BaseModel):
    analysis: str
    risk_score: int
    recommendations: List[str]
    checklist: Dict[str, bool]
