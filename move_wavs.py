import os

names = []

for filename in os.listdir("ft_npy"):
    if filename.endswith(".TextGrid"):
        filename = filename[:-9]
        names.append(filename)
        print(filename)
        os.system(f"mv ft_wav_pre/{filename}.wav ft_wav/{filename}.wav")

print(len(names))