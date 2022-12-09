# Short-Quiz-Python

### Overview
This quiz takes questions randomly from a database in SQL and displays it in a GUI created using tkinter. It consists of 5 questions and it is in Multiple Choice Question format with 4 options per question. Further, the quiz is timed.
1. The quiz begins with a welcome page which the python program reads from a text file.  
<img
  src="[/path/to/img.jpg](https://user-images.githubusercontent.com/105154462/206639329-cf8c221c-0c24-413a-9cf0-068f81434f5c.png)"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
2. This is then followed by a login page.
3. The login page verifies the credentials entered with the database in SQL. If the credentials are invalid, a message box pops up saying that the credentials are not registered with the school.
4. If the credentials are valid, the quiz starts. The questions appear. The options are radiobuttons. Upon selecting an option, the submit button appears. When the submit button is clicked the radiobuttons are disabled.
5. If the answer selected is correct, "Correct!" is displayed and the Next button appears.
6. If the answer selected is incorrecy, "Incorrect. The correct ans is " is displayed along with the correct answer. 
7. When the next button is clicked, it moves on to the next question.
8. When all the questions are over, the score is displayed. Because extra points are given for the amount of time saved, the user may randomly choose options, and still get a good score. To avoid this, if the number of wrong choices exceeds the correct, the final score will be zero.  
Else, score is (number of correct ans - number of incorrect ans) * 15 + (time in seconds remaining) * 2

### Modules used
- tkinter
- random
- mysql.connector

