"""
Napisać program pobierający w pętli od
użytkownika liczbę rzeczywistą x (typ float) i wypisujący
x oraz trzecią potęgę x. Zatrzymanie programu następuje po
wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis
zamiast liczby, to program ma wypisać komunikat o
błędzie i kontynuować pracę
"""


def app():
    while True:
        try:
            user_input = input('Wpisz liczbę lub stop aby zakończyć: ')
            if user_input == 'stop':
                break
            number = float(user_input)

        except ValueError:
            print('Błąd! Wpisano niepoprawnie liczbę!', flush=True)
            continue

        print(f'x={number} i x^3={pow(number, 3)}')


def main():
    app()


if __name__ == '__main__':
    main()
