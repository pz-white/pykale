# Link Prediction: GripNet framework on PoSE sample dataset.

## 1. Description
This example is constructed by [GripNet Framework](https://arxiv.org/abs/2010.15914) on Polypharmacy Side Effect (PoSE) prediction task. The PoSE sample dataset is from BioSNAP-Decagon dataset and the target is to predict relations between drug nodes on the whole gene-drug heterogeneous graph.

The original implementation of GripNet is [here](https://github.com/NYXFLOWER/GripNet.git).

## 2. Usage
* Dataset download: [PoSE](https://drive.google.com/file/d/1FQ8VFPDYeuXq3pKfV7HXk5Vf41vbRNHn/view?usp=sharing)

* Algorithm: GripNet

`python main.py --cfg configs/Drug_MINI-GripNet.yaml`
