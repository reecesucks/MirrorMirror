import sqlHelper
from voice_message import VoiceMessage
import glob
from gtts import gTTS
from random import randrange


class AudioBank:
    def __init__(self, sqlHelper):
        self.message_bank = []
        self.audio_list = []
        self.sql_Helper = sqlHelper

    def fill_bank(self):
        print(self.sql_Helper.host)
        db_messages = self.sql_Helper.get("SELECT * FROM voice_messages")
        print(db_messages)
        for msg in db_messages:
            message = VoiceMessage(msg[0], msg[2], msg[3].seconds, msg[4].seconds, msg[1], msg[5], msg[6], msg[7])
           # days, display_before, display_after, message, tag, recipient, language):
            self.message_bank.append(message)

    def generate_audio(self):
        path = './audio/'
        files = glob.glob(path + '*,mp3', recursive=False)
        #compare files list with updating list
        print(files)
        count = 1
        for msg in self.message_bank:
            text = msg.message
            language = msg.language
            audio = gTTS(text=text, lang=language, slow=False)
            file_name = './audio/{}.mp3'.format(str(count))
            audio.save(file_name)
            count = count + 1

    def play_random_audio(self):
        num = randrange(len(self.message_bank))
        if self.message_bank[num].is_playing_now():
            print(num)




