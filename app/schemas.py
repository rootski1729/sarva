from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class WheelSpecificationFields(BaseModel):
    treadDiameterNew: Optional[str] =Field(None, example="915 (900-1000)")
    lastShopIssueSize: Optional[str] =Field(None, example="837 (800-900)")
    condemningDia: Optional[str]= Field(None, example="825 (800-900)")
    wheelGauge: Optional[str] =Field(None, example="1600 (+2,-1)")
    variationSameAxle: Optional[str]= Field(None, example="0.5")
    variationSameBogie: Optional[str] =Field(None, example="5")
    variationSameCoach: Optional[str]= Field(None, example="13")
    wheelProfile: Optional[str] = Field(None, example="29.4 Flange Thickness")
    intermediateWWP: Optional[str] = Field(None, example="20 TO 28")
    bearingSeatDiameter: Optional[str] =Field(None, example="130.043 TO 130.068")
    rollerBearingOuterDia: Optional[str]= Field(None, example="280 (+0.0/-0.035)")
    rollerBearingBoreDia: Optional[str]= Field(None, example="130 (+0.0/-0.025)")
    rollerBearingWidth: Optional[str]= Field(None, example="93 (+0/-0.250)")
    axleBoxHousingBoreDia: Optional[str] = Field(None, example="280 (+0.030/+0.052)")
    wheelDiscWidth: Optional[str] =Field(None, example="127 (+4/-0)")

class WheelSpecificationCreate(BaseModel):
    formNumber: str = Field(..., example="WHEEL-2025-001", description="unique form number")
    submittedBy: str = Field(..., example="inspector_raj_001", description="user id of personn who submitted")
    submittedDate: str = Field(..., example="2025-07-13", description="date of submission")
    fields: WheelSpecificationFields
    
    class Config:
        json_schema_extra = {
            "example": {
                "formNumber": "WHEEL-2025-001",
                "submittedBy": "inspector_raj_001",
                "submittedDate": "2025-07-13",
                "fields": {
                    "treadDiameterNew": "915 (900-1000)",
                    "lastShopIssueSize": "837 (800-900)",
                    "condemningDia": "825 (800-900)",
                    "wheelGauge": "1600 (+2,-1)",
                    "variationSameAxle": "0.5",
                    "variationSameBogie": "5",
                    "variationSameCoach": "13",
                    "wheelProfile": "29.4 Flange Thickness",
                    "intermediateWWP": "20 TO 28",
                    "bearingSeatDiameter": "130.043 TO 130.068",
                    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
                    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
                    "rollerBearingWidth": "93 (+0/-0.250)",
                    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
                    "wheelDiscWidth": "127 (+4/-0)"
                }
            }
        }

class WheelSpecificationResponse(BaseModel):
    formNumber:str
    submittedBy:str
    submittedDate: str
    status: str

class WheelSpecificationFieldsPartial(BaseModel):
    treadDiameterNew: Optional[str]= None
    lastShopIssueSize: Optional[str]= None
    condemningDia: Optional[str] =None
    wheelGauge: Optional[str] =None

class WheelSpecificationGet(BaseModel):
    formNumber:str
    submittedBy:str
    submittedDate: str
    fields:WheelSpecificationFieldsPartial

class BogieDetails(BaseModel):
    bogieNo: str =Field(..., example="BG1234")
    makerYearBuilt: str= Field(..., example="RDSO/2020")
    incomingDivAndDate:str = Field(..., example="NR / 2025-07-01")
    deficitComponents: str = Field(..., example="None")
    dateOfIOH: str= Field(..., example="2025-07-10")

class BogieChecksheetDetails(BaseModel):
    bogieFrameCondition: str = Field(..., example="Good")
    bolster: str =Field(..., example="Good")
    bolsterSuspensionBracket: str = Field(..., example="Cracked")
    lowerSpringSeat: str = Field(..., example="Good")
    axleGuide: str= Field(..., example="Worn")

class BmbcChecksheetDetails(BaseModel):
    cylinderBody: str=Field(..., example="WORN OUT")
    pistonTrunnion: str = Field(..., example="GOOD")
    adjustingTube: str= Field(..., example="DAMAGED")
    plungerSpring:str = Field(..., example="GOOD")

class BogieChecksheetCreate(BaseModel):
    formNumber: str = Field(..., example="BOGIE-2025-001", description="unique form number")
    inspectionBy: str = Field(..., example="inspector_singh_456", description="inspector user ID")
    inspectionDate: str = Field(..., example="2025-07-13", description="date of inspection")
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheetDetails
    bmbcChecksheet: BmbcChecksheetDetails
    
    class Config:
        json_schema_extra = {
            "example": {
                "formNumber": "BOGIE-2025-001",
                "inspectionBy": "inspector_singh_456", 
                "inspectionDate":"2025-07-13",
                "bogieDetails": {
                    "bogieNo": "BG1234",
                    "makerYearBuilt": "RDSO/2020",
                    "incomingDivAndDate": "NR / 2025-07-01",
                    "deficitComponents": "None",
                    "dateOfIOH":"2025-07-10"
                },
                "bogieChecksheet": {
                    "bogieFrameCondition": "Good",
                    "bolster": "Good", 
                    "bolsterSuspensionBracket": "Cracked",
                    "lowerSpringSeat": "Good",
                    "axleGuide": "Worn"
                },
                "bmbcChecksheet": {
                    "cylinderBody": "WORN OUT",
                    "pistonTrunnion": "GOOD",
                    "adjustingTube": "DAMAGED",
                    "plungerSpring": "GOOD"
                }
            }
        }

class BogieChecksheetResponse(BaseModel):
    formNumber:str
    inspectionBy:str
    inspectionDate: str
    status: str

class StandardResponse(BaseModel):
    success:bool
    message:str
    data: Optional[dict] = None

class WheelSpecStandardResponse(BaseModel):
    success:bool
    message:str
    data: WheelSpecificationResponse

class BogieCheckStandardResponse(BaseModel):
    success:bool
    message:str
    data: BogieChecksheetResponse

class WheelSpecGetStandardResponse(BaseModel):
    success: bool
    message: str
    data: List[WheelSpecificationGet]