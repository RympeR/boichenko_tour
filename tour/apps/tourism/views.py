from typing import Any, Dict
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserLoginForm
from .models import (
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
from dataclasses import dataclass


class StatusChangeView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        model = None
        if data.get("model") == "room":
            model = Roomorders

        if data.get("model") == "transfer":
            model = Transferorders

        if data.get("model") == "tour":
            model = Tourorders

        if model:
            model.objects.filter(pk=data.get("pk")).update(
                status=data.get("status"))
        return render(request, "tour/status_change.html", {})


class PolicyChangeView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        model = None
        if data.get("model") == "room":
            model = Roomorders

        if data.get("model") == "transfer":
            model = Transferorders

        if data.get("model") == "tour":
            model = Tourorders

        if model:
            model.objects.filter(pk=data.get("pk")).update(
                insurancepolicy=data.get("insurancepolicy"))
        return render(request, "tour/insurancepolicy_change.html", {})


class PriceChangeView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        model = None
        if model == "room":
            model = Roomorders

        if model == "transfer":
            model = Transferorders

        if model == "tour":
            model = Tourordersz

        if model:
            model.objects.filter(pk=data.get("pk")).update(
                insurpricesancepolicy=data.get("prices"))
        return render(request, "tour/price_change.html", {})


class StatusRetrieveTourView(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, "tour/status_change.html", {
            "status": Tourorders.objects.filter(pk=pk).values("status")[0]["status"],
            'obj_info': model.objects.get(pk=pk),
        })


class StatusRetrieveRoomView(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, "tour/status_change.html", {
            "status": Roomorders.objects.filter(pk=pk).values("status")[0]["status"],
            'obj_info': model.objects.get(pk=pk),
        })


class StatusRetrieveTransferView(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, "tour/status_change.html", {
            "status": Transferorders.objects.filter(pk=pk).values("status")[0]["status"],
            'obj_info': model.objects.get(pk=pk),
        })


class ChangePasswordView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user
        user.set_password(data['password'])
        user.save()
        return render(request, "tour/change_password.html", {})


class InfoRetrieveRoomView(View):
    template_name = "tour/info_retrieve.html"

    def get(self, request, *args, **kwargs):
        data = request.query_params
        if data.get('pk'):
            return redirect(model, pk=data.get('pk'))
        else:
            qs = Rooms.objects.all()
            return render(request, self.template_name, {
                'model_name': 'Комнаты',
                "info": qs
            })
        return render(request, self.template_name, {})


class InfoRetrieveToursView(View):
    template_name = "tour/info_retrieve.html"

    def get(self, request, *args, **kwargs):
        data = request.query_params
        if data.get('pk'):
            return redirect(model, pk=data.get('pk'))
        else:
            qs = Tours.objects.all()
            return render(request, self.template_name, {
                'model_name': 'Туры',
                "info": qs
            })
        return render(request, self.template_name, {})


class InfoRetrieveTransferView(View):
    template_name = "tour/info_retrieve.html"

    def get(self, request, *args, **kwargs):
        data = request.query_params
        if data.get('pk'):
            return redirect(model, pk=data.get('pk'))
        else:
            qs = Transfers.objects.all()
            return render(request, self.template_name, {
                'model_name': 'Трансферы',
                "info": qs
            })
        return render(request, self.template_name, {})


class RemoveStaffView(View):
    def post(self, request):
        data = request.POST
        Users.objects.filter(pk=data.get("pk")).update(
            is_staff=False, is_active=False)
        return render(request, "tour/remove_staff.html", {})


class OrderTransferView(CreateView):
    model = Transfers
    fields = [
        'userid',
        'transfer',
        'startdate',
        'enddate',
        'places',
        'prices',
        'orderdate',
        'insurancepolicy',
        'status',
        'manager',
    ]
    template_name = "tour/order_transfer.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class OrderTourView(CreateView):
    model = Tours
    fields = [
        'userid',
        'tour',
        'enddate',
        'places',
        'prices',
        'orderdate',
        'insurancepolicy',
        'status',
        'manager',
    ]
    template_name = 'tour/order_tour.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class OrderRoomView(CreateView):
    model = Rooms
    fields = [
        'userid',
        'room',
        'startdate',
        'enddate',
        'places',
        'price',
        'insuarancepolicy',
        'status',
        'manager',
    ]
    template_name = 'tour/order_room.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class RetrieveUsersView(ListView):
    model = Users
    template_name = 'tour/retrieve_users.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class RetrieveUsersOrdersView(View):
    model = Users
    fields = []
    template_name = 'tour/retrieve_users_orders.html'

    def get(self, request, pk, *args, **kwargs):
        results = []
        models = [
            Transferorders,
            Tourorders,
            Roomorders,
        ]
        for model_object in models:
            qs = model_object.objects.filter(userid__pk=pk)
            for obj in qs:
                results.append(obj)
        return results

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


def register(request):
    if request.user.is_authenticated:
        return redirect('tourism:index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('tourism:index')
    context = {}
    context['title'] = 'Регистрация'
    return render(request, 'tour/registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('tourism:index')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('tourism:main')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
            return redirect('tourism:main')
        else:
            result = {
                "status": "error",
                "errors": form.errors
            }
            print(result)
    context = {}
    context['form'] = UserLoginForm()
    context['title'] = 'Вход'

    return render(request, 'tour/login.html', context)


def main(request):
    context = {}
    if request.user:
        user = request.user
        context['user'] = user
        

    return render(request, 'tour/main.html', context=context)
