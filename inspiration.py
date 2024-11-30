import random
from timestampassistant import timestamp_assistant

class Inspiration:
    instance = None
    phrases = ["Je relache maintenant toutes les impulsions irréfléchies et destructrices",
           "Je me libère de la croyance que je serai submergé par l'anxiété",
           "Je me libère de toutes mes compulsions et addictions",
           "Je me libère du besoin de me consumer en essayant de satisfaire tous mes désirs",
           "Je me libère de la tenatavie de fuir les conséquences de mes actes",
           "Je me libère de la tentative de fuir les conséquences de mes actes",
           "Je me libère du fait d'autoriser mes insécurités à me mener dans des situations dangereuses et de mauvais comportements",
           "Je me libère du fait de sacrifier ma santé et mon bonheur pour des moments éphémères et de mauvais comportements",
           "Je me libère de cette exigence et impatience que j'ai envers les autres",
           "Je me libère de la peur qu'il n'y ait pas assez pour moi",
           "Je me libère du sentiment que j'ai besoin de toujours plus",
           "je me libère du désir que chaque moment soit excitant ou tragique",
           "je me libère de ce besoin constant de voiloir m'échapper au travers de distraction et d'activités constantes",
           "Je me libère du fait de laisser mon manque d'autodiscipline ruiner mes opportunités",
           "Je me libère du besoin de toujorus chercher plus, plus que je ne suis capable de bien faire",
           "Je relâche la croyance que des choses externes me procureront du bonheur",
           "J'affirme désormais que je suis le plus heureux quand je suis calme et centré",
           "J'affirme que je peux dire non sans me sentir privé",
           "J'affirme désormais qu'il y aura assez pour moi quelques soient mon besoin",
           "J'affirme que je suis résilient face aux adversités",
           "J'affirme que je trouve satisfaction dans les choses du quotidien",
           "J'affirme que je resterai sur mes projets jusqu'à ce que je les finisse",
           "J'affirme que je vais prendre soin des gens et que je suis engagé vis à vis de leur bonheur",
           "J'affirme qu'il ya une dimension spirituelle à ma vie",
           "J'affirme que je suis profondément reconnaissant d'être en vie"]

    @staticmethod
    def get_instance():
        if Inspiration.instance == None:
            Inspiration.instance = Inspiration()
        return Inspiration.instance
    
    def loop(self,speaker):
        time_to_speak = random.randint(0,10)
        print("inspi" + str(time_to_speak))
        if time_to_speak > 5:
            sentence = random.randint(0,len(Inspiration.phrases)-1)
            # voices=speaker.getProperty('voices')
            # speaker.setProperty('voice',voices[3].id)
            speaker.say(Inspiration.phrases[sentence])
            speaker.runAndWait()
            print("inspiration")
