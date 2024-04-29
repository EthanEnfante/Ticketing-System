from django.shortcuts import render

# Create your views here.
def index(request):
    context = 'Hello World!'
    return render(request, template_name='submission_form/index.html', context=context)