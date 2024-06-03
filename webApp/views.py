from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login, logout

# admin(admin)
# user(user@8987)

def home(request):
  template = loader.get_template('home1.html')
  return HttpResponse(template.render())

# def login(request):
#   template = loader.get_template('login.html')
#   return HttpResponse(template.render())

def signup(request):
  template = loader.get_template('registration.html')
  return HttpResponse(template.render())

def loginUser(request):
   if request.method == 'POST':
   # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
   else: 
        return render(request, 'login.html', {'error': 'Invalid username or password'})
   
def logoutUser(request):
   logout(request)
   return redirect("/login")
