# Generated by Django 3.1.6 on 2021-02-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categorys',
            field=models.CharField(choices=[('CLNG', 'C'), ('CPSC', 'ComScience'), ('HTML', 'HTML(CSS)'), ('PYTH', 'Python'), ('JVSC', 'Javascript'), ('JAVA', 'Java'), ('PROJ', 'Project'), ('DATA', 'Data(DB)'), ('ALGO', 'Algorithm')], max_length=80, null=True),
        ),
    ]