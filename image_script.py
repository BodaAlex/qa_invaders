from PIL import Image, ImageDraw, ImageFont
import os

def generate_image(width, height, file_format, filename):
    # Create a blank image with the given width, height, and white background
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Prepare the text to be added (size in format width x height)
    text = f"{width}x{height}"

    # Define the font size as a percentage of the smaller dimension (width or height)
    font_size = min(width, height) // 10  # Font size is 10% of the smaller dimension

    # Load the font (default to a PIL built-in font if specific font is not available)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # You can change the font
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font if custom font fails

    # Get the bounding box of the text
    bbox = draw.textbbox((0, 0), text, font=font)

    # Calculate the width and height of the text from the bounding box
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate the position to center the text in the image
    position = ((width - text_width) // 2, (height - text_height) // 2)

    # Draw the text on the image
    draw.text(position, text, fill="black", font=font)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Save the image in the specified format
    img.save(filename, format=file_format.upper())
    print(f"Image saved as {filename}")
