from fastapi import FastAPI, status
from schemas import InspectionCreate

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/inspections", status_code=status.HTTP_201_CREATED)
def create_inspection(inspection: InspectionCreate):
    return {
        "message": "Inspection accepted for validation test.",
        "inspection": inspection.model_dump()
    }