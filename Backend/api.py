from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
@app.get("/hello")
def hello():
    return("welcome")

@app.get("/centiment_analysis")
def sentiment_analysis():
    return({"levi": "bad",
             "cedric": "not interested"})


@app.get("/centiment_analysis{text}")
def sentiment_analysis(text):
    if text.lower in {"good, nice, better"}:
     return({"levi": "is a good student",
             "cedric": "a good student"})
    else:
     return({"levi":"is a bad student",
               "cedric":"is also a bad student"
               })
    
#router = APIRouter()
@app.get("/test")
def get_students():
   return{
      "students":["alice", "bob"]
   }
  

