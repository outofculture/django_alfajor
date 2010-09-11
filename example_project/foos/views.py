from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from forms import FooForm
from models import Foo


def list(request):
    return render_to_response('list.html', {
        'foos': Foo.objects.all()
    })


def addfoo(request):
    foo = Foo(name="New Foo")
    foo.save()

    return HttpResponseRedirect(reverse("list"))


def editfoo(request, foo_id):
    foo = Foo.objects.get(id=foo_id)

    if request.method == 'GET':
        form = FooForm(instance=foo)

    if request.method == 'POST':
        form = FooForm(request.POST, instance=foo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("list"))
        
    return render_to_response('edit.html',
            { 'foo' : foo, 'form' : form, },
            context_instance=RequestContext(request))

   
def deletefoo(request, foo_id):
    foo = Foo.objects.get(id=foo_id)
    foo.delete()
        
    return HttpResponseRedirect(reverse("list"))
