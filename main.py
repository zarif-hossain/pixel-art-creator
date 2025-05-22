import sys
from PIL import Image
from apply_filter import filter

def create_pixel_art(image_path: str, output_image_path: str, 
                     pixel_size: int, filter_type=None) -> None:
    # Open the original image and convert it to RGB
    img = Image.open(image_path).convert('RGB')
    
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
    
    # Apply filter if provided
    if filter_type:
        img = filter(img, filter_type)

    # Save the pixel art image
    img.save(output_image_path, 'PNG')  # Save the pixel art image
    print(f"Pixel art saved as {output_image_path}")
    sys.exit(0)


if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        print("Usage: python pixel_art_generator.py <input_image_path> "
        "<output_image_path> <pixel_size> [optional:<filter_type>]")

        print("Example: python pixel_art_generator.py input.jpg output.png 16 TRANSPARENT")
        print("Example: python pixel_art_generator.py input.jpg output.png 16")
        sys.exit(1)

    # Get the command line arguments
    input_image_path = sys.argv[1]  # Path to the input image
    output_image_path = sys.argv[2]  # Path to save the pixel art image
    pixel_size = sys.argv[3]  # Size of the pixels in the pixel art

    if len(sys.argv) == 5:
        filter_type = sys.argv[4]
        create_pixel_art(input_image_path, output_image_path, int(pixel_size), filter_type)
    elif len(sys.argv) == 4:
        filter_type = None
        create_pixel_art(input_image_path, output_image_path, int(pixel_size))
