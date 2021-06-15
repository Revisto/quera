class PhoneValidations():
    def __init__(self, phone_number):
        self.phone_number = phone_number    
        
    def vallidate1(self):
        number_counts = {}
        for number in self.phone_number:
            if number not in number_counts:
                number_counts[number] = self.phone_number.count(number)
        all_values = number_counts.values()
        max_value = max(all_values)
        if max_value >= 4:
            return True
        return False

    def vallidate2(self):
        numbers_in_phone_number = list(set(self.phone_number))
        for number in numbers_in_phone_number:
            if number * 3 in self.phone_number:
                return True
        return False

    def vallidate3(self):
        if self.phone_number == self.phone_number[::-1]:
            return True
        return False

    def vallidate_all(self):
        if PhoneValidations(self.phone_number).vallidate1():
            return True
        if PhoneValidations(self.phone_number).vallidate2():
            return True
        if PhoneValidations(self.phone_number).vallidate3():
            return True
        return False

class InputHandler():
    def run(self):
        count = int(input())
        for i in range(count):
            phone_number = input()
            if PhoneValidations(phone_number).vallidate_all() is True:
                print("Ronde!")
            else:
                print("Rond Nist")

InputHandler().run()