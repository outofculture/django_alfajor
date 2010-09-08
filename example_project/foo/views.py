from django.shortcuts import render_to_response
from foo.models import Foo

def foocount(request):
    return render_to_response('foo/foocount.html', {'foocount': Foo.objects.count()})

def index(request):
    return render_to_response('foo/index.html')
