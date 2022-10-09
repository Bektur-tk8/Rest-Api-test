

from django.urls import path
from .views import *

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail)
    path('detail/<int:id>', ArticleDetails.as_view()),
    path('generic/article/<int:pk>/', GenericAPIView.as_view())
]
