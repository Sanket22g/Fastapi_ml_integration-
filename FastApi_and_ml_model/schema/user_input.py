from pydantic import BaseModel, Field, computed_field, field_validator
from typing import List, Optional,Annotated,Literal

class person(BaseModel):
    age:Annotated[int,Field(gt=0,lt=120,description="Age must be between 0 and 120")]
    # weight	height	income_lpa	smoker	city	occupation	insurance_premium_category	
    weight:Annotated[float,Field(gt=0,lt=500,description="Weight must be between 0 and 500 kgs")]
    height:Annotated[float,Field(gt=0,lt=2.5,description="Height must be between 0 and 2.5 meters")]
    income_lpa:Annotated[float,Field(gt=0,description="Income must be between 0 and 100 lpa")]
    smoker:Annotated[int,Field(ge=0,le=1,description="Smoker must be 0 or 1")]
    city:Annotated[str,Field(description="City must be one of the predefined city names")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'],Field(description="Occupation must be one of 'retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job ")]
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 23:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_a"
        else:
            return "senior"
    @computed_field
    @property
    def life_risk(self) -> str:
        if self.smoker == 1 and self.bmi > 30:
            return "high"
        elif self.smoker == 1 or self.bmi > 30:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def city_tier(self)-> int:
        row=self.city
        tier_11=["Delhi","Mumbai","Bangalore","Chennai","Hyderabad","Kolkata","Pune"]
        tier_22=["Chandigarh","Lucknow","Gaya","Mysore","Jalandhar","Kota","Indore","Jaipur"]
        if row in tier_11:
           return 1
        elif row in tier_22:
           return 2
        return 3
    @field_validator('city')
    @classmethod
    def validate_city(cls, v:str) -> str:
        v=v.strip().title()
        return v
    
class prediction_response(BaseModel):
    predicted_insurance_premium: str
    class_probabilities: dict
    