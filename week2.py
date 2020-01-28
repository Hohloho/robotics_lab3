#check only number 4 or 6 long only alphabet and special char is not allowed 
import TimeTester
def check(input_pin):
    try:
        int(input_pin)
        return True
    except ValueError:
        return False

def validate_pin(pin):
    list(pin)
    if((len(pin)==4 or len(pin)==6) and check(pin) == True):
        return True
    return False

def x():
    validate_pin("123a")

print(TimeTester.run(100000, x))

