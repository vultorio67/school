g = []
print("start")

def ok():
    for i in range(100):
        n = i - 50
        try:
            a = (3*n-17) # faut compléter la fonction qui se fait diviser
            u = n-4 # faut compléter la fonction qui divise
            a = a/u
            for s in range(100):
                b = s-50
                if(a == b):
                    g.append(n)

        except:
            None
    return(g)

print(ok())



