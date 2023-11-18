# -*- coding: utf-8 -*-

"""
@author: HZX
@software: PyCharm
@file: data_prepross.py
@time: 2023/5/9 20:16
Description:
"""

# code N percursor function
def code_NP(Np):
    if Np == 'Yes':
        Np = 1
    if Np == 'No':
        Np = 0
    return Np

# code Oxi function
def code_Oxi(ox):
    if ox == 'PMS':
        ox = 1
    if ox == 'PDS':
        ox = 0
    return ox

# code non-metallic elements function
def code_NME(nme):
    if nme == 'Yes':
        nme = 1
    if nme == 'No':
        nme = 0
    return nme

# code metallic elements function
def code_ME(me):
    if me == 'No':
        me = 0
    if me == 'Single':
        me = 1
    if me == 'Bimetallic':
        me = 2
    return me

# code biomass function
def code_BM(BM):
    if BM == 'Agricultural residue':
        BM = 0
    if BM == 'Animal related':
        BM = 1
    if BM == 'Aquatic':
        BM = 2
    if BM == 'Forest':
        BM = 3
    if BM == 'Solid waste':
        BM = 4
    if BM == 'Terrestrial':
        BM = 5
    return BM