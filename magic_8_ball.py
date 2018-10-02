import random
import time

input("I am magic 8 ball, what is your question: ")

answer = random.randint(0, 19)
time.sleep(2.0)
if answer == 0:
    print("It is certain.")
elif answer == 1:
    print("It is decidedly so.")
elif answer == 2:
    print("Without a doubt.")
elif answer == 3:
    print("Yes - definitely.")
elif answer == 4:
    print("You may rely on it.")
elif answer == 5:
    print("As I see it, yes.")
elif answer == 6:
    print("Most likely.")
elif answer == 7:
    print("Outlook good.")
elif answer == 8:
    print("Yes.")
elif answer == 9:
    print("Signs point to yes.")
elif answer == 10:
    print("Reply hazy, try again")
elif answer == 11:
    print("Ask again later.")
elif answer == 12:
    print("Better not tell you now.")
elif answer == 13:
    print("Cannot predict now.")
elif answer == 14:
    print("Concentrate and ask again.")
elif answer == 15:
    print("Don't count on it.")
elif answer == 16:
    print("My reply is no.")
elif answer == 17:
    print("My sources say no.")
elif answer == 18:
    print("Outlook not so good.")
elif answer == 19:
    print("Very doubtful.")