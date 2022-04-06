

from invalidTimeError import invalidTimeError


class clockTime:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    #Uses ANSI Code to identify errors
    def setHours(self):
        valid = False
        hour = 0
        #Exception handling for invalid input types and invalid time formats
        while valid != True:
            hours = input("Enter hours(24 Hours Format): ")
            try:
                hour = toInteger(hours,24)
                self.hours = toString(hour)
                valid = True
            except ValueError:
                print("\033[1;31mInvalid input, please try again.\033[0m")
            except invalidTimeError:
                print("\033[1;31mInvalid time please try again\033[0m")
    
    #Uses ANSI Code to identify errors
    def setMinutes(self):
        valid = False
        minute = 0
        #Exception handling for invalid input types and invalid time formats
        while valid != True:
            minutes = input("Enter minutes: ")
            try:
                minute = toInteger(minutes,60)
                self.minutes = toString(minute)
                valid = True
            except ValueError:
                print("\033[1;31mInvalid input, please try again.\033[0m")
            except invalidTimeError:
                print("\033[1;31mInvalid time please try again\033[0m")

    #Uses ANSI Code to identify errors    
    def setSeconds(self):
        valid = False
        second = 0
        #Exception handling for invalid input types and invalid time formats
        while valid != True:
            seconds = input("Enter seconds: ")
            try:
                second = toInteger(seconds,60)
                self.seconds = toString(second)
                valid = True
            except ValueError:
                print("\033[1;31mInvalid input, please try again.\033[0m")
            except invalidTimeError:
                print("\033[1;31mInvalid time please try again\033[0m")
                
    def setTime(self):
        self.setHours()
        self.setMinutes()
        self.setSeconds()

    #Time always shown in 24 hour standard format
    def showTime(self):
        print("\033[1;33mCurrent clock's time is "+self.hours+":"+self.minutes+":"+self.seconds+"\033[0m")


#Helper Functions
def toInteger(string,maxRange):
    if int(string)<0 or int(string)>=maxRange:
        raise invalidTimeError
    else:
        return int(string)

def toString(integer):
    if len(str(integer))==1:
        return '0'+str(integer)
    else:
        return str(integer)



clock = clockTime("02","30","45",)
clock.showTime()
clock.setHours()
clock.setMinutes()
clock.showTime()
clock.setTime()
clock.showTime()