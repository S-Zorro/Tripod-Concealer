import cv2
import os
import argparse
import torch
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image
from utils.helper_functions import draw_circle

# Load the Stable Diffusion Inpainting model
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    revision="fp16",
    torch_dtype=torch.float16,
).to('cuda')  # Default device is set to 'cuda'

# Prompts for the inpainting model
prompt = "same floor, clean floor, remove objects, hide, completely hide, conceal the floor with the rectangular floor, same background,, detailed, high quality"
negative_prompt = 'mixed disrupted bulbs,switches, made up things, sheet,grass,new object, fan, objects, pieces, new, dirt, unclean floor, blur floor, mixing floor, low quality'

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Add a circle to an image.")
    parser.add_argument("-i", "--image_folder", required=True, help="Path to the image folder.")
    parser.add_argument("-r", "--radius", type=int, required=True, help="Radius of the circle for the mask.")
    parser.add_argument("-d", "--device", default="cuda", choices=["cuda", "cpu"], help="Device for processing ('cuda' or 'cpu'). Default is 'cuda'.")
    args = parser.parse_args()
    
    # Set the device for processing
    device = torch.device(args.device)
    pipe.to(device)
    
    mask_image = draw_circle(image_path, args.radius)
    # Check if the input folder exists
    if not os.path.exists(args.image_folder):
        print("Error: The specified image folder does not exist.")
        return

    # Process each image in the folder
    for filename in os.listdir(args.image_folder):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(args.image_folder, filename)
            init_image = Image.open(image_path).resize((1024, 1024))
            image = pipe(prompt=prompt, negative_prompt=negative_prompt, image=init_image, mask_image=mask_image,
                         guidance_scale=20, height=1024, width=1024, num_inference_steps=20).images[0]
            image.save(f'covered_images/covered_{filename}')

if _name_ == "_main_":
    main()