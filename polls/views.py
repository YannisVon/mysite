# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def login(request):
    username=request.GET.get('username')
    if request.method=='GET':
        print(1234)
        #print(username)

    password=request.GET.get('password')
    print(password)

    return HttpResponse()