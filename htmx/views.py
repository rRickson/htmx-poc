from django.shortcuts import render
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sample_post(request, *args, **kwargs):  
    

    if request.method == "POST":
        print(f'{request.POST = }')  
        name = request.POST.get('name', '')  
        email = request.POST.get('email', '')  
        favourite_colour = request.POST.get('favourite_color', '')  

        if name and email and favourite_colour:  
            return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')  
        else:  
            return HttpResponse('<p class="error">Please provide both name and email and favourite color.❌</p>')  
    if request.method == "DELETE":
        return HttpResponse('<p class="error">DELETE.❌</p>')  
    if request.method == "PUT":
        return HttpResponse('<p class="error">PUT.❌</p>')  
    


def example(request):  
    return render(request, 'first_page.html')