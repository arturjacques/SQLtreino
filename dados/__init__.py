def leiaInt(texto):
    while True:
        try:
            a=int(input(texto))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar')
            return 0
        except Exception:
            print('digite um número valido')
        else:
            return a

def leiaFloat(texto):
    while True:
        try:
            a=float(input(texto))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar')
            return 0
        except Exception:
            print('digite um número valido')
        else:
            return a