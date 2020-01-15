def ball():
    import random
    overs=int(input("How many overs would you like to play?\n"))
    print("The game is set for",overs,"overs")
    balls=overs*6
    com_total=0
    count=1
    target=com_total+1
    o=0
    print("you're going to bowl now")
    while count<=balls:
        user=int(input("Enter number \n"))
        if user<=6:
            print("You've inputed",user,"\n")
        else:
            print('Enter number from 1 to 6')
            continue
        comp = random.randint(1,6)
        print("Computer chose",comp,"\n")
        if (comp==user)and overs==1:
            print('out :¬)')
            break
        elif (comp==user)and overs==2:
            print('out :¬)')
            o += 1
            if o == 2:
                break
        elif (comp==user)and overs==3:
            print('out :¬)')
            o += 1
            if o == 3:
                break
        elif (comp==user)and overs==4:
            print('out :¬)')
            o += 1
            if o == 4:
                break
        elif (comp==user)and overs==5:
            print('out :¬)')
            o += 1
            if o == 5:
                break
        elif (comp==user)and overs==6:
            print('out :¬)')
            o += 1
            if o == 6:
                break
        elif (comp==user)and overs==7:
            print('out :¬)')
            o += 1
            if o == 7:
                break
        elif (comp==user)and overs==8:
            print('out :¬)')
            o += 1
            if o == 8:
                break
        elif (comp==user)and overs==9:
            print('out :¬)')
            o += 1
            if o == 9:
                break
        elif (comp==user)and overs>=10:
            print('out :¬)')
            o += 1
            if o == 10:
                break
        else:
            com_total=com_total+comp
            target=com_total+1
            print("computer's total is now",com_total)
        i=1
        count=count+i
    print("computer's score is:",com_total)
    print('target:',target)
    user_total=0
    count=1
    remaining=target-user_total
    print("you're going to bat now")
    while count<=balls:
        user=int(input("Enter number \n"))
        if user<=6:
            print("You've inputed",user,"\n")
        else:
            print('enter number from 1 to 6')
            continue
        comp=(random.randint(1,6))
        print("Computer chose",comp,"\n")
        if (comp==user)and overs==1:
            print('out :¬(')
            break
        elif (comp==user)and overs==2:
            print('out :¬(')
            o += 1
            if o == 2:
                break
        elif (comp==user)and overs==3:
            print('out :¬(')
            o += 1
            if o == 3:
                break
        elif (comp==user)and overs==4:
            print('out :¬(')
            o += 1
            if o == 4:
                break
        elif (comp==user)and overs==5:
            print('out :¬(')
            o += 1
            if o == 5:
                break
        elif (comp==user)and overs==6:
            print('out :¬(')
            o += 1
            if o == 6:
                break
        elif (comp==user)and overs==7:
            print('out :¬(')
            o += 1
            if o == 7:
                break
        elif (comp==user)and overs==8:
            print('out :¬(')
            o += 1
            if o == 8:
                break
        elif (comp==user)and overs==9:
            print('out :¬(')
            o += 1
            if o == 9:
                break
        elif (comp==user)and overs>=10:
            print('out :¬)')
            o += 1
            if o == 10:
                break
        else:
            user_total=user_total+user
            remaining=target-user_total
        print("your score is now:",user_total)
        if remaining<=0:
            print('you won')
            break
        i=1
        count=count+i
    if com_total>user_total:
       print('computer won')
    elif user_total==com_total:
        print('tie')


def bat():
    import random
    overs=int(input("How many overs would you like to play?\n"))
    print("The game is set for",overs,"overs")
    balls=overs*6
    user_total=0
    count=1

    target=user_total+1
    print("you're going to bat now")
    while count<=balls:
        user=int(input("Enter number \n"))
        if user<=6:
            print("You've inputed",user,"\n")
        else:
            print('Enter number from 1 to 6')
            continue
        comp = random.randint(1,6)
        print("Computer chose",comp,"\n")
        if (comp==user)and overs==1:
            print('out :¬(')
            break
        elif (comp==user)and overs==2:
            print('out :¬(')
            o += 1
            if o == 2:
                break
        elif (comp==user)and overs==3:
            print('out :¬(')
            o += 1
            if o == 3:
                break
        elif (comp==user)and overs==4:
            print('out :¬(')
            o += 1
            if o == 4:
                break
        elif (comp==user)and overs==5:
            print('out :¬(')
            o += 1
            if o == 5:
                break
        elif (comp==user)and overs==6:
            print('out :¬(')
            o += 1
            if o == 6:
                break
        elif (comp==user)and overs==7:
            print('out :¬(')
            o += 1
            if o == 7:
                break
        elif (comp==user)and overs==8:
            print('out :¬(')
            o += 1
            if o == 8:
                break
        elif (comp==user)and overs==9:
            print('out :¬(')
            o += 1
            if o == 9:
                break
        elif (comp==user)and overs>=10:
            print('out :¬)')
            o += 1
            if o == 10:
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
    print("you're going to bowl now")
    while count<=balls:
        user=int(input("Enter number \n"))
        if user<=6:
            print("You've inputed",user,"\n")
        else:
            print('enter number from 1 to 6')
            continue
        comp=(random.randint(1,6))
        print("Computer chose",comp,"\n")
        if (comp==user)and overs==1:
            print('out :¬)')
            break
        elif (comp==user)and overs==2:
            print('out :¬)')
            o += 1
            if o == 2:
                break
        elif (comp==user)and overs==3:
            print('out :¬)')
            o += 1
            if o == 3:
                break
        elif (comp==user)and overs==4:
            print('out :¬)')
            o += 1
            if o == 4:
                break
        elif (comp==user)and overs==5:
            print('out :¬)')
            o += 1
            if o == 5:
                break
        elif (comp==user)and overs==6:
            print('out :¬)')
            o += 1
            if o == 6:
                break
        elif (comp==user)and overs==7:
            print('out :¬)')
            o += 1
            if o == 7:
                break
        elif (comp==user)and overs==8:
            print('out :¬)')
            o += 1
            if o == 8:
                break
        elif (comp==user)and overs==9:
            print('out :¬)')
            o += 1
            if o == 9:
                break
        elif (comp==user)and overs>=10:
            print('out :¬)')
            o += 1
            if o == 10:
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
    if user_total>com_total:
       print('you win')
    elif user_total==com_total:
        print('tie')


import random
userinput1=input('choose odd or even')
userinput2=int(input('enter a number'))
computerinput=random.randint(1,6)
print('computer choose',computerinput)
toss1=(userinput2 + computerinput)%2
anyt=1
if toss1 == 0:
    toss1='even'
    print('its even')
    if userinput1 == 'even':
        anyt=input('you won the toss choose bat or ball:')
        if anyt == 'bat':
            bat()
        elif anyt == 'ball':
            ball()
    else:
        anyt=random.randint(1,2)
        if anyt == 1:
            bat()
        else:
            ball()

elif toss1 != 0:
    toss1='odd'
    print('its odd')
    if userinput1 == 'odd':
        anyt=input('you won the toss choose bat or ball:')
        if anyt == 'bat':
            bat()
        else:
            ball()
    else:
        anyt=random.randint(1,2)
        if anyt == 1:
            print('computer choses to bat first')
            ball()
        else:
            print('computer choses to ball first')
            bat()