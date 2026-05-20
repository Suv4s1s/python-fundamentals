import datetime

class Calender:
    def __init__(self):
        self.current_date= current.date.today()
    def today_date():
        print(f"Today is {self.current_date}")

class Time:
    def __init__(self):
        self.current_time= datetime.datetime.now().strftime("%H:%m:%S")
    def display_time(self):
        print(f"Current time is: {self.current_time}")
    
class CalenderTime(Calender,Time):
    def __init__(self):
        Calender.__init__(self)
        Time.__init__(self)
    
    def display_current(self):
        print(f"Date:{self.current_date}\n Time:{self.current_time}")

def main():
    t1= CalenderTime()
    t1= display_current()
    d1=Calender()
    d1=today_date()

if __name__=="__main__":
    main()
