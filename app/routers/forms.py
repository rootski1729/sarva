from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/api/forms", tags=["forms"])

# wheel related routes

@router.post(
    "/wheel-specifications",
    response_model=schemas.WheelSpecStandardResponse,
    status_code=201,
    summary="submit wheel specification record"
)
async def create_wheel_specification(
    wheel_spec: schemas.WheelSpecificationCreate,
    db: Session = Depends(get_db)):
    if crud.check_form_number_exists_wheel(db, wheel_spec.formNumber):
        raise HTTPException(
            status_code=400,
            detail={
                "success": False,
                "message": f"form number {wheel_spec.formNumber} already exists",
                "data": None
            }
        )
    try:
        db_wheel_spec = crud.create_wheel_specification(db, wheel_spec)
        return {
            "success": True,
            "message": "wheel specification submitted successfully.",
            "data": {
                "formNumber": db_wheel_spec.form_number,"submittedBy": db_wheel_spec.submitted_by,
                "submittedDate": db_wheel_spec.submitted_date,
                "status": db_wheel_spec.status
            }
        } 
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": f"internal server error: {str(e)}",
                "data": None
            }
        )

@router.get("/wheel-specifications",
response_model=schemas.WheelSpecGetStandardResponse,
    status_code=200,
    summary="Get wheel specifications with filters")
async def get_wheel_specifications(
    formNumber: Optional[str] =Query(None, description="filter by form number"),
    submittedBy: Optional[str]= Query(None, description="filter by submitted by"),
    submittedDate: Optional[str]= Query(None, description="filter by submitted date"),
    db: Session = Depends(get_db)):
    try:
        wheel_specs = crud.get_wheel_specifications(
            db, 
            form_number=formNumber,
            submitted_by=submittedBy,
            submitted_date=submittedDate)

        response_data = []
        for spec in wheel_specs:
            response_data.append({
                "formNumber":spec.form_number,
                "submittedBy":spec.submitted_by,
                "submittedDate": spec.submitted_date,
                "fields": {
                    "treadDiameterNew":spec.tread_diameter_new,
                    "lastShopIssueSize":spec.last_shop_issue_size,
                    "condemningDia":spec.condemning_dia,
                    "wheelGauge": spec.wheel_gauge}
            })
        return {
            "success": True,
            "message": "wheel specification forms fetched successfully.",
            "data": response_data,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": f"internal server error: {str(e)}",
                "data": []
            }
        )

# Extra third route
@router.post("/bogie-checksheet",response_model=schemas.BogieCheckStandardResponse, status_code=201, summary="submit bogie checksheet form")
async def create_bogie_checksheet(
    bogie_check: schemas.BogieChecksheetCreate,
    db: Session = Depends(get_db)):
   
    if crud.check_form_number_exists_bogie(db, bogie_check.formNumber):
        raise HTTPException(
            status_code=400,
            detail={
                "success": False,
                "message": f"form number {bogie_check.formNumber} already exists",
                "data": None}
        )
    
    try:
        db_bogie_check = crud.create_bogie_checksheet(db, bogie_check)
        return {
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": db_bogie_check.form_number,
                "inspectionBy": db_bogie_check.inspection_by,
                "inspectionDate": db_bogie_check.inspection_date,
                "status": db_bogie_check.status}
        }    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "message": f"Internal server error: {str(e)}",
                "data": None
            }
        )


@router.get("/health", summary="health check endpoint")
async def health_check():
    return {
        "success": True,
        "message": "KPA Forms API is running successfully!",
        "data": {
            "status": "healthy",
            "version": "1.0.0"
        }
    }