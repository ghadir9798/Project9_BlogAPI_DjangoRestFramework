from urllib.parse import quote_plus

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator

from comments.forms import CommentForm
from comments.models import Comment
from django.utils import timezone
from django.db.models import Q

from django.contrib.contenttypes.models import ContentType



def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active().order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all().order_by("-timestamp")

    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': 'List',
        'today': today,
    }
    return render(request, 'post_list.html', context)

def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     messages.error(request, 'You do not have permission to cresate a post, please login first')
    #     raise Http404
    if not request.user.is_authenticated:
        # raise Http404
        messages.error(request, 'You do not have permission to create a post, please login first')
        return redirect('accounts:login')
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }
    return render(request, 'post_form.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
        # print(form.cleaned_data)
        # {'content_type': 'posts | post', 'object_id': 20, 'parent_id': None, 'content': 'New comment'}
        c_type_raw = form.cleaned_data.get('content_type')
        c_type = c_type_raw.split()
        content_type = ContentType.objects.get(model=c_type[2])
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
                                    user = request.user,
                                    content_type = content_type,
                                    object_id = obj_id,
                                    content = content_data,
                                    parent = parent_obj,  
                                )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    comments = Comment.objects.filter_by_instance(instance)
    context = {
        'title': instance.title,
        'instance': instance,
        'share_string': share_string,
        'comments': comments,
        'comment_form': form,
    }
    return render(request, 'post_detail.html', context)

def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> has been Modified", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'post_form.html', context)

def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("posts:list")