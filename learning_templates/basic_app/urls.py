from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING

#in this part we tell to djando that look under the basic_app and find the url that match
app_name ='basic_app'

#now we have the url parttern list
urlpatterns =[
        url(r'^relative/$',views.relative,name='relative'),
        url(r'^other/$',views.other,name='other'),

]
