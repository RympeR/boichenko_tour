from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    userid = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
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

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'


class Address(models.Model):
    city = models.ForeignKey('City', models.DO_NOTHING, db_column='city')
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.city) + ' ' + self.name

    class Meta:
        managed = False
        db_table = 'address'


class City(models.Model):
    country = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.country + ' ' + self.name

    class Meta:
        managed = False
        db_table = 'city'


class Employees(models.Model):
    user = models.OneToOneField(
        Users, related_name='user_staff', on_delete=models.CASCADE)
    passport = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    employmentdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' ' + self.user.lastname

    class Meta:
        managed = False
        db_table = 'employees'


class Hotels(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.IntegerField()
    address = models.ForeignKey(
        Address, models.DO_NOTHING, db_column='address')

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'hotels'


class Roomorders(models.Model):
    ordernumber = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room')
    startdate = models.DateField()
    enddate = models.DateField()
    places = models.IntegerField()
    prices = models.IntegerField()
    orderdate = models.DateField()
    insurancepolicy = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    manager = models.ForeignKey(
        Employees, models.DO_NOTHING, db_column='manager')

    def __str__(self):
        return f'{self.ordernumber} {self.userid}'

    class Meta:
        managed = False
        db_table = 'roomorders'


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

    class Meta:
        managed = False
        db_table = 'rooms'


class Roomsfeedback(models.Model):
    room = models.ForeignKey(Rooms, models.DO_NOTHING, db_column='room')
    title = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    rating = models.IntegerField()
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    date = models.DateField()

    def __str__(self):
        return f'{self.room} {self.title}'

    class Meta:
        managed = False
        db_table = 'roomsfeedback'


class Tourfeedback(models.Model):
    tour = models.ForeignKey('Tours', models.DO_NOTHING, db_column='tour')
    title = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    rating = models.IntegerField()
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    date = models.DateField()

    def __str__(self):
        return f'{self.tour} {self.title}'

    class Meta:
        managed = False
        db_table = 'tourfeedback'


class Tourorders(models.Model):
    ordernumber = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    tour = models.ForeignKey('Tours', models.DO_NOTHING, db_column='tour')
    startdate = models.DateField()
    enddate = models.DateField()
    places = models.IntegerField()
    prices = models.IntegerField()
    orderdate = models.DateField()
    insurancepolicy = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    manager = models.ForeignKey(
        Employees, models.DO_NOTHING, db_column='manager')

    def __str__(self):
        return f'{self.ordernumber} {self.userid}'

    class Meta:
        managed = False
        db_table = 'tourorders'


class Tours(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city')
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.title} '

    class Meta:
        managed = False
        db_table = 'tours'


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

    class Meta:
        managed = False
        db_table = 'transferfeedback'


class Transferorders(models.Model):
    ordernumber = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    transfer = models.ForeignKey(
        'Transfers', models.DO_NOTHING, db_column='transfer')
    startdate = models.DateField()
    enddate = models.DateField()
    places = models.IntegerField()
    prices = models.IntegerField()
    orderdate = models.DateField()
    insurancepolicy = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    manager = models.ForeignKey(
        Employees, models.DO_NOTHING, db_column='manager')

    def __str__(self):
        return f'{self.ordernumber} {self.userid}'

    class Meta:
        managed = False
        db_table = 'transferorders'


class Transfers(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    places = models.IntegerField()
    price = models.IntegerField()
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city')
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.title} {self.price}'

    class Meta:
        managed = False
        db_table = 'transfers'