from django.shortcuts import render
from django.http import HttpResponse
import openai
import json

openai.api_key = "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"

def index(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        age = request.POST['age']
        description = request.POST['description']

        generated_prompt = f"a plain background full body picture of a {gender} of {age} of slim-build wearing {description}"
 
        # Use the text input as the prompt for the API
        response = openai.Image.create(
            prompt=generated_prompt,
            n=2,
        )

        j_response=json.dumps(response)
        parsed_response = json.loads(j_response)
        data = parsed_response["data"][0]
        image_url=data['url']

        return render(request, 'trial\image.html', {'image_url': image_url, 'description': description})
    else:
        return render(request, 'trial\index.html')