def verify_pin(pin):
    if pin == '1234':
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin")
            tries += 1
    print("Too many incorrect tries. Could not log in")
    return False

def run_atm(withdrawal_amount):  # this is a 'main' function
    print("Welcome to the ATM!")
    successful_login = log_in()
    balance = None
    if successful_login:
        balance = 100
        try:
            if withdrawal_amount > balance:
                raise ValueError("Insufficient funds on your account")

            balance = balance - withdrawal_amount
            print("Take the money.\n Your new balance is {}".format(balance))

        except ValueError as err:
            raise ValueError(err)

        else:
            print("Thank you for using ATM")
            return balance
    else:
        print("Exiting Program")
        return balance


#run_atm(50)
