from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    return render(request, 'survey/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    if ('count' in request.session) == False:
        request.session['count'] = 0
    request.session['count'] +=1
    return redirect('/finish')

def finish(request):
    if ('count' in request.session) == False:
        request.session['count'] = 0
    context = {
        'name' : request.session['name'],
        'location' : request.session['location'],
        'language' : request.session['language'],
        'comment' : request.session['comment'],
        'count' : request.session['count']
    }
    return render(request, 'survey/finish.html', context)
