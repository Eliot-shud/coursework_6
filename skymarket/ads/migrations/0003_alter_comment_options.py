# Generated by Django 4.2.1 on 2023-05-22 07:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ads", "0002_alter_ad_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
    ]