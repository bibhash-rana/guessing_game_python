#Make a guessing game where a number is hidden n user has to guess the number
#There will be a limited number of times giving to the user
#In every guess, how close the user is will be displayed printing the left or the right to number
#No. of guess will be displayed


print("Welcome to the guessing game \n No.of guess left = 8")
left=8
guess=46
while(left):
    num = int(input("Enter your guessing number: "))
    if num<guess:
        left = left - 1
        print("IT IS GREATER THAN THIS \n guessing left = ",left)
        continue
    elif num>guess:
        left = left - 1
        print("IT IS SMALLER THAN THIS \n guessing left = ",left)
        continue
    elif num==guess:
        print("Congrats!! You guessed the right number !!",guess)
        break

while(1):
    if left == 0:
        print("NO more trials left !!\n GAME OVER!!")
        left=left+1
    else:
        break
