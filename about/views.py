from django.shortcuts import render, redirect

def index(request):
    return render(request, 'about/plengngen.html')

# Create your views here.
#from . forms import santriforms
#from . models import santri 

#def index(request):
#    posts = santri.objects.all()
#
#    context = {
#        'page_title':'post list',
#        'posts': posts
#    }
#    return render(request, 'about/plengngen.html', context)


#def create (request):
#    Post_forms = santriforms (request.santri or None)
#    if request.method == 'POST':
#        if Post_forms.is_valid():
#            santri.object.create(
#                 nama = request.POST.get ('nama'),
#                 Asatidz = request.POST.get ('Asatidz'),
#            )

#        return redirect('about:index')

#    context = {
#        'post_title': 'create_post', 
#        'post_form' :santri
#    }

#    return render(request, 'about/create.html', context)