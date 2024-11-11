import random
import time
import pygame

class Mood:
    WOKE_UP = 1
    SEMI_WOKE_UP = 2
    instance = None
    def __init__(self):
        self.state = Mood.WOKE_UP
        self.last_mood = int(time.time() * 1000)
        self.files=['eyestr','eyestregg','eyestrfun','eyestrperp','eyestrsemi','eyestrtired']
        self.images = {}

    @staticmethod
    def get_instance():
        if Mood.instance == None:
            Mood.instance = Mood()
        return Mood.instance
    
    def get_mood(self):
        return self.state
    
    def loop(self):
        dt = (int(time.time() * 1000)) - self.last_mood
        if dt > 1500:
            time_to_change = random.randint(0,10)
            if time_to_change > 5:
                self.state = random.randint(0,len(self.files)-1)
            self.last_mood = int(time.time() * 1000)
            
    def render(self, screen):
        if self.images.get(self.files[self.state]) == None:
            eye_image = pygame.image.load('assets/' + self.files[self.state] + '.png')
            eye_image = pygame.transform.scale(eye_image,(200,200))
            self.images[self.files[self.state]] = eye_image
        screen.blit(self.images[self.files[self.state]],(0,0))
        
