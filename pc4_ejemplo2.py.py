import re
numeros_validos=r'(^[456][0-9]{4}\s?){16}^['']$'
tarjetas=['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456',' 5123 - 3567 - 8912 - 3456']

for i in tarjetas:
    x=re.findall(numeros_validos,i)
    if x:
        print(f'{i}-->YES')
    else:
        print(f'{i}--NO')