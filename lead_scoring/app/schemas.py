from pydantic import BaseModel

# Input offer schema
class Offer(BaseModel):
    name: str
    value_props: list
    ideal_use_cases: list

# Input lead schema
class Lead(BaseModel):
    name: str
    role: str
    company: str
    industry: str
    location: str
    linkedin_bio: str

# Scored lead schema
class ScoredLead(BaseModel):
    name: str
    role: str
    company: str
    intent: str
    score: int
    reasoning: str
