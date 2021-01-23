from yacs.config import CfgNode as CN
import os

_C = CN()

# -----------------------------------------------------------------------------
# Basic
# -----------------------------------------------------------------------------
_C.OUTPUT_DIR = 'results'

# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------
_C.DATASET = CN()
_C.DATASET.ROOT = "dataset/ogbl_ddi"  # ogbl-ddi will be automatically downloaded if not exist in root directory
_C.DATASET.NAME = 'ogbl-ddi'
_C.DATASET.NUM_HOPS = 1
_C.DATASET.TRAIN_PERCENT = 1.0  # neighbor node sample rate for constructing train dataset enclosing subgraph
# default 1.0 since ddi is a very high degree graph.
_C.DATASET.VAL_PERCENT = 100.0  # same as above but for val dataset.
_C.DATASET.TEST_PERCENT = 100.0  # same as above but for test dataset.
_C.DATASET.COALESCE = False  # whether to compress mutli-edge into edge with weight, default False
_C.DATASET.NODE_LABEL = 'drnl'  # Double-Radius Node Labeling, which is the method of node labeling for subgraph
_C.DATASET.RATIO_PER_HOP = 0.2
_C.DATASET.MAX_NODES_PER_HOP = False
_C.DATASET.BATCH_SIZE = 32
_C.DATASET.NUM_WORKERS = 0
_C.DATASET.MAX_Z = 1000  # set a large max_z so that every z has embeddings to look up
_C.DATASET.TRAIN_NODE_EMBEDDING = False

# -----------------------------------------------------------------------------
# Solver
# -----------------------------------------------------------------------------
_C.SOLVER = CN()
_C.SOLVER.SEED = 2020
_C.SOLVER.MAX_EPOCHS = 10
_C.SOLVER.LR = 0.0005
_C.SOLVER.EVAL_STEPS = 1

# -----------------------------------------------------------------------------
# SEAL config
# -----------------------------------------------------------------------------
_C.SEAL = CN()
_C.SEAL.MODEL = 'SAGE'  # for SEAL downstream gnn model selection, support 'DGCNN' or 'SAGE'
_C.SEAL.HIDDEN_CHANNELS = 32
_C.SEAL.NUM_LAYERS = 3
_C.SEAL.USE_FEATURES = False
_C.SEAL.EVAL = ['hits@20', 'hits@50', 'hits@100']  # hits list, the first is major metrics for saving best model.


def get_cfg_defaults():
    """Clone config"""
    return _C.clone()


def dump_cfg(cfg):
    """Dump config to the output directory"""
    cfg_file = os.path.join(cfg.output_dir, cfg.cfg_dest)
    with open(cfg_file, 'w') as wf:
        cfg.dump(stream=wf)
