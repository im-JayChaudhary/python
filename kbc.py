name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the KBC. Let's Play...")

print("Please enter 1 to get Started or 2 to know the rules!")
choise = int(input("Ente your choise: "))



# function that goes into action with 3 questions to answer
def runProgram():
    ques = [
        "Who is the second bhagat singh of Bharat?",
        "Who is the great prime minister of Bharat?",
        "Who is the person you believe in most in Bharat?"
    ]
    anss = [
        "bharat tiwari",
        "modi",
        "me"
    ]
    useranss = []
    for que in ques:
        useranss.append(input(f"{que}\nEnter answer: "))
    print(useranss)

    pay = 0;
    i = 0;

    while i<len(ques):
        if (anss[i]==useranss[i] or 
            anss[i].upper()==useranss[i].upper() or 
            anss[i].lower()==useranss[i].lower() or 
            anss[i].title()==useranss[i].title()):
            pay=pay+1
        i=i+1
    if pay==3:   
        print(f"Congratulation, {name}\nYou won 7 crore!!!")
    elif pay==2:
        print(f"Good, {name}\nBetter luck next time!!!")
    else:
        print(f"Oh noo, {name}\nYou are eliminated!!!")



# function that shows rules inside a tuple
def knowRules():
    rules = (
        "1. See the question.",
        "2. Answer the question.",
        "3. Answer the next question.",
        "4. And answer again till you want...",
        "5. Answer to win 10 pay",
        ("1 pay - 1 answer", "2 pay - 2 answers", "3 pay - 3 answers")
    )
    for rule in rules:
        if isinstance(rule, tuple):
            print(*rule, sep=" | ")
        else:
            print(rule)
    next = input("Do you want to play now(y/n): ")
    if next == 'y':
        runProgram()
    else:
        print("Next time ok!")
    



match choise:
    case 1:
        runProgram()
    case 2:
        knowRules()
    case _:
        print("Something went wrong!")