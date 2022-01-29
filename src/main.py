import argparse
import genanki
import os
from cards_template import video_and_original_subtitle_to_translation_template, video_to_subtitle, \
    translation_to_original_and_video, word_and_translation
from youtube_api import fetch_subtitle_data
from tokenizer import Tokenizer
from dictionary_translation import generate_vocabulary


from pathlib import Path
mod_path = Path(__file__).parent.parent
output = 'output'
output_folder = (mod_path / output).resolve()

parser = argparse.ArgumentParser(description='Anki Deck Creator')
parser.add_argument(
    '--video_id',
    type=str,
    help='The url id of the youtube video with subtitles',
    default='8Q1WDF6gUq0')
parser.add_argument(
    '--original_language',
    type=str,
    help='The original language of the video with subtitles',
    default='ru')
parser.add_argument(
    '--translation_language',
    type=str,
    help='The target translation language of the video',
    default='en')
parser.add_argument(
    '--generate_word_cards',
    type=bool,
    help='Whether or not to generate individual words',
    default=False)

if __name__ == '__main__':

    args = parser.parse_args()

    video_id = args.video_id
    original_language = args.original_language
    translation_language = args.translation_language
    generate_word_cards = args.generate_word_cards
    ol, tl = fetch_subtitle_data(video_id, original_language, translation_language)
    original = {t['start']: t['text'] for t in ol}

    duration = {t['start']: t['duration'] for t in ol}
    translation = {t['start']: t['text'] for t in tl}
    subtitles = {
        s: {
            "original": original[s],
            "translation": translation[s],
            "duration": duration[s],
            "start": s,
        } for s in original if s in translation
    }
    subtitles = [subtitles[s] for s in subtitles]
    counter = 0
    notes = []
    tokenizer = Tokenizer().get_tokenizer(original_language)
    seen_words = []
    for r in subtitles:
        if generate_word_cards:
            tokens = tokenizer.tokenize(r["original"])
            vocabulary = list(set([w for w in tokens if w not in seen_words]))
            vocabulary = generate_vocabulary(vocabulary, original_language)

            for word in vocabulary:
                print(word)
                seen_words.append(word['word'])
                notes.append(
                    genanki.Note(
                        model=word_and_translation,
                        fields=[word['word'], word['word'], word['translation']]
                    )
                )
        notes.append(
            genanki.Note(
                model=video_and_original_subtitle_to_translation_template,
                fields=[str(counter), r["original"], r["translation"], video_id, str(int(r["start"])),
                        str(int(r["start"] + r["duration"]))])
        )
        counter += 1
        notes.append(
            genanki.Note(
                model=video_to_subtitle,
                fields=[str(counter), r["original"], r["translation"], video_id, str(int(r["start"])),
                        str(int(r["start"] + r["duration"]))])
        )
        counter += 1
        notes.append(
            genanki.Note(
                model=translation_to_original_and_video,
                fields=[str(counter), r["original"], r["translation"], video_id, str(int(r["start"])),
                        str(int(r["start"] + r["duration"]))])
        )
        counter += 1
        print(r)

    my_deck = genanki.Deck(
        hash(video_id),
        f'{video_id}')
    for note in notes:
        my_deck.add_note(note)
    genanki.Package(my_deck).write_to_file(f'{output_folder}/{video_id}.apkg')
