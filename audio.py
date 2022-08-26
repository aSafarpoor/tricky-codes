import librosa
import soundfile as sf

input_name = ... 
output_name = ...

y, sr = librosa.load(input_name)

#do anything you want with y:
#exp, cut video:
y = y[:100]

sf.write(output_name, y, sr, 'PCM_24')