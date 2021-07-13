import random
def main():
    dice_rolls = 50
    roll_sum = 0
    for i in range(0, dice_rolls):
      rnd = random.randint(1, 6)
      roll_sum += rnd
      if rnd == 1:
       print (f'You rolled a {rnd} Fail' )
      elif rnd ==6: 
       print (f'you rolled a {rnd} success')
      else:
        print (f'You rolled a {rnd}')
    print (f'Total roll sum = {roll_sum} ')

if __name__== "__main__":
    main()
