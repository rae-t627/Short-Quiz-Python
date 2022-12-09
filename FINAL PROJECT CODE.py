import tkinter
from tkinter import messagebox
import random
import mysql.connector as tor

"""
MODULES USED IN THE PROGRAM :-
1.  tkinter - tkinter is the standard Python module for creating GUI applications, through the use of 'widgets'. Some of
    these widgets are buttons, entry boxes, text labels, radio buttons, etc., which the user can integrate into the
    code. This program makes extensive use of the tkinter module, along with basic Python concepts.
2.  tkinter.messagebox - tkinter.messagebox enables the user to make use of message boxes in the program. Message boxes
    are used to give some warning/choice/suggestion during program run.
3.  random - The random module is an inbuilt module which generates pseudo-random numbers (either float or integer),
    either within the default range of (0,1), or in any other range provided by the user.
4.  mysql.connector - This module enables Python programs to access MySQL databases, and use the data in the program. 
"""

########################################################################################################################

con = tor.connect(host="host_name", user="user_name", passwd="password", database="database_name")
# This is the standard syntax to establish a connection from Python to MySQL

cs_ques = con.cursor()  # Creating a cursor for the MySQL connection, to manage the quiz questions
# A cursor interacts with the MySQL server on behalf of the Python program.
cs_ques.execute("select * from questions")
# This is a standard MySQL command which brings all the data elements from the table. This data is stored by the cursor.
data_ques = cs_ques.fetchall()
# fetchall() function fetches all the data from the cursor, and stores it as a list of tuples.
# Each tuple in the list is in the format:
# ('Sl No', 'Question', 'Option 1', 'Option 2', 'Option 3', 'Option 4', 'Correct Option')

LNo = []  # List to store all 'Sl No' elements
LQ = []  # List to store all 'Question' elements
L1 = []  # List to store all 'Option 1' elements
L2 = []  # List to store all 'Option 2' elements
L3 = []  # List to store all 'Option 3' elements
L4 = []  # List to store all 'Option 4' elements
LC = []  # List to store all 'Correct Option' elements

LTemp = []  # Acts as a temporary list

for row in data_ques:

    LTemp = ["", "", "", "", "", "", ""]  # List with seven empty elements, because 'row' tuple also has seven elements
    LNo = []
    LTemp[0], LTemp[1], LTemp[2], LTemp[3], LTemp[4], LTemp[5], LTemp[6] = row  # unpacking the 'row' tuple
    LNo.append(LTemp[0])  # Now, LTemp has the elements of the 'row' tuple; adding it one-by-one to the respective lists
    LQ.append(LTemp[1])
    L1.append(LTemp[2])
    L2.append(LTemp[3])
    L3.append(LTemp[4])
    L4.append(LTemp[5])
    LC.append(LTemp[6])

LR = [i for i in range(len(LQ))]  # If total number of elements is 'n', this creates a list like: [1,2,3,4,...,(n-1),n]
random.shuffle(LR)  # Randomly shuffles the elements of the 'LR' list
# The purpose of 'LR' list is to ensure that the questions for each participant is randomly chosen, and does not repeat.
# The shuffled list will look like: [3,5,9,11,3,1,...], for example.
# Now, the individual elements of the shuffled list serve as position indices to visit the six lists above.
# We cannot simply generate a random integer, because there is a chance that we might get repeating questions.

########################################################################################################################

window = tkinter.Tk()  # Tk() function creates the primary window. There can be only one primary window.
window.title("Quiz")  # Naming the window
window.geometry('1920x1080')  # Defining the geometry of the window

correct_choice, incorrect_choice = 0, 0  # For storing the number of correct and incorrect choices
timer_sec, timer_min = 30, 1  # For displaying the timer
count = 0  # To keep count of number of questions
x = random.randrange(len(LQ))
q_no = x  # For the first question
LR.remove(x)  # Removing the already chosen number(x) to prevent repetition in questions
var = tkinter.StringVar()  # A tkinter variable is different from Python variable, this is the format to create it.
var.set(None)  # This function gives a value to the tkinter variable, we cannot use the assignment operator here.

"""
HOW TO USE A TKINTER WIDGET?
In any widget definition, we have to specify certain parameters: where the widget has to be placed (which window/frame);
the text it shall display; the font of the text; the background and text colour; the dimensions (width and height) of
the widget;the command (in case of a button); the value and variable (in case of a radiobutton); and various other
parameters to make the widget look appealing on the screen. These parameters need not be assigned all at once, but they
have to be assigned to define a widget properly and completely. Some of these parameters can also be edited according to
the purpose of the program.
"""

