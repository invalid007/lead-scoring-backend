from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas import Offer, Lead, ScoredLead
from app.scorer import score_leads
from app.utils import parse_csv
from typing import List

router = APIRouter()

# Store uploaded data in memory
offer_data = {}
leads_data = []
scored_results = []

# POST /offer
@router.post("/offer")
def create_offer(offer: Offer):
    global offer_data
    offer_data = offer.dict()
    return {"message": "Offer received", "offer": offer_data}

# POST /leads/upload
@router.post("/leads/upload")
def upload_leads(file: UploadFile = File(...)):
    global leads_data
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")
    leads_data = parse_csv(file)
    return {"message": f"{len(leads_data)} leads uploaded"}

# POST /score
@router.post("/score")
def run_scoring() -> List[ScoredLead]:
    global scored_results
    if not offer_data or not leads_data:
        raise HTTPException(status_code=400, detail="Offer or leads missing")
    scored_results = score_leads(offer_data, leads_data)
    return scored_results

# GET /results
@router.get("/results")
def get_results() -> List[ScoredLead]:
    return scored_results

# GET /results/csv (optional)
@router.get("/results/csv")
def get_results_csv():
    from fastapi.responses import FileResponse
    from app.utils import export_csv
    if not scored_results:
        raise HTTPException(status_code=400, detail="No results to export")
    filename = export_csv(scored_results)
    return FileResponse(filename, media_type='text/csv', filename='results.csv')
