# Solutions Engineer Tech Evaluation

## Instructions
Build a demo python application for a prospect or customer that demonstrates the power and value of OctoAI's image generation vertical solution, powered by SDXL 1.0, using Streamlit or Gradio. 

 Our Developer Experience team has been steadily building out new demo apps, many of which are directed at creative and brand-focused content for e-commerce use cases. The Stable Diffusion community at large is another great resource for inspiration.

**Product-placement Lightbox App**

<a href="https://www.loom.com/share/778a0bbf5d69474a8faf19d41e2fcb19?sid=21c838f0-53d5-4fe8-837e-e1606a3fa3d3"> </a>

**SDXL 1.0 Community Examples**
- Eg 1
- Eg 2
- Eg 3

**A Basic Streamlit app powered by OctoAI**
Run a basic streamlit app and checkout the code:

```bash
streamlit run eg_app.py
```

## The Basics
You will walk us through the the demo app you built. Be prepared to talk about the following:
- What was the use case? Why?
- What was the business problem you were trying to solve? 
- What was the technical problem you were trying to solve?
- How did you solve it?
- Anything else that helps a prospect or customer understand the value of OctoAI's image generation vertical solution, showcasing the speed and versatility of the platform.

## Bonus Points
### Upload and apply a custom asset
<a href="https://octoai.cloud/assets?type=lora&public=false"> Upload a custom asset via the Asset Library UI</a> to the OctoAI platform and use it in your demo app. A LoRA is probably the simplest, most extensible way to customize your image output. You can read more about this in the Quickstart below. 

<img src="images/asset_lib.png" alt="Alt Text" width="300" />

### Use other models in your app
Call other models in your demo app to exert maximum control and effect over the output image. For example, you can use a large-language model, such as llama, to improve the quality of your prompts. 

* Additional model endpoints can be found in the <a href="https://octoai.cloud/models">Example Models</a> page, under the "Compute Service" drop-down at the top of the UI. 

<img src="images/models_page.png" alt="Alt Text" width="300" />

You may be directed to create an endpoint for the model to secure the hardware resources neccesary to run it. 

Follow the instructions to create the endpoint, setting the number of min/max replicas, the hardware type, and the timeout. You shouldn't need more than a few replicas—I recommend using a10gs as these are cost-effective and plentiful.

## Quickstart: OctoAI's Image Generation Vertical Solution

### Basic Usage using Text-to-Image
To generate your first image, follow these steps:
* Login to OctoAI (https://octoai.cloud) and click "Try Image Gen Solution". This will launch a Demo page for gernerating SDXL images from text prompts. 
* Click the "Generate" button to generate an image from the default prompt.
* Edit the prompt to generate different images. 

### OctoAI Docs 

* [OctoAI Docs](https://docs.octoai.cloud/docs)
* [OctoAI CLI](https://octoai.cloud/demo/image-gen)
* [OctoAI Python SDK](https://octoai.cloud/demo/image-gen)

__NOTE__: The UI is designed to be self-explanatory and intuitive. Beyond this point, I've provided a very brief overview of the the Image Generation Solution's *Text-to-Image* modality. However, the best way to learn is to play around with the UI and see what you can create.


### Text to image | Customization
Customized image outputs can be achieved a number of different ways, by varying degrees of complexity. The most basic way to customize an image is hardcode part of the text prompt, producing similiar results each query. To achieve the best possible results, you can apply a combination of prompts, styles, LoRAs, textual inversions, and other parameters. 

#### Apply a style Preset
Apply a style from the "Style Preset" dropdown in the left-hand navigation bar and click generate. Your space-cat example will now render acording to the style you selected.

#### Apply a LoRA
LoRAs (sometimes called "fine tunes") are a resource-efficient way of achieving a very specific aesthetic or style, that may not be possible with a style preset. For example, you may want to generate a space-cat wearing a particular clothing brand or drinking a particular brand of soda. To reproduce this type of output without retraining the model, you can apply a LoRA. You can read more about LoRA's here. 

1. To use LoRAs, click the "LoRAs" tab in the left-hand navigation bar and select one of the pre-loaded public loras. 
2. The weight toggle adjusts the amount of influence the Lora has on the image.
3. Click "Generate" to generate an image with the selected Lora.


### Text to image | Code building blocks
You will have noticed already that the UI creates a code snippet each time you update your model input parameters. When you are happy with your image results, you can easily copy the code snippet to begin building your own custom application.





