from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.utils import timezone
from .forms import PostCreateForm


# home.html is the page that is displayed when the application runs
def home(request):
    return render(request, 'blog/home.html')


# landing.html is the page that is displayed after successful login
@login_required(login_url="/login/")
def landing(request):
    data = Post.objects.order_by('-posted_date')

    for obj in data:
        content = obj.content[0:300]
        obj.content = content

    p = Paginator(data, 3)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {}
    context['posts'] = page
    return render(request, 'blog/landing.html', context)


class PostDetailView(DetailView):
    model = Post


@login_required(login_url="/login/")
def post_detail(request, slug):
    context = {}
    obj = get_object_or_404(Post, slug=slug)
    context["object"] = obj
    return render(request, 'blog/post_detail.html', context)


@login_required(login_url="/login/")
def create_post(request):
    context = {}
    form = PostCreateForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        obj = form.save(commit=False)
        #obj.updated_date = None
        obj.user_id = request.user.id
        obj.save()
        messages.add_message(request, messages.SUCCESS, 'Post created successfully!')
        return HttpResponseRedirect('/landing')
    return render(request, 'blog/create_post.html', context)


@login_required(login_url="/login/")
def update_post(request, slug):
    context = {}
    obj1 = get_object_or_404(Post, slug=slug)
    if obj1.user != request.user:
        raise PermissionDenied()
    form = PostCreateForm(request.POST or None, instance=obj1)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_date = timezone.now()
        obj.save()
        messages.add_message(request, messages.SUCCESS, 'Post updated successfully!')
        return HttpResponseRedirect('/landing')

    context["form"] = form
    return render(request, 'blog/update_post.html', context)


@login_required(login_url="/login/")
def delete_post(request, slug):
    context = {}
    obj = get_object_or_404(Post, slug=slug)
    if obj.user != request.user:
        raise PermissionDenied()

    if request.method == "POST":
        obj.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted successfully!')
        return HttpResponseRedirect("/landing")
    context["post"] = obj
    return render(request, "blog/delete_post.html", context)


class PostSearchView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/searched_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query).order_by('-posted_date')
