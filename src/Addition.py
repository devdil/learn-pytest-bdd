class Addition:

    def add(self, num1, num2):
        if num1 is not int or num2 is not int:
            raise Exception("num1 and num2 should be integers")
        return num1 + num2
