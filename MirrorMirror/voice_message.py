import datetime


class VoiceMessage:
    def __init__(self, id, days, display_before, display_after, message, tag, recipient, language):
        self.id = id
        self.days = days
        self.display_before = display_before
        self.display_after = display_after
        self.message = message
        self.tag = tag
        self.recipient = recipient
        self.language = language

    def is_playing_now(self):
        print('\n')
        print(self.id, 'Checking day')
        print('days', self.days)
        print('today', datetime.datetime.today().weekday())
        if self.days[datetime.datetime.today().weekday()]:
            print(self.id, 'This audio is eligable to play today')
            print(self.id, 'playing today, checking time')
            now = datetime.datetime.now()
            midnight = datetime.datetime.combine(now.date(), datetime.time())
            seconds = (now - midnight).seconds

            if seconds > self.display_before and seconds < self.display_after:
                print(self.id , "Can play!")

        print('\n')

