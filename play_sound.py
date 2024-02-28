import random

from playsound import playsound


class PlaySound:

    def lookup_greeting(self, name: str):
        playsound('audio/hi_' + name + '.wav')

    def send_welcome_message(self):
        greetings = ['i_hope_you_have_a_great_day_today.mp3',
                     'i_love_that_shirt.mp3',
                     'its_nice_seeing_you_again.mp3',
                     'keep_up_the_great_work.mp3',
                     'time_for_coffee_eh.mp3',
                     'welcome_back_to_the_office.mp3',
                     'your_hair_looks_really_nice.mp3']
        playsound('audio/' + random.choice(greetings))
