def oi(uhu:int) -> str:
    uhu = chr(uhu)
    return uhu


print(oi(80))

notas = [7,8,5,10]

def media(nota)->float:
    result = sum(notas)/len(notas)
    return result


print(media(notas))