"""
URL configuration for animemoments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from land.views import Land
from edits.views import Edits
from social.views import Social
from subscription.views import Subscription
from changelog.views import Changelog
from user.views import RegisterUser, LoginUserView, logout_user, UserPassChange, Clips


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Land.as_view(), name='land'),
    path('edits', Edits.as_view(), name='edits'),
    path('social', Social.as_view(), name='social'),
    path('subscription', Subscription.as_view(), name='subscription'),
    path('changelog', Changelog.as_view(), name='changelog'),

    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('password_change', UserPassChange.as_view(), name='forgot_pass'),
    path('clips', Clips, name='clips')
]
