import nltk
import fugashi
from languages import LANGUAGES


class Tokenizer:
    def get_tokenizer(self, language):
        if language in ["fr", "en", "ge", "it", "ru", "sp"]:
            return PunktTokenizer(language)
        if language == "jp":
            return MeCabTokenizer()
        if language == "cn":
            return ValueError(language, "TODO")
        else:
            return ValueError(language)


class PunktTokenizer():
    def __init__(self, language):
        self.language = LANGUAGES[language]["name"]

    def tokenize(self, s):
        words = nltk.tokenize.word_tokenize(s, language=self.language)
        stopwords = nltk.corpus.stopwords.words(self.language)
        filtered_words = [w.lower() for w in words if w.lower() not in stopwords]
        return filtered_words


class MeCabTokenizer():
    def __init__(self):
        self.language = "japanese"
