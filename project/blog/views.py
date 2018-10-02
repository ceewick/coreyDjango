from django.shortcuts import render
from .models import Post

# from django.http import HttpResponse

## Dummy data/posts
# posts = [
#     {
#         'author':'coreyMS',
#         'title':'Blog Post 1',
#         'content':'First post content!!',
#         'date_posted':'Sept 30, 2018 '
#     },
#     {
#         'author':'Clint W',
#         'title':'Blog Post 2',
#         'content':'Second post content!!',
#         'date_posted':'Sept 30, 2018 '
#     }
# ]

def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>About Blog</h1>')
    return render(request, 'blog/about.html',{'title':'About'})
