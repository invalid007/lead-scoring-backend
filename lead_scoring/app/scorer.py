from app.schemas import Lead, ScoredLead
from typing import List

# Simple role mapping
ROLE_SCORES = {
    "CEO": 20,
    "Head of Growth": 20,
    "VP": 20,
    "Manager": 10,
    "Lead": 10
}

INDUSTRY_SCORE = 20  # exact match
ADJACENT_SCORE = 10  # similar industry

# AI placeholder function
def ai_score(lead: Lead, offer: dict):
    # High if lead role is decision maker and company matches target
    if lead.role in ROLE_SCORES and offer["ideal_use_cases"][0].lower() in lead.company.lower():
        return "High", "Role and company fit well with offer"
    return "Medium", "Some fit with offer"

def score_leads(offer: dict, leads: List[Lead]) -> List[ScoredLead]:
    results = []
    for lead in leads:
        # Rule layer
        rule_score = 0
        role_points = ROLE_SCORES.get(lead.role, 0)
        rule_score += role_points

        if offer["ideal_use_cases"][0].lower() in lead.industry.lower():
            rule_score += INDUSTRY_SCORE
        else:
            rule_score += ADJACENT_SCORE

        # Data completeness
        if all([lead.name, lead.role, lead.company, lead.industry, lead.location, lead.linkedin_bio]):
            rule_score += 10

        # AI layer
        intent, reasoning = ai_score(lead, offer)
        ai_points = {"High":50, "Medium":30, "Low":10}.get(intent, 0)

        final_score = rule_score + ai_points

        results.append(ScoredLead(
            name=lead.name,
            role=lead.role,
            company=lead.company,
            intent=intent,
            score=final_score,
            reasoning=reasoning
        ))
    return results