from django.utils.encoding import force_text

from wagtail.core.blocks import CharBlock, IntegerBlock, RawHTMLBlock, RichTextBlock, StructBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail_blocks.blocks import (
    ChartBlock,
    CroppedImagesWithTextBlock,
    HeaderBlock,
    ImageSliderBlock,
    ImageTextOverlayBlock,
    ListBlock,
    ListWithImagesBlock,
    MapBlock,
    ThumbnailGalleryBlock,
)


class VideoBlock(StructBlock):
    title = CharBlock()
    embed = EmbedBlock(help_text='Insert full URL of video here. Ex. https://youtu.be/sdfk343244dfef5')
    max_width = IntegerBlock(default=1024, help_text='Set maximum width of the video frame in pixels.')

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        template = 'wagtail_blocks/video.html'
        icon = 'media'
        label = "Embed youtube or vimeo video"


STREAMFIELD_BLOCK_LIST = [
    ('header', HeaderBlock()),
    ('rich_text', RichTextBlock()),
    ('raw_HTML', RawHTMLBlock()),
    ('image_text_overlay', ImageTextOverlayBlock()),
    ('list', ListBlock()),
    ('embed', VideoBlock()),
    ('chart', ChartBlock()),
    ('map', MapBlock()),
    ('cropped_images_with_text', CroppedImagesWithTextBlock()),
    ('list_with_images', ListWithImagesBlock()),
    ('thumbnail_gallery', ThumbnailGalleryBlock()),
    ('image_slider', ImageSliderBlock()),
]

