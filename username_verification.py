def verification(username):

    """
       verification of a user's password.
       Requirements:
       length <= 12,
       must include: Latin letters in both low and upper cases, digit, and hyphens
    """

    if len(username) > 12: return False

    lower = upper = digit = hyphen = False

    for i in username:
        if i.isdigit():
            digit = digit or True
        elif i == "-":
            hyphen = hyphen or True
        else:
            # checking whether it is latin
            if not 63 < ord(i.lower()) < 123:
                return False 
            elif i.islower():
                lower = lower or True
            elif i.isupper():
                upper = upper or True
            
        
    return lower and upper and digit and hyphen

print(verification("d8q5-Fgk09"))
