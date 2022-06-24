# Generated by Django 4.0.5 on 2022-06-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_attrition_type_user_date_of_hire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bamboo_hr_active_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='clearance_and_exit_interview',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='company_assets_returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='deactivate_biometric_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='deactivate_client_tools_and_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='deactivate_door_badge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='deactivate_ev_mail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='deactivate_pc_login',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='nearest_payroll_salary_or_CA_on_hold',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='remove_from_evox_roster',
            field=models.BooleanField(default=False),
        ),
    ]
