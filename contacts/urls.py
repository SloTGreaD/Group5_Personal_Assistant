from django.urls import path
from .views import (
    ContactUpcomingBirthdayListView,
    ContactSearchResultsView,
    ContactUpdateView,
    ContactDeleteView,
    ContactCreateView,
    IndexView,
    ContactListView
)

app_name = 'contacts'

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('contacts/list/', ContactListView.as_view(), name='list'),
    path('contacts/create/', ContactCreateView.as_view(), name='create'),
    path('contacts/update/<int:pk>/', ContactUpdateView.as_view(), name='update'),
    path('contacts/delete/<int:pk>/', ContactDeleteView.as_view(), name='delete'),
    path('contacts/search/', ContactSearchResultsView.as_view(), name='search'),
    path('birthdays/', ContactUpcomingBirthdayListView.as_view(), name='birthdays'),
]