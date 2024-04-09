def n_høyeste(liste: list[int], n: int):
    høyeste_n = []
    for i in range(n):
        høyest = max(liste)
        liste.remove(høyest)
        høyeste_n.append(høyest)
    return høyeste_n

print(n_høyeste([1,2,3,-5,5,-5,3], 6))