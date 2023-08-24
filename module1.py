def secret_code(msg):
    # Secret Code
    print(msg)
    # msg = 'I am learning to code in python language'  # Message to be coded
    st = msg.upper()  # Converting msg to uppercase

    # Encryption key
    scd = 'IJKLMNOPQRABCDEFGHSTUVWXYZ ,.></"?;:]}[{=+-_1234567890)(*&^%$#@!`~'  # IJKLMNOPQRABCDEFGHSTUVWXYZ ,./"?;:]}[{=+-_1234567890)(*&^%$#@!`~

    # Segregating each letter from sentence(string)
    Rst1 = []
    Rst2 = []
    for i in st:
        Rst1.append(i)
    for j in scd:
        Rst2.append(j)

    # Recording variables
    Rp = []
    Rq = []
    q = 0

    # Knowing the index of each letter in segregated strings if msg
    for str1 in Rst1:
        q = q + 1
        p = 0
        for str2 in Rst2:
            p = p + 1
            if str1 == str2:
                Rp.append(p)
                Rq.append(q)

    # Our message is coded into numbers with help of "key"
    # print(Rp)  # Coded msg

    return Rp


def decode(dc):
    # Decoding the Message
    # dc = [9, 27, 1, 13, 27, 12, 5, 1, 18, 14, 9, 14, 7, 27, 20, 15, 27, 3, 15, 4, 5, 27, 9, 14, 27, 16, 25, 20, 8, 15, 14, 27, 12, 1, 14, 7, 21, 1, 7, 5]
    key = 'IJKLMNOPQRABCDEFGHSTUVWXYZ ,.></"?;:]}[{=+-_1234567890)(*&^%$#@!`~'

    R2 = []
    for d in key:
        R2.append(d)
    print(R2)

    Rmsg = []
    for i in dc:
        lll = R2[i-1]
        Rmsg.append(lll)

    cmsg = "".join(Rmsg)
    # print(cmsg)
    return cmsg


# Coding and Decoding the message by calling the function

# Encrypting msg
# import secret_code_lang as ss
numeric1 = secret_code("Shiv is Smart")
print(numeric1)

# Decrypting msg
mssg = decode([19, 18, 1, 22, 27, 1, 19, 27, 19, 5, 11, 10, 20])
print(mssg)
