from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def pricing(request):
  template = loader.get_template('pricing.html')
  return HttpResponse(template.render())

def worksingle(request):
  template = loader.get_template('work-single.html')
  return HttpResponse(template.render())

def work(request):
  template = loader.get_template('work.html')
  return HttpResponse(template.render())