name = input("Enter your name: ")
roll_number = input("Enter your roll number: ")

marks = 0

response = input("Type 'START' to start the exam: ").lower()
if response == "start":
    print()
    print("=====Examination Started=====")
    print()
    print("Q1)  MCQ:")
    print()

    print("1.  Which symbol is used to write a comment in Python?")
    print("Options:")
    print("1. // ")
    print("2. #")
    print("3. /**/")
    print("4. --")

    try:
        answer_1_1 = int(input("Select option: "))
        if answer_1_1 < 5:
            if answer_1_1 == 2:
                marks += 1
        else:
            print("Invalid Selection")
    except ValueError:
        print("Invalid Selection")

    print()
    print("2.  Which of the following is used to display output in Python?")
    print("Options:")
    print("1. display() ")
    print("2. echo()")
    print("3. print()")
    print("4. output()")

    try:
        answer_1_2 = int(input("Select option: "))
        if answer_1_2 < 5:
            if answer_1_2 == 3:
                marks += 1
        else:
            print("Invalid Selection")
    except ValueError:
        print("Invalid Selection")

    print()
    print("3.  Which data type is used to store whole numbers in Python?")
    print("Options:")
    print("1. int")
    print("2. str")
    print("3. bool")
    print("4. float")

    try:
        answer_1_3 = int(input("Select option: "))
        if answer_1_3 < 5:
            if answer_1_3 == 1:
                marks += 1
        else:
            print("Invalid Selection")
    except ValueError:
        print("Invalid Selection")

    print()
    print("4.  Which of the following is a valid variable name in Python?")
    print("Options:")
    print("1. 2name")
    print("2. my-name")
    print("3. my_name")
    print("4. class")

    try:
        answer_1_4 = int(input("Select option: "))
        if answer_1_4 < 5:
            if answer_1_4 == 3:
                marks += 1
        else:
            print("Invalid Selection")
    except ValueError:
        print("Invalid Selection")

    print()
    print("""5.  What is the output of ("5" * 2) in Python?""")
    print("Options:")
    print("1. 10")
    print("2. 22222")
    print("3. 55")
    print("4. 52")

    try:
        answer_1_5 = int(input("Select option: "))
        if answer_1_5 < 5:
            if answer_1_5 == 3:
                marks += 1
        else:
            print("Invalid Selection")
    except ValueError:
        print("Invalid Selection")

    print()
    print("Q2)  Answer in one word: ")
    print()

    print("1.  Which keyword is used to define a function in Python?")
    answer_2_1 = input("Enter your answer: ").lower()
    if answer_2_1 == "def":
        marks += 1

    print()    
    print("2.  Which function is used to take input in Python?")
    answer_2_2 = input("Enter your answer: ").lower()
    if answer_2_2 == "input":
        marks += 1

    print()
    print("3.  What data type stores True or False values?")
    answer_2_3 = input("Enter your answer: ").lower()
    if answer_2_3 == "boolean" or answer_2_3 == "bool":
        marks += 1

    print()
    print("4.  Which keyword is used to create a loop that repeats while a condition is true?")
    answer_2_4 = input("Enter your answer: ").lower()
    if answer_2_4 == "while":
        marks += 1

    print()
    print("5.  What is the name of the Python data type used to store a sequence of characters?")
    answer_2_5 = input("Enter your answer: ").lower()
    if answer_2_5 == "string" or answer_2_5 == "str":
        marks += 1

    print()
    print()
    submit = input("""Type "SUBMIT" to submit your response: """).lower()

    if submit == "submit":
        print()
        print("=====Examination Ended=====")
        print()
        print("=====RESULT=====")
        print(f"Student Name: {name}")
        print(f"Roll Number: {roll_number}")
        print()
        if marks >= 4:
            print("Congratulations! You have passed in your examination.")
        else:
            print("Better luck for next time. You have failed in your exam.")
        print(f"Percentage: {(marks/10)*100}%")
        print(f"Total marks obtained: {marks}/10")