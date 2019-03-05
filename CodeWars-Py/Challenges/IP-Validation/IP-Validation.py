def is_valid_IP(strng):
    digits = strng.split('.')
    if len(digits) != 4: return False
    for i in digits:
        if not i.isnumeric() or len(i)>3 or int(i)>255 or int(i)<0 or (i.startswith('0') and len(i)>1):
            return False
    return True

