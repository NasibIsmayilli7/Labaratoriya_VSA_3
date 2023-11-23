import numpy as np

def menfi_cem_sutun(A):
    n, m = A.shape
    menfi_cem_sutunlar = []

    for j in range(m):
        cem = np.sum(A[:, j])
        
        if cem < 0:
            menfi_cem_sutunlar.append(j)

    return menfi_cem_sutunlar

np.random.seed(42)  
random_A = np.random.randint(-10, 10, size=(3, 3))  
print("Random massiv:")
print(random_A)

menfi_cem_sutunlar = menfi_cem_sutun(random_A)
print("Mənfi cəmə malik sütunların nömrəsi:", menfi_cem_sutunlar)
