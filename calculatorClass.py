

class Calculator:
    def __init__(self):
        self.output = 0
        
        
    #Uses ANSI Code to color format the output for better UI
    def displayOut(self):
        print("\033[1;32m Output is:",self.output,"\033[0m")

    def adder(self):
        first = input("Enter first number: ")
        second = input("Enter second number: ")
        valid = False
        #Exception handling for invalid input types such as letter/characters
        while valid != True:
            try:
                self.output = float(first)+float(second)
                valid = True
                self.displayOut()
            except ValueError:
                print("\033[1;31mInvalid input, please enter an integer.\033[0m")
                break

    
    def subtractor(self):
        first = input("Enter first number: ")
        second = input("Enter second number: ")
        valid = False
        #Exception handling for invalid input types such as letter/characters
        while valid != True:
            try:
                self.output = float(first)-float(second)
                valid = True
                self.displayOut()
            except ValueError:
                print("\033[1;31mInvalid input, please enter an integer.\033[0m")
                break

    
    def multiplier(self):
        first = input("Enter first number: ")
        second = input("Enter second number: ")
        valid = False
        #Exception handling for invalid input types such as letter/characters
        while valid != True:
            try:
                self.output = float(first)*float(second)
                valid = True
                self.displayOut()
            except ValueError:
                print("\033[1;31mInvalid input, please enter an integer.\033[0m")
                break

    
    def divider(self):
        first = input("Enter first number: ")
        second = input("Enter second number: ")
        valid = False
        #Exception handling for invalid input types such as letter/characters
        while valid != True:
            try:
                self.output = float(first)/float(second)
                valid = True
                self.displayOut()
            except ZeroDivisionError:
                print("\033[1;31mMath Error, cannot divide by 0\033[0m")
                break
            except ValueError:
                print("\033[1;31mInvalid input, please enter an integer.\033[0m")
                break

    
    def clear(self):
        self.output = 0
        self.displayOut();

def runFunction():
    calc = Calculator()
    while True:
            print("\nWhat would you like to do?")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Quit")
            choice = input("Choice?: ")
            if choice=='5':
                return False
            elif choice == '1':
                calc.adder()
            elif choice == '2':
                calc.subtractor()
            elif choice == '3':
                calc.multiplier()
            elif choice == '4':
                calc.divider()
            else:
                print("Invalid input, try again")

runFunction()