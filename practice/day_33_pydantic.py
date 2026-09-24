from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr,field_validator
from typing import Optional

app = FastAPI(
    title='Pydantic Validation Demo',
    description='Learn how to validate data with Pydantic',
    version='1.0.0'

)

class User(BaseModel):
    name: str = Field(...,min_length=2,max_length=50)
    age: int = Field(...,gt=0,lt=120)
    email:EmailStr
    password: str = Field(...,min_length=8)
    bio: str = Field(None,max_length=200)

@app.post('/users')
def create_user(user: User):
    return{
        'message':f'User {user.name} creeated',
        'user':user,
        'password_length':len(user.password)
    }

class Product(BaseModel):
    name:str
    price:float = Field(...,gt=0)
    discount: float = Field(0,ge=0,le=100)

    @field_validator('name')
    def name_must_be_capt(cls,v):
        if not v[0].isupper():
            raise ValueError
        return v

@app.post('/product')
def create_product(product:Product):
    final = product.price*(1-product.discount/100)
    return{
        'product':product.name,
        'Original':product.price,
        'Discount':f"{product.discount}%",
        'Final_price':round(final,2)


    }   
class LLMRequest(BaseModel):
    prompt: str = Field(...,min_length=1,max_length=5000)
    model: str = Field("gpt-4", pattern="^(gpt-4|gpt-3.5-turbo|claude-3|llama-3)$")
    temperature: float = Field(0.7,ge=0.0,le=2.0)
    max_token: int = Field(500, gt=0, le=4000)

@app.post('/llm')
def call_llm(request:LLMRequest):
    return{
        "message": "LLM request validated!",
        "prompt_length": len(request.prompt),
        "model": request.model,
        "temperature": request.temperature,
        "max_tokens": request.max_tokens
    }

class UserResponse(BaseModel):
    name:str
    email:EmailStr

@app.post('/signup',response_model=UserResponse)
def signup(user:User):
    return user

class Address(BaseModel):
    street:str
    city:str
    country: str = 'India'

class Employee(BaseModel):
    name:str    
    age: int
    address:Address
    skills:list[str]=[]

@app.post('/employee')
def create_employee(employee:Employee):
    return {
        "message": f"Employee {employee.name} from {employee.address.city} added",
        "data": employee
    }        