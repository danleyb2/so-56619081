from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from .forms import CommentForm
from .models import Comment,Post

# Create your views here.
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/posts/{}/'.format(post.pk))
    else:
        form = CommentForm()
        return render(request, 'blog/post.html', {"form":form})
    form = CommentForm(request.POST)

form = CommentForm()
