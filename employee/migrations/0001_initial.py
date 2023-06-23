# Generated by Django 4.2.2 on 2023-06-23 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20, null=True)),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('designation', models.CharField(max_length=20)),
                ('team', models.CharField(max_length=20, null=True)),
                ('salary', models.TextField(null=True)),
                ('phonenumber', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('leave_type', models.CharField(choices=[('Half day', 'Half day'), ('Full day', 'Full day')], max_length=300)),
                ('purpose', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]