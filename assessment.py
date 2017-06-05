"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation

   Encapsulation means keeping the data close to and with an object. When you have an object, you also have attributes and methods that come with it.

   Abstraction

   Abstraction means some of the information can be hidden and you don't need to know and understand a method, etc. to use it.

   Polymorphism

   Polymorphism means an object can take on different forms. For example, you can have an instance that comes from animal but can be a member of the cat, dog, or another class.

2. What is a class?

    Classes are the basic units in object-orientated programming. They are used to create a template for objects to allow uniformity and so you don't have to recreate each method, etc. every time you create a new object.

3. What is an instance attribute?

    It's a variable or quality that is associated with an object/instance.

4. What is a method?
    
    A method is a function that is defined in and belongs to a class (and potentially subsequent subclasses.)

5. What is an instance in object orientation?

    It's an an object created out of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute belongs to a class while an instance attibute belongs to an instance. Instance attributes take precedence over class attibutes. 
   You would use an instance attribute if you wanted it to belong to just one instance. For example, only 1 lion is named "Liony".
   You wuld use a class attribute if you want to apply it to all in the class. For example, all lions in the lion class can have a lion species attibute.


"""


# Parts 2 through 5:
# Create your classes and class methods

# Some items were printed and returned to accomodate different needs.
# print statements are for testing/debugging

class Student(object):
    """creates a class of students"""

    def __init__(self, first_name, last_name, address):
        """adds first_name, last_name, address for a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """creates a class of questions"""

    def __init__(self, question, correct_answer):
        """add question and answer"""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """asks a question and checks the answer"""

        user_answer = raw_input(self.question)
        is_correct = user_answer == self.correct_answer
        # print is_correct
        return is_correct


class Exam(object):
    """creates a class of exams"""

    def __init__(self, name):
        """creates an empty list of questions associated with exam"""

        self.questions = []
        self.name = name

    def add_questions(self, *questions):
        """adds questions to the exam"""

        self.questions.extend(questions)

    def administer(self):
        """gives exam"""

        total_correct = 0.00 # to prevent rounding later on

        for question in self.questions:
            # print self.questions
            is_correct = question.ask_and_evaluate()
            # print "is_correct:", is_correct
            if is_correct:
                total_correct += 1
            # print "total_correct:", total_correct
            # print "len(self.questions):", len(self.questions)
        percent_correct = (total_correct / len(self.questions)) * 100
        # print "percent_correct:", percent_correct
      
        print percent_correct
        return percent_correct


# instructions say it should have 3 methods but didn't list 3
class StudentExam(object):
    """creates an entry for a student and their score on an exam"""

    def __init__(self, student, exam, score = None):
        """creates the entry"""

        self.student = student
        self.exam = exam
        self.score = score

    def take_test(self, exam):
        """gives test"""

        self.score = exam.administer()
        print "Your score is {}%".format(self.score) 


# I considered having exam and quiz inherit from 1 parent, but I wanted to maintain the code so that it still follows the previous instructions.
# There could be 1 parent that quiz and exam both inherit from. The ovelapping part would be in the parent class. The part that differs would be a new method in each subclass.

class Quiz(Exam):
    """creates a quiz (like an exam but with only pass/fail)"""

    def administer(self):
        """gives quiz"""

        # to prevent rounding later on
        total_correct = 0.00

        for question in self.questions:
            # print self.questions
            is_correct = question.ask_and_evaluate()
            # print "is_correct:", is_correct
            if is_correct:
                total_correct += 1
       
        percentage = (total_correct / len(self.questions)) * 100
        if percentage >= 50:
            return 1
        else:
            return 0


# Maybe it should inherit from StudentExam.
class StudentQuiz():
    """creates entries for student quizzes"""

    def __init__(self, student, quiz, score = None):
        """creates the entry"""

        self.student = student
        self.quiz = quiz
        self.score = score

    def take_test(self, quiz):
        """gives quiz"""

        self.score =  quiz.administer()
        if self.score == 1:
            print "You have passed."
        else:
            print "You have failed."


# Not sure whether this was suppose to creat a specific example or any possible example. Functionality could be expanded allowing the user to input the arguments and info for everything.
def example():
    """creates an example with instances of the clssses"""
    
    math_exam = Exam("math_exam")

    question1 = Question("What is 2 + 2?", "4") 
    question2 = Question("What is 4 * 2?", "8")
    question3 = Question("What is 50% of 8?", "4")

    math_exam.add_questions(question1, question2, question3)

    jc = Student("Jen", "Chan", "Hackbright Avenue")

    jc_math = StudentExam(jc, math_exam)

    jc_math.take_test(math_exam)

    # print "jc_math.score:", jc_math.score

example()

def example_quiz():
    """creates an example for testing quizes"""

    quiz1 = Quiz("quiz1")

    question1 = Question("What is 2 + 2?", "4") 
    question2 = Question("What is 4 * 2?", "8")
    question3 = Question("What is 50% of 8?", "4")
    quiz1.add_questions(question1, question2, question3)

    jc = Student("Jen", "Chan", "Hackbright Avenue")

    jc_math = StudentQuiz(jc, quiz1)

    jc_math.take_test(quiz1)
    # print "jc_math.score:", jc_math.score

example_quiz()


