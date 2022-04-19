from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'tourism'

urlpatterns = [
    path('', main, name='main'),
    path('order-room/', OrderRoomView.as_view(), name='room_order'),
    path('status-change/', StatusChangeView.as_view(), name='status_change'),
    path('policy-change/', PolicyChangeView.as_view(), name='policy_change'),
    path('price-change/', PriceChangeView.as_view(), name='price_change'),
    path('status-retrieve-tour/<int:pk>',
         StatusRetrieveTourView.as_view(), name='status_retrieve'),
    path('status-retrieve-room/<int:pk>',
         StatusRetrieveRoomView.as_view(), name='status_retrieve'),
    path('status-retrieve-transfer/<int:pk>',
         StatusRetrieveTransferView.as_view(), name='status_retrieve'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('info-retrieve-tour/', InfoRetrieveToursView.as_view(),
         name='info_retrieve_tour'),
    path('info-retrieve-room/', InfoRetrieveRoomView.as_view(),
         name='info_retrieve_room'),
    path('info-retrieve-transfer/', InfoRetrieveTransferView.as_view(),
         name='info_retrieve_transfer'),
    path('remove-staff/', RemoveStaffView.as_view(), name='remove_staff'),
    path('order-transfer/', OrderTransferView.as_view(), name='order_transfer'),
    path('order-tour/', OrderTourView.as_view(), name='order_tour'),
    path('order-room/', OrderRoomView.as_view(), name='order_room'),
    path('retrieve-users/', RetrieveUsersView.as_view(), name='retrieve_users'),
    path('retrieve-orders/', RetrievesOrdersView.as_view(), name='retrieve_orders'),
    path('retrieve-users-orders/', RetrieveUsersOrdersView.as_view(),
         name='retrieve_users_orders'),
    path('register/', register, name='register'),
#     path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
