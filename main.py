from Student import Student
from Test import Test

def showScores():
    student.showAllScores()

def takeTest():
    chapter = input("what chapter would you like to test on")
    test = Test(chapter)
    score = test.run()
    student.saveScore(chapter, score)

name = input("What is your name")
id = input("what is your id")
student = Student(name, id)

run = True
while run:
    choice = input("1: take test, 2: show scores, 3: quit")
    if choice == "1":
        takeTest()
    elif choice == "2":
        showScores()
    elif choice == "3":
        print("Thanks for testing!")
        run = False
        break
    else:
        print("invalid choice")














def saveTestToDB(self):
    data = [{
       "chapter": "1",
       "questions": [
           {
               "question": "A _____ is an electronic device that stores and processes data.",
               "answer": "computer"
           },
           {
               "question": "_____ is the physical aspect of the computer that can be touched.",
               "answer": "hardware"
           },
           {
               "question": "_____ is the writing of instructions (i.e., code) for computers to perform",
               "answer": "computer programming"
           },
           {
               "question": "The _____ is a computer's brain.  It retrieves instructions from memory and executes them.",
               "answer": "CPU"
           },
           {
               "question": "A _____ is a binary digit 0 or 1.",
               "answer": "bit"
           },
           {
               "question": "A _____ is a sequence of 8 bits.",
               "answer": "byte"
           },
           {
               "question": "A _____ is an ordered sequence of bytes.",
               "answer": "memory unit"
           },
           {
               "question": "The _____ is a set of primitive instructions built into every computer.",
               "answer": "machine language"
           },
           {
               "question": "_____ is a low-level programing language in which a mnemonic is used to represent each machine-language instruction.",
               "answer": "assembly language"
           },
           {
               "question": "A _____ is a software program that translates the source program into a machine-language program.",
               "answer": "compiler"
           }
       ]
    },
    {
        "chapter": "2",
        "questions": [
            {
                "question": "You can get input using the input function and convert a string into a numerical value using the _____ function.",
                "answer": "eval"
            },
            {
                "question": "_____ are the name used for elements in a program.",
                "answer": "identifiers"
            },
            {
                "question": "_____ are used to store data in a program.",
                "answer": "variables"
            },
            {
                "question": "The _____ sign is used as the assignment operator.",
                "answer": "equals"
            },
            {
                "question": "The _____ operators in a Python expression are applied the same way as in an arithmetic expression.",
                "answer": "numeric"
            },
            {
                "question": "Python provides _____ that perform numeric operations: + (addition), - (subtraction), * (multiplication), / (division), // (integer division), % (remainder), and ** (exponent).",
                "answer": "assignment operators"
            },
            {
                "question": "There are two types of number data in Python: _____ and real numbers.",
                "answer": "integers"
            },
            {
                "question": "You can convert a _____ to an int using the int(value) function.",
                "answer": "float"
            },
            {
                "question": "_____ _____ seeks to analyze the data flow and to identify the system's input and output.",
                "answer": "system analysis"
            },
            {
                "question": "_____ _____ is the stage when programmers develop a process for obtaining the output from the input.",
                "answer": "system design"
            }
        ]
    },
    {
        "chapter": "3",
        "questions": [
            {
                "question":"Python provides the mathematical functions in the _____ module.",
                "answer":"math" 
            },
            {
                "question":"A _____ is a sequence of characters.",
                "answer":"string"
            },
            {
                "question": "_____ are used to store data in a program.",
                "answer": "variables"
            },
            {
                "question":"Python does not have a _____ _____ for characters.",
                "answer":"data type"
            },
            {
                "question":"An _____ _____ is a special syntax that begins with the character \ followed by a letter of a combination of digits to represent special characters."
                "answer":"escape sequence"
            },
            {
                "question":"All data including numbers and strings are _____ in Python.",
                "answer":"objects"
            },
            {
                "question":"You can invoke _____ to perform operations on the objects.",
                "answer":"methods"
            },
            {
                "question":"You can use the _____ function to format a number or a string and return the result as a string.",
                "answer":"format"
            },
            {
                "question":"The _____ for the objects are called methods in Python.",
                "answer":"functions"
            },
            {
                "question":"The _____ function can be used to convert a number into a string.",
                "answer":"str"
            }
        ]
    },
    {
        "chapter": "4",
        "questions": [
            {
                "question": "A _____ type variable can store a True or False value.",
                "answer": "boolean"
            },
            {
                "question": "The _____ operators (<, <=, ==, !=, >, >=), which work with numbers and characters, yield a Boolean value.",
                "answer": "relational"
            },
            {
                "question": "The Boolean operators and, or, and _____ operate with Boolean values and variables.",
                "answer": "not"
            },
            {
                "question": "There are several types of _____: if statements, if-else statements, nested if-elif-else statements, and conditional expressions",
                "answer": "selection statements"
            },
            {
                "question": "The various _____ statements all make control decisions based on a Boolean expression.  Based on the True or False evaluation of the expression, these statements take one of two possible courses.",
                "answer": "if"
            },
            {
                "question": "The _____ in arithmetic expressions are evaluated in the order determined by the rules of parentheses, operator precedence, and operator associativity.",
                "answer": "operators"
            },
            {
                "question": "_____ can be used to force the order of evaluation to occur in any sequence.",
                "answer": "parentheses"
            },
            {
                "question": "Operators with higher precedence are evaluated earlier. For operators of the same precedence, their _____ determines the order of evaluation.",
                "answer": "associativity"
            },
            {
                "question":"_____ can be used to force the order of evaluation to occur in any sequence.",
                "answer":"parentheses"
            },
            {
                "question":"Operators with a higher precedence are evaluated _____.",
                "answer":"earlier"
            }
        ]
    },
    {
        "chapter": "5",
        "questions": [
            {
                "question":"There are tow types of repetition statements: the while loop and the _____ loop.",
                "answer":"for" 
            },
            {
                "question":"The part of the loop that contains the statements to be repeated is called the loop _____.",
                "answer":"body"
            },
            {
                "question":"A one-time execution of a loop body is referred to as an _____ of the loop.",
                "answer":"iteration"
            },
            {
                "question":"An _____ loop is a loop statement that executes infinitely.",
                "answer":"infinite"
            },
            {
                "question":"In designing loops, you need to consider both the loop-control structure and the loop _____.",
                "answer":"body"
            },
            {
                "question":"The _____ loop checks the loop-continuation-condition first.  If the condition is true, the loop body is executed.",
                "answer":"while"
            },
            {
                "question":"A _____ value is a special value that signifies the end of the input.",
                "answer":"sentinel"
            },
            {
                "question":"The for loop is a _____-controlled loop and is used to execute a loop body a predictable number of times.",
                "answer":"count"
            },
            {
                "question":"Two keywords, _____ and continue, can be used in a loop.",
                "answer":"break"
            },
            {
                "question":"The break keyword immediately ends the _____ loop, which contains the break.",
                "answer":"innermost"
            }
        ]
    },
    {
         "chapter": "6",
        "questions": [
            {
                "question":"Making programs modular and reusable is one of the central goals in software engineering.  _____ can help to achieve this goal.",
                "answer":"functions"
            },
            {
               "question":"A function _____ begins with the def keyword followed by function's name and parameters, and ends with a colon.",
                "answer":"header"
            },
            {
                "question":"Parameters are _____; that is, a function does not have to contain any parameters.",
                "answer":"optional"
            },
            {
                "question":"A function is called a _____ or None function if it does not return a value.",
                "answer":"void"
            },
            {
                "question":"A _____ statement can also be used in a void function for terminating the function and returning to the function's caller.",
                "answer":"return"
            },
            {
                "question":"The _____ that are passed to a function should have the same number, type, and order as the parameters in the function header.",
                "answer":"arguements"
            },
            {
                "question":"A function's arguements can be passed as positional arguements or _____ arguements.",
                "answer":"keyword"
            },
            {
                "question":"_____ variables are created outside all functions and are accessible to all functions in their scope.",
                "answer":"global"
            },
            {
                "question":"Function _____ is achieved by separating the use of a function from its implementation.",
                "answer":"abstraction"
            },
            {
                "question":"Function abstraction _____ programs in a neat, hierarchical manner.",
                "answer":"modularizes"
            }
        ]
    },
    {
         "chapter": "7",
        "questions": [
            {
                "question":"A _____ is a template, a blueprint, a contract, and a data type for objects.",
                "answer":"class"
            },
            {
               "question":"A class defines the properties of objects and provides an _____ for initializing objects and methods for manipulationg them.",
                "answer":"initializer"
            },
            {
                "question":"The intitializer is always named _____.",
                "answer":"__init__"
            },
            {
                "question":"The first parameter in each method including the initializer in the class refers to the object that calls the method. By convention, this parameter is named _____.",
                "answer":"self"
            },
            {
                "question":"An object is an _____ of a class.",
                "answer":"instance"
            },
            {
                "question":"A _____ is used to create an object",
                "answer":"constructor"
            },
            {
                "question":"A _____ is used to access members of an object through its reference variable.",
                "answer":"dot operator"
            },
            {
                "question":"An _____ variable or method belongs to an instance of a class.",
                "answer":"instance"
            },
            {
                "question":"_____ fields in classes should be hidden to prevent data tampering and to make classes easy to maintain.",
                "answer":"data"
            },
            {
                "question":"You can provide a _____ method or a set method to enable clients to see or modify the data.",
                "answer":"get"
            }
        ]
    },
    {
         "chapter": "8",
        "questions": [
            {
                "question":"A string is _____.  Its contents cannot be changed.",
                "answer":"immutable"
            },
            {
               "question":"You can use the _____ function to return the length of a string.",
                "answer":"len"
            },
            {
                "question":"You can use the _____ operator to reference an individual character in a string.",
                "answer":"index"
            },
            {
                "question":"You can use the _____ operator to duplicate strings.",
                "answer":"repetition"
            },
            {
                "question":"You can use the _____ operator to get a substring.",
                "answer":"slicing"
            },
            {
                "question":"The _____ operators can be used to compare two strings.",
                "answer":"comparision"
            },
            {
                "question":"You can use a _____ loop to iterate all characters in a string.",
                "answer":"for"
            },
            {
                "question":"You can define special methods for overloading the _____.",
                "answer":"operators"
            },
            {
                "question":"Strings are objects of the _____ class.",
                "answer":"str"
            },
            {
                "question":"The _____ function returns a string frp, the keyboard.",
                "answer":"input"
            }
        ]
    },
    {
         "chapter": "9",
        "questions": [
            {
                "question":"To place a widget in a container, you have to specify its _____ manager.",
                "answer":"geometry"
            },
            {
               "question":"The _____ manager places widgets side by side or on top of eachother.",
                "answer":"pack"
            },
            {
                "question":"The _____ manager places widgets in grids.",
                "answer":"grid"
            },
            {
                "question":"The _____ manager places the widgets in absolute locations.",
                "answer":"place"
            },
            {
                "question":"Many widgets have the command option for binding an event with a _____ function.  When an event occurs, this function is invoked.",
                "answer":"callback"
            },
            {
                "question":"The _____ widget can be used to draw lines, rectagles, ovals, arcs, and polygons, and to display images and text strings.",
                "answer":"canvas"
            },
            {
                "question":"You can use the _____ class to create menu bars, menu items, and pop-up menus.",
                "answer":"menu"
            },
            {
                "question":"You can bind mouse and key events to a widget with a _____ function.",
                "answer":"callback"
            },
            {
                "question":"You can use _____ to develop animations.",
                "answer":"canvases"
            },
            {
                "question":"You can use standard dialog boxes to display _____ and receive input",
                "answer":"messages"
            }
        ]
    },
    {
         "chapter": "10",
        "questions": [
            {
                "question":"",
                "answer":""
            },
            {
               "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            }
        ]
    },
    {
         "chapter": "11",
        "questions": [
            {
                "question":"",
                "answer":""
            },
            {
               "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            }
        ]
    },
    {
         "chapter": "12",
        "questions": [
            {
                "question":"",
                "answer":""
            },
            {
               "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            }
        ]
    },
    {
         "chapter": "13",
        "questions": [
            {
                "question":"",
                "answer":""
            },
            {
               "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            }
        ]
    },
    {
         "chapter": "14",
        "questions": [
            {
                "question":"",
                "answer":""
            },
            {
               "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            }
        ]
    },
    {
         "chapter": "15",
        "questions": [
            {
                "question":"",
                "answer":""
            },
            {
               "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            },
            {
                "question":"",
                "answer":""
            }
        ]
    },
    {
    }]
    table = db.table('tests')
    table.insert(data)