label_ques = tkinter.Label(window, text="")  # Text label to display the questions
label_correct = tkinter.Label(window)  # Label to display whether the ans is correct/ incorrect
rad1 = tkinter.Radiobutton(window, font=('times new roman', 13), variable=var, value="1")  # Radiobuttons for options
rad2 = tkinter.Radiobutton(window, font=('times new roman', 13), variable=var, value="2")
rad3 = tkinter.Radiobutton(window, font=('times new roman', 13), variable=var, value="3")
rad4 = tkinter.Radiobutton(window, font=('times new roman', 13), variable=var, value="4")
submit_button = tkinter.Button(window, text="Submit", font=("times new roman ", 13), bg="light green", fg="Black",
                               width=8, height=1)  # Button to submit the answer, this stops the timer
next_button = tkinter.Button(window, text="Next", font=("times new roman ", 13), bg="light green", fg="Black",
                             width=8, height=1)  # Button to move on to next question
timer_label = tkinter.Label(window, font=("times new roman", 15))  # Creating a label for the timer
label_final = tkinter.Label(window, font=("Arial bold", 15), width=48)  # Creating a label to display the final score
# All these widgets are placed directly on the window; they can also be placed on a frame, if needed


def next_button_clicked():

    global count, q_no, correct_choice
    q_no = LR[count]  # Taking next number from shuffled list (this is equivalent to choosing a random number)

    if count >= 5:  # If 5 questions have already been displayed, skip this part, and move on to final screen
        final()
        return  # Exit this function

    var.set(None)  # Reset the variable used to store the option chosen
    label_correct.config(text="")  # Reset the text in the label

    label_ques.config(text=LQ[q_no] + " \n")  # Edit the question, and all the options
    rad1.config(text=L1[q_no], state="normal")  # Enable all the radiobuttons for the next question
    rad2.config(text=L2[q_no], state="normal")
    rad3.config(text=L3[q_no], state="normal")
    rad4.config(text=L4[q_no], state="normal")
    next_button.place_forget()  # place_forget() is used to remove the widget from the screen, but without destroying it
    submit_button.place_forget()
    submit_button.config(state="normal")  # Enable the submit button
    return


def final():

    # For the final screen, destroy all the radiobuttons and all the unnecessary labels
    rad1.destroy()
    rad2.destroy()
    rad3.destroy()
    rad4.destroy()
    label_ques.destroy()
    label_correct.destroy()
    timer_label.destroy()
    submit_button.destroy()
    """
    SCORING SCHEME :-
    Because extra points are given for the amount of time saved, the user may randomly choose options, and still get
    a good score. To avoid this, if the number of wrong choices exceeds the correct, the final score will be zero.
    Otherwise, scoring will be as mentioned on the welcome screen.
    """
    if correct_choice <= incorrect_choice:
        score_final = 0
    else:
        score_final = (correct_choice-incorrect_choice)*15 + (timer_sec+(timer_min*60))*2
    label_final.config(text=f"Congratulations! The Quiz is complete!\n\nYour final score is {score_final} points.\n\n")
    label_final.pack()
    next_button.config(text="Exit", command=window.quit)  # window.quit closes the main window
    next_button.pack()


def submit_button_clicked():

    global correct_choice, incorrect_choice, count

    count += 1

    rad1.config(state="disabled")  # Disable the radiobuttons so that options cannot be changed after submission
    rad2.config(state="disabled")
    rad3.config(state="disabled")
    rad4.config(state="disabled")
    submit_button.config(state="disabled")
    user_ans = str(var.get())  # Find out which option has been chosen
    correct_ans = str(LC[q_no])  # Find out which is the correct answer
    if user_ans == correct_ans:  # If the correct answer has been chosen
        label_correct.config(text="\nCorrect!\n", font=("times new roman bold", 13))  # Tell that it is correct
        correct_choice += 1  # Update number of correct answers
    else:  # If the correct answer has not been chosen
        label_correct.config(text="\nIncorrect. The correct answer is " + correct_ans+".\n",
                             font=("times new roman bold", 13))  # Tell which options was actually correct
        incorrect_choice += 1  # Update number of incorrect answers
    next_button.config(command=next_button_clicked)
    next_button.place(x=150, y=205)  # Display the next button after telling whether chosen option is correct or not


def radiobutton_clicked():

    submit_button.config(command=submit_button_clicked)
    submit_button.place(x=20, y=205)  # Display the submit button after an option has been chosen


def timer_update():

    global timer_sec, timer_min

    if timer_sec >= 11:  # If number of seconds is in double digits
        timer_label.config(text="0%i : " % timer_min + "%i " % (timer_sec-1))
    else:  # Else if it is single digit
        timer_label.config(text="0%i : " % timer_min + "0%i " % (timer_sec-1))

    timer_sec -= 1

    if timer_sec == 0 and timer_min != 0:  # If the second count has become zero, decrement minute count by 1
        timer_min -= 1
        timer_sec = 60

    window.update()  # update() function changes the details of the widgets in the window/frame


