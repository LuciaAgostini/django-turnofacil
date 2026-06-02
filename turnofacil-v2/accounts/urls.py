from django.urls import path

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from .views import registro

urlpatterns = [
    path(
        "registro/",
        registro,
        name="registro",
    ),

    path(
        "login/",
        LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
]