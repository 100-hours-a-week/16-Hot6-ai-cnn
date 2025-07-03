from fastapi import FastAPI
from pydantic import BaseModel
import requests, os, logging
from services.desk_classify import Desk_classifier
from routers import healthcheck

app = FastAPI()

app.include_router(healthcheck.router)

logger = logging.getLogger(__name__)

class ImageRequest(BaseModel):
    initial_image_url: str
    # concept: str

@app.post("/classify")
def classify_image(req: ImageRequest):
    
    image_url = req.initial_image_url
    img_bytes_data = requests.get(image_url).content
    
    classifier = Desk_classifier()
    is_desk = classifier.predict(img_bytes_data)
    
    if not is_desk:
        return {
            "initial_image_url": image_url,
            "classify": "false"
        }
    
    return {
        "initial_image_url": image_url,
        "classify": "true"
    }

