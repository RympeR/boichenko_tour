from dataclasses import dataclass
from typing import Any, Dict

from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from .forms import (ModelInfoRetrievePolicyRoomOrderForm,
                    ModelInfoRetrievePolicyTourOrderForm,
                    ModelInfoRetrievePolicyTransferOrderForm,
                    ModelInfoRetrievePriceRoomOrderForm,
                    ModelInfoRetrievePriceTourOrderForm,
                    ModelInfoRetrievePriceTransferOrderForm,
                    ModelInfoRetrieveRoomForm, ModelInfoRetrieveRoomOrderForm,
                    ModelInfoRetrieveTourForm, ModelInfoRetrieveTourOrderForm,
                    ModelInfoRetrieveTransferForm,
                    ModelInfoRetrieveTransferOrderForm, ModelsRetrieveForm,
                    RegisterForm, UserLoginForm,
                    LocalPasswordChangeForm)
from .models import (Roomorders, Rooms, Roomsfeedback, Tourfeedback,
                     Tourorders, Tours, Transferfeedback, Transferorders,
                     Transfers, Users)
from django.http import HttpResponseRedirect


class StatusChangeView(View):
    template_name = "tour/status_change.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'form': ModelsRetrieveForm
        })

    def post(self, request, *args, **kwargs):

        data = request.POST
        if data.get('id_s'):
            model = None
            if data.get("model") == "room":
                model = Roomorders

            if data.get("model") == "transfer":
                model = Transferorders

            if data.get("model") == "tour":
                model = Tourorders

            if model:
                model.objects.filter(pk=data.get("id_s")).update(
                    status=data.get("new_status"))
                return render(request, self.template_name, {
                    'form': ModelsRetrieveForm
                })
        else:
            form = None
            if data.get('models') == "room":
                form = ModelInfoRetrieveRoomOrderForm

            if data.get('models') == "transfer":
                form = ModelInfoRetrieveTransferOrderForm

            if data.get('models') == "tour":
                form = ModelInfoRetrieveTourOrderForm
            if form:
                return render(request, self.template_name, {
                    'form': form,
                    'model': data.get('models')
                })
        return render(request, self.template_name, {
            'form': ModelsRetrieveForm
        })


class PolicyChangeView(View):
    template_name = "tour/insurancepolicy_change.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'form': ModelsRetrieveForm
        })

    def post(self, request, *args, **kwargs):

        data = request.POST
        if data.get('id_s'):
            model = None
            if data.get("model") == "room":
                model = Roomorders

            if data.get("model") == "transfer":
                model = Transferorders

            if data.get("model") == "tour":
                model = Tourorders

            if model:
                model.objects.filter(pk=data.get("id_s")).update(
                    insurancepolicy=data.get("policy"))
                return render(request, self.template_name, {
                    'form': ModelsRetrieveForm
                })
        else:
            form = None
            if data.get('models') == "room":
                form = ModelInfoRetrievePolicyRoomOrderForm

            if data.get('models') == "transfer":
                form = ModelInfoRetrievePolicyTransferOrderForm

            if data.get('models') == "tour":
                form = ModelInfoRetrievePolicyTourOrderForm
            if form:
                return render(request, self.template_name, {
                    'form': form,
                    'model': data.get('models')
                })
        return render(request, self.template_name, {
            'form': ModelsRetrieveForm
        })


class PriceChangeView(View):
    template_name = "tour/price_change.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'form': ModelsRetrieveForm
        })

    def post(self, request, *args, **kwargs):

        data = request.POST
        if data.get('id_s'):
            model = None
            if data.get("model") == "room":
                model = Roomorders

            if data.get("model") == "transfer":
                model = Transferorders

            if data.get("model") == "tour":
                model = Tourorders

            if model:
                model.objects.filter(pk=data.get("id_s")).update(
                    prices=data.get("price"))
                return render(request, self.template_name, {
                    'form': ModelsRetrieveForm
                })
        else:
            form = None
            if data.get('models') == "room":
                form = ModelInfoRetrievePriceRoomOrderForm

            if data.get('models') == "transfer":
                form = ModelInfoRetrievePriceTransferOrderForm

            if data.get('models') == "tour":
                form = ModelInfoRetrievePriceTourOrderForm
            if form:
                return render(request, self.template_name, {
                    'form': form,
                    'model': data.get('models')
                })
        return render(request, self.template_name, {
            'form': ModelsRetrieveForm
        })


class StatusRetrieveTourView(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, "tour/status_change.html", {
            "status": Tourorders.objects.filter(pk=pk).values("status")[0]["status"],
            'obj_info': Tourorders.objects.get(pk=pk),
        })


class StatusRetrieveRoomView(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, "tour/status_change.html", {
            "status": Roomorders.objects.filter(pk=pk).values("status")[0]["status"],
            'obj_info': Roomorders.objects.get(pk=pk),
        })


class StatusRetrieveTransferView(View):
    def get(self, request, pk, *args, **kwargs):
        return render(request, "tour/status_change.html", {
            "status": Transferorders.objects.filter(pk=pk).values("status")[0]["status"],
            'obj_info': Transferorders.objects.get(pk=pk),
        })


class ChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tour/change_password.html", {
            'form': LocalPasswordChangeForm
        })

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            print("valid")
            print(form.cleaned_data)
            update_session_auth_hash(request, form.user)
        else:
            print(form.errors)
        return render(request, "tour/change_password.html", {
            'form': LocalPasswordChangeForm
        })


