


class AlarmClock:
    def __init__(self):
        self.current_time = '1200'
        self.alarm_set = False
        self.alarm_time = ""

    def set_time(self):
        self.current_time = input('Please enter the current time: ')
        print(f'The current time is {self.current_time}')

    def set_alarm(self):
        self.alarm_time = input("Enter time for your alarm: ")
        self.alarm._set = True
        print(f'Your alarm is set to {self.alarm_time}')

