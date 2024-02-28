import random
import time

OPERATORS = ['+', '-', '*']     #Problem content
MIN_OPERANDS = 3
MAX_OPERANDS = 12
TOTAL_PROBLEMS = 10

def generate_problem():     #Generating Problem
    left = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    right = random.randint(MIN_OPERANDS, MAX_OPERANDS)
    operator = random.choice(OPERATORS)
    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)
    return exp, answer

wrong = 0
input("Press any key to start!")
print('------------------------')

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    exp, answer = generate_problem()
    while True:
        guess = input(f"Problem # {i + 1}: {exp} = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time)

print('-------------------------')
if total_time <= 20:
    print(f"Excellent! You finished in {total_time}s.")
elif total_time <= 30:
    print(f"Good! You finished in {total_time}s.")
elif total_time <= 40:
    print(f"Nice! You finished in {total_time}s.")
elif total_time <= 50:
    print(f"Fair! You finished in {total_time}s.")
elif total_time <= 60:
    print(f"Need improvement! You finished in {total_time}s.")
elif total_time > 60:
    print(f"You really need to improve your basic math! You finished in {total_time}s.")
