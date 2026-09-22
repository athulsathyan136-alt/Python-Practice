from fastapi import FastAPI

app = FastAPI(
    title='My First API',
    description='Learning FastAPI - Day 31',
    version='1.0.0'
    )

@app.get('/')
def root():
    return{
        'message': 'Welcome to my first API!',
        'author':'Athul Sathyan',
        'status':'healthy'
    }

@app.get('/ping')
def ping():
    return{'message':'pong'}

@app.get('/greet/{name}')
def greet(name: str):
    return{
        'greeting':f"Hello',{name}!",
        'message':"welcome to FastAPI"
    }

@app.get('/square/{number}')
def square(number: int):
    return{
        "input":number,
        "square":number**2
    }

@app.get('about')
def about():
    return {
        "name": "Athul Sathyan",
        "role": "Cloud AI Engineer",
        "skills": ["Python", "FastAPI", "AWS", "LangChain"],
        "certifications": [
            "IIT Kharagpur - Analog Comm",
            "IIT Madras - Wireless Comm",
            "Oracle Agentic AI",
            "AWS Cloud Practitioner",
            "Kaggle ML & DL"
        ]
    }