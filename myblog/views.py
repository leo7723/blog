from django.shortcuts import render
from myblog.models import BlogsPost
from django.http import Http404 , HttpResponseRedirect
import re


# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.all().order_by('-timestamp')
    for blog in blog_list:
        summary = re.sub("[\!\%\[\]\,\.\#]", "", blog.body)
        if len(summary) > 50 :
            blog.summary = summary[0:116]+'...'
        else:
            blog.summary = re.sub("[\!\%\[\]\,\.\#]","",blog.body)
    return render(request, 'home.html', {'blog_list': blog_list})


def detail(request,id):
    try:
        post = BlogsPost.objects.get(id=str(id))
    except BlogsPost.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post': post})


def main_redirect(request):
    return HttpResponseRedirect("/blog/index/")
