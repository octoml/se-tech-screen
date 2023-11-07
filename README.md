# Technical Screen | Create an Image Generation Demo App with Streamlit, Powered by OctoAI 🦑
__Time Budget__: 2-4 hours

**Table of Contents**

- [Instructions](#Instructions)
- [Getting Started with OctoAI](#Getting-Started)
  - [Create an OctoAI Account](#Create-an-OctoAI-Account)
  - [OctoAI Docs](#OctoAI-Docs)
  - [Get an Application Token](#Get-an-Application-Token)
  - [Demo Image Generation Apps (examples)](#Demo-Image-Generation-Apps-examples)
- [Basic Image Gen Examples](#Basic-Image-Gen-Examples)
  - [Generating with Text-to-Image](#Generating-with-Text-to-Image)
  - [Text-to-image | Customization](#Text-to-image--Customization)
    - [Apply a style Preset](#Apply-a-style-Preset)
    - [Apply a LoRA](#Apply-a-LoRA)
  - [Text-to-image | Code building blocks](#Text-to-image--Code-building-blocks)
- [Bonus Points](#Bonus-Points)
  - [Upload and apply a custom asset](#Upload-and-apply-a-custom-asset)
  - [Use other models in your app](#Use-other-models-in-your-app)

## Instructions  🖥️ 👓 📑

Build a demo python application for a prospect or customer that demonstrates the power and value of OctoAI's Image Generation vertical solution, powered by SDXL 1.0. 

You can use any demo application framework you like. We are fond of Streamlit and Gradio. 

When you are finished, please save and check-in your application code (as a git branch), and be prepared to give a brief presentation on what you built.


> * What is the use case you picked? Why?
> 
> * What is the business problem you were trying to solve?
> 
> * What is the technical problem you were trying to solve?
> 
> * How did you solve it?
> 
> * Tell us about anything else that helps a prospect or customer understand the value of OctoAI's image generation vertical solution, showcasing the speed and versatility of the platform

## Getting Started
### Create an OctoAI Account


* Go to [octoai.cloud ](https://octoai.cloud/docs) and create a user to get started.
*  Most of the tools you will need to complete this exercise can be found within the *Image Generation Solution* section of the platform, which can be accessed via the dropdown at the top of the page. 

> __NOTE__: We provide all new customers and users with free credit to get started. If you hit a limit, let us know, and we will lift the cap for you. 😎

### OctoAI Docs 
* [OctoAI Docs](https://docs.octoai.cloud/docs)
* [Image Generation](https://docs.octoai.cloud/docs/stable-diffusion-guide)
* [OctoAI CLI & Python SDK](https://docs.octoai.cloud/docs/installation-links)

### Get an Application Token
To use the SDK or the CLI, navigate to User Settings (located in the upper right-hand corner of the UI) and generate an account token. Save this token as an environment variable in your terminal.


<img src="images/new_token.png" alt="Alt Text" width="300" />


```bash
OCTOAI_TOKEN=<my_new_token>
```

### Demo Image Generation Apps (examples)
 Our Developer Experience team has been steadily building out new demo apps, many of which are directed at creative and brand-focused content for e-commerce use cases. The Lightbox App (below) combines the best of OctoAI and the Image Generation solution to deliver a compelling e-commerce solution. The Stable Diffusion community at large is another great resource for inspiration. I've included some examples to get you started.

> <a href="https://www.loom.com/share/778a0bbf5d69474a8faf19d41e2fcb19"> Product-placement Lightbox App</a>


> SDXL 1.0 Community Examples
> * <a href="https://www.youtube.com/watch?v=LBTAT5WhFko">Create Ads with Automatic 1111+SDXL</a> 
> * <a href="https://mybyways.com/blog/scale-and-composite-latents-with-sdxl">Scale and Composite Latents with SDXL</a>

> Launch bare-bones starter app powered by OctoAI Image Gen

```bash
pip install -r requirements.txt # installs streamlit, octoai-sdk, and pydantic
streamlit run eg_app.py
```

## Basic Image Gen Examples
__NOTE__: The UI is designed to be self-explanatory and intuitive. Beyond this point, I've provided a basic examples of how to use the the Image Generation Solution's *Text-to-Image* modality. However, the best way to learn is to play around within the UI to get a feel for what's possible.

### Generating with Text-to-Image
To generate your first image, follow these steps:

* Login to OctoAI (https://octoai.cloud) and click "Try Image Gen Solution". This will launch a Demo page for gernerating SDXL images from text prompts. 
* Click the "Generate" button to generate an image from the default prompt.
* Edit the prompt to generate different images. 

### Text-to-image | Customization
Customized image outputs can be achieved a number of different ways, by varying degrees of complexity. The most basic way to customize an image is to hardcode the start or end of the text prompt, which can reprooduce the same desired aesthetic or style, if done correctly. 

To achieve the best possible results, you can apply a combination of prompts, styles, LoRAs, textual inversions, and toggle outputs with other parameters. 

#### Apply a style Preset
Apply a style from the "Style Preset" dropdown in the left-hand navigation bar and click generate. The "space cat" example prompt will now render acording to the style you selected.

#### Apply a LoRA
LoRAs (sometimes called "fine tunes") are a resource-efficient way of achieving a very specific aesthetic or style, that may not be possible with a style preset or any amount of prompt engineering. 

For example, you may want to generate a space cat wearing a particular clothing brand or drinking a specific brand of soda. To reproduce this type of output without retraining the full model, you can apply a LoRA. 

1. To use LoRAs, click the "LoRAs" tab in the left-hand navigation bar and select one of the pre-loaded public loras. 
2. The weight toggle adjusts the amount of influence the Lora has on the image.
3. Click "Generate" to generate an image with the selected Lora.


### Text-to-image | Code building blocks
You will have noticed already that the UI creates a code snippet each time you update your model input parameters. When you are happy with your image results, you can easily copy the code snippet to begin building your own custom application.


## Bonus Points
### Upload and apply a custom asset
<a href="https://octoai.cloud/assets?type=lora&public=false"> Upload a custom asset via the Asset Library UI</a> to the OctoAI platform and use it in your demo app. A LoRA is simple, extensible way to customize the base SDXL model and resultant image outputs. You can find loads of SD community created LoRAs at civitai.com.

<img src="images/asset_lib.png" alt="Alt Text" width="300" />

### Use other models in your app
Call other models in your demo app to exert maximum control over resultant image. For example, you can use a large-language model, such as Llama-2-13, to improve the quality of your prompts. 

__NOTE__: You will need to spin up replica, which is not part of the Image Gen service. This will burn through credits more quickly. Please let us know if you need more credit hours.

Additional model endpoints can be found in the <a href="https://octoai.cloud/models">Example Models</a> page, under the "Compute Service" drop-down at the top of the UI. 

<img src="images/models_page.png" alt="Alt Text" width="300" />

You may be directed to create an endpoint for the model to secure the hardware resources neccesary to run it. 

Follow the instructions to create the endpoint, setting the number of min/max replicas, the hardware type, and the timeout. You shouldn't need more than a few replicas. I recommend using a10gs as these are cost-effective and plentiful.

<img src="images/deployment_settings.png" alt="Alt Text" width="300" />

At last, you will be directed to the model's endpoint page. 