from django.conf.urls import url

from blog import views
urlpatterns = [
  url(r'^$',views.index),
  url(r'^post_list/$',views.post_list),
]
