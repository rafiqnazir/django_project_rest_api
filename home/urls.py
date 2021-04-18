from home.views import (GetView,PostView,UpdateView,DeleteView,ListAll)
from django.urls import path

app_name='home'
urlpatterns = [
    path('<str:type>/<id>/',GetView.as_view(),name="get_view"),
    path("<str:type>/create",PostView.as_view(),name="post_view"),
    path("<str:type>/<id>/update",UpdateView.as_view(),name="update_view"),
    path("<str:type>/<id>/delete",DeleteView.as_view(),name="delete_view"),
    path("<str:type>/",ListAll.as_view(),name="list_all"),    
]
