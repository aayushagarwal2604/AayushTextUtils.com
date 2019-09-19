#I created this file
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
#   return HttpResponse('''<h1>Hello! This is Aayush Agarwal</h1>
#    <ol>
#       <li><a href="https://www.linkedin.com/feed/">My LinkedIn Feed </a></li>
#       <li><a href="https://drive.google.com/drive/my-drive">My Drive-Google Drive </a></li>''' )

def index(request):
    #return HttpResponse("Home")
    return render(request, "index.html")

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))

def analyze(request):
    djtext= (request.GET.get('text','default'))
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    #analyzed = djtext
    c=0
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        c=1
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        c=1
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        c=1
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        c=1
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
    if(c==1):
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("charcount ")
