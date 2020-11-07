from django.contrib import admin

from .models import Customers, Rent, Payment, Driver, TypeOfVehicle, Vehicle, SpecialEquipment, PaymentStatus


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_address')
    list_filter = ('customer_age', 'customer_citizenship')
    search_fields = ('customer_name', 'customer_address', 'customer_email')
    ordering = ('customer_name', 'customer_age')


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('rent_id', 'customer_id', 'vehicle_id', 'rent_fromdate', 'rent_todate', 'payment_id',
                    'driver_id', 'equipment_id')
    list_filter = ('driver_id', 'equipment_id', 'vehicle_id')
    search_fields = ('customer_id', 'payment_id')
    ordering = ('rent_fromdate', 'rent_todate')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'payment_amount', 'payment_status')
    list_filter = ('payment_status',)
    search_fields = ('payment_id', 'payment_amount', 'payment_status')
    ordering = ('payment_id',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('driver_id', 'vehicle_category', 'driver_name', 'driver_email', 'driver_phone_num')
    list_filter = ('driver_name', 'driver_email')
    search_fields = ('phone_num', 'driver_name', 'payment_status')
    ordering = ('driver_id',)


@admin.register(TypeOfVehicle)
class TypeOfVehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'vehicle_type_description')
    list_filter = ('vehicle_type', )
    search_fields = ('vehicle_type', )
    ordering = ('vehicle_type', )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'vehicle_brand', 'vehicle_model', 'vehicle_regnum', 'vehicle_type')
    list_filter = ('vehicle_brand', 'vehicle_type')
    search_fields = ('vehicle_model', 'vehicle_regnum', 'vehicle_type')
    ordering = ('vehicle_id', 'vehicle_regnum')


@admin.register(SpecialEquipment)
class SpecialEquipmentAdmin(admin.ModelAdmin):
   list_display = ('equipment_id', 'equipment_description', 'equipment_type')
   list_filter = ('equipment_type',)
   search_fields = ('equipment_type', )
   ordering = ('equipment_id',)


@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
   list_display = ('payment_status', 'payment_status_description')
   list_filter = ('payment_status', )
   search_fields = ('payment_status', )
   ordering = ('payment_status', )

