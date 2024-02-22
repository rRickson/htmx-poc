from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

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
    


def widget(request,widget_type):
    print(widget_type)
    template = loader.get_template(f'components/widget{widget_type}.html')
    html_content = template.render(None, request)

    return HttpResponse(html_content)

def landing(request):  
    return render(request, 'first_page.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def form_sign(request):
    return render(request, 'form.html')

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if name == "error":
            # If request method is not POST, return a JSON response with an error
            return HttpResponse('<p class="error">Oops Something went wrong.❌</p>'  , status=405)

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Form submitted successfully!'})
