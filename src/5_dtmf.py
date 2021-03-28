#!/usr/bin/env python3

# %%
import numpy as np
from librosa import stft, amplitude_to_db

# note: librosa defaults to 22.050 Hz sample rate; adjust if needed!

# %%
dtmf_tones = [
    ('1', 697, 1209), 
    ('2', 697, 1336), 
    ('3', 697, 1477), 
    ('A', 697, 1633),
    ('4', 770, 1209),
    ('5', 770, 1336),
    ('6', 770, 1477),
    ('B', 770, 1633),
    ('7', 852, 1209),
    ('8', 852, 1336),
    ('9', 852, 1477),
    ('C', 852, 1633),
    ('*', 941, 1209),
    ('0', 941, 1336),
    ('#', 941, 1477),
    ('D', 941, 1633)
    ]

# %%

# TODO
# 1. familiarize with librosa stft to compute powerspectrum
# 2. extract the critical bands from the power spectrum (ie. how much energy in the DTMF-related freq bins?)
# 3. define template vectors representing the state (see dtmf_tones)
# 4. for a new recording, extract critical bands and do DP do get state sequence
# 5. backtrack & collapse

# note: you will need a couple of helper functions...

def decode(y: np.ndarray, sr: float) -> list:
	"""y is input signal, sr is sample rate; returns list of DTMF-signals (no silence)"""
	pass
