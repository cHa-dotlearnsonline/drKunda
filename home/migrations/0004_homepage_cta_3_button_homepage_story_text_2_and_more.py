# Generated by Django 4.2.7 on 2024-02-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_homepage_cta_1_homepage_cta_1_image_homepage_cta_2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="cta_3_button",
            field=models.CharField(
                blank=True,
                help_text="The Text on the call to action button",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="story_text_2",
            field=models.TextField(
                blank=True,
                help_text="your second story text or description.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="story_title_2",
            field=models.CharField(
                blank=True,
                help_text="your second story title",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="cta_3",
            field=models.CharField(
                blank=True,
                help_text="your other Call to action",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="story_text_1",
            field=models.TextField(
                blank=True,
                help_text="your first story text or description. The story in short",
                null=True,
            ),
        ),
    ]