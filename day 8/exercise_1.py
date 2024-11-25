# print area calculator
import math
def paint_calc(height, width, cover):
    num_of_cans = (height * width)/ cover
    round_up_cans= math.ceil(num_of_cans)
    print(f"You will need {round_up_cans} cans of paints.")

test_h = int(input())
test_w = int(input())
coverage = 5

paint_calc(height = test_h, width= test_w, cover= coverage)