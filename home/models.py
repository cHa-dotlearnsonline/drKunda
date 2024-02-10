from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):

    #TODO: add content panels and add verbose names to eveything
    #Big Hero Image 1
    image = models.ForeignKey(
        "wagtailimages.Image",
        #So that if there's no image no erros are thrown
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="This is here as the Main image on your home page. The first one"
    )
    # Hero Message
    main_image_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="This is your main image text like your Title and name."

    )
    main_image_text = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        help_text="This is your main image small text."
    )
    main_image_subText = models.CharField(
        max_length = 255,
        null=True,
        blank=True,
        help_text= "this is the samll text you will have under your main Image text"
    )

    #: Call to Action 1
    cta_1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="you first call to action text"
    )
    #: Call to ACtion Image
    cta_1_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text = "Another Image"

    )
    cta_2= models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Text to Display over the image"
    )
    # Story Title 1
    story_title_1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="your first Story title"
    )
    # Story Text
    story_text_1 = models.TextField(
        null=True,
        blank=True,
        help_text = "your first story text or description. The story in short"
    )
    story_title_2 = models.CharField(
        max_length = 255,
        null=True,
        blank =True,
        help_text="your second story title"
    )

    story_text_2 = models.TextField (
        null=True,
        blank=True,
        help_text= "your second story text or description."
    )

    # CAll to Action 3 Huge
    cta_3 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="your other Call to action"
    )
     
    #: call to ACtion 3 button
    cta_3_button = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text= "The Text on the call to action button"
    )
    # Customer Review Section (Make streamfield)
    customer_review = StreamField(
        [
            ('review', blocks.StructBlock([
            ("review_text", blocks.CharBlock()),
            ("person", blocks.CharBlock()),
            ("transformation_photo", ImageChooserBlock(required=False))
            
            ]))
        ],
        verbose_name="Customer Reviews",
        use_json_field=True,
        null=True,
        blank=True,
    )

    #Social Media Links and Images
    social_media = StreamField(
        [
            ("socials", blocks.StructBlock([
            ("logo", ImageChooserBlock(required=True)),
            ("your_link", blocks.CharBlock(required=True))
        ]))
        ],
        verbose_name="Social Media Links",
        use_json_field=True,
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("image"),
            FieldPanel("main_image_title"),
            FieldPanel("main_image_subText"),
            FieldPanel("main_image_text"),
            
        ], heading="Hero Section"),
        FieldPanel("cta_1_image"),
        FieldPanel("cta_2"),
        FieldPanel("cta_3"),
        FieldPanel("cta_3_button"),

        MultiFieldPanel(
            [
                FieldPanel("story_title_1"),
                FieldPanel("story_text_1")
            ],
            heading="Your first Story"
        ),

        MultiFieldPanel(
            [
                FieldPanel("story_title_2"),
                FieldPanel("story_text_2")
            ],
            heading="your second story"
        ),
        FieldPanel("customer_review"),
        FieldPanel("social_media")
    ]