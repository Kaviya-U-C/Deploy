import uvicorn
from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def home():
    return "Learning Heroku"

if __name__ =="__main__":
    uvicorn.run(app)
