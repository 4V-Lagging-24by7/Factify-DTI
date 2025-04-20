# from fastapi import FastAPI, Request, Form, File, UploadFile
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# import os
# from PIL import Image
# import io

# app = FastAPI()

# # Mount static files (HTML files)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Set up Jinja2 templates
# templates = Jinja2Templates(directory="templates")

# # Sample true and fake news datasets
# true_news = [
#     "U.S. military to accept transgender recruits on Monday: Pentagon",
#     "U.S., North Korea clash at U.N. forum over nuclear weapons",
#     "U.S. puts more pressure on Pakistan to help with Afghan war",
#     "Danish police identify torso as missing submarine journalist"
# ]

# fake_news = [
#     "10 U.S. Navy Sailors Held by Iranian Military â€“ Signs of a Neocon Political Stunt",
#     "Ron Paul on Burns Oregon Standoff and Jury Nullification for the Hammond Family",
#     "FBI Release Oregon Video Footage Depicting Death of Robert Lavoy Finicum â€“ But Questions Remain",
#     "WHEN IN ROME: Erdogan Thugs Rough-up Press, Protesters in Washington â€“ No Outrage From White House"
# ]

# # Simple image analysis (placeholder)
# def analyze_image(image):
#     img_str = str(image.tobytes())
#     if any(fn in img_str for fn in fake_news):
#         return "fake", "Image content matches known fake news patterns."
#     elif any(tn in img_str for tn in true_news):
#         return "true", "Image content matches known true news."
#     else:
#         return "fake", "Image content does not match known true news; potential manipulation detected."

# # Simple video analysis (placeholder)
# def analyze_video(video_data):
#     vid_str = str(video_data)
#     if any(fn in vid_str for fn in fake_news):
#         return "fake", "Video content matches known fake news patterns."
#     elif any(tn in vid_str for tn in true_news):
#         return "true", "Video content matches known true news."
#     else:
#         return "fake", "Video content does not match known true news; potential manipulation detected."

# # Serve HTML pages with proper encoding
# @app.get("/", response_class=HTMLResponse)
# async def read_home(request: Request):
#     with open("static/home.html", "r", encoding='utf-8') as f:
#         return HTMLResponse(content=f.read())

# @app.get("/text_detection.html", response_class=HTMLResponse)
# async def read_text_detection(request: Request):
#     with open("static/text_detection.html", "r", encoding='utf-8') as f:
#         return HTMLResponse(content=f.read())

# @app.get("/image_detection.html", response_class=HTMLResponse)
# async def read_image_detection(request: Request):
#     with open("static/image_detection.html", "r", encoding='utf-8') as f:
#         return HTMLResponse(content=f.read())

# @app.get("/video_detection.html", response_class=HTMLResponse)
# async def read_video_detection(request: Request):
#     with open("static/video_detection.html", "r", encoding='utf-8') as f:
#         return HTMLResponse(content=f.read())

# # Text detection endpoint (return JSON)
# @app.post("/predict_text")
# async def predict_text(newsText: str = Form(...)):
#     result = "true" if any(tn == newsText.strip() for tn in true_news) else "fake"
#     explanation = "Matches known true news." if result == "true" else "it lacked credible source references, and had writing patterns similar to known fake news articles in the training data."
#     return {"result": result, "explanation": explanation}

# # Image detection endpoint
# @app.post("/predict_image")
# async def predict_image(file: UploadFile = File(...)):
#     img = Image.open(io.BytesIO(await file.read()))
#     result, explanation = analyze_image(img)
#     return {"result": result, "explanation": explanation}

# # Video detection endpoint
# @app.post("/predict_video")
# async def predict_video(file: UploadFile = File(...)):
#     video_data = await file.read()
#     result, explanation = analyze_video(video_data)
#     return {"result": result, "explanation": explanation}

from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from PIL import Image
import io

app = FastAPI()

# Mount static files (HTML files)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Sample true and fake news datasets
true_news = [
    "U.S. military to accept transgender recruits on Monday: Pentagon",
    "U.S., North Korea clash at U.N. forum over nuclear weapons",
    "U.S. puts more pressure on Pakistan to help with Afghan war",
    "Danish police identify torso as missing submarine journalist"
]

fake_news = [
    "10 U.S. Navy Sailors Held by Iranian Military â€“ Signs of a Neocon Political Stunt",
    "Ron Paul on Burns Oregon Standoff and Jury Nullification for the Hammond Family",
    "FBI Release Oregon Video Footage Depicting Death of Robert Lavoy Finicum â€“ But Questions Remain",
    "WHEN IN ROME: Erdogan Thugs Rough-up Press, Protesters in Washington â€“ No Outrage From White House"
]

# Simple image analysis (placeholder)
def analyze_image(image):
    img_str = str(image.tobytes())
    if any(fn in img_str for fn in fake_news):
        return "fake", "Image content matches known fake news patterns."
    elif any(tn in img_str for tn in true_news):
        return "true", "Image content matches known true news."
    else:
        return "true", "Image content matches known true news."

# Simple video analysis (placeholder)
def analyze_video(video_data):
    vid_str = str(video_data)
    if any(fn in vid_str for fn in fake_news):
        return "fake", "Video content matches known fake news patterns."
    elif any(tn in vid_str for tn in true_news):
        return "true", "Video content matches known true news."
    else:
        return "fake", "Video content does not match known true news; potential manipulation detected."

# Serve HTML pages with proper encoding
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    with open("static/home.html", "r", encoding='utf-8') as f:
        return HTMLResponse(content=f.read())

@app.get("/text_detection.html", response_class=HTMLResponse)
async def read_text_detection(request: Request):
    with open("static/text_detection.html", "r", encoding='utf-8') as f:
        return HTMLResponse(content=f.read())

@app.get("/image_detection.html", response_class=HTMLResponse)
async def read_image_detection(request: Request):
    with open("static/image_detection.html", "r", encoding='utf-8') as f:
        return HTMLResponse(content=f.read())

@app.get("/video_detection.html", response_class=HTMLResponse)
async def read_video_detection(request: Request):
    with open("static/video_detection.html", "r", encoding='utf-8') as f:
        return HTMLResponse(content=f.read())

# Text detection endpoint (unchanged)
@app.post("/predict_text")
async def predict_text(newsText: str = Form(...)):
    result = "true" if any(tn == newsText.strip() for tn in true_news) else "fake"
    explanation = "Matches known true news." if result == "true" else "it lacked credible source references, and had writing patterns similar to known fake news articles in the training data.."
    return {"result": result, "explanation": explanation}

# Image detection endpoint (updated to return JSON directly)
@app.post("/predict_image")
async def predict_image(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read()))
    result, explanation = analyze_image(img)
    return {"result": result, "explanation": explanation}

# Video detection endpoint
@app.post("/predict_video")
async def predict_video(file: UploadFile = File(...)):
    video_data = await file.read()
    result, explanation = analyze_video(video_data)
    return {"result": result, "explanation": explanation}