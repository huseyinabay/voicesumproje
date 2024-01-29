'''from flask import Flask, render_template, request
import speech_recognition as ses_tanima
from googletrans import Translator
from summarizer import Summarizer

app = Flask(__name__)


@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('index.html', original_text=text, translated_text=translated_text, summary=summary)

@app.route('/translate', methods=['POST'])
def translate():
    # recognizer sınıfının tanıtılması
    sesi_tani = ses_tanima.Recognizer()

    # Mikrofonun tanıtılması
    mikrofon = ses_tanima.Microphone()

    # Kayıdın okutulması
    with mikrofon as source:
        print("Konuşun...")
        ses_metni = sesi_tani.listen(source, timeout=10)  # Timeout süresi 10 saniye

        try:
            # Google ses tanıma servisini kullan
            text = sesi_tani.recognize_google(ses_metni, language="tr-TR")
            print('Ses metni:')
            print(text)

        except ses_tanima.UnknownValueError:
            print('Hata: Ses tanınamadı.')
        except ses_tanima.RequestError as e:
            print(f'Hata: {e}')

    # Çeviri işlemi
    translator = Translator()
    translated_text = translator.translate(text, dest='en').text

    # Özetleme işlemi (bert-extractive-summarizer)
    summarizer = Summarizer()
    summary = summarizer(text)

    # Çevrilen metni ve özeti yazdır
    print('Çevrilen metin:')
    print(translated_text)
    print('Özetlenen metin:')
    print(summary)

    return render_template('index.html', original_text=text, translated_text=translated_text, summary=summary)

    # Çevrilmemiş metni, çevrilen metni ve özeti de web sayfasında göstermek için kullanılan şablonu render et
    return render_template('translated.html', original_text=text, translated_text=translated_text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
 '''

from flask import Flask, render_template, request
import speech_recognition as ses_tanima
from googletrans import Translator
from summarizer import Summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # recognizer sınıfının tanıtılması
    sesi_tani = ses_tanima.Recognizer()

    # Mikrofonun tanıtılması
    mikrofon = ses_tanima.Microphone()

    # Kayıdın okutulması
    with mikrofon as source:
        print("Konuşun...")
        ses_metni = sesi_tani.listen(source, timeout=0)  # Timeout süresi 10 saniye

        try:
            # Google ses tanıma servisini kullan
            text = sesi_tani.recognize_google(ses_metni, language="tr-TR")
            print('Ses metni:')
            print(text)

        except ses_tanima.UnknownValueError:
            print('Hata: Ses tanınamadı.')
        except ses_tanima.RequestError as e:
            print(f'Hata: {e}')

    # Çeviri işlemi
    translator = Translator()
    translated_text = translator.translate(text, dest='en').text

    # Özetleme işlemi (bert-extractive-summarizer)
    summarizer = Summarizer()
    summary = summarizer(translated_text)

    #summary_turkish = translator.translate(translated_text, dest='tr').text
    summary_turkish = translator.translate(summary, dest='tr').text


    # Çevrilen metni ve özeti yazdır
    print('Çevrilen metin:')
    print(translated_text)
    print('Özetlenen metin:')
    print(summary)

    # Çevrilmemiş metni, çevrilen metni ve özeti de web sayfasında göstermek için kullanılan şablonu render et
    #return render_template('index.html', original_text=text, translated_text=translated_text, summary=summary)
    return render_template('index.html', original_text=text, translated_text=translated_text, summary_turkish=summary_turkish)

if __name__ == '__main__':
    app.run(debug=True)
