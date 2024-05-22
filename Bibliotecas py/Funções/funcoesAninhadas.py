# a variavel oii pode ser mencionada na função tchau(), agora a variavel tchauu não pode ser mencionada na função oi()
def oi(oi):
    oii = oi
    def tchau():
        nonlocal oii
        oii = 'oi'
        tchauu = 'tchauu'
        print(1)
    tchau()
    # print(tchauu)


oi('oi')