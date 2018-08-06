import random
from time import sleep

PERIOD = 1
number_to_guess = random.randint(1, 10)

user_number = int(input("Adivina un número del 1 al 10: "))
sleep(PERIOD)
if user_number == number_to_guess:
    print("¡Has acertado!, el número es {}".format(number_to_guess))
elif user_number != number_to_guess:
    print("Te has equivocado, el número era {}".format(number_to_guess))
