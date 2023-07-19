
#Piper Jones
def encode(password):
    enc_pass = ""
    for i in range(len(password)):
        new_dig = int(password[i]) + 3 #this is implemented incorrectly let me make some correct changes
        if new_dig > 9: #here now it shifts instead of adding
            new_dig -= 10
        enc_pass += str(new_dig)
    return enc_pass

def decode(enc_pass): #here are my changes
    dec_pass = ''
    for i in range(len(enc_pass)):
        new_dig = int(enc_pass[i]) - 3
        if new_dig < 0:
            new_dig += 10
        dec_pass += str(new_dig)
    return dec_pass


while True:
    print("""
Menu
-------------
1. Encode
2. Decode
3. Quit\n""")

    opt = input("Please enter an option: ")
    opt = int(opt)

    if opt == 1:
        password = input('Please enter your password to encode: ')
        print("Your password has been encoded and stored!")
        enc_pass = encode(password)
    elif opt == 2:
        dec_pass = decode(enc_pass)
        print(f"The encoded password is {enc_pass}, and the original password is {dec_pass}.")
    elif opt == 3:
        quit()
