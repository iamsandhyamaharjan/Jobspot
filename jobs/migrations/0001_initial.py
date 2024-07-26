# Generated by Django 5.0.7 on 2024-07-26 14:31

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('company_website', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='logo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('location', models.CharField(blank=True, max_length=201, null=True)),
                ('no_of_openings', models.PositiveIntegerField()),
                ('salary', models.CharField(choices=[('None', 'Select Salary Range'), ('10000-20000', '10000-20000'), ('20000-30000', '20000-30000'), ('30000-40000', '30000-40000'), ('40000-50000', '40000-50000'), ('50000-60000', '50000-60000'), ('60000-70000', '60000-70000'), ('70000-80000', '70000-80000'), ('80000-90000', '80000-90000'), ('90000-100000', '90000-100000')], default=None, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application_valid', models.DateField()),
                ('category', models.CharField(choices=[('None', 'Select One Category'), ('Free Lancer', 'Free Lancer'), ('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Intern', 'Intern'), ('Temporary', 'Temporary'), ('Contract', 'Contract')], default=None)),
                ('type', models.CharField(choices=[('None', 'Select One Type'), ('Teacher', 'Teacher'), ('IT', 'IT'), ('Computer Programmer', 'Computer Programmer'), ('Graphics Designer', 'Graphics Designer'), ('Web Developer', 'Web Developer'), ('Database Administrator', 'Database Administrator'), ('Technician', 'Technician'), ('Accountant', 'Accountant'), ('Software Developer', 'Software Developer'), ('Web Designer', 'Web Designer'), ('Hardware Engineer', 'Hardware Engineer'), ('Network Administrator', 'Network Administrator'), ('Hardware Architect', 'Hardware Architect'), ('Data Analyst', 'Data Analyst'), ('System Administrator', 'System Administrator'), ('Computer Scientist', 'Computer Scientist'), ('Software Engineer', 'Software Engineer'), ('System Securtiy', 'System Securtiy'), ('Mobile Application Developer', 'Mobile Application Developer'), ('Game Designer', 'Game Designer'), ('Game Developer', 'Game Developer'), ('Visual Developer', 'Visual Developer'), ('Network Analyst', 'Network Analyst'), ('Network Manager', 'Network Manager'), ('Network Designer', 'Network Designer'), ('Network Engineer', 'Network Engineer'), ('Software Tester', 'Software Tester'), ('Data Scientist', 'Data Scientist'), ('Data Architect', 'Data Architect'), ('Software Architect', 'Software Architect'), ('Information Architect', 'Information Architect'), ('Statistical Programmer', 'Statistical Programmer'), ('IT Instructor', 'IT Instructor'), ('Texture Artist', 'Texture Artist'), ('Technical Artist', 'Technical Artist'), ('Game Director', 'Game Director'), ('Game Producer', 'Game Producer'), ('Animator', 'Animator'), ('animationsupervisor', 'Animation Supervisor'), ('Animation Supervisor', 'IT Manager'), ('Web Master', 'Web Master'), ('Web Editor', 'Web Editor'), ('Content Manager', 'Content Manager'), ('Cinematic Artist', 'Cinematic Artist'), ('Character Designer', 'Character Designer'), ('Supervisor', 'Supervisor'), ('Profesional Gamer', 'Profesional Gamer')], default=None)),
                ('level', models.CharField(choices=[('None', 'Select One Level'), ('Entry', 'Entry'), ('Mid', 'Mid'), ('Senior', 'Senior'), ('Manager', 'Manager')], default=None)),
                ('modified_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employer.company')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('submitted_on', models.DateField(auto_now=True)),
                ('posted_by', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('submitted_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=1055, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('applicant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.application')),
            ],
        ),
    ]
