import random
import time

class Autohypnose:
    instance = None
    def __init__(self):
        self.last_sentence = int(time.time() * 1000)
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
                                                      "Je suis une äme forte et résiliente, capable de surmonter toutes les épreuvex",
                                                        "Je suis aimé, apprécié, et respecté tel que je suis",
                                                          "Je m'autorise à me valoriser et à croire en mes capacités",
                                                            "Je pardonne à tous ceux qui m'ont blessé, et je prends la responsabilité de ma croissance",
                                                              ]

    @staticmethod
    def get_instance():
        if Autohypnose.instance == None:
            Autohypnose.instance = Autohypnose()
        return Autohypnose.instance

    def loop(self,speaker):
        dt = (int(time.time() * 1000)) - self.last_sentence
        if dt > 50000:
            self.last_sentence = int(time.time() * 1000)
            time_to_speak = random.randint(0,10)
            if time_to_speak > 5:
                sentence = random.randint(0,len(self.sentences)-1)
                speaker.say(self.sentences[sentence])
                speaker.runAndWait()