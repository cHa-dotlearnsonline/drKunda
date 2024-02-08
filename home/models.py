from django.db import models

from wagtail.models import Page


class HomePage(Page):
    #TODO: Big Hero Image 1
    image = models.ForeignKey(
        "wagtailimages.Image",
        #So that if there's no image no erros are thrown
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="This is here as the Main image on your home page. The first one"
    )

    main_image_text = models.Charfield(
        max_length=255,
        help_text="This is your main image text like your Title and name."
    )
    main_image_subText = models.Charfield(
        max_length = 255,
        help_text= "this is the samll text you will have under your main Image text"
    )

    

    #TODO: Hero Message

    #TODO: Call to Action 1
    #TODO: Call to ACtion Image

    #TODO: Story Title 1
    #TODO: Story Text

    #TODO: CAll to Action 2 Huge
    #TODO: call to ACtion 2 button

    #TODO: Customer Review Section (Make streamfield)

    #TODO: Social Media Links and Images

    pass
