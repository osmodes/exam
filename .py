from Question import Question
print("Instructions")
print(" .....You have 5minutes to attempt these questions (35Questions)" 
             "\n.......After supplying your answers, press 'enter key' to load the next question"
      "\n.....Good luck as u attempt every questions")
name = input("Enter student's name to continue: \n")
print(name + " your test is about to start. press enter to continue \n")

questions_prompts = [
    "1. Do you work on Saturdays?\nA Yes, I work \nB Yes, I do \nC Yes, I am\n\n",
    "2. How old are you?\nA No, I'm not \nB I'm 35 \nC I'm a waiter\n\n",
    "3. Do you have a brother? \nA No, I not have \nB No, they don't \nC No, I don't\n\n",
    "4. Where are they from?\nA There from Bath\nB They're from Bath\nC I'm from Bath\n\n",
    "5. My name's john.\nA What's their name?\nB What's your name?\nC How's your name?\n\n",
    "6. She's a doctor.\nA What's his job?\nB What's your job?\nC What's her job?\n\n",
    "7. It's a notebook.\nA What's this in English?\nB What's in English? \nC What's it English?\n\n",
    "8. Yes, I do.\nA Have you got children?\nB Do you like your job? \nC How are you?\n\n",
    "9. He's from Scotland.\nA Where's he from?\nB Where is she from?\nC Where does he live?\n\n",
    "10. They are playing football.\nA What are you doing? \nB What are they doing? \nC What do you do?\n\n",
    "11. ….................. the summer, we go to the beach.\nA In \nB At\n\n",
    "12. We sometimes eat dinner ….................. seven o'clock.\nA on \nB at\n\n",
    "13. Her exams are …...................... June.\nA at\nB in\n\n",
    "14. My brother always goes to the restaurant …...................... his birthday.\nA on \nB in\n\n",
    "15. Do you sleep well …...................... night? \nA in \nB at\n\n",
    "16. …...................... do you work?\nA WHAT \nB WHERE \nC WHO\n\n",
    "17. …...................... do you work for?\nA WHAT \nB WHERE \nC WHO\n\n",
    "18. …...................... music do you like?\nA WHAT \nB WHERE \nC WHO\n\n",
    "19. …...................... restaurant do you want to go to?\nA HOW\nB WHERE\nC WHICH\n\n",
    "20 I come ..... Italy. \nA to \nB from \nC at\nD in\n\n",
    "21 ......... do you go to the gym? - Twice a week. \nA How often \nB Where \nC How\nD Why\n\n",
    "22 I like ........ in my spare time.\nA reading \nB read \nC to read \nD to reading\n\n",
    "23 ........................ \nA I is a cold.\nB I am cold \nC I has cold \nD I have cold.\n\n",
    "24 Chopin .................. music when he was three.\nA can read \nB could read \nC can to read\nD can't read\n\n",
    "25 Ann, how are you? \nA I'm a nurse.\nB I'm fine, thanks. And you? \nC I am working. \nD Good.\n\n",
    "26 I ......... born in 1992.\nA was \nB am \nC were \nD is\n\n",
    "26 Whose key is that? \nA It's of Cate. \nB It's Cate's.\nC It's Cate.\nD It's to Cate.\n\n",
    "27 Where ......... Ann and Mary at 6pm yesterday? \nA are \nB were \nC was \nD have been\n\n",
    "28 His office is on the first ........\nA level \nB ground \nC stage \nD floor\n\n",
    "29 I speak Hebrew and French but Ann ....\nA don't \nB doesn't \nC speaks \nD doesn 't speaks\n\n",
    "30 He is interested ......... learning Romanian.\nA in \nB on\nC to \nD for \n\n",
    "31 I can't find my glasses. Can you look for.., please?\nA they\nB them \nC it \nD their\n\n",
    "32 Would you like .......... to drink, sir? \nA anything \nB anywhere \nC nothing\nD something\n\n",
    "33 ...... there any cars on the street? \nA Are \nB Is \nC Am \nD Isn't\n\n",
    "34 The doctor gave me a ..........for some medicine last week. \n A note \n B recipe \n C prescription\n\n",
    "35 (On the phone) Hello. Juliet ......... \nA speak \nB speaking \nC talking \nD talk D receipt\n\n",


]

questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "c"),
    Question(questions_prompts[3], "b"),
    Question(questions_prompts[4], "b"),
    Question(questions_prompts[5], "c"),
    Question(questions_prompts[6], "c"),
    Question(questions_prompts[7], "b"),
    Question(questions_prompts[8], "a"),
    Question(questions_prompts[9], "b"),
    Question(questions_prompts[10], "b"),
    Question(questions_prompts[11], "b"),
    Question(questions_prompts[12], "b"),
    Question(questions_prompts[13], "a"),
    Question(questions_prompts[14], "b"),
    Question(questions_prompts[15], "b"),
    Question(questions_prompts[16], "c"),
    Question(questions_prompts[17], "a"),
    Question(questions_prompts[18], "c"),
    Question(questions_prompts[19], "b"),
    Question(questions_prompts[20], "a"),
    Question(questions_prompts[21], "c"),
    Question(questions_prompts[22], "d"),
    Question(questions_prompts[23], "d"),
    Question(questions_prompts[24], "b"),
    Question(questions_prompts[25], "b"),
    Question(questions_prompts[26], "b"),
    Question(questions_prompts[27], "a"),
    Question(questions_prompts[28], "b"),
    Question(questions_prompts[29], "a"),
    Question(questions_prompts[30], "c"),
    Question(questions_prompts[31], "d"),
    Question(questions_prompts[32], "b"),
    Question(questions_prompts[33], "c"),
    Question(questions_prompts[34], "b"),
    Question(questions_prompts[35], "b"),
]

def run_test(questions):
    score = 0
    for questions in questions:
        answer = input(questions.prompt)
        if answer == questions.answer:
            score += 1
    if score <= 14:
        print(name +" you score " +  str(score) + "/" + "35, you failed. Try again")
    elif score >= 15:
        print(name + " You got " + str(score) + "/" + "35 correctly. Put more effort")
    else:
        print(name + " Congratulations you go it all")
run_test(questions)

import msvcrt

while 1:
    print
    'Testing..'
    # body of the loop ...
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 27:
            break

"""
Here the key used to exit the loop was <ESC>, chr(27).

You can use the following variation for special keys:

    if ord(msvcrt.getch()) == 0:
        if ord(msvcrt.getch()) == 59:    # <F1> key
            break

With the following, you can discover the codes for the special keys:
    if ord(msvcrt.getch()) == 0:
        print ord(msvcrt.getch())
        break

Use getche() if you want the key pressed be echoed."""
