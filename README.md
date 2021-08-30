# create-qti12
*Creates a QTI 1.2 from plain text file*

The Python scripts provided here allow creation of a QTI 1.2 formatted .zip file (suitable for import into an LMS) and Word files for paper-based assessment.

* `create-qti.py` generates QTI .zip
* `create-quiz.py` generates a .docx Word file in the form of a paper-based quiz
* `create-key.py` generates a .docx Word file with the answers provided

## INPUT FILE NAMING CONVENTION  

The scripts above expect input files to be named with Unit, Chapter, Lesson numbers followed by a hyphen then the name of the lesson.

Example: `1.1.1 - NAME OF QUIZ.txt`    or    `6.2.4 - QUIZ NAME.txt`

--------------------------
# Question Format

Questions should be numbered with a PERIOD `.` after each question number.  

Question number order does not matter and duplicates are allowed. New question numbers will be assigned in the generated artifacts.

## EXAMPLE FORMAT:

```
1. The capitol of the United States is:
a) Baltimore
b) New York City
*c) Washington DC
d) Houston
```

## MULTIPLE CHOICE
Answer choices should be provided with an closing parenthesis `)` after each choice.
The correct answer should be denoted by an asterisk `*` preceeding the letter choice.
There must be a minimum of ONE answer choice and a minimum of ONE correct answer.

```
a) incorrect
*b) correct
c) incorrect
d) incorrect
```


## TRUE FALSE

Answer choices should be provided as `a) True` and `b) False`

The correct answer should be denoted by an asterisk `*` preceeding the letter choice.

```
Hertz is the unit of measure for radio frequency.
*a) True
b) False
```

## MULTIPLE ANSWER

Answer choices should be provided with an closing parenthesis `)` after each letter.

The correct answers should each be denoted by an asterisk `*` preceeding the letter choice.

```
The following states have shores along the Gulf of Mexico:
*a) Alabama
b) Oklahoma
*c) Mississippi
d) Delware
e) Arkansas
*f) Florida
*g) Texas
h) Gulf Shores
*i) Louisiana
```
