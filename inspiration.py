import random

class Inspiration:
    phrases = ["Je relache maintenant toutes les impulsions irréfléchies et destructrices",
           "Je me libère de la croyance que je serai submergé par l'anxiété",
           "Je me libère de toutes mes compulsions et addictions",
           "Je me libère du besoin de me consumer en essayant de satisfaire tous mes désirs",
           "Je me libère de la tenatavie de fuir les conséquences de mes actes",
           "Je me libère de la tentative de fuir les conséquences de mes actes"]
    
    @staticmethod
    def pick_inspiration():
        val = random.randint(0,len(Inspiration.phrases)-1)
        return Inspiration.phrases[val]
