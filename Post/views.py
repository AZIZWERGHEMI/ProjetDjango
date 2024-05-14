from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseNotAllowed
from Post.models import Post, Likes
from django.contrib.auth.models import User
from utilusateur.models import Profile
from comment.models import Comment
from comment.forms import NewCommentForm
from django.core.paginator import Paginator
from django.db.models import Q
from utilusateur.models import Profile  
from .forms import LogementForm
from .forms import  EvenClubForm, EvenSocialForm, StageForm, LogementForm, TransportForm
from django.contrib import messages
from .models import EvenClub, EvenSocial, Stage, Logement, Transport

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post



@login_required
def index(request):
    # Filtrer les publications de chaque type
    even_club_posts = Post.objects.filter(post_type='EvenClub')
    even_social_posts = Post.objects.filter(post_type='EvenSocial')
    stage_posts = Post.objects.filter(post_type='Stage')
    transport_posts = Post.objects.filter(post_type='Transport')
    logement_posts = Post.objects.filter(post_type='Logement')
    
    return render(request, 'index.html', {
        'even_club_posts': even_club_posts,
        'even_social_posts': even_social_posts,
        'stage_posts': stage_posts,
        'transport_posts': transport_posts,
        'logement_posts': logement_posts,
    })

@login_required
def PostDetail(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-date')

    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('post-details', args=[post.id]))
    else:
        form = NewCommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments
    }

    return render(request, 'postdetail.html', context)

@login_required
def like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    liked = Likes.objects.filter(user=user, post=post).exists()

    if not liked:
        Likes.objects.create(user=user, post=post)
        Post.objects.filter(id=post_id).update(likes=F('likes') + 1)
    else:
        Likes.objects.filter(user=user, post=post).delete()
        Post.objects.filter(id=post_id).update(likes=F('likes') - 1)

    return HttpResponseRedirect(reverse('post-details', args=[post_id]))


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  EvenSocialForm, StageForm, LogementForm, TransportForm
@login_required
def create_post(request):
    form = None  # Initialisation en dehors du bloc if

    if request.method == 'POST':
        post_type = request.POST.get('post_type')
        if post_type == 'EvenClub':
            form = EvenClubForm(request.POST, request.FILES)
        elif post_type == 'EvenSocial':
            form = EvenSocialForm(request.POST, request.FILES)
        elif post_type == 'Stage':
            form = StageForm(request.POST, request.FILES)
        elif post_type == 'Transport':
            form = TransportForm(request.POST, request.FILES)
        elif post_type == 'Logement':
            form = LogementForm(request.POST, request.FILES)
        
        else:
            messages.error(request, 'Invalid post type!')
            return redirect('index')

        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.user = request.user
            post_instance.save()
            messages.success(request, 'Post created successfully!')
            return redirect('index')
        else:
            form.full_clean() 
    else:
        # Initialisation dans le bloc else
        form = EvenClubForm()  # Vous pouvez choisir un formulaire par défaut ici ou laisser form à None
    
    return render(request, 'newpost.html', {'form': form})
