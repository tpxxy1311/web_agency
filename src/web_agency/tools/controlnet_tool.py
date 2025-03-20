import requests
import base64
from crewai.tools import tool

CONTROLNET_API_URL = "https://modelslab.com/api/v5/controlnet"
STABLEDIFFUSION_API_URL = "https://modelslab.com/api/v6/realtime/img2img"
API_KEY = "qhRdRd1nnj4euUSa2DGejDOTdrGiZUl5fCD10lik5eYfbPPfwmiAbYjuu5lT"  # Replace with your actual API key

@tool
def generate_wireframe(prompt: str) -> str:
    """
    Uses Stable Diffusion + ControlNet to generate a wireframe from a text description.
    
    Args:
        prompt (str): A detailed wireframe description.
        use_base64 (bool, optional): If True, encodes the local image as Base64 instead of using a URL.

    Returns:
        str: URL of the generated wireframe image or error message.
    """

    print(f"🔹 Sending request to API with prompt:\n{prompt}")  # Debugging
    


    # payload = {
    # "key": API_KEY,
    # "prompt": prompt,
    # "negative_prompt": "photographic, realistic, detailed UI, full color, blurry, distorted, abstract shapes",
    # "model_id": "boziorealvisxlv4",
    # "init_image": init_image,
    # "auto_hint": "yes",
    # "guess_mode": "no",
    # "strength": 0.8,
    # "controlnet_conditioning_scale": "0.7",
    # "guidance_scale": 7,
    # "tomesd": "yes",
    # "samples": 1,
    # "instant_response": "no",
    # "width": "1024",
    # "height": "720",
    # "num_inference_steps": 21,
    # "scheduler": "KarrasVeScheduler",
    # "controlnet_type": "mlsd",
    # "controlnet_model": "mlsd",
    # "upscale": "no"
    # }

    payload = {
    "key": API_KEY,
    "prompt": prompt,
    "negative_prompt": "photographic, realistic, detailed UI, full color, blurry, distorted, abstract shapes",
    "init_image": "https://imgur.com/a/ekHmbw7",
    "width": "1024",
    "height": "720",
    "samples": "1",
    "temp": False,
    "safety_checker": False,
    "strength": 0.7,
    }

    response = requests.post(STABLEDIFFUSION_API_URL, json=payload)
    
    try:
        data = response.json()
        print(f"🔹 API Response: {data}")  # Debugging: Print full API response

        if "output" in data:
            return f"Generated Wireframe: {data['output'][0]}"
        else:
            return f"Error: {data.get('message', 'Unknown API error')}"
    
    except Exception as e:
        return f"Error parsing API response: {str(e)}"
