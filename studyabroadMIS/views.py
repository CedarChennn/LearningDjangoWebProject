from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.template import loader
from django.urls import reverse
# Create your views here.
def index(request):
    # return render(request,'store/index.html')
    template = loader.get_template('index.html')
    context = {
        'context_test': "THis is a contest test",
    }
    return render(request, 'index.html', context)  
    # return HttpResponse(template.render(context,request))  # context和request位置不能交换！