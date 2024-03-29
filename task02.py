"""
Second code@home homework task
"""

### variables def ###
question_number = 0
score = 0
total_questions = 5


### function to ask questions and increase score if the user is correct ###
def askquestion(question, correct_answer):
    ### defines varibables as global so they are accessible inside the function scope ###
    global question_number
    global score
    global total_questions
    question_number += 1
    print(f"Question {question_number} of {total_questions}:")
    print(question)
    response = input("> ").lower()
    if response == correct_answer.lower():
        print(f"Well done, your answer of {response} was correct!")
        score += 1
    else:
        print(f"Uh oh! {response} is not the correct answer")


print("Welcome to Liam's Interactive Python Quiz!")
askquestion("Which country has been in the news lately after the US and UK remived their armies from it?", "Afganistan")
askquestion("What is the currency of Denmark?", "Krone")
askquestion("Street artist Banksy is originally associated with which city?", "Bristol")
askquestion("How much is the US entrepreneur Jeff Bezos worth? (in billions of dollars)", "200.6")
askquestion("What's the biggest animal in the world?", "Blue Whale")
print(f"Your score was {score}")
print()

