import sys
from PIL import Image

def create_pixel_art(image_path, output_image_path, pixel_size):
    # Open the original image
    img = Image.open(image_path)
    
    # Resize the image to create a pixelated effect
    img = img.resize(
        (img.width // pixel_size, img.height // pixel_size),
        Image.NEAREST
    )
    
    # Scale it back up to original size
    img = img.resize(
        (img.width * pixel_size, img.height * pixel_size),
        Image.NEAREST
    )
    
    img.save(output_image_path)  # Save the pixel art image


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python pixel_art_generator.py <input_image_path> <output_image_path> <pixel_size>")
        print("Example: python pixel_art_generator.py input.jpg output.png 16")
        sys.exit(1)

    input_image_path = sys.argv[1]  # Path to the input image
    output_image_path = sys.argv[2]  # Path to save the pixel art image
    pixel_size = sys.argv[3]  # Size of the pixels in the pixel art

    # Create and save pixel art
    create_pixel_art(input_image_path, output_image_path, int(pixel_size))
    
    # Print success message
    print(f"Pixel art saved as {output_image_path}")