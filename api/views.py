from django.http import JsonResponse
from django.shortcuts import render
import requests
#from .gpt import generate_text


def generate_images(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        api_key = 'gzolY1EtvWzTnyBGYhJdiYylC3t6kkF6SEcy0tbhC4E8YcfnpTmdBqM6SHag'
        url = 'https://stablediffusionapi.com/api/v3/text2img'
        headers = {'Content-Type': 'application/json'}
        data = {
            'key': api_key,
            'prompt': prompt,
            'samples': 1,
            'negative_prompt': '',
            'width': 512,
            'height': 512,
            'prompt_strength': 1.0,
            'num_inference_steps': 20,
            'guidance_scale': 7.5,
            'enhance_prompt': 'yes',
            'seed': None,
            'webhook': None,
            'track_id': None,
            'safety_checker': 'yes',
        }
        response = requests.post(url, headers=headers, json=data)
        json_response = response.json()
        if response.ok and 'output' in json_response and len(json_response['output']) > 0:
            image_url = json_response['output'][0]
            print(image_url)
            return JsonResponse({'image_url': image_url})
        else:
            print(json_response)
            return None
    else:
        return render(request, 'generate_images.html')


def generate_text_view(request):
    if request.method == 'POST':
        prompt = request.POST['prompt']
        generated_text = generate_text(prompt)
        return JsonResponse({'generated_text': generated_text})
    return render(request, 'gpt.html')


def generate_text(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
        # generate the text
        text = 'This is the generated text.'

        # send the text back to the client
        data = {
            'text': text
        }
        return JsonResponse(data)
    return render(request, 'generate_text.html')