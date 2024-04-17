def maskify(cc):
    last_four = cc[-4:]
    hashtag_length = len(cc) - len(last_four)
    if len(cc) > 4:
        return "#" * hashtag_length + last_four
    else:
        return cc

print("Enter your credit card number")
message = input("")
Masked_message = maskify(message)
print("Your masked Credit Number is " + Masked_message)
