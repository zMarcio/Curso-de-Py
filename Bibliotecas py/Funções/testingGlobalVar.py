# oi = 'oi'
# varzea = 1
def chama():
    global varzea
    varzea = 1
    print(varzea)

# Por varzea está definida dentro de chama quando se coloca ela primeiro você da valor a ela, e se ela vim primeiro da erro, pois não está definida!
chama()
print(varzea)
chama()