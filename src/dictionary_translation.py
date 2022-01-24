from wordfreq import word_frequency
from translate import Translator


def generate_vocabulary(words, original_language, translation_language='en',
                        freq_min=10**-6, freq_max=10**-3):

    translator = Translator(from_lang=original_language, to_lang=translation_language, email="test@gmail.com")
    frequency = [
        {
            "word": word,
            "frequency": word_frequency(word, lang=original_language),
            "translation": translator.translate(word)
        } for word in words if
        (
                (word_frequency(word, lang=original_language) > freq_min) and
                (word_frequency(word, lang=original_language) < freq_max)
        )
    ]

    return frequency
