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
        # ans = input('input your answer here and return/enter: ')
        # print(type(ans))

        #handle exception
        # if len(ans) == 0:
        #     print('Incorrect input, you need to input an integer!')
        #     continue
        # for l in ans:
        #     if l > '9' or l < '0':
        #         print('Incorrect input, you need to input an integer!')
        #         continue

        while True:
            try:
                userdata = input("input your answer here and return/enter: ")
                ans = int(userdata)
                break
            except ValueError:
                print("The input was not a valid integer.")

        # ans = int(ans)
        if ans == a+b:
            print('Great! This is correct!')
            num_correct += 1
            continue
        
        while ans != a+b:
            print('_'*80)
            print('Oh, your answer is incorrect!')
            print('Please count how many starts are here...')
            print('* '*a, '\t', a)
            print('* '*b, '\t', b)
            print('\n')

            val1, val2 = max(a, b), min(a, b)
            showStr = ""
            for j in range(val2):
                showStr += ' -> '
                showStr += str(val1 + j + 1)
            print(showStr)

            
            ans = input('input your answer here again and return/enter: ')
            ans = int(ans)
        
        print('Alright! Now your got this correct! ')

    print(f'You got {num_correct} out of 100 questions right at the first try!')

