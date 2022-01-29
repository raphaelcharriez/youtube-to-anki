# youtube-to-anki
Convert Youtube Videos with bilingual subtitles into Anki Decks

I found that repetition learning works the best for me when I learn languages, but quickly becomes repetitive and uninteresting.

I use this code to download bilingual subtitles from Youtube videos, and transform them into flashcards I can learn. The flashcards have a Youtube iframe that will play the relevant sentence.

I learn the vocabulary and the pronunciation sentence by sentence with the flashcards, then play the Youtube video a few time. It's been efficient, funny and rewarding to learn this way.
### Basic Usage 
1/ installing the requirements with 
`pip install -r requirements.txt`

2/ Find a video with subtitles in the language you want to learn.
For instance for russian: https://www.youtube.com/watch?v=8Q1WDF6gUq0

3/ Take the video id and generate the flashcards by typing:

`python3 src/main.py --video_id '8Q1WDF6gUq0' --original_language 'ru' --translation_language 'en'`

4/ Find the .apkg file in the output folder, open it with the ank app to add it to your decks,

### Words Flashcards

Set the generate_word_cards option to True to add vocabulary flash cards in the deck. It will cut the sentences into words, remove the stop words, very frequent and very rare words, and then translate them.

The words with translation flashcard are added just before the line of subtitle so that you can learn the vocabulary before getting the full sentence.

For now this doesn't work for japanese, chinese and korean as those language need a special tokenizer to split the sentence into word. I haven't set them up yet.

I ended up not using that feature much as it really increases the size of the deck, and prefer to copy past the sentences into dictionary apps like imiwa for japanese or Pleco for chinese   
