from fastapi import FastAPI
from models import ScenarioRequest, AnalysisResponse
from cohere_handler import analyze_ethics

app = FastAPI(title="Ethical Scenario Analyzer")

@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: ScenarioRequest):
    result = analyze_ethics(request.scenario)
    return AnalysisResponse(**result)
