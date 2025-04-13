from fastapi import FastAPI
from models import ScenarioRequest, AnalysisResponse
from cohere_handler import analyze_ethics
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can later restrict this to just your Netlify/Render URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI(title="Ethical Scenario Analyzer")

@app.post("/analyze", response_model=AnalysisResponse)
def analyze(request: ScenarioRequest):
    result = analyze_ethics(request.scenario)
    return AnalysisResponse(**result)
