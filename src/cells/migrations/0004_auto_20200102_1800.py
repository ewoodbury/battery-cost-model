# Generated by Django 2.2.5 on 2020-01-03 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0003_auto_20200101_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cellinput',
            old_name='alfoilthickness',
            new_name='al_foil_thickness',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='anactivefrac',
            new_name='an_active_frac',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='anbinderfrac',
            new_name='an_binder_frac',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='anconductorfrac',
            new_name='an_conductor_frac',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='angravcapacity',
            new_name='an_grav_capacity',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='avgdischargevoltage',
            new_name='avg_discharge_voltage',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='catactivefrac',
            new_name='cat_active_frac',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='catbinderfrac',
            new_name='cat_binder_frac',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='catconductorfrac',
            new_name='cat_conductor_frac',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='catformulaid',
            new_name='cat_formula_id',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='catgravcapacity',
            new_name='cat_grav_capacity',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='cattotalloading',
            new_name='cat_total_loading',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='cellid',
            new_name='cell_id',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='cellname',
            new_name='cell_name',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='celltype',
            new_name='cell_type',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='cufoilthickness',
            new_name='cu_foil_thickness',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='electrodelength',
            new_name='electrode_length',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='electrodewidth',
            new_name='electrode_width',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='npratio',
            new_name='np_ratio',
        ),
        migrations.RenameField(
            model_name='cellinput',
            old_name='separatorname',
            new_name='separator_name',
        ),
    ]
