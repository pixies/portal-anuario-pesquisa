from django.conf.urls import url

from .views import minhas_pesquisas, todos_pesquisadores

urlpatterns = [
    url(r'^$', minhas_pesquisas, name="minhas"),
    url(r'^todos/$', todos_pesquisadores, name="todos"),
]
