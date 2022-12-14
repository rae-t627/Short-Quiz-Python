# Short-Quiz-Python

### Overview
This quiz takes questions randomly from a database in SQL and displays it in a GUI created using tkinter. It consists of 5 questions and it is in Multiple Choice Question format with 4 options per question. Further, the quiz is timed.
1. The quiz begins with a welcome page which the python program reads from a text file.  

![1) Welcome page](https://user-images.githubusercontent.com/105154462/206639329-cf8c221c-0c24-413a-9cf0-068f81434f5c.png)

2. This is then followed by a login page. 

![2) Login page](https://user-images.githubusercontent.com/105154462/206640046-341d099f-a2ad-483e-88de-23d7fe9d9651.png)

3. The login page verifies the credentials entered with the database in SQL. If the credentials are invalid, a message box pops up saying that the credentials are not registered with the school.

![3) Login fail](https://user-images.githubusercontent.com/105154462/206641156-e6514f88-08f3-46c9-a41d-4705b9f68a97.png)

4. If the credentials are valid, the quiz starts. The questions appear. The options are radiobuttons. Upon selecting an option, the submit button appears. When the submit button is clicked the radiobuttons are disabled.

5. If the answer selected is correct, "Correct!" is displayed and the Next button appears.

![4) Correct_Ans](https://user-images.githubusercontent.com/105154462/206641168-19468fc8-021a-48ac-b59b-91b6e3317872.png)

6. If the answer selected is incorrect, "Incorrect. The correct ans is " is displayed along with the correct answer. 

![5) Incorect Ans](https://user-images.githubusercontent.com/105154462/206641185-cb6de684-abc3-4bb2-bbf4-e7e8e63bdc4e.png)

7. When the next button is clicked, it moves on to the next question.

8. When all the questions are over, the score is displayed. Because extra points are given for the amount of time saved, the user may randomly choose options, and still get a good score. To avoid this, if the number of wrong choices exceeds the correct, the final score will be zero.  
Else, score is (number of correct ans - number of incorrect ans) * 15 + (time in seconds remaining) * 2

![6) Score](https://user-images.githubusercontent.com/105154462/206640562-c9427db2-1a9a-4ffe-80eb-9069ed8c405b.png)

### Modules used
- tkinter
- random
- mysql.connector

