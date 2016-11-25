# Our quiz!

score = 0

def quiz():
    global score
    global name

    name = input("Enter your name ")

    question1()
    question2()
    question3()
    question4()

    print(name + ":", score)
    

    
    

    
def question1():
    global score
    global name

    print("What is the richest country in the world?")
    print("A.Qatar")
    print("B.Singapore")
    print("C.USA")
    print("D.UK")
    print("E.China")

    answer = input("Answer: ")

    if answer.upper() == "A":
        score=score + 1000
        print("Correct")
    else:
        print("Incorrect")
        

    
def question2():
    global score
    global name
    
    print("What is meaning of life?")
    print("A.To die")
    print("B.42")
    print("C.To love")

    answer = input("Answer: ")

    if answer.upper() == "B":
        score=score + 1000
        print("Correct")
    else:
        print("Incorrect")

def question3():
    global score
    global name
    
    
    print("Who was the richest youtuber in 2015?")
    print("A.Smosh")
    print("B.Skydoesminecraft")
    print("C.Pewdiepie")
    print("D.Fine Brothers")
    print("E.I has Carrot")

    answer = input("Answer: ")

    if answer.upper() == "C":
        score=score + 1000
        print("Correct")
    else:
        print("Incorrect")

def question4():
    global score
    global name
    
    print("What is No.1 on the uk top 40?")
    print("A.Heathens ,twenty one pilots .")
    print("B.Say You Won't Let Go ,James Arthur .")
    print("C.Sensual (feat. Dyo) ,NEIKED .")
    print("D.Shout Out To My Ex ,Little Mix ")

    answer = input("Answer: ")

    if answer.upper() == "D":
        score=score + 1000
        print("Correct")
    else:
        print("Incorrect")
        
          
          





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
