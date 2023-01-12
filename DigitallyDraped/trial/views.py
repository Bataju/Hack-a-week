from django.shortcuts import render
from django.http import HttpResponse
import openai
import json

openai.api_key = "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"

def index(request):
    if request.method == 'POST':
        description = request.POST['description']

        # Use the text input as the prompt for the API
        response = openai.Image.create(
            prompt=description,
            n=1,
        )

        j_response=json.dumps(response)
        parsed_response = json.loads(j_response)
        data = parsed_response["data"][0]
        image_url=data['url']
        
        return render(request, 'trial\image.html', {'image_url': image_url})
    else:
        return render(request, 'trial\index.html')