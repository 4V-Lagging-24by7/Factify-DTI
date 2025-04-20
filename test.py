from PIL import Image
import pytesseract

# Replace with a path to an image file
image_path = "C:/Users/nehal/Downloads/image_det/Screenshot 2025-04-12 162050.png"
image = Image.open(image_path)
text = pytesseract.image_to_string(image)
print(text)