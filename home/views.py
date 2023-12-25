from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':'this is sent',   
    }
    # return HttpResponse("This is my homepage  ")
    return render(request, 'index.html',context)
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
