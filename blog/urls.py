from django.urls import path

# import about
from blog.views import *


urlpatterns = [
    path('',index,name="index"),

    path('about/<int:id>/', about_detail, name='about_detail'),
    path('popular/<int:id>/', popular_detail, name='popular_detail'),
    path('avesome/<int:id>/', avesome_detail, name='avesome_detail'),
    path('meet/<int:id>/', meet_detail, name='meet_detail'),
    path('aur/<int:id>/', aur_detail, name='aur_detail'),
    path('',index,name="index"),
    path('a404/',a404,name="404"),
    path('about/', about, name="about"),
    path('booking/', booking, name="booking"),
    path('contact/', contact, name="contact"),
    path('destination/', destination, name="destination"),
    path('package/', package, name="package"),
    path('service/', service, name="service"),
    path('team/', team, name="team"),
    path('testimonial/', testimonial, name="testimonial"),


    path('add-comment/int:about_id>/', add_comment, name='add_comment')

]
