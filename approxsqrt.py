import sys

n = float(sys.argv[1])

guess = n / 2
# # new_guess = (guess + n / guess) / 2
# # guess = new_guess
# # new_guess = (guess + n / guess) / 2
# # guess = new_guess
# # new_guess = (guess + n / guess) / 2
# # guess = new_guess
# # new_guess = (guess + n / guess) / 2
# guess = new_guess

diff = 0.000001

while abs(n - guess * guess) > diff:
    guess = (guess + n / guess) / 2

print(guess)
