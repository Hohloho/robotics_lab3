def validate_pin(pin):
    try:
        int(pin)
        length = list(map(int, str(pin)))
        if(len(length) == 4 or len(length) == 6):
            return True
        else:
            return False
    except ValueError:
        return False
