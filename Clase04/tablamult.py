#
#Ejercicio 4.12: Tablas de multiplicar
#

def tablamult():
    headers = (0,1,2,3,4,5,6,7,8,9)
    print(f"     {headers[0]:>d}    {headers[1]:>d}    {headers[2]:>d}    {headers[3]:>d}    {headers[4]:>d}    {headers[5]:>d}    {headers[6]:>d}    {headers[7]:>d}    {headers[8]:>d}    {headers[9]:>d}")
    print(f'{"-"*55}')
    for i in headers:
        row = [f'{i + j:<4d}' for j in headers]  
        print(f"{i:<2d}:  {' '.join(row)}")



tablamult()