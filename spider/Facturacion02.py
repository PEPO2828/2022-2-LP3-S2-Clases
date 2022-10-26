# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:57:29 2022

@author: victo
"""

import Financieros
total = 1000.49

print(f"Subtotal: {Financieros.obtenerSubtotalconTotal(total):.2f}")
print(f"IGV : {Financieros.obtenerIGVconTotal(total):.2f}")
print(f"Total:{total}")
