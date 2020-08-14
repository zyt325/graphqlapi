from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=11)
    uuid = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=255)
    hostname = models.CharField(unique=True, max_length=50, blank=True, null=True)
    room = models.PositiveIntegerField(blank=True, null=True)
    rack = models.ForeignKey('Rack', models.DO_NOTHING, db_column='rack', blank=True, null=True)
    rack_unit = models.PositiveIntegerField(blank=True, null=True)
    rack_pos_depth = models.CharField(max_length=6, blank=True, null=True)
    rack_size = models.IntegerField(blank=True, null=True)
    parent = models.PositiveIntegerField(blank=True, null=True)
    owner = models.PositiveIntegerField(blank=True, null=True)
    responsible = models.PositiveIntegerField(blank=True, null=True)
    pre_assigned = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    ram = models.PositiveIntegerField(blank=True, null=True)
    max_ram = models.IntegerField(blank=True, null=True)
    ram_slots = models.IntegerField(blank=True, null=True)
    single_ram = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True, null=True)
    serial = models.CharField(max_length=255)
    qube_status = models.CharField(max_length=7)
    nagios_status = models.CharField(max_length=8)
    os = models.ForeignKey('Os', models.DO_NOTHING, db_column='os', blank=True, null=True)
    system_class = models.PositiveSmallIntegerField(blank=True, null=True)
    cpu_quantity = models.PositiveIntegerField(blank=True, null=True)
    cpu = models.CharField(max_length=18, blank=True, null=True)
    gpu_quantity = models.PositiveIntegerField(blank=True, null=True)
    gpu = models.CharField(max_length=45, blank=True, null=True)
    drafts = models.IntegerField()
    workstation_type = models.CharField(max_length=7, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    scrap_status = models.CharField(max_length=1, blank=True, null=True)
    script_add = models.CharField(max_length=1, blank=True, null=True)
    quantity = models.SmallIntegerField(blank=True, null=True)
    warehouse = models.PositiveIntegerField(blank=True, null=True)
    blade = models.CharField(max_length=50, blank=True, null=True)
    blade_parent = models.PositiveIntegerField(blank=True, null=True)
    blade_parent_pos = models.PositiveIntegerField(blank=True, null=True)
    location = models.PositiveIntegerField()
    component_type = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    last_update = models.DateTimeField()
    asset_number = models.CharField(unique=True, max_length=50, blank=True, null=True)
    company = models.IntegerField(blank=True, null=True)
    lending_out = models.CharField(max_length=7, blank=True, null=True)
    purchasing = models.IntegerField(blank=True, null=True)
    asset_number_bak = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'
        app_label = 'inventory'


class Rack(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100)
    room = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'rack'
        app_label = 'inventory'


class Os(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'os'
        app_label = 'inventory'


class SystemClass(models.Model):
    value = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_class'
        app_label = 'inventory'


class PuppetVariable(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puppet_variable'
        app_label = 'inventory'


class PuppetVariableMap(models.Model):
    item = models.ForeignKey('Item', models.DO_NOTHING, db_column='item')
    variable = models.ForeignKey('PuppetVariable', models.DO_NOTHING, db_column='variable')
    value = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puppet_variable_map'
        unique_together = (('id', 'item'),)
        app_label = 'inventory'


class ItemView(models.Model):
    id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=11)
    uuid = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    hostname = models.CharField(max_length=50, blank=True, null=True)
    room = models.PositiveIntegerField(blank=True, null=True)
    rack = models.PositiveIntegerField(blank=True, null=True)
    rack_unit = models.PositiveIntegerField(blank=True, null=True)
    rack_pos_depth = models.CharField(max_length=6, blank=True, null=True)
    rack_size = models.IntegerField(blank=True, null=True)
    parent = models.PositiveIntegerField(blank=True, null=True)
    owner = models.PositiveIntegerField(blank=True, null=True)
    responsible = models.PositiveIntegerField(blank=True, null=True)
    pre_assigned = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    ram = models.PositiveIntegerField(blank=True, null=True)
    max_ram = models.IntegerField(blank=True, null=True)
    ram_slots = models.IntegerField(blank=True, null=True)
    single_ram = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50, blank=True, null=True)
    serial = models.CharField(max_length=255)
    qube_status = models.CharField(max_length=7)
    nagios_status = models.CharField(max_length=8)
    os = models.PositiveIntegerField(blank=True, null=True)
    system_class = models.PositiveSmallIntegerField(blank=True, null=True)
    cpu_quantity = models.PositiveIntegerField(blank=True, null=True)
    cpu = models.CharField(max_length=18, blank=True, null=True)
    gpu_quantity = models.PositiveIntegerField(blank=True, null=True)
    gpu = models.CharField(max_length=45, blank=True, null=True)
    drafts = models.IntegerField()
    workstation_type = models.CharField(max_length=7, blank=True, null=True)
    scrap_status = models.CharField(max_length=1, blank=True, null=True)
    script_add = models.CharField(max_length=1, blank=True, null=True)
    quantity = models.SmallIntegerField(blank=True, null=True)
    blade = models.CharField(max_length=50, blank=True, null=True)
    blade_parent = models.PositiveIntegerField(blank=True, null=True)
    blade_parent_pos = models.PositiveIntegerField(blank=True, null=True)
    location = models.PositiveIntegerField()
    component_type = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    last_update = models.DateTimeField()
    asset_number = models.CharField(max_length=50, blank=True, null=True)
    company = models.IntegerField(blank=True, null=True)
    lending_out = models.CharField(max_length=7, blank=True, null=True)
    purchasing = models.IntegerField(blank=True, null=True)
    asset_number_bak = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    gpu_score = models.SmallIntegerField(blank=True, null=True)
    gpu_model = models.CharField(max_length=15, blank=True, null=True)
    gpu_number = models.CharField(max_length=15, blank=True, null=True)
    cpu_model = models.CharField(max_length=15, blank=True, null=True)
    cpu_version = models.PositiveIntegerField(blank=True, null=True)
    cpu_clock_speed = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cpu_socket = models.CharField(max_length=15, blank=True, null=True)
    cpu_cores = models.PositiveIntegerField(blank=True, null=True)
    cpu_tdp = models.PositiveSmallIntegerField(blank=True, null=True)
    cpu_single = models.SmallIntegerField(blank=True, null=True)
    cpu_score = models.PositiveSmallIntegerField(blank=True, null=True)
    warehouse = models.PositiveIntegerField(blank=True, null=True)
    owner_name = models.CharField(max_length=55, blank=True, null=True)
    owner_logical_company = models.PositiveIntegerField(blank=True, null=True)
    department = models.PositiveIntegerField(blank=True, null=True)
    responsible_name = models.CharField(max_length=55, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    line = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_view'
        app_label = 'inventory'
