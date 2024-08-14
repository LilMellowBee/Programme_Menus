from datetime import date, datetime
import random
from Idées_menus import *

def saison():
    tps = date.today()
    if tps >= date(2024, 3, 20) and tps <= date(2024, 6, 20):
        return menus_printemps
    
    elif tps >= date(2024, 6, 21) and tps <= date(2024, 9, 22):
        return menus_ete
    
    elif tps >= date(2024, 9, 23) and tps <= date(2024, 12, 21):
        return menus_automne
         
    elif tps >= date(2024, 12, 22) and tps <= date(2025, 3,19):
       return menus_hiver
       