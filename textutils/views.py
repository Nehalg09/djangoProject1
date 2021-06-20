#I have created this file-Nehal
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse('''<h1>Hello Home!</h1> <a href="https://www.google.com/">Google</a>''')
    #params={'name':'Nehal','occupation':'Software Engineer'}
    #return render(request,'index.html',params)
    return render(request,'index.html')

def about(request):
    return HttpResponse("About!")


def analyse(request):
    text=request.POST.get('text','default')
    flag=request.POST.get('removepunc','off')
    flag1=request.POST.get('fullcaps','off')
    flag2=request.POST.get('newlineremover','off')
    flag3=request.POST.get('spaceremover','off')
    flag4=request.POST.get('charcount','off')
    analyzed_string=''
    buffer_string=''
    if flag=='on':
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for i in text:
            if i not in punctuations:
                analyzed_string+=i
        buffer_string=analyzed_string
        #params={'purpose':'Remove Punctuation','analyzed_text':analyzed_string}
        # return render(request,'analyse.html',params)
    if flag1=='on':
        analyzed_string=''
        analyzed_string=str(buffer_string).upper()
        buffer_string=analyzed_string
        # params={'purpose':'UPPERCASE','analyzed_text':analyzed_string}
        # return render(request,'analyse.html',params)
    if flag2=='on':
        analyzed_string=''
        for i in buffer_string:
            if i != '\n' and i !='\r':
                analyzed_string+=i
        buffer_string=analyzed_string
        # params={'purpose':'New Line Remover','analyzed_text':analyzed_string}
        # return render(request,'analyse.html',params)
    if flag3=='on':
        analyzed_string=''
        for i in buffer_string:
            if i != ' ':
                analyzed_string+=i
        buffer_string=analyzed_string
        # params={'purpose':'Space Remover','analyzed_text':analyzed_string}
        # return render(request,'analyse.html',params)
    if flag4=='on':
        count=0
        for i in buffer_string:
            # if not str(i).isspace and i !='\n': 
                count+=1
                print(i,end='')
        # params={'purpose':'Character count','analyzed_text':count}
        # return render(request,'analyse.html',params)
    if analyzed_string=='':
        return HttpResponse("Error")
    else:
        params={'purpose':'multiple','analyzed_text':analyzed_string}
        return render(request,'analyse.html',params)

def aboutus(request):
    return render(request,'aboutus')

def contactus(request):
    return render(request,'contactus')
# def capitalizefirst(request):
#     return HttpResponse("Capitalize first! <a href='\'>Back</a>")

# def newlineremover(request):
#     return HttpResponse("New line remover! <a href='\'>Back</a>")

# def spaceremove(request):
#     return HttpResponse("Space remover! <a href='\'>Back</a>")

# def charcount(request):
#     return HttpResponse("char count! <a href='\'>Back</a>")