class InfoRetrieveRoomView(View):
    template_name = "tour/info_retrieve.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'model_name': 'Номера',
            "form": ModelInfoRetrieveRoomForm
        })

    def post(self, request, *args, **kwargs):
        data = request.POST
        if data.get('id_s'):
            return render(request, self.template_name, {
                'model_name': 'Номера',
                "info": Rooms.objects.get(pk=data.get('id_s')),
            })
        return render(request, self.template_name, {})


class InfoRetrieveToursView(View):
    template_name = "tour/info_retrieve.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'model_name': 'Туры',
            "form": ModelInfoRetrieveTourForm
        })

    def post(self, request, *args, **kwargs):
        data = request.POST
        if data.get('id_s'):
            return render(request, self.template_name, {
                'model_name': 'Туры',
                "info": Tours.objects.get(pk=data.get('id_s')),
            })
        return render(request, self.template_name, {})


class InfoRetrieveTransferView(View):
    template_name = "tour/info_retrieve.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'model_name': 'Трансферы',
            "form": ModelInfoRetrieveTransferForm
        })

    def post(self, request, *args, **kwargs):
        data = request.POST
        if data.get('id_s'):
            return render(request, self.template_name, {
                'model_name': 'Трансферы',
                "info": Transfers.objects.get(pk=data.get('id_s')),
            })
        return render(request, self.template_name, {})


class RemoveStaffView(View):
    def post(self, request):
        data = request.POST
        Users.objects.filter(pk=data.get("pk")).update(
            is_staff=False, is_active=False)
        return render(request, "tour/remove_staff.html", {})


class OrderTransferView(CreateView):
    model = Transferorders
    fields = [
        'userid',
        'transfer',
        'startdate',
        'enddate',
        'places',
        'insurancepolicy',
        'status',
        'manager',
    ]
    template_name = "tour/order_transfer.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'трансфера'
        return context

    def form_valid(self, form):
        try:
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/order-transfer/')


class OrderTourView(CreateView):
    model = Tourorders
    fields = [
        'userid',
        'tour',
        'startdate',
        'enddate',
        'places',
        'insurancepolicy',
        'status',
        'manager',
    ]
    template_name = 'tour/order_tour.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'тура'
        return context

    def form_valid(self, form):
        try:
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/order-tour/')
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect


class OrderRoomView(CreateView):
    model = Roomorders
    fields = [
        'userid',
        'room',
        'startdate',
        'enddate',
        'places',
        'insurancepolicy',
        'status',
        'manager',
    ]
    template_name = 'tour/order_room.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Номера'
        return context

    def form_valid(self, form):
        try:
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/order-room/')


class RetrieveUsersView(ListView):
    model = Users
    template_name = 'tour/retrieve_users.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Пользователи'
        return context


class RetrieveUsersOrdersView(View):
    model = Users
    fields = []
    template_name = 'tour/retrieve_users_orders.html'

    def get(self, request, *args, **kwargs):
        results = []
        models = [
            Transferorders,
            Tourorders,
            Roomorders,
        ]
        user = request.user
        results = {
            'transferorders': [],
            'tourorders': [],
            'roomorders': [],
        }
        for model_object in models:
            qs = model_object.objects.filter(userid__pk=user.pk)
            for obj in qs:
                results[model_object.__name__.lower()].append(obj)
        return render(request, self.template_name, results)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class RetrievesOrdersView(View):
    model = Users
    fields = []
    template_name = 'tour/retrieve_users_orders.html'

    def get(self, request, *args, **kwargs):
        models = [
            Transferorders,
            Tourorders,
            Roomorders,
        ]
        results = {
            'transferorders': [],
            'tourorders': [],
            'roomorders': [],
        }
        for model_object in models:
            qs = model_object.objects.all()
            for obj in qs:
                results[model_object.__name__.lower()].append(obj)
        return render(request, self.template_name, results)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


def register(request):
    if request.user.is_authenticated:
        return redirect('tourism:main')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('tourism:main')
        else:
            print(form.errors)
    context = {}
    context['title'] = 'Регистрация'
    context['form'] = RegisterForm
    return render(request, 'tour/registration.html', context)


def logout_view(request):
    logout(request)
    return redirect('tourism:main')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('tourism:main')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            new_user = authenticate(
                username=form.cleaned_data['username'],
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


class OrderClientTransferView(CreateView):
    model = Transferorders
    fields = [
        'transfer',
        'startdate',
        'enddate',
        'places',
        'insurancepolicy',
        'manager',
    ]
    template_name = "tour/order_transfer.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'трансфера'
        return context

    def form_valid(self, form):
        form.instance.userid = self.request.user
        form.instance.status = 'New'
        try:
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/order-transfer-client/')


class OrderClientTourView(CreateView):
    model = Tourorders
    fields = [
        'tour',
        'startdate',
        'enddate',
        'places',
        'insurancepolicy',
        'manager',
    ]
    template_name = 'tour/order_tour.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'тура'
        return context

    def form_valid(self, form):
        form.instance.userid = self.request.user
        form.instance.status = 'New'
        try:
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/order-tour-client/')
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect


class OrderClientRoomView(CreateView):
    model = Roomorders
    fields = [
        'room',
        'startdate',
        'enddate',
        'places',
        'insurancepolicy',
        'manager',
    ]
    template_name = 'tour/order_room.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Номера'
        return context

    def form_valid(self, form):
        form.instance.userid = self.request.user
        form.instance.status = 'New'
        try:
            self.object = form.save()
            return HttpResponseRedirect(self.get_success_url())
        except Exception as e:
            print(e)
            return HttpResponseRedirect('/order-room-client/')
