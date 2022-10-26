# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:57:29 2022

@author: victo
"""

import Financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {Financieros.obtenerIGVconSubtotal(subtotal):.2f}")
print(f"Total: {Financieros.obtenerSubtotalconTotal(subtotal):.2f}")
