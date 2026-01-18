import math
Talents=int(input("Input the number of Talents: "))
Pounds=int(input("Input the number of Pounds: "))
Lots=int(input("Input the number of Lots: "))
Total_lots=Talents*20*32 +Pounds*32+Lots
Total_Grams=(Total_lots) *13.3
Kilograms=int(Total_Grams//1000)
Grams=Total_Grams%1000
print("The weight in medival units: ")
print(Kilograms,"Kilograms and",Grams,"Grams.")




