from django.db import models


# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    client_type = models.CharField(max_length=255)


class TestStandard(models.Model):
    standard_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    published_date = models.CharField(max_length=255)


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)


class Location(models.Model):
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255)


class Product(models.Model):
    model_number = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    manufacturing_date = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    width = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    cell_area = models.CharField(max_length=255)
    cell_technology = models.CharField(max_length=255)
    total_num_cells = models.CharField(max_length=255)
    num_cells_series = models.CharField(max_length=255)
    num_series_strings = models.CharField(max_length=255)
    num_bypass_diodes = models.CharField(max_length=255)
    series_fuse_rating = models.CharField(max_length=255)
    interconnect_material = models.CharField(max_length=255)
    interconnect_supplier = models.CharField(max_length=255)
    superstrate_type = models.CharField(max_length=255)
    substrate_manufacturer = models.CharField(max_length=255)
    frame_material = models.CharField(max_length=255)
    frame_adhesive = models.CharField(max_length=255)
    encapsulant_type = models.CharField(max_length=255)
    encapsulant_manufacturer = models.CharField(max_length=255)
    junction_box_type = models.CharField(max_length=255)
    junction_box_manufacturer = models.CharField(max_length=255)
    junction_box_adhesive = models.CharField(max_length=255)
    cable_type = models.CharField(max_length=255)
    connector_type = models.CharField(max_length=255)


class Certificate(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.CharField(max_length=255)
    issue_date = models.CharField(max_length=255)
    standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)


class Service(models.Model):
    service_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    published_date = models.CharField(max_length=255)
    standard_id = models.ForeignKey(TestStandard, on_delete=models.CASCADE, null=True)


class TestSequence(models.Model):
    sequence_name = models.CharField(max_length=255)


class PerformanceData(models.Model):
    model_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    sequence_id = models.ForeignKey(TestSequence, on_delete=models.CASCADE, null=True)
    max_system_voltage = models.CharField(max_length=255)
    rated_voc = models.CharField(max_length=255)
    rated_isc = models.CharField(max_length=255)
    rated_vmp = models.CharField(max_length=255)
    rated_imp = models.CharField(max_length=255)
    rated_pmp = models.CharField(max_length=255)
    rated_ff = models.CharField(max_length=255)
