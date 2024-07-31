# 1
'''
Мама спекла пиріг з яблуками, в якому було 60% яблук, а решта - тісто. При цьому 30% тіста становили яйця і цукор, решта - борошно. Вся маса пирога дорівнює m кг. Яка маса борошна в пирозі в грамах?

Вхідні дані:

1.2
1
1.5
Вихідні дані:

336.0
280.0
420.0
Розділ: ЗМІННІ І ТИПИ ДАНИХ | Рівень складності: СЕРЕДНІЙ
'''

'''
My mom baked an apple pie with 60% apples and the rest was dough. Eggs and sugar made up 30% of the dough, and flour made up the rest. The total weight of the pie is m kg. What is the mass of flour in the pie in grams?

The input data is given:

1.2
1
1.5
The output data:

336.0
280.0
420.0
Section: VARIABLES AND DATA TYPES | Difficulty level: middle
'''

def composition_of_flour_in_cake(cake_kg: float, apples_percent: float=0.6, dough_egg_sugar_percent: float=0.3) -> float:
    cake_in_grams = cake_kg * 1000
    dough_grams = cake_in_grams * (1 - apples_percent)
    flour_percent = 1 - dough_egg_sugar_percent
    flour_grams = dough_grams * flour_percent 
   
    return flour_grams


if __name__ == '__main__':
    def _test_composition_and_print_result(cake_kg: float) -> None:
       
        flour_grams  = composition_of_flour_in_cake(cake_kg)

        print(f'The frequent flour in a pie is {flour_grams} grams')
    

    _test_composition_and_print_result(1.2)
    _test_composition_and_print_result(1)
    _test_composition_and_print_result(1.5)
   