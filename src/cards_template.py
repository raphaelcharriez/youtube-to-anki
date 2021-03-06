import genanki

from pathlib import Path


mod_path = Path(__file__).parent
css = 'resources/card.css'
css_path = (mod_path / css).resolve()

with open(css_path, 'r') as css_file:
    css = css_file.read()


video_and_original_subtitle_to_translation_template = genanki.Model(
  11,
  'Video With Subtitles To Translation',
  sort_field_index=0,
  fields=[
    {'name': "id"},
    {'name': 'original'},
    {'name': 'translation'},
    {'name': 'video_id'},
    {'name': 'start'},
    {'name': 'end'}
  ],
  templates=[
    {
      'name': 'Video With Subtitles To Translation',
      'qfmt': '''
        <div>
          <div>
            <b>{{original}}</b>
          </div>
          <hr>
          <div>
          <iframe width="420px" height="300px"
            src="https://www.youtube.com/embed/{{video_id}}?autoplay=1&controls=1&start={{start}}&end={{end}}">
          </iframe>
          </div>
        </div> 
        ''',
      'afmt': '''{{FrontSide}}<hr id="answer">{{translation}}''',
    },
  ],
  css=css
)


translation_to_original_and_video = genanki.Model(
  12,
  'Translation To Video and Subtitles',
  sort_field_index=0,
  fields=[
    {'name': "id"},
    {'name': 'original'},
    {'name': 'translation'},
    {'name': 'video_id'},
    {'name': 'start'},
    {'name': 'end'}
  ],
  templates=[
    {
      'name': 'Translation To Video and Subtitles',
      'qfmt': '''
        <div>
          {{translation}}
        </div>
      ''',
      'afmt': '''
        <div>
          {{FrontSide}}
          <hr id="answer">
          <div>
            <b>{{original}}</b>
          </div>
          <hr>
          <div>
            <iframe width="420px" height="300px"
              src="https://www.youtube.com/embed/{{video_id}}?autoplay=1&controls=1&start={{start}}&end={{end}}">
            </iframe>
          </div>
        </div> 
      ''',


    },
  ],
  css=css
)

video_to_subtitle = genanki.Model(
  13,
  'Video to Subtitles',
  sort_field_index=0,
  fields=[
    {'name': "id"},
    {'name': 'original'},
    {'name': 'translation'},
    {'name': 'video_id'},
    {'name': 'start'},
    {'name': 'end'}
  ],
  templates=[
    {
      'name': 'Video to Subtitles',
      'qfmt': '''
        <div>
            <iframe width="420px" height="300px"
              src="https://www.youtube.com/embed/{{video_id}}?autoplay=1&controls=1&start={{start}}&end={{end}}">
            </iframe>
        </div>
      ''',
      'afmt': '''
        <div>
          {{FrontSide}}
          <hr id="answer">
          <div>
            <b>{{original}}</b>
          </div>
          <hr>
          <div>
            {{translation}}
          </div>
        </div> 
      ''',


    },
  ],
  css=css
)

word_and_translation = genanki.Model(
  15,
  'Word And Translation',
  sort_field_index=0,
  fields=[
    {'name': "id"},
    {'name': 'original'},
    {'name': 'translation'},
  ],
  templates=[
    {
      'name': 'Translation Voice',
      'qfmt': '''
        <div>
            {{original}}
        </div>
      ''',
      'afmt': '''
        <div>
          {{FrontSide}}
          <hr id="answer">
          <div>
            {{translation}}
          </div>
        </div> 
        ''',
    },
  ],
  css=css
)







