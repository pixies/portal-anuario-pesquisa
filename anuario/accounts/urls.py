from django.conf.urls import include, url
from anuario.accounts.views import (
    add_account,
    login_account,
    edit_account,
    del_account,
    request_pass_account,
    new_pass_account,
    logout_account
)
urlpatterns = [
    url(r'^nova', add_account, name='novo'),
    url(r'^entrar', login_account, name='entrar'),
    url(r'^editar', edit_account, name='editar'),
    url(r'^apagar', del_account, name='apagar'),
    #url(r'^solicitar-senha', request_pass_account, name='solicitar-senha'),
    #url(r'^solicitar-senha/$', 'django.contrib.auth.views.password_change', name='solicitar-senha'),
    #url(r'^solicitar-senha/feito$', 'django.contrib.auth.views.password_reset_done', name='nova-senha-feito'),
    #url(r'^solicitar-senha/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
    #    'django.contrib.auth.views.password_reset_confirm',
    #    name='confirme-nova-senha'),
    #url(r'^solicitar-senha/completo$', 'django.contrib.auth.views.password_reset_complete', name='nova-senha-completa'),
    #url(r'^nova-senha/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^sair', logout_account, name='sair'),
]
