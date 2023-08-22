#Ejercicio 1.11: Hipoteca ajustado

#Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.


#David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.
#El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:

#Ejericio a corregir:

#    saldo = 500000.0
#    tasa = 0.05
#    pago_mensual = 2684.11
#    total_pagado = 0.0

#    while saldo > 0:        
    #    saldo = saldo * (1+tasa/12) - pago_mensual
    #    total_pagado = total_pagado + pago_mensual

#    print('Total pagado', round(total_pagado, 2))   


# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual_base = 2684.11
total_pagado = 0.0
pago_extra = 1000
mes = 0

while saldo > 0:
    mes = mes + 1
    if mes <= 12: 
        pago_mensual = pago_mensual_base + pago_extra
    else: 
        pago_mensual = pago_mensual_base
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))