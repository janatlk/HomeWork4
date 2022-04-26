import re
class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
    def split1(self):
        x = re.split('[ ]',self.sentence)
        '''В [скобках] можно указать любой символ который будет разделять слова'''
        print(x[-1])
        lst = list(x[-1])
        print(len(lst))


sen = Sentence("Pleae,eat this strawberries")
sen.split1()