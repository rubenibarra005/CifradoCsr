def descifrar(cadena):
    alfabeto = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    cadena = cadena.lower()
    tam = len(alfabeto)

    for i in range(tam):
        print(i,": ",end=" ")
        for j in cadena:
            if j == " ":
                print(" ", end=" ")
            else:
                pos = alfabeto.index(j)
                nuevPos = (pos + i) % tam   
                print(alfabeto[nuevPos], end="")
        print()
            
def main():
    descifrar("Lzav lz bu tluzhql kl wyblihz")


    

if __name__ == "__main__":
    main()