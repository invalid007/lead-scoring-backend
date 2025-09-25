import csv
from app.schemas import Lead, ScoredLead
from typing import List

# Parse CSV file to list of Lead objects
def parse_csv(file) -> List[Lead]:
    decoded = file.file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded)
    leads = []
    for row in reader:
        lead = Lead(
            name=row.get("name", ""),
            role=row.get("role", ""),
            company=row.get("company", ""),
            industry=row.get("industry", ""),
            location=row.get("location", ""),
            linkedin_bio=row.get("linkedin_bio", "")
        )
        leads.append(lead)
    return leads

# Export results as CSV
def export_csv(results: List[ScoredLead]) -> str:
    filename = "results.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name","role","company","intent","score","reasoning"])
        for lead in results:
            writer.writerow([lead.name, lead.role, lead.company, lead.intent, lead.score, lead.reasoning])
    return filename
