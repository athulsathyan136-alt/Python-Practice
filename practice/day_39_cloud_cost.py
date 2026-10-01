from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI(
    title='Cloud cost Estimator',
    description='Estimate AWS costs for AI/ML Workloads',
    version='1.0.0'
)

PRICING = {
    "ec2_t3_micro_hourly": 0.0116,
    "ec2_gpu_t4_hourly": 0.526,
    "s3_storage_gb": 0.023,
    "lambda_per_million": 0.20,
    "bedrock_per_1k_tokens": 0.003,
    "cloudwatch_per_gb": 0.50,
}

class EC2Request(BaseModel):
    instance_type: str = Field(...,pattern="^(t3.micro|gpu.t4)$")
    hours_per_day : str = Field(...,gt=0,le=24)
    days: str = Field(30,gt=0,le=365)

class S3Request(BaseModel):
    storage_gb : float = Field(...,gt=0)
    request_millions: float  = Field(0,gt=0)

class LLMRequest(BaseModel):
    token_per_request: int =Field(...,gt=0)
    requests_per_day: int = Field(...,gt=0)
    days: int = Field(30,gt=0,le=365)

class LambdaRequest(BaseModel):
    invocations_millions: float = Field(...,gt=0)
    avg_duration_ms: int =Field(...,gt=0)
    memory_mb: int = Field(128,ge=128,le=10240)

def estimate_ec2(req:EC2Request) -> dict:
    rate = PRICING["ec2_t3_micro_hourly"] if req.instance_type == "t3.micro" else PRICING["ec2_gpu_t4_hourly"]
    monthly_cost = rate * req.hours_per_day * req.days
    return{
        "service": "EC2",
        "Instance_type":req.instance_type,
        "hours_rate":rate,
        "total_hours":req.hours_per_day*req.days,
        "monthly_cost_usd":round(monthly_cost,2)

    }

def estimate_S3(req:S3Request) -> dict:
    storage_cost = req.storage_gb*PRICING['s3_storage_gb']
    request_cost = req.request_millions*0.005
    total = storage_cost + request_cost
    return{
        "service":'S3',
        "storage_gb":req.storage_gb,
        "storage_cost":round(storage_cost,2),
        "request_cost": round(request_cost,2),
        "monthly_cost_usd":round(total,2)
    }

def estimate_LLM(req:LLMRequest) -> dict:
    monthly_token = req.token_per_request * req.requests_per_day*req.days
    thousands = monthly_token/1000
    cost = thousands * PRICING['bedrock_per_1k_tokens']
    return{
        "service": "LLM (Bedrock)",
        "total_token":monthly_token,
        "total_requests":req.requests_per_day * req.days,
        "monthly_cost_usd":round(cost,2)

    }

def estimate_lambda(req:LambdaRequest) -> dict:
    invocatons = req.invocations_millions*PRICING["lambda_per_million"]
    gb_seconds = (req.memory_mb/1024) * (req.avg_duration_ms/1000) * (req.invocations_millions * 1000000)
    compute_cost = gb_seconds * 0.0000166667
    total = invocatons + compute_cost
    return{
        "service":'Lambda',
        "invocations_millions":req.invocations_millions,
        "request_cost": round(invocatons,2),
        "compute_cost":round(compute_cost,2),
        "monthly_cost_usd":round(total,2)

    }

@app.get('/')
def root():
    return{
        "message": "Cloud Cost Estimator API",
        "endpoints": [
            "POST /estimate/ec2",
            "POST /estimate/s3",
            "POST /estimate/llm",
            "POST /estimate/lambda",
            "POST /estimate/full-stack",
        ],
    }

@app.post('/estimate/ec2')
def ec2_cost(req:EC2Request):
    return estimate_ec2(req)

@app.post('/estimate/S3')
def S3_cost(req:S3Request):
    return estimate_S3(req)

@app.post('/estimate/LLM')
def LLM_cost(req:LLMRequest):
    return estimate_LLM(req)

@app.post('/estimate/lambda')
def Lambda_cost(req:LambdaRequest):
    return estimate_lambda(req)

class RAGEstimate(BaseModel):
    pdfs_upload : int = Field(...,gt=0)
    avg_pdf_mb: float = Field(5,gt=5)
    daily_queries: int = Field(...,gt=0)
    token_per_query:int = Field(2000,gt=0)

@app.post('/estimate/RAG')
def full_stack(req:RAGEstimate):
    storage_gb = (req.pdfs_upload * req.avg_pdf_mb)/1024
    s3_cost = storage_gb * PRICING["s3_storage_gb"]

    lambda_invocations = req.pdfs_upload / 1000000
    lambda_cost = lambda_invocations*PRICING["lambda_per_million"] 

    monthly_queries = req.daily_queries *30
    tokens = monthly_queries * req.token_per_query
    llm_cost = (tokens/1000) * PRICING["bedrock_per_1k_tokens"]

    total = s3_cost+lambda_cost+llm_cost
    return {
        "system": "Enterprise RAG System",
        "breakdown": {
            "s3_storage_usd": round(s3_cost, 2),
            "lambda_processing_usd": round(lambda_cost, 2),
            "llm_queries_usd": round(llm_cost, 2),
        },
        "total_monthly_cost_usd": round(total, 2),
        "total_yearly_cost_usd": round(total * 12, 2),
        "usage": {
            "pdfs": req.pdfs_uploaded,
            "daily_queries": req.daily_queries,
            "monthly_queries": monthly_queries,
        },
    }