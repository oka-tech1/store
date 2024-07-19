from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import tools, contactus, nameofuser
from .forms import contactform



class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class details(ListView):
    model = tools
    template_name = 'details.html'
    
        
def order(request, id):
    orders = tools.objects.get(id=id)
    template = loader.get_template('order.html')
    context = {
        'orders': orders,
    }
    return HttpResponse(template.render(context, request))

    
def contact(request):
    if request.method =="POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    form = contactform()
            
    return render(request, 'contactform.html', {'form':form})        
    
    
def success(request):
    template = loader.get_template('success.html')
    return HttpResponse(template.render())    


def wallets(request):
    entries = nameofuser.objects.all()
    template = loader.get_template('home.html')
    context = {'entries': entries,}
    return HttpResponse(template.render(context, request))


def fund(request):
    template = loader.get_template('fundaccount.html')
    return HttpResponse(template.render())

def forum(request):
    template = loader.get_template('forum.html')
    return HttpResponse(template.render())
