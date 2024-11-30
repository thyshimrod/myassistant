import random
import os
from timestampassistant import timestamp_assistant

class Recurrent:
    instance = None

    @staticmethod
    def get_instance():
        if Recurrent.instance == None:
            Recurrent.instance = Recurrent()
        return Recurrent.instance


    def loop(self,speaker):
        time_to_speak = random.randint(0,10)
        print("recurrent" + str(time_to_speak))
        if time_to_speak > 7:
            list_files = os.listdir("C:\\pascal\\pogideaverse\\Efforts\\Actions Recurrentes")
            index_file_to_explore = random.randint(0,len(list_files)-1)
            text = os.path.splitext(list_files[index_file_to_explore])[0]
            
            # voices=speaker.getProperty('voices')
            # speaker.setProperty('voice',voices[3].id)
            speaker.say("A tu pensé aujourd'hui à " + text)
            speaker.runAndWait()
            print("inspiration")
