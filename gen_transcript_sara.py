import os
import random

training = {}
validation = {}

for filename in os.listdir("ft_npy"):
    if filename.endswith(".TextGrid"):
        filename = filename[:-9]
        with open(f"../Sara/blacher-retter/{filename}.lab", "r") as f:
            for line in f:
                training[filename] = line.strip()

for i in range(len(training)//10):
    rankey = random.choice(list(training.keys()))
    validation[rankey] = training.pop(rankey)

with open(f"Sara/training.txt", "w") as f:
    for k in training:
        f.write(f"{k}|{training[k]}|{training[k]}\n")

with open(f"Sara/validation.txt", "w") as f:
    for k in validation:
        f.write(f"{k}|{validation[k]}|{validation[k]}\n")