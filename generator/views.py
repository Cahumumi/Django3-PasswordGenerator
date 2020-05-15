from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
              return render(request, 'generator-homepage/home.html',{'password':'huanqwkhofnlq19124'})
def about(request):
              return render(request, 'generator-homepage/about.html')              
def password(request):
              
              characters = list('abskjfuohqwrlncpokmnji')
              if request.GET.get('uppercase'):
                            characters.extend(list('ABCHDJUWNFLKASOIFJNKLJWUIRS1235096834'))
              if request.GET.get('special'):
                            characters.extend(list('!@#$%^&*'))
              if request.GET.get('numbers'):
                            characters.extend(list('123456789'))
              length = int(request.GET.get('length'))
              thepassword = ''
              for x in range (length):
                            thepassword += random.choice(characters)
              return render(request, 'generator-homepage/password.html',{'password': thepassword })
