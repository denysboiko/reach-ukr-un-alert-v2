"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
import six
from google.cloud import translate_v2 as translate
translate_client = translate.Client()


def translate_field(obj, field_name):
    targets = ["en","ru","uk"]

    original_text = getattr(obj, field_name)

    if original_text is not None:
        for target in targets:
            translated_field_name = field_name + "_" + target
            setattr(obj, translated_field_name, translate_text(original_text, target))


def translate_text(text, target):

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    result = translate_client.translate(text, target_language=target)
    return result['translatedText']