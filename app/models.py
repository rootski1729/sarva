from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from sqlalchemy.sql import func
from app.database import Base

class WheelSpecification(Base):
    __tablename__ ="wheel_specifications"
    
    id= Column(Integer, primary_key=True, index=True)
    form_number=Column(String(50), unique=True, nullable=False, index=True)
    submitted_by= Column(String(100), nullable=False)
    submitted_date =Column(String(20), nullable=False)  
    status= Column(String(20), default="Saved")
    
    tread_diameter_new= Column(String(100))
    last_shop_issue_size=Column(String(100))
    condemning_dia=Column(String(100))
    wheel_gauge= Column(String(100))
    variation_same_axle =Column(String(50))
    variation_same_bogie =Column(String(50))
    variation_same_coach =Column(String(50))
    wheel_profile= Column(String(100))
    intermediate_wwp= Column(String(100))
    bearing_seat_diameter =Column(String(100))
    roller_bearing_outer_dia= Column(String(100))
    roller_bearing_bore_dia= Column(String(100))
    roller_bearing_width=Column(String(100))
    axle_box_housing_bore_dia =Column(String(100))
    wheel_disc_width= Column(String(100))
    

    created_at= Column(DateTime(timezone=True), server_default=func.now())
    updated_at =Column(DateTime(timezone=True), onupdate=func.now())

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheets"
    

    id=Column(Integer, primary_key=True, index=True)
    
    form_number= Column(String(50), unique=True, nullable=False, index=True)
    inspection_by =Column(String(100), nullable=False)
    inspection_date =Column(String(20), nullable=False)
    status =Column(String(20), default="Saved")
    
    bogie_details= Column(JSON, nullable=False)
    bogie_checksheet= Column(JSON, nullable=False)
    bmbc_checksheet=Column(JSON, nullable=False)
    created_at =Column(DateTime(timezone=True), server_default=func.now())
    updated_at =Column(DateTime(timezone=True), onupdate=func.now())