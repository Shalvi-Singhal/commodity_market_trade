# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CmGroup(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    virtul_amount = models.FloatField(blank=True, null=True)
    start_date = models.CharField(max_length=45, blank=True, null=True)
    end_date = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cm_group'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LiveQuotes(models.Model):
    idlive_quotes = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=145, blank=True, null=True)
    expiry_date = models.CharField(max_length=45, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    ltp = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    change_percentage = models.FloatField(blank=True, null=True)
    avtp = models.FloatField(blank=True, null=True)
    spot_price = models.FloatField(blank=True, null=True)
    sp_date_time = models.CharField(max_length=45, blank=True, null=True)
    best_buy = models.FloatField(blank=True, null=True)
    best_sell = models.FloatField(blank=True, null=True)
    oi = models.IntegerField(blank=True, null=True)
    graph = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_quotes'


class NonAgro(models.Model):
    id_na = models.AutoField(primary_key=True)
    commodity = models.CharField(max_length=45, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    change = models.FloatField(blank=True, null=True)
    change_per = models.FloatField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    time = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_agro'


class NonAgroProducts(models.Model):
    id_nap = models.AutoField(primary_key=True)
    instrument = models.CharField(max_length=45, blank=True, null=True)
    commodity = models.CharField(max_length=45, blank=True, null=True)
    expiry_date = models.CharField(max_length=45, blank=True, null=True)
    option_type = models.CharField(max_length=45, blank=True, null=True)
    strike_price = models.FloatField(blank=True, null=True)
    unit = models.FloatField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    ltp = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    abs_change = models.FloatField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    oi = models.FloatField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    premium_to = models.FloatField(blank=True, null=True)
    ul_product_ltp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_agro_products'


class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    mobileno = models.CharField(max_length=45, blank=True, null=True)
    usercol = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    confirmpassword = models.CharField(max_length=45, blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
