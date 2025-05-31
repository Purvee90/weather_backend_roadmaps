from fastapi import FastAPI,Query
from fastapi.responses import JSONResponse
from .weather import get_weather
app = FastAPI(title="Weather API",version="1.0")

@app.get("/")
def root():
    return {"Hello": "World",
            "message": "Weather API is working"}
    
@app.get("/weather")
def weather(city:str=Query(....,description="City to get weather for")):
    try:
        data=get_weather(city)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error":str(e)},status_code=500)
    
@app.get("/health")
def health() :
    return {"status":"ok"}


   