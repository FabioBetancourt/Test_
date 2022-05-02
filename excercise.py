# game of guess

guess_correct = "Fabio"
guess=""
guess_count = 0
guess_limit = 3
out_gasses = False

while guess != guess_correct and not (out_gasses):
    if guess_count < guess_limit:
        guess=input("Enter the name of progammer: ")
        guess_count += 1
    else:
        out_gasses = True

if out_gasses:
    print("You Lose!")
else:
    print("You win!")