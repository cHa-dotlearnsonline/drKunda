# Generated by Django 4.2.7 on 2024-02-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_cta_3_button_homepage_story_text_2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="main_image_title",
            field=models.CharField(
                blank=True,
                help_text="This is your main image text like your Title and name.",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="main_image_text",
            field=models.TextField(
                blank=True,
                help_text="This is your main image small text.",
                max_length=255,
                null=True,
            ),
        ),
    ]