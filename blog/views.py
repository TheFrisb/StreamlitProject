from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator


'''
- get_object_or_404 is a django shortcut that returns an object if it exists, 
or a 404 error if it doesn't, very convienient for blog posts

- from .models import * | This (*), means all, so it imports every model from the blog\models.py file

- from django.core.paginator import Paginator | This is used for paginating the blog posts, 
so that only a certain number of posts are shown per page, 
and the user can navigate to the next page to see more posts
'''


# Create your views here.

#make a home view
def home(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at') # this is a queryset, it returns all blog posts ordered by the created_at field in descending order
    blog_categories = BlogCategory.objects.all() # this is a queryset, it returns all blog categories
    recent_posts = blog_posts[:4] # this is a list, it returns the first 4 blog posts
    paginator = Paginator(blog_posts, 12) # Show 12 blog posts per page.
    page_number = request.GET.get('page') # this gets the page number from the url
    blog_posts_paginated = paginator.get_page(page_number) # this paginates the blog posts queryset
    
    context = {
        'title': 'Blog Home',
        'blog_posts': blog_posts_paginated,
        'blog_categories': blog_categories,
        'recent_posts': recent_posts,
        'english': True,
    }
    if request.user.is_authenticated: # check if the user is logged in
        user_profile = UserProfile.objects.get(user=request.user) # get the user profile of the logged in user
        print(user_profile.notification)
        if user_profile.notification is not None:
            context['notification'] = user_profile.notification
            user_profile.notification = None
            user_profile.save()
        context['user_profile'] = user_profile 
    return render(request, 'blog/home.html', context)


def blog_category_view(request, string):
    blog_category = get_object_or_404(BlogCategory, slug=string) # this gets the blog category from the url
    blog_posts = BlogPost.objects.filter(category=blog_category).order_by('-created_at') # this is a queryset, it returns all blog posts ordered by the created_at field in descending order
    blog_categories = BlogCategory.objects.all() # this is a queryset, it returns all blog categories
    recent_posts = blog_posts[:4] # this is a list, it returns the first 4 blog posts
    paginator = Paginator(blog_posts, 12) # Show 12 blog posts per page.
    page_number = request.GET.get('page')# this gets the page number from the url
    blog_posts_paginated = paginator.get_page(page_number) # this paginates the blog posts queryset

    context = {
        'title': blog_category.name,
        'blog_posts': blog_posts_paginated,
        'blog_categories': blog_categories,
        'active_category': blog_category.name,
        'recent_posts': recent_posts,
        'english': True,
    }
    if request.user.is_authenticated: # check if the user is logged in
        user_profile = UserProfile.objects.get(user=request.user) # get the user profile of the logged in user
        print(user_profile.notification)
        if user_profile.notification is not None:
            context['notification'] = user_profile.notification
            user_profile.notification = None
            user_profile.save()
        context['user_profile'] = user_profile 
    return render(request, 'blog/home.html', context)


#make a search view
def blog_search_view(request):
    query = request.GET.get('query')  # this gets the search query from the url ( what the user wrote in the search bar )
    blog_posts = BlogPost.objects.filter(title__icontains=query).order_by('-created_at') # this is a queryset, it returns all blog posts ordered by the created_at field in descending order
    blog_categories = BlogCategory.objects.all() # this is a queryset, it returns all blog categories
    recent_posts = blog_posts[:4] # this is a list, it returns the first 4 blog posts
    paginator = Paginator(blog_posts, 12) # Show 12 blog posts per page.
    page_number = request.GET.get('page') # this gets the page number from the url
    blog_posts_paginated = paginator.get_page(page_number) # this paginates the blog posts queryset

    context = {
        'title': 'Blog Search' + ' - ' + query,
        'blog_posts': blog_posts_paginated,
        'blog_categories': blog_categories,
        'active_category': 'Search Results',
        'recent_posts': recent_posts,
        'english': True,

    }
    if request.user.is_authenticated: # check if the user is logged in
        user_profile = UserProfile.objects.get(user=request.user) # get the user profile of the logged in user
        print(user_profile.notification)
        if user_profile.notification is not None:
            context['notification'] = user_profile.notification
            user_profile.notification = None
            user_profile.save()
        context['user_profile'] = user_profile 
    return render(request, 'blog/home.html', context)



def blog_detail_view(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk) # this gets the blog post from the url
    blog_categories = BlogCategory.objects.all() # this is a queryset, it returns all blog categories
    recent_posts = BlogPost.objects.all().order_by('-created_at')[:4] # this is a list, it returns the first 4 blog posts
    try:
        next_post = BlogPost.objects.get(pk=pk+1) # this gets the next blog post if it exists
    except:
        next_post = None
    try:
        previous_post = BlogPost.objects.get(pk=pk-1) # this gets the previous blog post if it exists
    except:
        previous_post = None
    
    context = {
        'title': blog_post.title,
        'post': blog_post,
        'blog_categories': blog_categories,
        'recent_posts': recent_posts,
        'next_post': next_post,
        'previous_post': previous_post,
        'english': True,
    }
    if request.user.is_authenticated: # check if the user is logged in
        user_profile = UserProfile.objects.get(user=request.user) # get the user profile of the logged in user
        print(user_profile.notification)
        if user_profile.notification is not None:
            context['notification'] = user_profile.notification
            user_profile.notification = None
            user_profile.save()
        context['user_profile'] = user_profile 
    return render(request, 'blog/blog_detail_view.html', context)


