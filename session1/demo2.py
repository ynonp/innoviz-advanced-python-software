from typing import List
import numpy as np

class Person:
    def __init__(self, name):
        self.name = name

def get_age_in_months(age_in_years: float) -> float:
    return age_in_years * 12


x = input("How old are you (in months) ?")
print(get_age_in_months(x))


# It's called ndarray :)
items: List[np.ndarray] = []
items.append(np.arange(1, 10))
items.append(7)