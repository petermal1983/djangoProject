# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import template


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    customer_age = models.SmallIntegerField()
    customer_citizenship = models.CharField(max_length=255)
    customer_passportnum = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)
    customer_phone_num = models.CharField(max_length=255)
    customer_licence_num = models.CharField(max_length=255)

    


class Driver(models.Model):
    driver_id = models.IntegerField(primary_key=True)
    vehicle_category = models.SmallIntegerField(unique=True)
    driver_name = models.CharField(unique=True, max_length=255)
    driver_email = models.CharField(unique=True, max_length=255)
    driver_phone_num = models.CharField(unique=True, max_length=255)
    english_speaking = models.BooleanField(blank=True, null=True)
    works_from_date = models.DateField(blank=True, null=True)
    driving_experience_in_years = models.SmallIntegerField(blank=True, null=True)
    rating = models.SmallIntegerField(blank=True, null=True)
    #pic_path = models.CharField(blank=True, null=True, max_length=500)
    pic_path = models.FileField(upload_to='pic_path')
    objects = models.Manager()



class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.ForeignKey('PaymentStatus', models.CharField, db_column='payment_status')


class PaymentStatus(models.Model):
    payment_status = models.AutoField(primary_key=True)
    payment_status_description = models.CharField(unique=True, max_length=255)

    def __str__(self):  # Подумать о корректном отображении экземпляра
        return "Number status: " + str(self.payment_status) + " Description: " + str(self.payment_status_description)



class ValentinManager(models.Manager):
    def get_queryset(self):
        return super(ValentinManager, self).get_queryset().filter(driver_id=2)


class Rent(models.Model):
    rent_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    rent_fromdate = models.DateField()
    rent_todate = models.DateField()
    payment = models.OneToOneField(Payment, models.DO_NOTHING)
    driver = models.ForeignKey(Driver, models.DO_NOTHING)
    equipment = models.ForeignKey('SpecialEquipment', models.DO_NOTHING)
    objects = models.Manager()
    objvalent = ValentinManager()



class SpecialEquipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_description = models.CharField(max_length=255)
    equipment_type = models.CharField(max_length=255)
    pic_path = models.CharField(blank=True, null=True, max_length=500)
    objects = models.Manager()



class TypeOfVehicle(models.Model):
    vehicle_type = models.AutoField(primary_key=True)
    vehicle_type_description = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return str(self.vehicle_type)



class SpcManager(models.Manager):
    def get_queryset(self):
        return super(SpcManager, self).get_queryset().filter(vehicle_type__lte=15)


class Vehicle(models.Model):
    vehicle_id = models.AutoField(db_column='vehicle_Id', primary_key=True)  # Field name made lowercase.
    vehicle_brand = models.CharField(max_length=255)
    vehicle_model = models.CharField(max_length=255)
    vehicle_regnum = models.CharField(max_length=255)
    vehicle_type = models.ForeignKey(TypeOfVehicle, models.DO_NOTHING, db_column='vehicle_type')
    objects = models.Manager()
    spec_objects = SpcManager()
    # vehicle_type = models.SmallIntegerField(unique=True)
    veh_type = template.Library()
    pic_path = models.CharField(blank=True, null=True, max_length=500)

    @veh_type.simple_tag
    def vehicle_type_get(self):
        return int(str(self.vehicle_type))
