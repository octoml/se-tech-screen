import os
from octoai.clients.image_gen import Engine, ImageGenerator

if __name__ == "__main__":
    image_gen = ImageGenerator(token=os.environ.get("OCTOAI_TOKEN"))
    image_gen_response = image_gen.generate(
        engine=Engine.SDXL,
        prompt="A photo of a cute cat astronaut in space",
        negative_prompt="Blurry photo, distortion, low-res, poor quality",
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
    images = image_gen_response.images

    for i, image in enumerate(images):
        image.to_file(f"result{i}.jpg")