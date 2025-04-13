from fastapi import FastAPI
from models import ScenarioRequest, AnalysisResponse
from cohere_handler import analyze_ethics
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ethical Scenario Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace * with your frontend domain if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: ScenarioRequest):
    result = analyze_ethics(request.scenario)
    return AnalysisResponse(**result)
