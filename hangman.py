import  random

#Step1 To create the list of the words

word_list = ["apple","mango","beautiful","gentleman"]
random_word = random.choice(word_list)
print(random_word)

#Step2 To create the length of the random word
word_length = len(random_word)

#Step3 Making the list in ______ format to disply the progress of each choice

display = []
for i in range(word_length):
    display += "_"

#Step4 creating the list of punishment
total_play_count = 7
list_of_punishment = ["Your hands are tied","Your legs are tied","You have been taken to the hanging place","Your head is covered with the black cloth","Your neck is tied with rope","The rope is fixed at top ","You have been Hanged\nGame Over"]

#Step Asking the user for input and validating the user input

inital_play_count = 0
print(f"Hey!,You have {total_play_count} total play count.Best of Luck😊")
punishment_index_count = 0
while inital_play_count<total_play_count:
    print(type(random_word))
    #Condition when the user all input and random_word input is correct it will get out of the loop
    if "".join(display) == random_word:
        print("Congratulation,You Won the game")
        break
    user_input_choice = input("Please Enter the Character that you think it contains in the word")
    # condition ==> what if the user input is incorrect and giving the list of punishment
    if user_input_choice != random_word:
        print(f"OH, You gussed the incorrect word. {list_of_punishment[punishment_index_count]}")
        punishment_index_count += 1;
    for position in range(word_length):
        letter = random_word[position]
        if user_input_choice == letter:
            display[position] = user_input_choice
            disply_in_str = "".join(display)
            print(disply_in_str)
    inital_play_count += 1









