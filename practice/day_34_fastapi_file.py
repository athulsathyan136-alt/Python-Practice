from fastapi import FastAPI,UploadFile,File,HTTPException
from typing import List

app = FastAPI(
    title='File upload Demo',
    description='Upload files via Fastapi',
    version='1.0.0'
)

@app.post('/upload')
async def upload_file(file:UploadFile = File(...)):
    contents = await file.read()
    return{
        "Filename":file.filename,
        "Content_type":file.content_type,
        "size_byte":len(contents),
        "size_kb":round(len(contents)/1024,2),
        "preview":contents[:100].decode("utf-8",errors='ignore') if file.content_type.startswith("text") else "(binary file)"
    }


@app.post('/upload/text')
async def upload_text(file:UploadFile = File(...)):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400,detail="only.txt files allowed")

    contents = await file.read()
    text = contents.decode("utf-8")
    return{
        "filename":file.filename,
        "total_lines": len(text.splitlines()),
        "total_word":len(text.split()),
        "total_chars":len(text),
        "first_100_chars":text[:100]
    }

@app.post('/upload/PDF')
async def upload_pdf(file:UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400,detail='Only .pdf files allowed')

    contents = await file.read()

    return{
        "filename":file.filename,
        "size_mb":round(len(contents)/(1024*1024),2),
        "message":"PDF received . In Day 35 + we'll extract text from it!",
        "next_steps":[
            "Extract text with PyPDF2",
            "Split into chunks",
            "Generate embeddings",
            "Store in vector DB"            
        ]
    }

@app.post('/upload/mutiple')
async def upload_multiple(files: List[UploadFile] = File(...)):
    result =[]
    for file in files:
        contents = await file.read()
        result.append({
            "filename":file.filename,
            "size_kb":round(len(contents)/1024,2)
        })

    return {
        "total_files":len(file),
        "total_size_kb":sum(r["size_kb"] for r in result),
        "files":result
    }

@app.post('/upload/with-metadata')
async def upload_multiple(file: UploadFile  = File(...),category:str = 'general',tags: str = ""):
    contents = await file.read() 
    tag_list = [t.strip() for t in tags.split(',') if t.strip()]

    return{
        "filename":file.filename,
        "category":category,
        "tags":tag_list,
        "size_kb":round(len(contents)/1024,2)
    }   