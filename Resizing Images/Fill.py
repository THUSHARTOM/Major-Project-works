'''
Resizing program
'''

import pandas as pd
from scipy import *


def fill(x, Q1=60, Q2=40, r=255):
    (a, b) = shape(x)[:2]
    df = pd.DataFrame(x)
    if a >= Q1 and b >= Q2:
        print("1")
        return x[0:Q1, 0:Q2]
    if a >= Q1 and b <= Q2:
        print("2")
        im = pd.DataFrame(x[0:Q1, 0:b])
        N = int((Q2 - b) / 2)
        D1 = pd.DataFrame(r * sign(rand(Q1, N)))
        D2 = pd.DataFrame(r * sign(rand(Q1, Q2 - b - N)))
        return (pd.concat([D2, im, D1], axis=1))

    if a <= Q1 and b >= Q2:
        print("3")
        im = pd.DataFrame(x[0:a, 0:Q2])
        N = int((Q1 - a) / 2)
        D1 = pd.DataFrame(r * sign(rand(N, Q2)))
        D2 = pd.DataFrame(r * sign(rand(Q1 - a - N, Q2)))
        return (pd.concat([D2, im, D1]))

    if a <= Q1 and b <= Q2:
        print("4")
        N = int((Q2 - b) / 2)
        B1 = pd.DataFrame(r * sign(rand(a, N)))
        B2 = pd.DataFrame(r * sign(rand(a, Q2 - b - N)))
        p = pd.concat([B2, df, B1], axis=1)
        M = int((Q1 - a) / 2)
        D3 = pd.DataFrame(r * sign(rand(M, Q2)))
        D4 = pd.DataFrame(r * sign(rand(Q1 - a - M, Q2)))
        return (concatenate([array(D4), array(p), array(D3)]))
    print(a)
    print(b)
