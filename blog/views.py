from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog, Profile
from .forms import PostForm, SearchForm
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

def home(request):
    form = SearchForm(request.GET or None)
    posts_list = Blog.objects.all()
    
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            posts_list = posts_list.filter(title__icontains=q)
    

    paginator = Paginator(posts_list, 5)  
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
     
        posts = paginator.page(1)
    except EmptyPage:
     
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/home.html', {'posts': posts, 'form': form})

def create_post(request):
    page_title = 'Nueva página'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Página creada exitosamente.')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {'form': form, 'title': page_title})

def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def update_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    page_title = 'Editar página'
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Página actualizada exitosamente.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/form.html', {'form': form, 'title': page_title})

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Página eliminada exitosamente.')
        return redirect('home')
    
    return render(request, 'blog/confirm_delete.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile_detail(request):
    profile = request.user.profile
    return render(request, 'profile/detail.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('profile-detail')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/form.html', {'form': form})
