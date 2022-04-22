import re

class ValidCarNumber:
    def __init__(self,number):
        self.number = number
    def is_valid(self):
        isvalid = re.search(r"(01|02|03)(KG|RU|KZ)([0-9]{3})(BMW|TYT|LEX)",self.number)
        # if isvalid == None:
        #     print("Невалидный номер")
        if isvalid and self.number == self.number[isvalid.start():isvalid.end()]:
            print("Валидный номер")
        else:
            print('Невалидный номер')
num = ValidCarNumber('01KG777BMW')
num.is_valid()
