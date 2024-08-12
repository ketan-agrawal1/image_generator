import json
from django.http import JsonResponse
from .tasks import generate_image


def generate_images(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompts = data.get('prompts', [])
        if len(prompts) != 3:
            return JsonResponse({'error': 'Exactly 3 prompts are required'}, status=400)
        
        task_ids = [generate_image.delay(prompt) for prompt in prompts]
        
        return JsonResponse({'task_ids': task_ids}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
