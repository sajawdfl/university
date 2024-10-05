from errors.CustomError import CustomError

class ValidationError(CustomError):
    pass

    def print(self):
        print('student not found !!!')

    