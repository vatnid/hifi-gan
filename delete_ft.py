import os

files = []
to_del = []

for filename in os.listdir("ft_dataset"):
    if filename.endswith(".wav"):
        files.append(filename[:-4])

for filename in os.listdir("ft_dataset"):
    if filename.endswith(".npy"):
        if filename[:-4] not in files:
            os.system(f"rm ft_dataset/{filename}")
            to_del.append(filename[:-4])

for file in sorted(to_del):
    print(file)

print(len(to_del))

"""
with open(f"unaligned.txt", "r") as f:
    for name in f:
        name = name.strip()
        print(name)
        os.system(f"rm ft_dataset/{name}.wav Herbikher2/unaligned/{name}.wav")
"""