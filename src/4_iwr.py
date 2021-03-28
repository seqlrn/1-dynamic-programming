#!/usr/bin/env python3

# %%
import numpy as np
from librosa.feature import mfcc

# TODO: read in files, compute MFCC, organize

# %%
def dtw(obs1: list, obs2: list, sim) -> float:
    pass

# %% [markdown]
"""
# Experiment 1

Compute DTW scores between different digits and speakers.
How do scores change across speakers and across digits?
""" 

# %%
def recognize(obs: list, refs: dict) -> str:
    """
    obs: input observations (mfcc)
    refs: dict of (classname, observations) as references
    returns classname where distance of observations is minumum
    """
    pass

# %% [markdown]
"""
# Experiment 2: speaker-dependent IWR

From the same speaker, pick training and test recordings

# Experiment 3: speaker-independent IWR

Select training/reference set from one speaker, test recordings from the other. 
Can you compute Prec/Recall/F1?
"""