import os
import torch

data_dir = os.getcwd() + '/data/clue/'
train_dir = data_dir + 'train.npz'
test_dir = data_dir + 'test.npz'
files = ['train', 'test']
bert_model = 'pretrained_bert_models/bert-base-chinese/'
roberta_model = 'pretrained_bert_models/chinese_roberta_wwm_large_ext/'
model_dir = os.getcwd() + '/experiments/clue/'
log_dir = model_dir + 'train.log'
case_dir = os.getcwd() + '/case/bad_case.txt'

# 训练集、验证集划分比例
dev_split_size = 0.1
n_split = 5
# 是否加载训练好的NER模型
load_before = False

# 是否对整个BERT进行fine tuning
full_fine_tuning = True

# hyper-parameter
learning_rate = 3e-5
weight_decay = 0.01
clip_grad = 5

batch_size = 16
epoch_num = 50
min_epoch_num = 5
patience = 0.0002
patience_num = 10

gpu = '0'

if gpu != '':
    device = torch.device(f"cuda:{gpu}")
else:
    device = torch.device("cpu")

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
