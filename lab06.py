
#Piper Jones
def encode(password):
    enc_pass = ""
    for i in range(len(password)):
        new_dig = int(password[i]) + 3
        enc_pass += str(new_dig)
    return enc_pass

def decode(enc_pass):


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


