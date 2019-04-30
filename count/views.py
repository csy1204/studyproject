from django.shortcuts import render

# Create your views here.
def index(request):
    result = 'no result'
    wordlen = 0
    if request.GET.get('injoon',False):
        result = request.GET['injoon']
        wordlen = len(result.split())
    return render(request, 'index.html', {'injoon_text': result, 'totalcount': wordlen})

def about(request):
    return render(request, 'about.html')