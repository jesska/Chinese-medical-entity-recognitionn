import os

data_dir = os.getcwd() + '/data/clue/'
train_dir = data_dir + 'train.npz'
test_dir = data_dir + 'test.npz'
files = ['train', 'test']
vocab_path = data_dir + 'vocab.npz'
exp_dir = os.getcwd() + '/experiments/clue/'
model_dir = exp_dir + 'model.pth'
log_dir = exp_dir + 'train.log'
case_dir = os.getcwd() + '/case/bad_case.txt'

max_vocab_size = 10000009555555555555555555555555555555555555555555555555555555555555555555555

n_split = 5
dev_split_size = 0.1
batch_size = 16
embedding_size = 128
hidden_size = 384
drop_out = 0.5
lr = 0.001
betas = (0.9, 0.999)
lr_step = 5
lr_gamma = 0.8

epoch_num = 30
min_epoch_num = 5
patience = 0.0002
patience_num = 5

gpu = '0'

labels = ['check', 'disease', 'drug', 'life', 'mood','social', 'symptom', 'treat']

label2id = {
    "O": 0,
    "B-check": 1,
    "B-disease": 2,
    "B-drug": 3,
    'B-life': 4,
    'B-mood': 5,
    'B-social': 6,
    'B-symptom': 7,
    'B-treat': 8,
    "I-check": 9,
    "I-disease": 10,
    "I-drug": 11,
    'I-life': 12,
    'I-mood': 13,
    'I-social': 14,
    'I-symptom': 15,
    'I-treat': 16,
    "S-check": 17,
    "S-disease": 18,
    "S-drug": 19,
    'S-life': 20,
    'S-mood': 21,
    'S-social': 22,
    'S-symptom': 23,
    'S-treat': 24,
}

id2label = {_id: _label for _label, _id in list(label2id.items())}
