def find_average(a: int, b: int) -> int:
    return (a + b) / 2


#print(find_average(1, 1))
def divide_num(a: int, b: int) -> int:
    if b == 0:
        raise ValueError('Division by 0 not allowed')
    else:
        return a / b

import pandas as pd
pd.DataFrame()