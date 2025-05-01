from PIL import Image

def purple_tint(image: Image.Image) -> Image.Image:
    """
    Apply a purple tint to the image.
    """
    # Create a purple overlay
    purple_overlay = Image.new('RGB', image.size, (128, 0, 128, 128))
    
    # Blend the original image with the purple overlay
    tinted_image = Image.blend(image.convert('RGB'), purple_overlay, alpha=0.3)
    
    return tinted_image

def transparency_filter(image: Image.Image) -> Image.Image:
    """
    Apply a transparency filter to the image.
    """
    # Convert the image to RGBA if not already in that mode
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    datas = image.getdata()

    new_data = []
    for item in datas:
        # Change all white (also shades of whites) pixels to transparent
        if item[0] in list(range(245, 256)):    # ranges of white to choose from
            new_data.append((255, 255, 255, 0))  # Change to transparent
        else:
            new_data.append(item)
    
    image.putdata(new_data)
    return image


def filter(image: Image.Image, filter_type: str) -> Image.Image:
    """
    Apply a filter to the image based on the filter type.

    """
    filters = {
        'PURPLE_TINT': purple_tint,
        'TRANSPARENT': transparency_filter
    }
    
    if filter_type in filters:
        return filters[filter_type](image)
    else:
        raise ValueError(f"Unknown filter type: {filter_type}")