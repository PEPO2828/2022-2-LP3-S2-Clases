# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:51:00 2022

@author: victo
"""

import financieros
subtotal = 800.77
print(f"Subtotal:{subtotal}")
print(f"IGV:{financieros.obtenerIGVconSubtotal(subtotal):.2f}")
print(f"Total:{financieros.obtenerTotalconSubtotal(subtotal):.2f}")
