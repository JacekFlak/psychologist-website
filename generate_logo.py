from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with transparent background
img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw a circle (logo background) - blue colors matching the psychologist's website
draw.ellipse([10, 10, 190, 190], fill='#4A90E2', outline='#357ABD', width=6)

# Try to load font for emoji
try:
    emoji_font = ImageFont.truetype('seguiemj.ttf', 70)
except:
    try:
        emoji_font = ImageFont.truetype('C:/Windows/Fonts/seguiemj.ttf', 70)
    except:
        emoji_font = ImageFont.load_default()

# Try to load font for text
try:
    text_font = ImageFont.truetype('arial.ttf', 28)
except:
    try:
        text_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 28)
    except:
        text_font = ImageFont.load_default()

# Draw brain symbol - fits the psychologist theme
draw.text((100, 70), '🧠', fill='#FFFFFF', anchor='mm', font=emoji_font)

# Draw initials - MF for Maria Flak
draw.text((100, 145), 'MF', fill='#FFFFFF', anchor='mm', font=text_font)

# Save the file
img.save('logo.png')
print("Logo has been generated as logo.png")
