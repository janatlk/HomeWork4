import re

class ValidCarNumber:
    def is_valid(self,number):
        isvalid = re.search(r"(01|02|03)(KG|RU|KZ)([0-9]{3})(BMW|TYT|LEX)",number)
        if isvalid == None:
            print("Невалидный номер")
        else:
            print("Валидный номер")
num = ValidCarNumber.is_valid(0,"02KG777BMW")
num2 = ValidCarNumber.is_valid(0,"hhh777hhh")
