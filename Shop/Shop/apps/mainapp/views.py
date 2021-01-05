from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *

''' Blocking a user by IP '''
def ban(request):
    ban = Ban.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    all_questions = Support.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    all_comments = Comment.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    settings = Settings.objects.all()
    for i in all_questions:
       i.delete() 
    for  i in all_comments:
        i.delete()

    if not ban:
        return redirect('home')
        
    context = {'title': 'You are blocked!', 'ban':ban, 'settings':settings}
    return render(request, 'Shop/ban.html', context)
        
''' Main Page '''
def home(request):
    ban = Ban.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    if ban:
        return redirect('BAN')
    else:
        faq = FAQ.objects.all()
        settings = Settings.objects.all()
        slider = Slider.objects.all()
        messenger = Messenger.objects.all()
        answers = Support.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
        
        # User requests
        support_form = SupportFrom()
        if request.method == 'POST':
            support_form = SupportFrom(request.POST)
            if support_form.is_valid():
                obj = support_form.save(commit=False)
                obj.answer = "Enter your answer..."
                obj.ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
                obj.save()
                return redirect('home')

        # Slider   
        if slider:
            first_slide = slider[0]
            slider_num = []
            for i in slider:
                slider_num.append(i)
            slider_num.pop(0)
        else:
            first_slide = "NO"
            slider_num = "NO"
    
        context = {'products': Product.objects.all(), 'FAQ': faq, 'settings':settings, 'answers':answers, 'support_form':support_form, 'messenger':messenger, 'first_slide':first_slide, 'slider_num':slider_num, 'title': 'Main page'}
        return render(request, 'Shop/home.html', context)

''' Product Page '''
def product(request, pk):
    ban = Ban.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    if ban:
        return redirect('BAN')
    else:
        faq = FAQ.objects.all()
        settings = Settings.objects.all()
        messenger = Messenger.objects.all()
        product = Product.objects.get(id=pk)
        answers = Support.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
        
        # Product gallery
        gallery = Gallery.objects.filter(product=product)
        if len(gallery) == 0:
            gallery = "NO"
        
        # Product Comments
        form = CommentFrom()
        if request.method == 'POST':
            form = CommentFrom(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.product = product
                obj.ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
                obj.save()
                return redirect('product', pk)
        
        # User requests
        support_form = SupportFrom()
        if request.method == 'POST':
            support_form = SupportFrom(request.POST)
            if support_form.is_valid():
                obj = support_form.save(commit=False)
                obj.answer = "Enter your answer..."
                obj.ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
                obj.save()
                return redirect('home')
                
        comments = Comment.objects.filter(product=product)
        
        context = {'product': product, 'form':form, 'FAQ': faq, 'support_form':support_form, 'answers':answers, 'gallery':gallery, 'settings':settings, 'comments':comments, 'title': product.name, 'messenger':messenger}
        return render(request, 'Shop/product.html', context)

''' FAQ '''
def faq(request):
    ban = Ban.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
    if ban:
        return redirect('BAN')
    else:
        messenger = Messenger.objects.all()
        faq = FAQ.objects.all()
        settings = Settings.objects.all()
        answers = Support.objects.filter(ip=request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip())
        
        # User requests
        support_form = SupportFrom()
        if request.method == 'POST':
            support_form = SupportFrom(request.POST)
            if support_form.is_valid():
                obj = support_form.save(commit=False)
                obj.answer = "Enter your answer..."
                obj.ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
                obj.save()
                return redirect('home')
                
        context = {'FAQ': faq, 'settings':settings, 'messenger':messenger, 'answers':answers, 'support_form':support_form, 'title': 'FAQ'}
        return render(request, 'Shop/FAQ.html', context)