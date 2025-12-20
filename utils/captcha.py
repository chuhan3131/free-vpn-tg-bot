import io
import random
import asyncio
from PIL import Image
from captcha.image import ImageCaptcha


async def generate_captcha() -> tuple:
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    captcha_text = ''.join(random.choices(chars, k=6))

    image = ImageCaptcha(width=280, height=90)
    data = image.generate(captcha_text)

    img = Image.open(data)
    image_bytes = io.BytesIO()
    img.save(image_bytes, format='PNG')
    image_bytes.seek(0)
    
    return image_bytes.getvalue(), captcha_text