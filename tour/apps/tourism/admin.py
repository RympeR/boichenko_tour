from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.contrib.auth.admin import UserAdmin
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


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'city', 'name'
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'city__country', 'name'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'country', 'name'
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'country', 'name'


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'address', 'user', 'employmentdate'
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'user__first_name', 'user__username'
    ordering = '-user__dateofbirthday',
    list_filter = (
        ('user__dateofbirthday', DateFieldListFilter),
    )


@admin.register(Hotels)
class HotelsAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'rating',
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'title',


@admin.register(Roomorders)
class RoomordersAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'userid', 'room',
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'room__title',


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'price',
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'title', 'hotel__title'


@admin.register(Tourorders)
class TourordersAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'tour', 'userid', 'orderdate'
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'tour__title',
    list_filter = (
        ('startdate', DateFieldListFilter),
        ('orderdate', DateFieldListFilter),
    )


@admin.register(Tours)
class ToursAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'price', 'city'
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'title', 'city__country', 'city__name'


@admin.register(Transferorders)
class TransferordersAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'userid', 'transfer'
    )
    list_display_links = (
        'pk',
    )
    list_filter = (
        ('startdate', DateFieldListFilter),
        ('enddate', DateFieldListFilter),
        ('orderdate', DateFieldListFilter),
    )


@admin.register(Transfers)
class TransfersAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'price', 'rating'
    )
    list_display_links = (
        'pk',
    )
    ordering = '-rating',
    search_fields = 'city__name', 'city__country', 'title'
    list_filter = (
    )


@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = (
        'pk', 'username', 'first_name', 'last_name',
    )
    list_display_links = (
        'pk',
    )
    search_fields = 'first_name', 'last_name'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'email',
            'phone',
            'address',
            'first_name',
            'last_name',
        )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
         'fields': ('dateofbirthday', 'last_login', 'date_joined')}),
    )
