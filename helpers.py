'''Helpers functions
for extracting non-overlapping windows and return dummy predictions

Feel free to modify it

William Thong
<w.e.thong@uva.nl>
'''
import numpy as np
import pandas as pd
import ipdb
from sklearn.metrics import accuracy_score


FREQ = 60
CLASSES = ['sitting', 'lying', 'standing', 'lift', 'snowboarding', 'towlift']


def extract_windows(feat, label, freq=FREQ):
    feat_keys = list(feat.keys())
    feat_keys.remove('Time')
    d = len(feat_keys)
    n = len(feat)

    label_key = ['activity']

    x = np.reshape(feat[feat_keys].values, (n/freq, freq, d))
    y = np.squeeze(np.asarray(label[label_key]))

    return x, y


def predict(window, classes=CLASSES):
    return classes[np.random.randint(6)]


if __name__ == '__main__':
    train_feat = pd.read_csv('train_feat.csv')
    train_label = pd.read_csv('train_label.csv')

    x, y = extract_windows(train_feat, train_label)

    pred = []
    for idx in range(x.shape[0]):
        p = predict(x[idx, :, :])
        pred.append(p)

    print('Accuracy: %.02f' % (accuracy_score(y, pred) * 100))
