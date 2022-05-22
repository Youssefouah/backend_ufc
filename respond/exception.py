



class expression_errors():
    """
    Exception for invalid expression
    """
    def __init__(self):
        self.message = {}
    
    def exprission_error(self):
        self.message["user not found"] = 1
        self.message ["user already exists"] = 2
        self.message ["the username or password is incorrect"] = 3
        self.message["the username is not exist"] = 4
        self.message ["the username or password is not correct.please try again"] = 5
        self.message ["the username is already exist"] = 6
        self.message["the email is already exist"] = 7
        self.message["the email is not exist"] = 8
        self.message ["the email is not correct"] = 9
        self.message ["the password is not correct"] = 10
        self.message ["edit data in table users"] = 11
        self.message ["your input is not confirm"] = 12
        self.message ["delete data in table users"] = 13
        self.message ["status.HTTP_404_NOT_FOUND"] = 14
        self.message ["this opertion is failed"] = 15

        return self.message