from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Question
# Create your views here.
def index(request):
    # return render(request,'store/index.html')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('store/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'store/index.html', context)  
    # return HttpResponse(template.render(context,request))  # context和request位置不能交换！

def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    ##return render(request,'store/index.html',{'question':question})
    #return HttpResponse("You're looking at the results of question:" +"<h1>"+str(question)+"</h1>")
    question = get_object_or_404(Question,pk=question_id)
    return HttpResponse("You're looking at the results of question:" +"<h1>"+str(question)+"</h1>")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)