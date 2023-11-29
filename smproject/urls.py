from django.urls import path
from . import views
from .views import  IndexView, PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDetailView
from .views import NewListView, NewCreateView, NewUpdateView, NewDetailView
from .views import CommentListView, CommentCreateView, CommentUpdateView, CommentDetailView
from .views import NewsgridListView, NewsgridCreateView, NewsgridUpdateView, NewsgridDetailView
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView
from .views import PortfolioListView, PortfolioUpdateView, PortfolioCreateView, PortfolioDetailView
from .views import SpecialListView, SpecialCreateView, SpecialUpdateView, SpecialDetailView
from .views import ParallaxListView,  ParallaxUpdateView, ParallaxCreateView, ParallaxDetailView
from .views import WorkgridListView,  WorkgridUpdateView, WorkgridCreateView, WorkgridDetailView





urlpatterns = [
    # path('', PostView.as_view(), name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
   
    path('', IndexView.as_view(), name='index'),
    path('not_allowed/', views.not_allowed, name='not_allowed'),

    path('post_list', PostListView.as_view(), name='post_list'),
    path('grid_news', views.news_grid, name='grid_news'),
    path('client_list', ClientListView.as_view(), name='client_list'),
    path('special_list', SpecialListView.as_view(), name='special_list'),
    path('special_list/<int:pk>', SpecialListView.as_view(), name='special_list'),
    path('workgrid_list', WorkgridListView.as_view(), name='workgrid_list'),
    path('workgrid_list/<int:pk>', WorkgridListView.as_view(), name='workgrid_list'),
    path('client_list/<int:pk>', ClientListView.as_view(), name='client_list'),
    path('portfolio_list', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolio_list/<int:pk>', PortfolioListView.as_view(), name='portfolio_list'),
    path('parallax_list', ParallaxListView.as_view(), name='parallax_list'),
    path('parallax_list/<int:pk>', ParallaxListView.as_view(), name='parallax_list'),

    path('post_details/<int:pk>', PostDetailView.as_view(), name="post_details"),
    path('client_details/<int:pk>', ClientDetailView.as_view(), name="client_details"),
    path('portfolio_details/<int:pk>', PortfolioDetailView.as_view(), name="portfolio_details"),
    path('parallax_details/<int:pk>', ParallaxDetailView.as_view(), name="parallax_details"),
    path('new_details/<int:pk>', NewDetailView.as_view(), name="new_details"),
    path('comment_details/<int:pk>', CommentDetailView.as_view(), name="comment_details"),
    path('newsgrid_details/<int:pk>', NewsgridDetailView.as_view(), name="newsgrid_details"),
    path('workgrid_details/<int:pk>', WorkgridDetailView.as_view(), name="workgrid_details"),
    path('special_details/<int:pk>', SpecialDetailView.as_view(), name="special_details"),

    
    path('newsgrid_list', NewsgridListView.as_view(), name='newsgrid_list'),
    path('newsgrid_list/<int:pk>', NewsgridListView.as_view(), name='newsgrid_list'),
    path('new_list', NewListView.as_view(), name='new_list'),
    path('comment_list', CommentListView.as_view(), name='comment_list'),
    path('new_list/<int:pk>', NewListView.as_view(), name='new_list'),
    path('comment_list/<int:pk>', CommentListView.as_view(), name='comment_list'),
    path('post_list/<int:pk>', PostListView.as_view(), name='post_list'),
    path('update_list/<int:pk>/', PostUpdateView.as_view(), name='update_list'),
    path('update_new/<int:pk>/', NewUpdateView.as_view(), name='update_new'),

    path('success_news/', views.success_news, name='success_news'),
    path('success_list/', views.success_list, name='success_list'),
    path('success_comment/', views.success_comment, name='success_comment'),
    path('success_newsgrid/', views.success_newsgrid, name='success_newsgrid'),
    path('success_client/', views.success_client, name='success_client'),
    path('success_workgrid/', views.success_workgrid, name='success_workgrid'),
    path('success_portfolio/', views.success_portfolio, name='success_portfolio'),
    path('success_parallax/', views.success_parallax, name='success_parallax'),
    path('success_special/', views.success_special, name='success_special'),

    path('success_add_news/', views.success_add_news, name='success_add_news'),
    path('success_add_list/', views.success_add_list, name='success_add_list'),
    path('success_add_comment/', views.success_add_comment, name='success_add_comment'),
    path('success_add_newsgrid/', views.success_add_newsgrid, name='success_add_newsgrid'),
    path('success_add_client/', views.success_add_client, name='success_add_client'),
    path('success_add_workgrid/', views.success_add_workgrid, name='success_add_workgrid'),
    path('success_add_portfolio/', views.success_add_portfolio, name='success_add_portfolio'),
    path('success_add_parallax/', views.success_add_parallax, name='success_add_parallax'),
    path('success_add_special/', views.success_add_special, name='success_add_special'),
    
    path('update_workgrid/<int:pk>/', WorkgridUpdateView.as_view(), name='update_workgrid'),
    path('update_newsgrid/<int:pk>/', NewsgridUpdateView.as_view(), name='update_newsgrid'),
    path('update_comment/<int:pk>/', CommentUpdateView.as_view(), name='update_comment'),
    path('update_portfolio/<int:pk>/', PortfolioUpdateView.as_view(), name='update_portfolio'),
    path('update_parallax/<int:pk>/', ParallaxUpdateView.as_view(), name='update_parallax'),
    path('update_special/<int:pk>/', SpecialUpdateView.as_view(), name='update_special'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_list/<int:id>/', views.delete_post, name='delete_list'),
    path('delete_workgrid/<int:id>/', views.delete_workgrid, name='delete_workgrid'),
    path('delete_new/<int:id>/', views.delete_new, name='delete_new'),
    path('delete_newsgrid/<int:id>/', views.delete_newsgrid, name='delete_newsgrid'),
    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('delete_client/<int:id>/', views.delete_client, name='delete_client'),
    path('delete_portfoilo/<int:id>/', views.delete_portfoilo, name='delete_portfolio'),
    path('delete_special/<int:id>/',  views.delete_special, name='delete_special'),
    path('delete_parallax/<int:id>/',  views.delete_parallax, name='delete_parallax'),
    path('create', PostCreateView.as_view(), name='create'),
    path('create_new', NewCreateView.as_view(), name='create_new'),
    path('create_workgrid', WorkgridCreateView.as_view(), name='create_workgrid'),
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('create_comment', CommentCreateView.as_view(), name='create_comment'),
    path('create_parallax', ParallaxCreateView.as_view(), name='create_parallax'),
    path('create_newsgrid', NewsgridCreateView.as_view(), name='create_newsgrid'),
    path('create_portfolio', PortfolioCreateView.as_view(), name='create_portfolio'),
    path('create_special', SpecialCreateView.as_view(), name='create_special'),
    path('contact/', views.contact, name='contact'),
    path('page/', views.page, name='page'),
    path('page_2/', views.page_2, name='page_2'),
    path('work/', views.work, name='work'),
    path('work_2/', views.work_2, name='work_2'),
    path('work_3/', views.work_3, name='work_3'),
    path('work_4/', views.work_4, name='work_4'),
    path('single/', views.single, name='single'),
    path('single_2/', views.single_2, name='single_2'),
    path('single_3/', views.single_3, name='single_3'),
    path('news_2/', views.news_2, name='news_2'),
    path('send_email/', views.sendEmail, name="send_email"),
    path('news_3/', views.news_3, name='news_3'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]
