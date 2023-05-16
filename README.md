## Dataset
Experimental data from the Good Doctor online at www.haodf.com

There are 8 different categories including: check, disease, drug, life, mood, social, symptom, and treat.

The raw data are located under the /data/clue/ path of the specific model, in the train.json and test.json files respectively. Each line in the file is a separate piece of data, and one piece of data includes a raw sentence and the label on it
## Model

- BiLSTM-CRF
- BERT-Softmax
- BERT-CRF
- BERT-LSTM-CRF

In this case, the BERT-base-X model can be converted to a Roberta-X model depending on the pre-trained model used.

## Requirements

This repo was tested on Python 3.6+ and PyTorch 1.5.1. The main requirements are:

- tqdm
- scikit-learn
- pytorch >= 1.5.1
- 🤗transformers == 2.2.2

To get the environment settled, run:

```
pip install -r requirements.txt
```

## Pretrained Model Required

Pre-training models for BERT need to be downloaded in advance, including

- pytorch_model.bin
- vocab.txt

placed in the . /pretrained_bert_models corresponding to the pre-trained models folder.

**bert-base-chinese model：**[Download Address](https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip) 。

Note that the above downloads are only available for the tensorflow version and need to be downloaded according to[huggingface suggest](https://huggingface.co/transformers/converting_tensorflow_models.html)Convert it to the pytorch version。

**chinese_roberta_wwm_large model：**[Download Address](https://github.com/ymcui/Chinese-BERT-wwm#%E4%BD%BF%E7%94%A8%E5%BB%BA%E8%AE%AE) 。

For those who find it troublesome, the pytorch version of the above model can be accessed directly via the **weblink** below 😊:

链接: https://pan.baidu.com/s/1rhleLywF_EuoxB2nmA212w  password: isc5



## Parameter Setting

### 1.model parameters

In . /experiments/clue/config.json sets the basic parameters of the Bert/Roberta model, while in . /pretrained_bert_models under the two pre-training folders, config.json sets the basic parameters for Bert/Roberta in addition to the parameters for the 'X' model (e.g. LSTM), which can be changed as required.
### 2.other parameters

The environment path and other hyperparameters are set in . /config.py.
## Usage

To open the directory corresponding to the specified model, on the command line enter:

```
python run.py
```

After the model has been run, the optimal model and training logs are stored in the . /experiments/clue/ path. The bad cases in the test set are saved in . /case/bad_case.txt.
## Attention

The current model's train.log is currently saved in the . /experiments/clue/ path. To rerun the model, please move the train.log out of the current path first to avoid overwriting it.
