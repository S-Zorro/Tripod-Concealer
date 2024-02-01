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
    cache_dir='./models/'
).to('cuda')
pipe.safetey_checker = None

# Prompts for the inpainting model
prompt = "same floor, clean floor, remove objects, hide, completely hide, conceal the floor with the rectangular floor, same background,, detailed, high quality"
negative_prompt = 'mixed disrupted bulbs,switches, made up things, sheet,grass,new object, fan, objects, pieces, new, dirt, unclean floor, blur floor, mixing floor, low quality'

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Add a circle to an image.")
    parser.add_argument("-i", "--image_path", required=True, help="Path to the input image.")
    parser.add_argument("-r", "--radius", type=int, required=True, help="Radius of the circle for the mask.")
    parser.add_argument("-d", "--device", default="cuda", choices=["cuda", "cpu"], help="Device for processing ('cuda' or 'cpu'). Default is 'cuda'.")
    args = parser.parse_args()

    # Set the device for processing
    device = torch.device(args.device)
    pipe.to(device)

    # Check if the input image exists
    if not os.path.exists(args.image_path):
        print("Error: The specified image file does not exist.")
        return

    # Process the input image
    image_path = args.image_path
    mask_image = draw_circle(image_path, args.radius)
    init_image = Image.open(image_path).resize((1024, 1024))
    image = pipe(prompt=prompt, negative_prompt=negative_prompt, image=init_image, mask_image=mask_image,
                 guidance_scale=20, height=1024, width=1024, num_inference_steps=12).images[0]

    # Uncomment the lines below if you want to resize the output image to 640x640
    # image = cv2.resize(np.asarray(image, dtype='uint8'), (640, 640), interpolation=cv2.INTER_CUBIC)
    # image = Image.fromarray(image)

    # Save the processed image
    output_path = f'outputs/covered_{os.path.basename(image_path)}'
    image.save(output_path)
    print(f"Processed image saved as {output_path}")

if __name__ == "__main__":
    main()
