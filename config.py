from dotenv import load_dotenv
import os

load_dotenv

VC_API_KEY = os.getenv('VC_API_KEY')
VC_API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

