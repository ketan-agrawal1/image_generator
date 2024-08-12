from celery import shared_task
import requests
import os


@shared_task
def generate_image(prompt):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    headers = {
        "Authorization": f"Bearer {os.getenv('STABILITY_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "width": 1024,
        "height": 1024
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()
