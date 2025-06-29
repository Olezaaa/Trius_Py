#Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S
#вставить строку S0.
def insert_string(c, S, S0):
    return S.replace(c, S0 + c)
c = 'a'
S = 'Taros'
S0 = 'x'
result = insert_string(c, S, S0)
print(result)