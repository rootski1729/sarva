from sqlalchemy.orm import Session
from sqlalchemy import and_
from app import models, schemas
from typing import List, Optional



def create_wheel_specification(db: Session, wheel_spec: schemas.WheelSpecificationCreate):
    db_wheel_spec= models.WheelSpecification(
        form_number=wheel_spec.formNumber,
        submitted_by=wheel_spec.submittedBy,
        submitted_date= wheel_spec.submittedDate,
        status= "Saved",
        
        tread_diameter_new= wheel_spec.fields.treadDiameterNew,
        last_shop_issue_size= wheel_spec.fields.lastShopIssueSize,
        condemning_dia= wheel_spec.fields.condemningDia,
        wheel_gauge=wheel_spec.fields.wheelGauge,
        variation_same_axle=wheel_spec.fields.variationSameAxle,
        variation_same_bogie= wheel_spec.fields.variationSameBogie,
        variation_same_coach=wheel_spec.fields.variationSameCoach,
        wheel_profile=wheel_spec.fields.wheelProfile,
        intermediate_wwp=wheel_spec.fields.intermediateWWP,
        bearing_seat_diameter= wheel_spec.fields.bearingSeatDiameter,
        roller_bearing_outer_dia= wheel_spec.fields.rollerBearingOuterDia,
        roller_bearing_bore_dia= wheel_spec.fields.rollerBearingBoreDia,
        roller_bearing_width= wheel_spec.fields.rollerBearingWidth,
        axle_box_housing_bore_dia= wheel_spec.fields.axleBoxHousingBoreDia,
        wheel_disc_width= wheel_spec.fields.wheelDiscWidth
    )
    
    db.add(db_wheel_spec)
    db.commit()
    db.refresh(db_wheel_spec)
    return db_wheel_spec

def get_wheel_specifications(
    db: Session,
    form_number: Optional[str]= None,
    submitted_by: Optional[str]= None,
    submitted_date: Optional[str]= None
) -> List[models.WheelSpecification]:
    
    query=db.query(models.WheelSpecification)
    
    filters=[]
    if form_number:
        filters.append(models.WheelSpecification.form_number == form_number)
    if submitted_by:
        filters.append(models.WheelSpecification.submitted_by== submitted_by)
    if submitted_date:
        filters.append(models.WheelSpecification.submitted_date== submitted_date)
    if filters:
        query=query.filter(and_(*filters))
    
    return query.all()

def get_wheel_specification_by_form_number(db: Session, form_number: str):
    return db.query(models.WheelSpecification).filter(
        models.WheelSpecification.form_number == form_number
    ).first()


def create_bogie_checksheet(db: Session, bogie_check: schemas.BogieChecksheetCreate):
    db_bogie_check= models.BogieChecksheet(
        form_number= bogie_check.formNumber,
        inspection_by =bogie_check.inspectionBy,
        inspection_date =bogie_check.inspectionDate,
        status="Saved",
        
        bogie_details=bogie_check.bogieDetails.dict(),
        bogie_checksheet =bogie_check.bogieChecksheet.dict(),
        bmbc_checksheet= bogie_check.bmbcChecksheet.dict()
    )
    
    db.add(db_bogie_check)
    db.commit()
    db.refresh(db_bogie_check)
    return db_bogie_check

def get_bogie_checksheet_by_form_number(db: Session, form_number: str):
    return db.query(models.BogieChecksheet).filter(
        models.BogieChecksheet.form_number== form_number
    ).first()


def check_form_number_exists_wheel(db: Session, form_number: str) ->bool:
    return db.query(models.WheelSpecification).filter(
        models.WheelSpecification.form_number==form_number
    ).first() is not None

def check_form_number_exists_bogie(db: Session, form_number: str) ->bool:
    return db.query(models.BogieChecksheet).filter(
        models.BogieChecksheet.form_number == form_number
    ).first() is not None