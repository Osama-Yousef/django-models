from django.urls import path
from .views import  HomePageView , BlogDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailsView.as_view(), name='post_detail'),
]
