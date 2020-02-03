def validate_pin(pin):
    try:
        int(pin)
        list(pin)
        if(len(pin) == 4 or len(pin) == 6):
            return True
        else:
            return False
    except ValueError:
        return False
