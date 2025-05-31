import requests
import redis
import json
from config import VC_API_KEY, VC_API_URL

r = redis.Redis(host='localhost',port=6379,db=0)

def get_weather(city:str):
    cache_key =  f"weather:{city.lower()}"
    # Try to fetch Redis cache
    cached_data = r.get(cache_key)
    if cached_data:
        return json.loads(cached_data)
    # If not cached, then call the API
    url = f"{VC_API_URL}/{city}?unitGroup=us&key={VC_API_KEY}&contentType=json"
    response = requests.get(url)
    
    if response.status_code != 200 :
        return {"error" : "API request failed"}
    
    weather_data = response.json()
    
    # 7 days data
    url = f"{VC_API_URL}/{city}%2CUK/last7days?unitGroup=metric?&key={VC_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200 :
        return {"error" : "API request failed"}
    
    seven_days_data = response.json()
    
    # Save to Redis with TTL
    r.setex(cache_key,600,json.dumps(weather_data))
    r.setex(cache_key,600,json.dumps(seven_days_data))
    
    return weather_data,seven_days_data
    
