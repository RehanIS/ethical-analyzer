import cohere

co = cohere.Client("rLz5cKn5fMeWUyPsOwxAx4WYVyKezdbOHy1xEfbt")  # Replace with your actual API key

import json
import re

def analyze_ethics(scenario_text: str) -> dict:
    prompt = f"""
You are an expert in engineering ethics. Analyze the following AI-based scenario using ethical frameworks such as Utilitarianism, Deontology, and the Engineering Code of Conduct.

SCENARIO:
\"\"\"
{scenario_text}
\"\"\"

Provide a JSON response with the following keys:
{{
  "analysis": "<Detailed ethical evaluation>",
  "risk_score": <integer between 0 and 100>,
  "recommendations": [
    "First actionable suggestion",
    "Second suggestion"
  ],
  "checklist": {{
    "Bias Detection": true/false,
    "Transparency": true/false,
    "Data Privacy": true/false,
    "Human Oversight": true/false
  }}
}}

Please be realistic in risk scoring:
- 0–30: Low risk
- 31–60: Moderate risk
- 61–100: High risk

Respond ONLY in JSON.
"""

    response = co.chat(
        model='command-r',
        message=prompt,
        max_tokens=800,
        temperature=0.4,
    )

    raw = response.text.strip()

    # Extract JSON from a markdown-style code block if present
    if "```json" in raw:
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', raw, re.DOTALL)
        if json_match:
            raw = json_match.group(1)

    try:
        parsed = json.loads(raw)

        # Sanitize checklist values to be real booleans
        checklist = parsed.get("checklist", {})
        parsed["checklist"] = {
            key: str(value).lower() == "true" for key, value in checklist.items()
        }

        return parsed

    except json.JSONDecodeError:
        return {
            "analysis": raw,
            "risk_score": 50,
            "recommendations": [],
            "checklist": {
                "Bias Detection": False,
                "Transparency": False,
                "Data Privacy": False,
                "Human Oversight": False
            }
        }