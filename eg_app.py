# Simple streamlit starter page
import streamlit as st
from octoai.client import Client
from octoai.clients.image_gen import Engine, ImageGenerator
import os
from pydantic import BaseModel
from typing import Dict
import random

# Initialize the client
OCTOAI_TOKEN = os.getenv("OCTOAI_TOKEN")
client = Client(token=OCTOAI_TOKEN)

# Base model schema for SDXL requests
class SDXLRequest(BaseModel):
    prompt: str
    seed: int
    negative_prompt: str
    loras: Dict[str, float]
    width: int
    height: int
    num_images: int
    sampler: str
    steps: int
    cfg_scale: int
    use_refiner: bool
    high_noise_frac: float
    style_preset: str
    
def random_seed():
    return random.randint(0, 10000000000)
    
base_payload = SDXLRequest(
    prompt="A photo of a cute cat astronaut in space",
    seed=random_seed(),
    negative_prompt="Blurry photo, distortion, low-res, poor quality",
    loras={},
    width=1024,
    height=1024,
    num_images=1,
    sampler="DDIM",
    steps=30,
    cfg_scale=12,
    use_refiner=True,
    high_noise_frac=0.8,
    style_preset="base",
)

# Helper funcs for the cli
from pathlib import Path
image_path = Path("sd_images")
image_path.mkdir(exist_ok=True)

def imagen_request(image_path: str):
    image_gen = ImageGenerator(token=os.environ.get("OCTOAI_TOKEN"))
    image_gen_response = image_gen.generate(
        engine = Engine.SDXL,
        prompt = base_payload.prompt,
        negative_prompt = base_payload.negative_prompt,
        loras = base_payload.loras,
        width = base_payload.width,
        height = base_payload.height,
        num_images = base_payload.num_images,
        sampler = base_payload.sampler,
        steps = base_payload.steps,
        cfg_scale = base_payload.cfg_scale,
        use_refiner = base_payload.use_refiner,
        high_noise_frac = base_payload.high_noise_frac,
        style_preset = base_payload.style_preset
    )
    images = image_gen_response.images
    #output images to list
    _images = []
    for i, image in enumerate(images):
        img_path = f"{image_path}/result{i}.jpg"
        image.to_file(img_path)
        _images.append(image.to_bytes())
    return _images
    
    
# Sidebar
generate_button = st.sidebar.button("Generate Image")
# increase number images returned
num_images = st.sidebar.slider("Number of images", 1, 10, 1)
base_payload.num_images = num_images

# change up the prompt
prompt = st.sidebar.text_input("Prompt", value=base_payload.prompt)
base_payload.prompt = prompt


# Page Layout

# Container 1 - Run, Customize, Control
container1 = st.container()
tab1, tab2, tab3 = container1.tabs(["Kick the tires, light the fires", "Upload your control image", "Upload your image"])


container2 = st.container()
col1, col2 = container2.columns(2)


def main():
    with container1:
        if generate_button:
            st.spinner("Generating Image")  
              
        with col1:
            st.write(base_payload.model_dump())
        
        with col2:
            if generate_button:
                images = imagen_request(image_path)
                # Create a list of images to display
                
                st.image(images)
    
    
    # container 1 - "Kick the tires, light the fires"
    
    with container2:
        with tab1:
            st.write("## Kick the tires, light the fires")
            st.markdown("""
            1. Generate an image using the default settings in displayed payload. Click the 'Generate' button to generate an image.
            2. Change up the prompt to generate a different image. Try something like, \"A pyschedelic toad god in a primordial nightmare forest\""
            """)
        
        with tab2:
            st.write("## Customize using an Asset")
            st.write("""The simplest way to begin stylizing an image or images in a predictable, uniform way, is to add a style preset to the input params.
                     You can see a full list of available styles in the [Image Generation text-to-image page](https://octoai.cloud/tools/image/text-to-image?engine=image%2Fstable-diffusion-xl-v1-0&mode=demo).)
                     You may have noticed by now that you can do many of the same tasks in the UI as you can in this app :)""")
            
            st.write("""Next up, let's apply a custom asset to the image. We'll download a custom asset, in this case, a LoRA, from 
                     civit.ai and upload it to the Asset Library using the SDK.""")
        
        with tab3:
            st.write("## Refine and control your image using a controlnet")
        

            
    


if __name__ == "__main__":
    main()