def maskify(cc):
    last_four = cc[-4:]
    hashtag_length = len(cc) - len(last_four)
    if len(cc) > 4:
        return "#" * hashtag_length + last_four
    else:
        return cc

print(maskify("123456789101234567"))
