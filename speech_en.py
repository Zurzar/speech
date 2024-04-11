from deep_translator import GoogleTranslator
import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS
import os

output_dir = "audio_chunks"
os.makedirs(output_dir, exist_ok=True)

# Function to split the audio file into approximately one-minute chunks
def split_audio(input_audio, output_dir):
    audio = AudioSegment.from_file(input_audio)
    fragment_length = 3 * 60 * 1000  # Fragment length in milliseconds (3 minutes)
    for i, chunk in enumerate(audio[::fragment_length]):
        chunk.export(os.path.join(output_dir, f"chunk{i}.wav"), format="wav")

# Function to recognize speech from an audio file
def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        return text
    except sr.UnknownValueError:
        return "Unable to recognize speech"
    except sr.RequestError:
        return "Unable to access the speech recognition service"

# Function to translate text from French to English
def translate_text(text):
    try:
        translator = GoogleTranslator(source='fr', target='en', raise_exception=True)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Translation error: {e}"

# Function to convert text to speech in English language
def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)

# Main function
def main():
    # Path to the audio file with French speech
    mp3_file = "speech.mp3"
    output_dir = "audio_chunks"
    # Splitting the audio file into chunks
    split_audio(mp3_file, output_dir)
    # Translation and conversion of each chunk
    for audio_file in os.listdir(output_dir):
        if audio_file.endswith(".wav"):  # Check for file type
            recognized_text = recognize_speech(os.path.join(output_dir, audio_file))
            translated_text = translate_text(recognized_text)
            text_to_speech(translated_text, f"translated_{audio_file[:-4]}.mp3")

if __name__ == "__main__":
    main()
