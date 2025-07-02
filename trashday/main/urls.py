from django.urls import path
from . import views

app_name = 'main'    # このアプリケーションのルーティングに名付け

# アプリケーションのルーティング設定
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]