# Link Prediction: SEAL on ogbl-ddi dataset.

## 1. Description
This example is constructed by [SEAL](https://arxiv.org/pdf/1802.09691.pdf) on ogbl-ddi link prediction task. The ogbl-ddi dataset is from [OGB](https://ogb.stanford.edu/docs/linkprop/#ogbl-ddi) and the target is to predict drug-drug interaction.

The original implementation of SEAL is [here](https://github.com/facebookresearch/SEAL_OGB).

## 2. Usage
* Dataset download: [ogbl-ddi](https://ogb.stanford.edu/docs/linkprop/#ogbl-ddi)

* Algorithm: SEAL

`python main.py --cfg configs/SEAL-DDI.yaml`