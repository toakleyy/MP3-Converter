from pydub import AudioSegment
import os

root_dir = os.getcwd()

# PUT YOUR "FILES TO CONVERT" IN THIS FOLDER
try:
    os.chdir('mp3 files to convert')
    os.chdir(root_dir)
except FileNotFoundError:
    os.mkdir('mp3 files to convert')

# CONVERTED FILES WILL END UP IN THIS FOLDER
try:
    os.chdir('converted mp3 files')
    os.chdir(root_dir)
except FileNotFoundError:
    os.mkdir('converted mp3 files')

os.chdir('mp3 files to convert')
for wav in os.listdir():
    AudioSegment.from_wav(wav).export(f'{root_dir}/converted mp3 files/{wav.split(".wav")[0]}.mp3', format='mp3')
    print('converted', wav)

