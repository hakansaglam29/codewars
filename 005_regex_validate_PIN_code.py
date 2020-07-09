def validate_pin(pin):
    if (len(pin) == 4 or len(pin) ==6) and pin.isdigit() ==True:
        return True
    else:
        return False

# validate_pin = lambda pin: len(pin) in [4, 6] and pin.isdigit()

# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()