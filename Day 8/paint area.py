def paint_calc(hieght, width, cover):
    number_of_cans = math.ceil(hieght*width/cover)
    return number_of_cans


height = int(input("What is the hieght of the wall ? "))
width = int(input("What is the width of the wall ? "))
cover = 5
ans = paint_calc(height, width, cover)
print(f"The wall will need {ans} can of paint ")
