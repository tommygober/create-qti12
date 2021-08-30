# create-qti12
Creates a QTI 1.2 from plain text file

The tools here allow creation of a QTI 1.2 formatted .zip file (suitable for import into an LMS).

create-qti.py generates QTI .zip
create-quiz.py generates a .docx Word file in the form of a paper-based quiz
create-key.py generates a .docx Word file with the answers provided

INPUT:
The scripts above expect input files to be named with Unit, Chapter, Lesson numbers followed by a hyphen then the name of the lesson.
Example: 1.1.1 - NAME OF QUIZ.txt    or    6.2.4 - QUIZ NAME.txt

Questions should be numbered with a PERIOD after each question number. Question number order does not matter and duplicates are allowed. New question numbers will be assigned in the generated artifacts.

==========================

MULTIPLE CHOICE
Answer choices should be provided with an closing parenthesis ")" after each choice.
The correct answer should be denoted by an asterisk preceeding the letter choice.
There must be a minimum of ONE answer choice and a minimum of ONE correct answer.

a) incorrect
*b) correct
c) incorrect
d) incorrect

EXAMPLE FORMAT:
1. The capitol of the United States is:
a) Baltimore
b) New York City
*c) Washington DC
d) Houston

--------------------------

TRUE FALSE
Answer choices should be provided as a) True and b) False
The correct answer should be denoted by an asterisk preceeding the letter choice.

--------------------------

MULTIPLE ANSWER
Answer choices should be provided with an closing parenthesis ")" after each letter.
The correct answers should each be denoted by an asterisk preceeding the letter choice.
