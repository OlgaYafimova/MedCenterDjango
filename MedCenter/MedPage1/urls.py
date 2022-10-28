from django.urls import path
from .views import HomeView, ContactsView, InfoView, InfoDocView

urlpatterns = [
    path('', HomeView, name="home_view"),
    path('contacts/', ContactsView, name="contacts_view"),
    path('information/', InfoView, name="info_view"),
    path('info_doc/<int:num>', InfoDocView, name="info_docview"),
]
