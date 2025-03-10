from tokenize import Comment

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404

from blog.forms import PostForms
from blog.models import *


from django.shortcuts import render, get_object_or_404
from blog.models import *

def about_detail(request, id):
    about = get_object_or_404(About, id=id)
    return render(request, 'detail/about_detail.html', {'about': about})
def popular_detail(request, id):
    popular = get_object_or_404(Popular, id=id)
    return render(request, 'detail/popular_detail.html', {'popular': popular})
def avesome_detail(request, id):
    avesome = get_object_or_404(Avesome, id=id)
    return render(request, 'detail/avesome_detail.html', {'avesome': avesome})
def meet_detail(request, id):
    meet = get_object_or_404(Meet, id=id)
    return render(request, 'detail/meet_detail.html', {'meet': meet})
def aur_detail(request, id):
    aur = get_object_or_404(Aur, id=id)
    return render(request, 'detail/aur_detail.html', {'aur': aur})






def index(request):

    form=PostForms(request.POST or None)
    if request.method=="POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2> Sorov qabul qilindi javobini kuting <h2/>")

    about = About.objects.all()
    our = Our.objects.all()
    popular=Popular.objects.all()
    avesome=Avesome.objects.all()
    easy=Easy.objects.all()
    meet=Meet.objects.all()
    aur = Aur.objects.all()

    context = {
        'about':about,
        'our':our,
        'popular':popular,
        'avesome':avesome,
        'easy':easy,
        'meet':meet,
        'aur':aur
    }
    return render(request, "index.html",context)  # blog.html fayli mavjud bo‘lishi kerak

def about(request):
    return render(request, 'about.html',context={})
def a404(request):
    return render(request, '404.html',context={})
def booking(request):
    return render(request, 'booking.html',context={})
def contact(request):
    return render(request, 'contact.html',context={})
def destination(request):
    return render(request, 'destination.html',context={})
def package(request):
    return render(request, 'package.html',context={})
def service(request):
    return render(request, 'service.html',context={})
def team(request):
    return render(request, 'team.html',context={})
def testimonial(request):
    return render(request, 'testimonial.html',context={})


@login_required
def add_comment(request, about_id):
    about= get_object_or_404(About, id=about_id)
    if request.method=='POST':
        text=request.POST.get('text')
        if not text :
            return HttpResponseForbidden("vayy br.ro manbu joyyi man toldramanmi?")
        Comment.objects.create(
            about=about,
            user=request.user,
            text=text
        )
        return redirect('aboutDetail', id=about.id)
    return HttpResponseForbidden("Chitterlarga olim")



