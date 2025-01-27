import random
import os
from os import listdir
from os.path import isfile, join
from timestampassistant import timestamp_assistant


class Todo:
    instance = None
        
    @staticmethod
    def get_instance():
        if Todo.instance == None:
            Todo.instance = Todo()
        return Todo.instance
    
    def get_random_file_from_directory_and_nb_files(self,directory):
        list_files = os.listdir(directory)
        index_file_to_explore = random.randint(0,len(list_files)-1)
        text = os.path.splitext(list_files[index_file_to_explore])[0]

        return len(list_files), text
    
    def get_exploration_perso(self):
        nbfile, file_name = self.get_random_file_from_directory_and_nb_files('C:\\pascal\\pogideaverse\\Efforts\\Explorations personnelles')
        text =  "Tu as " + str(nbfile) + "explorations personnelles à faire. Et par exemple " + file_name
        return text
    
    def get_video(self):
        nbfile, file_name = self.get_random_file_from_directory_and_nb_files('C:\\pascal\\pogideaverse\\Efforts\\Evideos')
        text =  "Tu as " + str(nbfile) + "videos à faire. Et par exemple " + file_name
        return text

    def get_explorations(self):
        nbfile, file_name = self.get_random_file_from_directory_and_nb_files('C:\\pascal\\pogideaverse\\Efforts\\Explorations')
        text =  "Tu as " + str(nbfile) + "Explorations à faire. Et par exemple " + file_name
        return text

    
    def loop(self,speaker):
        time_to_speak = random.randint(0,10)
        print("todo" + str(time_to_speak))
        if time_to_speak > 7:
            categorie = random.randint(0,2)
            if categorie == 0:
                text = self.get_exploration_perso()
            elif categorie == 1:
                text = self.get_explorations()
            elif categorie == 2:
                text = self.get_video()
            # voices=speaker.getProperty('voices')
            # speaker.setProperty('voice',voices[1].id)
            speaker.say(text)
            speaker.runAndWait()
            print("todo")
