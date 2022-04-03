from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from .models import (
    Address,
    City,
    Employees,
    Hotels,
    Roomorders,
    Rooms,
    Roomsfeedback,
    Tourfeedback,
    Tourorders,
    Tours,
    Transferfeedback,
    Transferorders,
    Transfers,
    Users,
)


class StatusChangeView(UpdateView):
    ...


class RetrieveOrdersList(ListView):
    ...


class StaffListView(ListView):
    ...


class WorkAccept(CreateView):
    ...


class RemoveStaffView(DeleteView):
    ...


class ChangePriceView(UpdateView):
    ...


class AddView(CreateView):
    ...
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('GET request!')

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')


class ResieveKeyForPasswordChangeView(View):
    ...


class PasswordChangeView(View):
    ...


class LoginView(View):
    ...


class CreateUserView(CreateView):
    model = Users
    fields = []


class OrderTransferView(CreateView):
    model = Transfers
    fields = []


class OrderTourView(CreateView):
    model = Tours
    fields = []


class OrderRoomView(CreateView):
    model = Rooms
    fields = []
    # template_name = 'books/acme_list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)



class RetieveUsersView(ListView):
    model = Users
    fields = []

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
