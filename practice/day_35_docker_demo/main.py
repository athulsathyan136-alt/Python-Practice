from fastapi import FastAPI


app = FastAPI(
    title='Docker Demo API',
    description='Docker demo api ',
    version='1.0.0'
)

@app.get('/')
def root():
    return{
        'message':'Hello from Docker! 🐳','stats':'healthy'
    }

@app.get('/ping')
def ping():
    return{
        'message':'pong'
    }

@app.get('/add/{a}/{b}')
def add_num(a: int,b: int):
    return{
        "result":a + b
    }

@app.get('/info')
def info():
    return{
        'app':'Docker',
        'version':'1.0.0',
        'author':'athul',
        'status':'Deployed in a container'
    }

