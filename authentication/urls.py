from django.urls import path

from .views import VRegister, end_session, log_in

urlpatterns = [
    path('', VRegister.as_view(), name="Authentication"),
    path('end_session', end_session, name="end_session"),
    path('log_in', log_in, name="log_in"),
]
