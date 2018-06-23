import os
import sys
import numpy as np
import shutil

directory = sys.argv[1]
train_dir = directory + '/train'

master = []

for base, subdirs, files in os.walk(train_dir):
	if files:
		for f in files:
			path = base + '/' + f
			master.append(path)

master = np.array(master)
np.random.shuffle(master)
size = len(master)
val_set = master[:int(size * 0.3)]

for source in val_set:
	destination = source.replace('/train/', '/validation/')
	os.makedirs(os.path.dirname(destination), exist_ok=True)
	shutil.move(source, destination)

