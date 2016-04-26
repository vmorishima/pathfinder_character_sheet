from django.conf.urls import include, url
from . import views

app_name = 'pf_char_sheet'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/', views.characterCreate.as_view(), name='new'),
    url(r'^(?P<character_id>[0-9]+)/$', views.char_page, name='char'),
    url(r'^save/', views.save, name='save'),
    url(r'^(?P<pk>[0-9]+)/character_update/$', views.characterUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/character_delete/$', views.characterDelete.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/stat_update/$', views.statUpdate.as_view(), name='stat update'),
    url(r'^(?P<pk>[0-9]+)/skill_update/$', views.skillUpdate.as_view(), name='skill update')
]