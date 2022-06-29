from django.shortcuts import render, redirect, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm
from .models import (SponsorModel,
                    SponsorClassModel,
                    MemberModel,
                    StaffModel,
                    Header,
                    CommunityBlock,
                    HistoryBlock)


# Create your views here.

def home(request):
    stuff = Header.objects.all()
    args = {'stuff': stuff}

    return render(request, 'sponsors/home.html', args)

def GoldSponsorView(request):

    sponsor = SponsorModel.objects.all()
    args = {'sponsor': sponsor}
    

    return render(request, 'sponsors/goldsponsorpage.html', args)


def SilverSponsorView(request):

    sponsor = SponsorModel.objects.all()
    args = {'sponsor': sponsor}
    

    return render(request, 'sponsors/silversponsorpage.html', args)


def BronzeSponsorView(request):

    sponsor = SponsorModel.objects.all()
    args = {'sponsor': sponsor}
    

    return render(request, 'sponsors/bronzesponsorpage.html', args)


def HistoryView(request):

    model = HistoryBlock.objects.all()
    args = {'model': model}
    
    return render(request, 'sponsors/aboutus.html', args)

def MemberView(request):

    student = MemberModel.objects.all()
    staff = StaffModel.objects.all()
    args = {'staff': staff,
            'student': student}
    
    return render(request, 'sponsors/members.html', args)

def BecomeView(request):
    
    return render(request, 'sponsors/become.html', {})


def SponsorDetailView(request, slug=None, *args, **kwargs):
    
    obj_init = None
    obj_name = None
    obj_stock = None
    obj_info = None
    obj_price = None
    obj_img = None
        
    qs = SponsorModel.objects.filter(slug__iexact=slug.upper())
    if qs.exists() and qs.count() == 1:
        
        obj = qs.first()
                
        obj_init = obj
        obj_img = obj.image
        obj_info = obj.description
        obj_name = obj.name
            
    
            
    args = {'obj_name': obj_name,
            'obj_img': obj_img,
            'obj_info': obj_info}
                
            
    return render(request, 'sponsors/sponsordetail.html', args)


def CommunityView(request):

    model = CommunityBlock.objects.all()
    args = {'model': model}
    
    return render(request, 'sponsors/community.html', args)

def BecomeView(request):
    
    return render(request, 'sponsors/become.html', {})


def ContactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            #messages.success(request, "Thanks, we will reply as soon as possible!")
            form.save()
            return redirect(reverse('sponsors:home'))


    else:
        form = ContactForm()
        args = {'form': form}

    return render(request, 'sponsors/contact.html', args)