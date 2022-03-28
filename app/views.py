"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Channel
from django.views import generic
from django.db.models import Q

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)

    """Load channels into the view"""
    chan = Channel.objects.order_by('pdb')
    numChan = Channel.objects.all().count()
    ORF3a = Channel.objects.filter(pdb__contains='7KJR')


    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Get in touch with us!',
            'year':datetime.now().year,
            'numChan': numChan,
            'ORF3a': ORF3a,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    numChan = Channel.objects.all().count()

    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'ChanFAD is a functional annotation database for ion channels.',
            'year':datetime.now().year,
            'numChan': numChan,
        }
    )

def search(request):
    assert isinstance(request, HttpRequest)

    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(pdb__icontains=query) | Q(species__icontains=query) | Q(geneName__icontains=query) | Q(description__icontains=query) | Q(ion__icontains=query) | Q(submitter__icontains=query) | Q(uniprot__icontains=query)
            results = Channel.objects.filter(lookups).distinct()
            context = {'results': results, 'submitbutton': submitbutton}
            return render(request, 'app/search.html', context)

        else:
            return render(request, 'app/search.html')

    else:
        return render(request, 'app/search.html')


        ''')'''

def resources(request):
    assert isinstance(request, HttpRequest)

    return render(
    request,
    'app/resources.html',
        {
            'title':'Resources',
            'message':'Other ion channel related resources you may find useful',
            'year': datetime.now().year,
        }
    )

class ChannelListView(generic.ListView):
    model = Channel

class ChannelDetailView(generic.DetailView):
    model = Channel
