# Generated by Django 4.1 on 2022-08-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("theblog", "0003_post_post_date_alter_post_title_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="catagory",
            field=models.CharField(default="coding", max_length=255),
        ),
    ]
