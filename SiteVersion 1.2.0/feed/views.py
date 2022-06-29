from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm, EditProfileForm, PostForm
from .models import Post

# Create your views here.


def login_redirect(request):
    return render(request, 'feed/login_redirect.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('sponsors:Post'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'feed/reg_form.html', args)


def view_profile(request):
    '''
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
        '''
    args = {'user': request.user}
    return render(request, 'feed/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('feed:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'feed/edit_profile.html', args)
    
  
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('feed:view_profile'))
        else:
            return redirect(reverse('feed:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'feed/change_password.html', args)

class PostView(TemplateView):
    template_name = 'feed/feed.html'

    def get(self, request):
        form = PostForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)

        args = {
            'form': form, 'posts': posts, 'users': users
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = PostForm()
            return redirect('feed:blog')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)