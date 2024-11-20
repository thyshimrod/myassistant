import random
import time

class Inspiration:
    instance = None
    phrases = ["Je relache maintenant toutes les impulsions irréfléchies et destructrices",
           "Je me libère de la croyance que je serai submergé par l'anxiété",
           "Je me libère de toutes mes compulsions et addictions",
           "Je me libère du besoin de me consumer en essayant de satisfaire tous mes désirs",
           "Je me libère de la tenatavie de fuir les conséquences de mes actes",
           "Je me libère de la tentative de fuir les conséquences de mes actes"]

    def __init__(self):
        self.last_sentence = int(time.time() * 1000)
        

    @staticmethod
    def get_instance():
        if Inspiration.instance == None:
            Inspiration.instance = Inspiration()
        return Inspiration.instance

    @staticmethod
    def pick_inspiration():
        val = random.randint(0,len(Inspiration.phrases)-1)
        return Inspiration.phrases[val]
    
    def loop(self,speaker):
        dt = (int(time.time() * 1000)) - self.last_sentence
        if dt > 50000:
            self.last_sentence = int(time.time() * 1000)
            time_to_speak = random.randint(0,10)
            if time_to_speak > 5:
                sentence = random.randint(0,len(Inspiration.phrases)-1)
                voices=speaker.getProperty('voices')
                speaker.setProperty('voice',voices[0].id)
                speaker.say(self.sentences[sentence])
                speaker.runAndWait()
