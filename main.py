seed = 1 # TODO: replace this with the random seed of your team!

# Note that this should be the general syntax and serves as a guidance,
# errors might appear because of the versions that these packages use

import numpy as np
np.random.seed(seed)
np.random.RandomState(seed)

import random
random.seed(seed)

import torch
torch.manual_seed(seed)
torch.use_deterministic_algorithms(True)

import tensorflow as tf
tf.random.set_seed(seed)

import jax
jax.random.PRNGKey(seed)

# -------------------------------------------------------------------------------------------------------------

import json
import csv
import random

numberList = [1, 0, 8, 15, 4, 11]

with open('Data/tag_to_id.json', 'r') as f:
    tag_to_id = json.load(f)

with open('Data/test.json', 'r') as fin:
    data = json.load(fin)

header = ["Id", "Ner_label"]
with open('submission1.csv', 'w') as fout:
    writer = csv.writer(fout)
    writer.writerow(header)

    csv_row = 0
    for line in range(len(data)):
        for word in data[line]["tokens"]:
            id = random.choices(numberList, weights = (30, 20, 15, 15, 10, 10), k = 1)
            if word[0] >= '0' and word[0] <= '9':
                id = 13 # NUMERIC
            elif word[0].isalpha() and word[0].isupper():
                id = 1 # PERSON
            else: id = id[0]

            writer.writerow([csv_row, id])
            csv_row = csv_row + 1