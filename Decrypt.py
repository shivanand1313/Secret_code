def decode(dc):
    # Decoding the Message
    # dc = [9, 27, 1, 13, 27, 12, 5, 1, 18, 14, 9, 14, 7, 27, 20, 15, 27, 3, 15, 4, 5, 27, 9, 14, 27, 16, 25, 20, 8, 15, 14, 27, 12, 1, 14, 7, 21, 1, 7, 5]
    key = 'IJKLMNOPQRABCDEFGHSTUVWXYZ ,.></\'\\"?;:]}[{=+-_1234567890)(*&^%$#@!`~'

    R2 = []
    for d in key:
        R2.append(d)
    # print(R2)

    Rmsg = []
    for i in dc:
        lll = R2[i-1]
        Rmsg.append(lll)

    cmsg = "".join(Rmsg)
    # print(cmsg)
    return cmsg
