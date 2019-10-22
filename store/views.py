from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponseRedirect,HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Question,Choice
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
    #return render(request,'store/detail.html',{'question':question})
    #return HttpResponse("You're looking at the results of question:" +"<h1>"+str(question)+"</h1>")
    question = get_object_or_404(Question,pk=question_id)
    #return HttpResponse("You're looking at the results of question:" +"<h1>"+str(question)+"</h1>")
    return render(request,'store/detail.html',{'question': question})
    # 对应的html中的注释，forloop.counter 指示 for 标签已经循环多少次。 POST 表单（它具有修改数据的作用），所以我们需要小心跨站点请求伪造对内部 URL 的 POST 表单都应该使用 {% csrf_token %} 模板标签来预防

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    question = get_object_or_404(Question,pk=question_id)
    #return HttpResponse(response % question_id)
    return render(request,'store/results.html',{'question':question})


def vote(requset,question_id): 
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=requset.POST['choice'])  #request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。 这个例子中， request.POST['choice'] 以字符串形式返回选择的 Choice 的 ID。 request.POST 的值永远是字符串。
    except(KeyError,Choice.DoesNotExist):                           # request.POS后面是中括号
        return render(requset,'store/detail.html',     
                      {
                          'question':question,
                          'error_message':"You didn't select a choice.",
                      })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('store:results',args=(question_id,)))   # reverse 等价于'/stire/3(id)/results/'

