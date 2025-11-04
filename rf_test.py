import os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ROBOFLOW_API_KEY")
MODEL_ID = os.getenv("ROBOFLOW_MODEL_ID", "mould-detection-aaron/8")

url = f"https://detect.roboflow.com/{MODEL_ID}"
params = {"api_key": API_KEY}
with open("test-mold.JPG", "rb") as f:
    files = {"file": f}
    r = requests.post(url, files=files, params=params, timeout=60)

print("Status:", r.status_code)
print("Response:", r.json())


