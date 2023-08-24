def secret_code(msg):
    # Secret Code
    print(msg)
    # msg = 'I am learning to code in python language'  # Message to be coded
    st = msg.upper()  # Converting msg to uppercase

    # Encryption key
    scd = 'IJKLMNOPQRABCDEFGHSTUVWXYZ ,.></\'\\"?;:]}[{=+-_1234567890)(*&^%$#@!`~'  # IJKLMNOPQRABCDEFGHSTUVWXYZ ,./"?;:]}[{=+-_1234567890)(*&^%$#@!`~

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
