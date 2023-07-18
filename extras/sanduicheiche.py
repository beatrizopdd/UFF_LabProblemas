while True:

    try:
        palavra = str(input())
        original = palavra
        
        for l in range(len(palavra)):
            substring = palavra[l:]
            if (palavra.count(substring) > 1):
                original = palavra[:l]
                break
        
        print(original)

    except EOFError:
        break
