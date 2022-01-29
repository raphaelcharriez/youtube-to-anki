# youtube-to-anki
Convert Youtube Video with bilingual subtitles into Anki Cards for learning

I found that repetition learning works the best for me when I learn language, but quickly becomes repetitive and uninteresting.

I use that program to download subtitles from youtube video, and transform them into flashcards I can learn. The flashcards have a an iframe that will play the relevant sentence.

I learn the video this way, then play it a few time. It's both efficient and funnier than most flashcard Decks I found.
## Basic Usage 
1/ installing the requirements with 
`pip install -r requirements.txt`

2/ Find a video with subtitles in the language you want to learn.
For instance for russian: https://www.youtube.com/watch?v=8Q1WDF6gUq0

3/ Take the video id and generate the flashcards by typing:

`python3 src/main.py --video_id '8Q1WDF6gUq0' --original_language 'ru' --translation_language 'en'`

4/ Find the .apkg file in the output folder, open it with the ank app to add it to your decks,
