# Generated by Django 3.1.6 on 2021-02-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorys',
            field=models.CharField(choices=[('JAVA', 'Java'), ('CPSC', 'ComScience'), ('ALGO', 'Algorithm'), ('JVSC', 'Javascript'), ('PYTH', 'Python'), ('CLNG', 'C'), ('HTML', 'HTML(CSS)'), ('PROJ', 'Project'), ('DATA', 'Data(DB)')], max_length=80, null=True),
        ),
    ]
