
import speech_recognition as sr
import pyttsx3
from inspiration import Inspiration
from autohypnose import Autohypnose
import pygame
from win32gui import SetWindowPos
import win32gui
import win32con
import win32api
from mood import Mood
from todo import Todo
from recurrent import Recurrent

class Myassistant:
    def __init__(self):
        self.recognizer=sr.Recognizer()
        self.engine=pyttsx3.init('sapi5')
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[3].id)
        self.rate = 130
        self.engine.setProperty('rate',self.rate)
        # voices = self.engine.getProperty('voices')
        # for voice in voices:
        #     print(voice, voice.id)
        #     self.engine.setProperty('voice', voice.id)
        #     self.engine.say("Hello World!")
        #     self.engine.runAndWait()
        #     self.engine.stop()
        pygame.init()
        screen_width = 200
        screen_height = 200
        self.window_screen  = pygame.display.set_mode((screen_width, screen_height))
        # pygame.display.set_window_position(1000, 1000)
        SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 1)
        hwnd = pygame.display.get_wm_info()["window"]
        # Getting information of the current active window
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
                            hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)

    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait() 

    def take_command(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio=self.recognizer.listen(source)
            try:
                statement=self.recognizer.recognize_google(audio,language='fr-FR')
                print(f"user said:{statement}\n")
                # self.speak(statement)

            except Exception as e:
                print("Je ne comprends pas, articule")
                return "None"
            return statement
    
    def loop(self):
        done = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = 1

    # Update the screen
            self.window_screen.fill((255,0,128)) 
            Mood.get_instance().loop()
            Mood.get_instance().render(self.window_screen)
            Autohypnose.get_instance().loop(self.engine)
            Inspiration.get_instance().loop(self.engine)
            Todo.get_instance().loop(self.engine)
            Recurrent.get_instance().loop(self.engine)
            pygame.display.update()
            
            # command = self.take_command().lower()
            # if 'inspiration' in command or 'aspiration' in command:
                # self.speak(Inspiration.pick_inspiration())
        pygame.quit()

           



if __name__=='__main__':
    app = Myassistant()
    app.loop()


