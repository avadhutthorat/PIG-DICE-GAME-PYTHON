import random

MIN = 3
MAX = 12
operators = ['+', '-', '*']

def rand():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    op = random.choice(operators)
    exp = str(num1) +  " " + op + " " + str(num2)
    
    return exp



while True:
    exp = rand()
    print('\n')
    ans = input(f"Enter your answer for {exp} : ")
    comp_ans = eval(exp)
    if int(comp_ans) == int(ans):
        print('Correct !!')
    else:
        print("Wrong !!")

    continuePlay = input('Do u want to continue ? (Y / N) : ')
    if(continuePlay.lower() != 'y'):
        print("Game ended !")
        break        

