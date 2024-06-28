#-------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, OR D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)

        question_num += 1

    display_score(correct_guesses,guesses)


#-------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
#-------------------------
def display_score(correct_guesses,guesses):
    print("----------------------------")
    print("RESULTS")
    print("----------------------------")
    print("Answer: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is: "+str(score)+"%")
#-------------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
#------------------------

questions = {
    "In what year was the first iPhone released?: ": "A",
    "Who was the first man to walk on the moon?: ": "B",
    "Who were the Wright Brothers?: ": "A",
    "Google is a Browser or a Search Engine?: ": "C",
    "What is the full form of VIRUS?: ": "B",
    "The process to find an error in a software code is called?: ": "A",
    "Who is the founder of Oracle Corporation?: ": "A"
}

options = [["A.2007", "B.2006", "C.2008", "D.2009"],
           ["A.John Glenn", "B.Neil Armstrong", "C.Buzz Aldrin", "D.Yuri Gagarin"],
           ["A.Pioneers in aviation", "B.Scientists who discovered electricity", "C.Astronauts who landed on the moon", "D.Soviet spies during the cold war"],
           ["A.Browser", "B.Both Browser and Search Engine", "C.Search Engine", "D.Neither Browser nor Search Engine"],
           ["A.Neither Browser nor Search Engine", "B.Vital Information Resources Under Siege", "C.Vital Information Rest Under Siege", "D.Virtual Information Resources Under Siege"],
           ["A.Debugging", "B.Compiling", "C.Error", "D.None of the above"],
           ["A.Lawrence J. Ellison", "B.Andrew N.", "C.Marc Anderson", "D.None"]]

new_game()

while play_again():
    new_game()

print("Byeeeee!")