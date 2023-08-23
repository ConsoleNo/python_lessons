# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 11:08:55 2023

@author: Raxmonov
"""

def baholash(baholar):
    new_baholar = {}
    i=0
    while i in range(len(baholar)):
        ism = baholar[i]
        new_baholar[ism] = int(input(f"{ism}ning bahosini kiriting: "))
        i+=1
    return new_baholar
    
ismlar = ['Ozodbek', 'Humoyun', 'Alisher', 'Dostonbek']
print(baholash(ismlar[:]))