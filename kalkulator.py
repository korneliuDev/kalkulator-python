import time 

print("__  _   ____  _      __  _  __ __  _       ____  ______   ___   ____")
print("|  |/ ] /    || |    |  |/ ]|  |  || |     /    ||      | /   \ |    \ ")
print("|  ' / |  o  || |    |  ' / |  |  || |    |  o  ||      ||     ||  D  ) ")
print("|    \ |     || |___ |    \ |  |  || |___ |     ||_|  |_||  O  ||    /  ")
print("|     \|  _  ||     ||     \|  :  ||     ||  _  |  |  |  |     ||    \  ")
print("|  .  ||  |  ||     ||  .  ||     ||     ||  |  |  |  |  |     ||  .  \ ")
print("|__|\_||__|__||_____||__|\_| \__,_||_____||__|__|  |__|   \___/ |__|\_| ")

print(" ")

print("Wybierz co chcesz zrobić, możesz : ")
print(">Dodać (znak +)")
print(">Odjąć (znak -)")
print(">Pomnożyć (znak *)")
print(">Podzielić (znak /)")
print(">Potęgować (znak **)")
print(" ")
l = input("wybierz odpowiedni znak : ")

x = input("Podaj pierwszą liczbę : ")
y = input("Podaj drugą liczbę : ")
x = int(x)
y = int(y)


if l == "+":
    print("Wynik : ", x+y)
elif l == "-":
    print("Wynik : ", x-y)
elif l == "*":
    print("Wynik : ", x*y)
elif l == "/":
    print("Wynik : ", x/y)
elif l == "**":
    print("Wynik : ", x**y)
else:
    print("Ten znak nie jest obsługiwany")
time.sleep(5)

print("Prawa autorskie osoby pod nickami : korneliudev, point , pointcik , Kornel")
print("Program się zakończył! Jeżeli chcesz coś jeszcze obliczyć, włącz program ponownie!")
print("python kalkulator.py")