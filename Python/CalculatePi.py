#import statement
import random

#function for calulating pi value
def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1
    
    return 4 * num_point_circle / num_point_total

#Calling the function estimate_pi
pi = estimate_pi(100000000)

#printing the value generated
print(pi)