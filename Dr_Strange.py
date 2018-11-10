import os
import random
import time

n =0
random_number = random.randint(1,101)
#random_number = 3
print("Random Number {}".format(random_number))

###method
def Dr_Strange_Bargain(n):
    print("Dr Strange:  Dormammu! I’ve come to bargain.\n")
    time.sleep(2)
    print("Dormammu: You’ve come to die.\n")
    print("Dormammu: Your world is now my world, like all worlds.\n")
    time.sleep(2)
    ##Recursion Method
    if n == 0:
        n = n+1
        Dr_Strange_Bargain(n)
    elif n == 1:
        time.sleep(2)
        print("Dormammu: What is this?\n")
        print("Dormammu: Illusion? - No, this is real.\n")
        time.sleep(2)
        n = n+1
        Dr_Strange_Bargain(n)
    elif (n > 1) & (n != random_number):
        time.sleep(2)
        print("Dormammu: You cannot do this forever.\n")
        print("Dormammu: No! Make it stop. \n")
        print("Dr Strange: Actually, I can.\n This is how things are now.\n You and me, trapped in this moment, endlessly.")
        time.sleep(2)
        n = n + 1
        Dr_Strange_Bargain(n)
    elif n == random_number:
        print("Dr Strange: Take your zealots from the Earth.\n End your assault on my world.\n Never come back.")


##Call method
Dr_Strange_Bargain(n)