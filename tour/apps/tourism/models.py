from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import datetime


class Users(AbstractUser):
    userid = models.AutoField(primary_key=True)
    email = models.EmailField(
        max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    dateofbirthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email'
    ]
    EMAIL_FIELD = None

    def __str__(self):
        return f'{self.userid} {self.username}'

    @staticmethod
    def _create_user(password, email, username, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given email must be set')
        user = Users.objects.create(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(password, email, username, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, email, username, **extra_fields)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пользователь'


class Address(models.Model):
    city = models.ForeignKey('City', models.DO_NOTHING, db_column='city')
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.city) + ' ' + self.name


class City(models.Model):
    country = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.country + ' ' + self.name


class Employees(models.Model):
    user = models.OneToOneField(
        Users, related_name='user_staff', on_delete=models.CASCADE)
    passport = models.ImageField(upload_to='docs/', blank=True, null=True)
    address = models.CharField(max_length=255)
    employmentdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Hotels(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.IntegerField()
    address = models.ForeignKey(
        Address, models.DO_NOTHING, db_column='address')

    def get_absolute_url(self):
        return reverse('hotel-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Roomorders(models.Model):
    ordernumber = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room')
    startdate = models.DateField()
    enddate = models.DateField()
    places = models.IntegerField()
    orderdate = models.DateField(auto_now=True)
    insurancepolicy = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    manager = models.ForeignKey(
        Employees, models.DO_NOTHING, db_column='manager')

    def get_absolute_url(self):
        if self.userid.is_staff:
            return reverse('tourism:retrieve_orders')
        return reverse('tourism:retrieve_orders_client')

    def __str__(self):
        return f'{self.ordernumber} {self.userid}'

    @property
    def time_differnce(self):
        return (self.enddate - self.startdate).days * self.room.price


class Rooms(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    places = models.IntegerField()
    price = models.IntegerField()
    hotel = models.ForeignKey(Hotels, models.DO_NOTHING, db_column='hotel')
    rating = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.title} {self.hotel}'

    def get_absolute_url(self):
        return reverse('room-info', kwargs={'pk': self.pk})


class Roomsfeedback(models.Model):
    room = models.ForeignKey(Rooms, models.DO_NOTHING, db_column='room')
    title = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    rating = models.IntegerField()
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    date = models.DateField()

    def __str__(self):
        return f'{self.room} {self.title}'


class Tourfeedback(models.Model):
    tour = models.ForeignKey('Tours', models.DO_NOTHING, db_column='tour')
    title = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    rating = models.IntegerField()
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    date = models.DateField()

    def __str__(self):
        return f'{self.tour} {self.title}'


class Tourorders(models.Model):
    ordernumber = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    tour = models.ForeignKey('Tours', models.DO_NOTHING, db_column='tour')
    startdate = models.DateField()
    enddate = models.DateField()
    places = models.IntegerField()
    orderdate = models.DateField(auto_now=True)
    insurancepolicy = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    manager = models.ForeignKey(
        Employees, models.DO_NOTHING, db_column='manager')

    def time_differnce(self):
        return (self.enddate - self.startdate).days * self.tour.price

    def get_absolute_url(self):
        if self.userid.is_staff:
            return reverse('tourism:retrieve_orders')
        return reverse('tourism:retrieve_orders_client')

    def __str__(self):
        return f'{self.ordernumber} {self.userid}'


class Tours(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    places = models.IntegerField()
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city')
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Transferfeedback(models.Model):
    transfer = models.ForeignKey(
        'Transfers', models.DO_NOTHING, db_column='transfer')
    title = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    rating = models.IntegerField()
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    date = models.DateField()

    def __str__(self):
        return f'{self.transfer} {self.title}'


class Transferorders(models.Model):
    ordernumber = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    transfer = models.ForeignKey(
        'Transfers', models.DO_NOTHING, db_column='transfer')
    startdate = models.DateField()
    enddate = models.DateField()
    places = models.IntegerField()
    orderdate = models.DateField(auto_now=True)
    insurancepolicy = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    manager = models.ForeignKey(
        Employees, models.DO_NOTHING, db_column='manager')

    def time_differnce(self):
        return (self.enddate - self.startdate).days * self.transfer.price

    def get_absolute_url(self):
        if self.userid.is_staff:
            return reverse('tourism:retrieve_orders')
        return reverse('tourism:retrieve_orders_client')

    def __str__(self):
        return f'{self.ordernumber} {self.userid}'


class Transfers(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    places = models.IntegerField()
    price = models.IntegerField()
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city')
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.title} {self.price}'
