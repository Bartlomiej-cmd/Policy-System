from datetime import datetime

import hashlib


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3, 1]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "female" if int(pesel[-2]) % 2 == 0 else "male"
    birth_date = datetime(
        int("19" + pesel[0:2]),
        int(pesel[2:4]),
        int(pesel[4:6]),
    )
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date,
    }
    return result


def hashed_password(password):

    special_chars = ['!', '@', "#", '$', '%', '^', '&', '*',
                     "(", ")", "_", "+", '-', '=', '{', "}",
                     "[", "]", '|', ":", '"', ';', "'", '<',
                     ">", '?', ",", ".", "/", '"', "\\"
    ]

    if len(password) < 7:
        return None
    else:
        upper_res = False
        lower_res = False
        digit_res = False
        spec_char_res = False
        for element in password:
            if element.isupper():
                upper_res = True
            elif element.islower():
                lower_res = True
            elif element.isdigit():
                digit_res = True
            elif element in special_chars:
                spec_char_res = True

        # print([upper_res, lower_res, digit_res, spec_char_res])

    if all([upper_res, lower_res, digit_res, spec_char_res]):
        encoded_password = password.encode('utf-8')
        hashed = hashlib.md5(encoded_password)
        return hashed.hexdigest()
    else:
        return None
