import random
t = 3
win=0
loss=0
tie=0
while (True):
    lst = ["snake", "water", "gun"]
    c = random.choice(lst)
    if (t == 0):
        print("Sorry u can't try more number of tries finishes")
        break
    else:
        print("Enter what u want to choose:")
        n = input()
        t = t - 1
        print("Number of times u can try=", t)
        if n == c:
            print("computer also chooses=",c)
            print("Try again depend on number of tries remaining:")
            continue
        elif c == "snake" and n == "water":
            print("computer chooses=", c)
            win+=1
            print("computer wins:")
            print("want to try again:type y for yes and n for no")
            nu = input()
            if (nu == "y"):
                continue
            else:
                break
        elif c == "water" and n == "gun":
            print("computer chooses=", c)
            win += 1
            print("computer wins:")
            print("wnat to try again:y for yes and nfor no")
            nu = input()
            if (nu == "y"):
                continue
            else:
                break
        elif c == "gun" and n == "water":
            print("computer chooses=", c)
            loss += 1
            print("you win:")
            print("wnat to try again:y for yes and nfor no")
            nu = input()
            if (nu == "y"):
                continue
            else:
                break
        elif c == "snake" and n == "gun":
            print("computer chooses=", c)
            loss += 1
            print("you win:")
            print("wnat to try again:y for yes and nfor no")
            nu = input()
            if (nu == "y"):
                continue
            else:
                break
        elif c == "water" and n == "snake":
            print("computer chooses=", c)
            loss += 1
            print("you win:")
            print("wnat to try again:y for yes and nfor no")
            nu = input()
            if (nu == "y"):
                continue
            else:
                break
        elif c == "gun" and n == "snake":
            print("computer chooses=", c)
            win += 1
            print("computer wins:")
            print("wnat to try again:y for yes and nfor no")
            nu = input()
            if (nu == "y"):
                continue
            else:
                break
        else:
            print("you entered wrong keyword:")
            exit()
if win==loss:
         print("no one wins")
         print("computer points=", win, "your points=", loss)
elif win>loss:
         print("computer wins")
         print("computer points=",win,"your points=",loss)
else:
            print("you win")
            print("computer points=", win, "your points=", loss)