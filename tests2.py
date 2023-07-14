import random

def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_hex = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return color_hex

# Generate a random color
color = generate_random_color()
print("Random Color:", color)
