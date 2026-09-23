from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='Query Params & POST Demo',
    version='1.0.0'
    )

@app.get('/add')
def add(a:int,b:int):
    return{'a':a,'b':b,"results": a + b}

@app.get('/Multiplication')
def add(a:int,b:int):
    return{'a':a,'b':b,"results": a * b}

@app.get('/greet')
def add(name: str ='Guest',language: str ='English'):
    greetings = {
        'English':f'Hello {name}',
        'Hindi': f'Namaste {name}',
        'Malayalam':f'Namaskaram {name}',
        'Spanish': f'Hola {name}' 
    }

    return{
        "greeting": greetings.get(language,f'Hi {name}!'),
        'name':name,
        'language': language
    }

class User(BaseModel):
    name:str
    age:int
    email:str

class ChatRequest(BaseModel):
    question:str
    model : str = 'gpt-4'

@app.post('/user')
def create_user(user:User):
    return{
        'message':'User created JSON body',
        'user': user,
        'status': 'sucess'
    }

@app.post('/chat')
def chat(request:ChatRequest):
    return{
        'question':request.question,
        'answer': f'This is a simulated answer to: {request.question}',
        'model_user':request.model

    }

@app.post('/search')
def search(query:str , limit : int = 10 ,tags : list[str]=[]):
    return{
        "query":query,
        "limit":limit,
        'tags':tags,
        'result_count':limit
    }