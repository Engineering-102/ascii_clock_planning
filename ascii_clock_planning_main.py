# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:  Tyler Haidaczuk
# Jai Joshi
# Benjamin Sparks
# NA
# Section: 571
# Assignment: Lab Topic 8 Team
# Date: 20 October 2026
#
time = input("Enter the time: ")
clock_type = int(input("Enter the clock type (12 or 24): "))
char = input("Enter your preferred character ")
if char not in "abcdeghkmnopqrsuvwxyz@$&*= ":
    char = input("Character not permitted! Try again: ")

def change_symbols(symbol, list):
    for x in range[:len(list) + 1]:
        list[x] = list[x].replace("*",symbol)
    return(list)
