import math
import random
import sys

if __name__ == '__main__':
    num_correct = 0
    for i in range(1, 100):
        print('='*100)
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        print(f"What is the sum of {a} and {b}?")
        ans = input('input your answer here and return/enter: ')
        # print(type(ans))
        ans = int(ans)
        if ans == a+b:
            print('Great! This is correct!')
            num_correct += 1
            continue
        
        while ans != a+b:
            print('_'*80)
            print('Oh, your answer is incorrect!')
            print('* '*a)
            print('* '*b)
            print('Please count how many starts are here...')
            ans = input('input your answer here again and return/enter: ')
            ans = int(ans)
        
        print('Alright! Now your got this correct! ')

    print(f'You got {num_correct} out of 100 questions right at the first try!')

