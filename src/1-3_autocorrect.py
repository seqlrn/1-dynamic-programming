#!/usr/bin/env python3

# %%
# Assignment Pt. 1: Edit Distances

gem_doppel = [
    ("GCGTATGAGGCTAACGC", "GCTATGCGGCTATACGC"),
    ("kühler schrank", "schüler krank"),
    ("the longest", "longest day"),
    ("nicht ausgeloggt", "licht ausgenockt"),
    ("gurken schaben", "schurkengaben")
]
# %%

def hamming(s1: str, s2: str) -> int:
    pass

# hamming('GCGTATGAGGCTAACGC', 'GCTATGCGGCTATACGC') = 10
# hamming('kühler schrank', 'schüler krank') = 13
# hamming('the longest', 'longest day') = 11
# hamming('nicht ausgeloggt', 'licht ausgenockt') = 4
# hamming('gurken schaben', 'schurkengaben') = 14

# %%
def levenshtein(s1: str, s2: str) -> (int, str):
    pass

# levenshtein('GCGTATGAGGCTAACGC', 'GCTATGCGGCTATACGC') = 3 (mmdmmmmsmmmmmimmmm)
# levenshtein('kühler schrank', 'schüler krank') = 6 (ssmimmmmsddmmmm)
# levenshtein('the longest', 'longest day') = 8 (ddddmmmmmmmiiii)
# levenshtein('nicht ausgeloggt', 'licht ausgenockt') = 4 (smmmmmmmmmmsmssm)
# levenshtein('gurken schaben', 'schurkengaben') = 7 (siimmmmmsdddmmmm)

# %%
# Assignment Pt. 2: Auto-Correct
def suggest(w: str, dist, max_cand=5) -> list:
    """
    w: word in question
    dist: edit distance to use
    max_cand: maximum of number of suggestions

    returns a list of tuples (word, dist, score) sorted by score and distance"""
    pass

examples = [
    "pirates",    # in-voc
    "pirutes",    # pirates?
    "continoisly",  # continuosly?
]

for w in examples:
    print(w, suggest(w, max_cand=3))

# sample result; your scores may vary!
# pirates [('pirates', 0, -11.408058827802126)]
# pirutes [('pirates', 1, -11.408058827802126), ('minutes', 2, -8.717825438953103), ('viruses', 2, -11.111468702571859)]
# continoisly [('continously', 1, -15.735337826575178), ('continuously', 2, -11.560071979871001), ('continuosly', 2, -17.009283000138204)]

# %%
# Assignment Pt. 3: Needleman-Wunsch

def keyboardsim(s1: str, s2: str) -> float:
    pass

def nw(s1: str, s2: str, d: float, sim) -> float:
    pass

# How does your suggest function behave with nw and a keyboard-aware similarity?
