import gradio as gr
from PIL import Image
import cv2
import tempfile
import base64
import requests

#Image parameter must be in b64 format as currently ollama cant accept raw images
def call_ollama(prompt, image_b64=None): 
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llava", #Model name 
        "prompt": prompt,
        "stream" : False
    }
    if image_b64:
        payload["images"] = [image_b64]

    #Forward request to Ollama
    response = requests.post("http://localhost:11434/api/generate", json=payload, stream=False) #Default port number for llama, turn stream off in case of decode error
    return response.json().get("response", "Failed to get response.")

# Converts a PIL image(binary format) to base64 (way to represent binary format as text) string for API transmission as JSON Transmission only allows for raw text.

def encode_image(image: Image.Image):
    buffered = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    #save pil image in jpg format
    image.save(buffered.name, format="JPEG")
    #open in rb = read bytes format 
    with open(buffered.name, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8") #Converts the binary bytes of the image into a base64-encoded string.

def extract_frame(video_path):
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()
    cap.release()
    if success:
        return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) #convert bgr format that cv uses to rgb format that PIL Requires.
    return None

#upload function
def process_input(image, video):
    if image is not None:
        img = Image.fromarray(image)
    elif video is not None:
        img = extract_frame(video)
        if img is None:
            return "Failed to extract frame"
    else:
        return "Please upload an image or a video."

    image_b64 = encode_image(img)
    system_prompt = (
    "You are a visual content analyzer. You will be given an image or a video frame.\n"
    "If the content has a clear main subject (like a product, person, or object in focus), center your output around it.\n"
    "Otherwise, describe the scene in general.\n\n"
    "Your output should strictly follow this format:\n\n"
    "Title: <one short line summarizing the main subject>\n"
    
    "Description: <Must have 2 or 3 sentences marketing-style description highlighting what is being shown. >\n"
    
    "Features:\n"
    "- <bullet point 1>\n"
    "- <bullet point 2>\n"
    "- <bullet point 3>\n\n"
    
    "(Must have 3 feature points. Include more points if it is highly relevant. Be concise and accurate.)"
    
    "IMPORTANT RULES: Description must have at least 2 sentences. Features must have at least 3 bullet points"
)


    response = call_ollama(system_prompt, image_b64=image_b64)
    return response

#Gradio Interface

iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.Image(label="Upload Image", type="numpy"),
        gr.Video(label="or Upload Video")
    ],
    outputs=gr.Textbox(label="Generated Output"),
    title="Image (or Video) Analyzer",
    
)

iface.launch()
