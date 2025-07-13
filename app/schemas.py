from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class WheelSpecificationFields(BaseModel):
    treadDiameterNew:Optional[str] None
    lastShopIssueSize:Optional[str]=None
    condemningDia:Optional[str]= None
    wheelGauge:Optional[str]=None
    variationSameAxle:Optional[str] =None
    variationSameBogie:Optional[str]=None
    variationSameCoach:Optional[str]=None
    wheelProfile:Optional[str] =None
    intermediateWWP:Optional[str]=None
    bearingSeatDiameter:Optional[str] =None
    rollerBearingOuterDia:Optional[str]=None
    rollerBearingBoreDia:Optional[str] =None
    rollerBearingWidth:Optional[str]=None
    axleBoxHousingBoreDia:Optional[str]= None
    wheelDiscWidth:Optional[str]= None

class WheelSpecificationCreate(BaseModel):
    formNumber: str=Field(..., description="unique form number")
    submittedBy:str=Field(..., description="user id of who submitted")
    submittedDate :str=Field(..., description="submission date")
    fields :WheelSpecificationFields

class WheelSpecificationResponse(BaseModel):
    formNumber: str
    submittedBy:str
    submittedDate:str
    status:str

class WheelSpecificationFieldsPartial(BaseModel):
    treadDiameterNew:Optional[str] =None
    lastShopIssueSize:Optional[str]=None
    condemningDia:Optional[str]= None
    wheelGauge:Optional[str]= None

class WheelSpecificationGet(BaseModel):
    formNumber: str
    submittedBy:str
    submittedDate: str
    fields:WheelSpecificationFieldsPartial

class BogieDetails(BaseModel):
    bogieNo :str
    makerYearBuilt: str
    incomingDivAndDate :str
    deficitComponents: str
    dateOfIOH: str

class BogieChecksheetDetails(BaseModel):
    bogieFrameCondition:str
    bolster:str
    bolsterSuspensionBracket:str
    lowerSpringSeat:str
    axleGuide:str

class BmbcChecksheetDetails(BaseModel):
    cylinderBody:str
    pistonTrunnion :str
    adjustingTube:str
    plungerSpring :str

class BogieChecksheetCreate(BaseModel):
    formNumber:str=Field(..., description= "unique form number")
    inspectionBy:str=Field(..., description ="user id of inspector")
    inspectionDate:str=Field(..., description ="inspection date")
    bogieDetails:BogieDetails
    bogieChecksheet:BogieChecksheetDetails
    bmbcChecksheet:BmbcChecksheetDetails

class BogieChecksheetResponse(BaseModel):
    formNumber:str
    inspectionBy:str
    inspectionDate:str
    status:str

class StandardResponse(BaseModel):
    success: bool
    message:str
    data:Optional[dict]= None

class WheelSpecStandardResponse(BaseModel):
    success:bool
    message:str
    data:WheelSpecificationResponse

class BogieCheckStandardResponse(BaseModel):
    success :bool
    message:str
    data:BogieChecksheetResponse

class WheelSpecGetStandardResponse(BaseModel):
    success:bool
    message:str
    data:List[WheelSpecificationGet]