from errors.CustomError import CustomError

class UnitError(CustomError):
    pass

    def print(self):
        print('unit should be a number between 1 and 3 !!!')