from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.subcategories_list,
        name='subcategory_by_category'),
    url(r'^[\d]/(?P<subcategory_slug>[-\w]+)/$',
        views.product_list,
        name='product_by_subcategory'),
    url(r'^[\d]/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]