def data_verified():

    welcome_frame.destroy()  # If the details match, destroy the welcome frame and all the widgets with it
    label_ques.config(text=LQ[q_no] + "\n", font=('times new roman', 15))  # Getting the question using random index
    label_ques.place(x=20, y=7)

    label_correct.place(x=20, y=250)

    rad1.config(text=L1[q_no], command=radiobutton_clicked)
    rad2.config(text=L2[q_no], command=radiobutton_clicked)
    rad3.config(text=L3[q_no], command=radiobutton_clicked)
    rad4.config(text=L4[q_no], command=radiobutton_clicked)

    rad1.place(x=20, y=50)
    rad2.place(x=20, y=80)
    rad3.place(x=20, y=110)
    rad4.place(x=20, y=140)

    timer_label.place(x=500, y=250)

    for i in range((60 * timer_min + timer_sec)):  # Total time of quiz (in seconds)
        timer_label.after(1000, timer_update())
        # after(t,c) function waits for 't' milliseconds, and then runs the command 'c'
        if count >= 5:  # If 5 questions have already been displayed, break the loop
            break
    else:  # If the countdown is over
        messagebox.showinfo("Time Countdown", "Time's up!")  # Message box
        timer_label.destroy()
        final()


########################################################################################################################

cursor_users = con.cursor()  # Creating another cursor for MySQL, this time for the login screen
cursor_users.execute("select * from users")  # Retrieving student details (name and school ID) for verification
data_users = cursor_users.fetchall()
name = tkinter.StringVar()
school_id = tkinter.StringVar()
name.set("")
school_id.set("")

users_list = []  # List to store the details entered


def login_window_function():

    global school_id, name

    login_button.config(state="disabled")  # config() function is used to edit any parameters of a widget
    # Disabling the button endures that only one login_window can be created at a time
    users_list.clear()  # Clears the list
    login_window = tkinter.Toplevel(window)  # Toplevel() function creates a secondary window.
    login_window.title("Login Page")
    login_window.geometry("600x300")

    label_login = tkinter.Label(login_window, text="LOGIN\n", font=("Arial bold", 20))
    label_login.pack(anchor=tkinter.CENTER)

    label_name = tkinter.Label(login_window, text="Full Name:\n", font=("Arial bold", 15))
    label_name.place(y=75)  # place() function accepts specific Cartesian coordinates on the screen.

    label_school_id = tkinter.Label(login_window, text="School ID:\n", font=("Arial bold", 15))
    label_school_id.place(y=130)

    enter_name = tkinter.Entry(login_window, width=30, textvariable=name)
    enter_name.place(x=135, y=75)

    enter_school_id = tkinter.Entry(login_window, width=30, textvariable=school_id, show="*")
    enter_school_id.place(x=135, y=130)

    def student_clicked():

        global school_id, name

        school_id = enter_school_id.get()
        users_list.append(school_id)
        name = enter_name.get()
        users_list.append(name)  # 'users_list' contains the details entered.

        users_tuple = tuple(users_list)  # Converts the list into a tuple, as the data from SQL is in form of a tuple.

        if users_tuple in data_users:  # Compare details entered to check if it is present in the list of data retrieved
            login_window.destroy()  # destroy() function destroys the widget/window
            data_verified()
        else:
            messagebox.showinfo("Access denied", """Your credentials are not registered with the school.
            Please check with the school authorities.""")  # Message box
            login_button.config(state="normal")  # If the details do not match, it should be possible to try again
            login_window.destroy()
        
    button_student = tkinter.Button(login_window, text="VERIFY AND START", font=("Arial bold", 12), bg="light green",
                                    fg="black", width=17, height=1, command=student_clicked)
    button_student.place(x=200, y=200)


########################################################################################################################

welcome_frame = tkinter.Frame(window)
# A frame works like a container for organising the widgets in a proper manner. It is also a widget.
welcome_frame.pack()  # pack() function places the widgets on to the screen

welcome_label = tkinter.Label(welcome_frame, text="\nWELCOME TO THE QUIZ!!!\n", font=("times new roman", 30, "bold"))
welcome_label.pack()
exclusive_label = tkinter.Label(welcome_frame, text="A quiz exclusively for Geetanjali students\n\n",
                                font=("times new roman", 23), bd=3)
exclusive_label.pack()
# Text labels for the welcome screen. These are placed on the frame, and not on the window.

rules_file = open("Rules.txt")  # .txt file which has the rules to be displayed on the welcome screen.
rules_list = rules_file.readlines()  # readlines() function reads all the individual lines in the file, one-by-one.

for line in rules_list:
    tkinter.Label(welcome_frame, text=line, font=("times new roman", 15)).pack(anchor=tkinter.W)
    # The anchor parameter along with pack() aligns the widget to any of the four cardinal directions, as specified.

tkinter.Label(welcome_frame, text="\n").pack()
login_button = tkinter.Button(welcome_frame, text="LOGIN NOW!", font=("Bodoni MT", 15, "bold"), bg="light green",
                              fg="black", width=10, height=1, command=login_window_function)
login_button.pack()

########################################################################################################################

window.mainloop()
# The mainloop() function is an infinite loop used to run the application. It processes all the events in the program,
# till the application window is not closed.

rules_file.close()  # Closing the connection to the .txt file
con.close()  # Closing the connection to the MySQL server
