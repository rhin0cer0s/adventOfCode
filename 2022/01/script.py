#! /usr/bin/env python3

import fileinput

meal = []
maxCalories = [0, 0, 0]

def findBestNCalories(calories, maxCalories) :
    for idx, mc in enumerate(maxCalories) :
        if calories > mc :
            print(f"{calories} > {mc}({idx})")
            maxCalories.insert(idx, calories)
            maxCalories.pop()
            return

for line in fileinput.input() :
    if line == "\n" :                
        calories = sum([int(m) for m in meal])
        # print(f"{meal} : {calories}")
        meal = []
        findBestNCalories(calories, maxCalories)

    else :
        meal.append(line.rstrip())

print(f"maxCalories : {maxCalories}({sum(maxCalories)})")