# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:56:07 2023

@author: Raxmonov
"""

menu = ['osh', 'manti', 'shashlik', 'do`lma', 'somsa']
taomlar = ['osh', 'grechka', 'Manti', "Limon choy"]

for taom in taomlar:
    if taom.lower() in menu:
        print(f'{taom.title()} ro`yxatda bor')
    else: 
        print(f'{taom.title()} ro`yxatda yo`q')