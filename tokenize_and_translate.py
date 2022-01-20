from wordfreq import word_frequency
import nltk
import fugashi
from nltk.corpus import stopwords
import PyDictionary



def generate_vocabulary(sentence, original_language, translation_language, freq_min = 10**-6, freq_max = 1):
    tokenized = [word.surface for word in sentence]

    frequency = [
        word for word in tokenized if
        (
                (word_frequency(word, lang='ja') > freq_min) and
                (word_frequency(word, lang='ja') < freq_max)
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