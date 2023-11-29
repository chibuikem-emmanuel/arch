from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post, New, Comment, Client, Portfolio, Special, Newsgrid, Parallax, Workgrid
from . import models
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from .forms import PostForm, NewForm, ParallaxForm, CommentForm, ClientForm, PortfolioForm, NewsgridForm, Workgrid

# Create your views here.



class IndexView(TemplateView):
    def get(self, request):
        posts = Post.objects.all()
        news =  New.objects.all()
        comments =  Comment.objects.all()
        clients =  Client.objects.all()
        portfolios =  Portfolio.objects.all()
        specials =  Special.objects.all()

        
        context = { 
            'posts':posts,
            'news':news,
            'comments':comments,
            'clients':clients,
            'portfolios':portfolios,
            'specials':specials
            }
        return render(request, 'index.html', context)



class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post
    template_name = 'post_list.html'




class PostCreateView(CreateView):
    fields = ('name', 'details')
    model = models.Post 
    template_name = 'post_form.html'
    success_url = reverse_lazy("success_add_list")

def success_add_list(request):
    return render(request, 'success_add_post.html')


class PostUpdateView(UpdateView):
    fields = ('name', 'details')
    model = models.Post
    template_name = 'update_list.html'

    success_url = reverse_lazy("success_list")

def success_list(request):
    return render(request, 'success_post.html')

def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')


class PostDetailView(DetailView):
    model = models.Post 
    template_name = 'post_details.html'
   

# news views

class NewListView(ListView):
    context_object_name = 'news'
    model = models.New
    template_name = 'new_list.html'


class NewCreateView(CreateView):
    fields = ('news_user', 'news_image', 'news_category', 'news_topic', 'news_details', 'news_created_at')
    model = models.New
    template_name = 'new_form.html'
    success_url = reverse_lazy("success_add_news")

def success_add_news(request):
    return render(request, 'success_add_news.html')



class NewDetailView(DetailView):
    model = models.New 
    template_name = 'new_details.html'


class NewUpdateView(UpdateView):
    fields = ('news_user', 'news_image', 'news_category', 'news_topic', 'news_details', 'news_created_at')
    model = models.New
    template_name = 'update_new.html'

    success_url = reverse_lazy("success_news")

def success_news(request):
    return render(request, 'success_news.html')


def delete_new(request, id):
    new = New.objects.get(pk=id)
    new.delete()
    return redirect('new_list')
#comment views


class CommentListView(ListView):
    context_object_name = 'comments'
    model = models.Comment
    template_name = 'comment_list.html'

class CommentDetailView(DetailView):
    model = models.Comment 
    template_name = 'comment_details.html'


class CommentCreateView(CreateView):
    fields = ('comment', 'commentator', 'commentator_position')
    model = models.Comment
    template_name = 'comment_form.html'
    success_url = reverse_lazy("success_add_comment")

def success_add_comment(request):
    return render(request, 'success_add_comment.html')



class CommentUpdateView(UpdateView):
    fields = ('comment', 'commentator', 'commentator_position')
    model = models.Comment
    template_name = 'update_comment.html'
    success_url = reverse_lazy("success_comment")

def success_comment(request):
    return render(request, 'success_comment.html')

def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    comment.delete()
    return redirect('comment_list')


#clients

class ClientListView(ListView):
    context_object_name = 'clients'
    model = models.Client
    template_name = 'client_list.html'

class ClientCreateView(CreateView):
    fields = ('client_image',)
    model = models.Client
    template_name = 'client_form.html'
    success_url = reverse_lazy("success_add_client")

def success_add_client(request):
    return render(request, 'success_add_client.html')


class ClientDetailView(DetailView):
    model = models.Client 
    template_name = 'client_details.html'

class ClientUpdateView(UpdateView):
    fields = ('client_image',)
    model = models.Client
    template_name = 'update_client.html'
    success_url = reverse_lazy("success_client")

