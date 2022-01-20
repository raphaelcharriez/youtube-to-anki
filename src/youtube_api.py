from youtube_transcript_api import YouTubeTranscriptApi

def fetch_subtitle_data(
        video_id,
        original_language,
        translation_language):
    transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
    original_language_script = transcripts.find_transcript([original_language])
    translated_script = original_language_script.translate(translation_language)
    return original_language_script.fetch(), translated_script.fetch()

