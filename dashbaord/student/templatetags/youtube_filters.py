from django import template
import re

register = template.Library()

@register.filter(name='youtube_id')
def youtube_id(value):
    """
    Extracts the YouTube ID from a given URL.
    """
    match = re.search(r"(?<=v=)[^&#]+", value) or re.search(r"(?<=be/)[^&#]+", value) or re.search(r"(?<=.be/)[^&#]+", value) or re.search(r"(?<=v/)[^&#]+", value) or re.search(r"(?<=yout\.be/)[^&#]+", value)
    return match.group(0) if match else None
