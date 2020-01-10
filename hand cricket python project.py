import random
overs=int(input("How many overs would you like to play?\n"))
print("The game is set for",overs,"overs")
balls=overs*6
user_total=0
count=1
target=user_total+1
while count<=balls:
    user=int(input("Enter number \n"))
    if user<=6:
        print("You've inputed",user,"\n")
    else:
        print('Enter number from 1 to 6')
        continue
    comp = random.randint(1,6)
    print("Computer chose",comp,"\n")
    if (comp==user):
        print("OUT :-( ","\n")
        break
    else:
        user_total=user_total+user
        target=user_total+1
        print("Your total is now",user_total)
    i=1
    count=count+i
print("Your score is:",user_total)
print('target:',target)
com_total=0
count=1
remaining=target-com_total
while count<=balls:
    user=int(input("Enter number \n"))
    if user<=6:
        print("You've inputed",user,"\n")
    else:
        print('enter number from 1 to 6')
        continue
    comp=(random.randint(1,6))
    print("Computer chose",comp,"\n")


    if (comp==user):
        print("out\nYou won")
        break

    else:
        com_total=com_total+comp
        remaining=target-com_total
        print("computer's score is now:",com_total)
    if remaining<=0:
        print('computer won')
        break




    i=1
    count=count+i








