import random
def main():
    dice_rolls = 50
    for i in range(0, dice_rolls):
      rnd = random.randint(1, 6)
      print (f' You rolled a {rnd}' )

if __name__== "__main__":
    main()
