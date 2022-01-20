from youtube_transcript_api import YouTubeTranscriptApi

import genanki
from cards_template import video_and_original_subtitle_to_translation_template, video_to_subtitle, translation_to_original_and_video


def fetch_subtitle_data(
        video_id,
        original_language,
        translation_language):
    transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
    original_language_script = transcripts.find_transcript([original_language])
    translated_script = original_language_script.translate(translation_language)
    return original_language_script.fetch(), translated_script.fetch()


if __name__ == '__main__':
    video_id = "RhsozwlVCZE"
    original_language = "ja"
    translation_language = "en"

    ol, fr = fetch_subtitle_data(video_id, original_language, translation_language)
    original = {t['start']: t['text'] for t in ol}
    duration = {t['start']: t['duration'] for t in ol}
    translation = {t['start']: t['text'] for t in fr}
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
    for r in subtitles:
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

    my_deck = genanki.Deck(
        hash(video_id),
        f'{video_id}')
    for note in notes:
        my_deck.add_note(note)
    genanki.Package(my_deck).write_to_file(f'{video_id}.apkg')
