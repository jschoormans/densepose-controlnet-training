import torch
from diffusers import StableDiffusionXLPipeline
from PIL import Image
from diffusers import StableDiffusionXLControlNetPipeline, ControlNetModel, AutoencoderKL
from diffusers.utils import load_image, make_image_grid

controlnet = ControlNetModel.from_pretrained(
    "model_out/checkpoint-15000/controlnet",
    torch_dtype=torch.float16,
    use_safetensors=True
)
vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16, use_safetensors=True)
pipe = StableDiffusionXLControlNetPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    controlnet=controlnet,
    vae=vae,
    torch_dtype=torch.float16,
    use_safetensors=True
)
pipe = pipe.to("cuda")

control_image=Image.open('validation_images/000988787_densepose.jpg')
prompt = "a photo of a woman doing yoga"
image = pipe(prompt=prompt,
    negative_prompt="",
    image=control_image,
    controlnet_conditioning_scale=0.5,
).images[0]
image.save('sdxl_output.jpg')