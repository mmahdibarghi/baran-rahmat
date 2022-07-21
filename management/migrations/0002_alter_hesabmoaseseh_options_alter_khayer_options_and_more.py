# Generated by Django 4.0.6 on 2022-07-21 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hesabmoaseseh',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='khayer',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='madadjo',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='sandoghkhayerieh',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='tahvilgirandehsandogh',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='sandogh',
            new_name='sandogh_khayerieh',
        ),
    ]