def success_client(request):
    return render(request, 'success_client.html')


@login_required(login_url="login")
def delete_client(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('client_list')

#portfolio

class PortfolioListView(ListView):
    context_object_name = 'portfolios'
    model = models.Portfolio
    template_name = 'portfolio_list.html'



class PortfolioDetailView(DetailView):
    model = models.Portfolio
    template_name = 'portfolio_details.html'


class PortfolioUpdateView(UpdateView):
    fields = ('news_image', 'title', 'description')
    model = models.Portfolio
    template_name = 'update_portfolio.html'
    success_url = reverse_lazy("success_portfolio")

def success_portfolio(request):
    return render(request, 'success_portfolio.html')


class PortfolioCreateView(CreateView):
    fields = ('news_image', 'title', 'description')
    model = models.Portfolio
    template_name = 'portfolio_form.html'
    success_url = reverse_lazy("success_add_portfolio")

def success_add_portfolio(request):
    return render(request, 'success_add_portfolio.html')

def delete_portfoilo(request, id):
    portfolio = Portfolio.objects.get(pk=id)
    portfolio.delete()
    return redirect('portfolio_list')

#specials
class SpecialListView(ListView):
    context_object_name = 'specials'
    model = models.Special
    template_name = 'special_list.html'

class SpecialDetailView(DetailView):
    model = models.Special 
    template_name = 'special_details.html'

class SpecialCreateView(CreateView):
    fields = ('title', 'description', 'special_image')
    model = models.Special
    template_name = 'special_form.html'
    success_url = reverse_lazy("success_add_special")

def success_add_special(request):
    return render(request, 'success_add_special.html')

class SpecialUpdateView(UpdateView):
    fields = ('title', 'description', 'special_image')
    model = models.Special
    template_name = 'update_special.html'
    success_url = reverse_lazy("success_special")

def success_special(request):
    return render(request, 'success_special.html')

def delete_special(request, id):
    special = Special.objects.get(pk=id)
    special.delete()
    return redirect('special_list')

#NEWSGRID
class NewsgridListView(ListView):
    context_object_name = 'newsgrids'
    model = models.Newsgrid
    template_name = 'newsgrid_list.html'

class NewsgridDetailView(DetailView):
    model = models.Newsgrid 
    template_name = 'newsgrid_details.html'

class NewsgridCreateView(CreateView):
    fields = ('ngrid_user', 'ngrid_image', 'category', 'ngrid_created_at', 'ngrid_description')
    model = models.Newsgrid
    template_name = 'newsgrid_form.html'
    success_url = reverse_lazy("success_add_newsgrid")

def success_add_newsgrid(request):
    return render(request, 'success_add_newsgrid.html')
 
class NewsgridUpdateView(UpdateView):
    fields = ('ngrid_user', 'ngrid_image', 'category', 'ngrid_created_at', 'ngrid_description')
    model = models.Newsgrid
    template_name = 'update_newsgrid.html'
    success_url = reverse_lazy("success_newsgrid")

def success_newsgrid(request):
    return render(request, 'success_newsgrid.html')


def delete_newsgrid(request, id):
    newsgrid = Newsgrid.objects.get(pk=id)
    newsgrid.delete()
    return redirect('newsgrid_list')

#parallax
class ParallaxListView(ListView):
    context_object_name = 'parallaxs'
    model = models.Parallax
    template_name = 'parallax_list.html'

class ParallaxDetailView(DetailView):
    model = models.Parallax 
    template_name = 'parallax_details.html'

class ParallaxCreateView(CreateView):
    fields = ('work_image', 'desc_work')
    model = models.Parallax
    template_name = 'parallax_form.html'
    success_url = reverse_lazy("success_add_parallax")

def success_add_parallax(request):
    return render(request, 'success_add_parallax.html')

class ParallaxUpdateView(UpdateView):
    fields = ('work_image', 'desc_work')
    model = models.Parallax
    template_name = 'update_parallax.html'
    success_url = reverse_lazy("success_parallax")

def success_parallax(request):
    return render(request, 'success_parallax.html')

def delete_parallax(request, id):
    parallax = Parallax.objects.get(pk=id)
    parallax.delete()
    return redirect('parallax_list')

#workgrid
class WorkgridListView(ListView):
    context_object_name = 'workgrids'
    model = models.Workgrid
    template_name = 'workgrid_list.html'

class WorkgridDetailView(DetailView):
    model = models.Workgrid 
    template_name = 'workgrid_details.html'

class WorkgridCreateView(CreateView):
    fields = ('ngrid_image', 'category', 'ngrid_description')
    model = models.Workgrid
    template_name = 'workgrid_form.html'
    success_url = reverse_lazy("success_add_workgrid")

def success_add_workgrid(request):
    return render(request, 'success_add_workgrid.html')

class WorkgridUpdateView(UpdateView):
    fields = ('ngrid_image', 'category', 'ngrid_description')
    model = models.Workgrid
    template_name = 'update_workgrid.html'
    success_url = reverse_lazy("success_workgrid")

def success_workgrid(request):
    return render(request, 'success_workgrid.html')

def delete_workgrid(request, id):
    workgrid = Workgrid.objects.get(pk=id)
    workgrid.delete()
    return redirect('workgrid_list')







def news_2(request):
    return render(request, 'news-listing.html')

def news_3(request):
    return render(request, 'news-sidebar.html')

def single(request):
    return render(request, 'single-post.html')

def single_2(request):
    return render(request, 'single-video.html')

def single_3(request):
    return render(request, 'single-post-gallery.html')

@login_required(login_url="login")
def contact(request):
    return render(request, 'contact.html')

def page_2(request):
    return render(request, 'index3.html')

def work(request):
    workgrids = Workgrid.objects.all()

    context = {
        'workgrids':workgrids
    }
    return render(request, 'works-grid.html', context)

def work_2(request):
    return render(request, 'work-masonary.html')

def work_3(request):
    parallaxs = Parallax.objects.all()

    context = {
        'parallaxs':parallaxs
    }
    return render(request, 'works-parallax.html', context)

def work_4(request):
    return render(request, 'project-details.html')


def news_grid(request):
    newsgrids =  Newsgrid.objects.all()

    context = { 
        'newsgrids':newsgrids
        }
    return render(request, 'news-grid.html', context)


def page(request):
    return render(request, 'home2.html')

def about(request): 
    return render(request, 'about.html')


def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['victorchibuikem90@gmail.com']
        )

        email.fail_silently=False
        email.send()
    return render(request, 'email_sent.html')

def not_allowed(request):
    return render(request, 'not_allowed.html')

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Input')
            return redirect('login')
    else:
         return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']    
        password1 = request.POST['password1']    
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')

    else:    
        return render(request, 'register.html')


@login_required(login_url="login")
def dashboard(request):
    posts = Post.objects.all()
    total_posts = posts.count()

    news =  New.objects.all()
    total_news = news.count()

    comments =  Comment.objects.all()
    total_comments = comments.count()

    clients =  Client.objects.all()
    total_clients = clients.count()

    portfolios =  Portfolio.objects.all()
    total_portfolios = posts.count()

    specials =  Special.objects.all()
    total_specials = specials.count()

    newsgrids =  Newsgrid.objects.all()
    total_newsgrids = newsgrids.count()

    parallaxs =  Parallax.objects.all()
    total_parallaxs = parallaxs.count()

    workgrids =  Workgrid.objects.all()
    total_workgrids = workgrids.count()

    context = { 
        'posts':posts,
        'news':news,
        'comments':comments,
        'clients':clients,
        'portfolios':portfolios,
        'specials':specials,
        'newsgrids':newsgrids,
        'parallaxs': parallaxs,
        'workgrids': workgrids,

        }
    return render(request, 'dashboard.html', context)
