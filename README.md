Recognize speech from mp3 to speech by voice (Fr to En)

There are now a huge number of scripts and sites that extract speech from files into text form or subtitles. I found this method a bit simple, so I made this script that converts mp3 audio file into a sound file automatically.
Of course, it is an automatic translation and not with the help of artificial intelligence, but it can translate simple texts to understand what it is about.

Python 3.12

requires packages:

pip install deep_translator
pip install pydub
pip install gtts
pip install googletrans
pip install SpeechRecognition

It works as follows: 
1. next to the scrypt .py we place an mp3 file named: speech.mp3
2. Run scrypt .py, speech.mp3 is converted to wav format and divided into 3 minute segments. Google Translate refused to work for me with longer segments :)
3. segments are placed in a folder: 'audio_chunks' and start translating.
