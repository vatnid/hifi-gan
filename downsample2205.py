import os
import librosa
import soundfile as sf

for filename in os.listdir("ft_wav"):
	if filename.endswith(".wav"):
		y, s = librosa.load(f"ft_wav/{filename}", sr=22050)
		sf.write(f"ft_wav2205/{filename}", y, s)