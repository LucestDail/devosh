# Generated by Django 3.1.6 on 2021-02-18 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210217_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorys',
            field=models.CharField(choices=[('DATA', 'Data(DB)'), ('CLNG', 'C'), ('HTML', 'HTML(CSS)'), ('PROJ', 'Project'), ('PYTH', 'Python'), ('JVSC', 'Javascript'), ('CPSC', 'ComScience'), ('ALGO', 'Algorithm'), ('JAVA', 'Java')], max_length=80, null=True),
        ),
    ]
