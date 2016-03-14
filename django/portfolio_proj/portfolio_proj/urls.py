"""portfolio_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from django.contrib import admin
#landing page
from homepage import urls as homepage_urls
from javapic import urls as javapic_urls
from price_list import urls as price_list_urls
from zengarden import urls as zengarden_urls
from forum import urls as forum_urls


#from portfolio_proj import urls as portfolio_proj_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', portfolio_index),
    url(r'^javapic/', include(javapic_urls)),
    
    url(r'^price_list/', include(price_list_urls)),

    url(r'^zengarden/', include(zengarden_urls)),

    url(r'^forum/', include(forum_urls)),

    #profile page is landing page for portfolio
    url(r'^', include(homepage_urls)),

    #url(r'^portfolio_proj/', include(portfolio_proj_urls))

]
