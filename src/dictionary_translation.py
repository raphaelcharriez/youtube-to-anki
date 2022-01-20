from wordfreq import word_frequency
from translate import Translator


def generate_vocabulary(words, original_language, translation_language='en',
                        freq_min=10**-6, freq_max=1):

    translator = Translator(from_lang=original_language, to_lang=translation_language)
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


'''
<script src="https://code.responsivevoice.org/responsivevoice.js"></script>
<script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>


<select id="voiceselection"></select> 

<input 
  onclick="responsiveVoice.speak('Hello','US English Male');" 
  type="button" 
  value="Play" 
/>

<script>
        //Populate voice selection dropdown
        var voicelist = responsiveVoice.getVoices();
        var vselect = $("#voiceselection");
        $.each(voicelist, function() {
                vselect.append($("<option />").val(this.name).text(this.name));
        });
</script>

'''