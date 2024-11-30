import random
from timestampassistant import timestamp_assistant

class Autohypnose:
    instance = None
    def __init__(self):
        self.sentences = ["Je suis digne de vivre une vie heureuse saine et épanouie",
                         "Je prends l engagement de faire au mieux avec moi même en toute situation",
                          "Merci",
                            "Je suis digne de respect, d'amour, et d'estime de moi même",
                              "Je m'autorise à vivre ma vie pleinement, libéré de toute humiliation",
                                "Je suis fier de la personne que je suis et des choix que je fais",
                                  "Je m'autorise à accepter et à aimer toutes les facettes de moi même",
                                    "Je suis digne d'amour, de compassion et de pardon envers moi même",
                                      "je suis fort, capable et digne de respect",
                                        "Je m'aime et je m'apprécie tel que je suis",
                                          "Je suis libre de toute humiliation, je choisis l'amour et la compassion",
                                            "Je m'autorise à être fier de moi et de mes accomplissements",
                                              "Je m'autorise à me pardonner et à me libérer de toute honte",
                                                "Je choisis de voir le bon en moi et en autrui",
                                                  "Je suis libéré de toute humiliation, je suis serein et confiant",
                                                    "Je suis fier de la personne que je suis devenu",
                                                      "Je suis une äme forte et résiliente, capable de surmonter toutes les épreuves",
                                                        "Je suis aimé, apprécié, et respecté tel que je suis",
                                                          "Je m'autorise à me valoriser et à croire en mes capacités",
                                                            "Je pardonne à tous ceux qui m'ont blessé, et je prends la responsabilité de ma croissance",
                "Je me rappelle que je cherche à avoir de l'impact par ce que je fais. J'aimerai pouvoir inspirer les gens.",
                "J'ai vraiment envie de continuer à faire prendre conscience aux gens, par mes vidéos, et articles du monde qui les entoure, de leur comportement, et leur donner l'espoir qu'on peut changer et mieux vivre.",
                "Je dois me rappeler que je suis puissant, et que je dois vivre les choses en conséquences. Je dois sortir de l'influence des victimes qui n'aspirent à ne rien changer pour leur propre confort",
                "Je suis puissant, et je suis capable de bien des choses. Je dois m'auto soutenir et continuer à croire dans mes rêves.",
                "J'aimerai changer la croyance que je doive faire les choses avec les autres. Il faut que je m'auto suffise, et que je crois en ce que je fais, pourquoi je le fais. J'ai beaucoup de choses à apporter au monde" ,
                "Ce qui me donne de l'énergie et m'aide à rester centré, est de pouvoir expérimenter, faire avancer un sujet, apprendre, confirmer que je suis capable par la créativité par exemple.",
                "Quand je me sens déconnecté, je peux peindre, méditer, écouter un podcast, faire du sport, écrire des articles."                                                           
                                                              ]

    @staticmethod
    def get_instance():
        if Autohypnose.instance == None:
            Autohypnose.instance = Autohypnose()
        return Autohypnose.instance

    def loop(self,speaker):
          time_to_speak = random.randint(0,10)
          print("hypnose" + str(time_to_speak))
          if time_to_speak > 5:
              sentence = random.randint(0,len(self.sentences)-1)
              # voices=speaker.getProperty('voices')
              # speaker.setProperty('voice',voices[1].id)
              speaker.say(self.sentences[sentence])
              speaker.runAndWait()
              print("autohypnose")