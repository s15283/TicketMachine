import json
import re

with open("prices.json", "r", encoding="UTF-8") as jf:
    prices = json.load(jf)

def display_menu(menu):
    print("Jaką opcję biletu chcesz kupić? ")
    options = list(menu.keys())
    for index, option in enumerate(options):
        print(f"{index} - {option}")
    try:
        choice = int(input("Wybór: "))
    except ValueError:
        print("Wprowaadzono niepoprawny typ wartości.")
        return display_menu(menu)
    if choice > len(options)-1 or choice < 0:
        print("Wprowadzono błędny numer opcji.")
        return display_menu(menu)
    menu = menu[options[choice]]
    if isinstance(menu ,dict):
        return display_menu(menu)
    else:
        return (option, menu)

def register_payment(cart):
    total = sum(price for _, price in cart)
    print(f"Kwota do zapłąty: {total} zł")
    payment_method = input("Wybierz metodę płatności: \nb - BLIK \nk- karta\ng - gotówka\n")
    if payment_method.lower()=='b':
        blik = input("Podaj kod BLIK: ")
        if re.search(r"^[0-9]{6}$", blik):
            print("Transakcja się powiodła")
        else:
            decision = input("Podano niepoprawny kod. Czy chcesz spróbować jeszcze raz (t/n)? ")
            if decision.lower()=='t':
                register_payment(cart)
            else: exit()
    elif payment_method.lower()=='k':
        print("Proszę zbliżyć kartę do czytnika...")
        input("Potwierdź transakcję: ")
        print("Transakcja się powiodła")
    elif payment_method.lower()=='g':
        paid = 0
        while paid < total:
            try:
                paid += float(input("Wprowadź gotówkę: "))
            except ValueError:
                paid += 0
            if paid < total:
                decision = input("Wprowadzono za mało gotówki. Czy chcesz dopłacić (t/n? )")
                if decision.lower()=='t':
                    continue
                else: exit()
    else:
        decision = input("Wybrano niepoprawną opcję. Czy chcesz spróbować jeszcze raz (t/n)? ")
        if decision.lower()=='t':
            register_payment(cart)
        else: exit()

def display_cart(cart):
    for ticket, price in cart:
        print(f"bilet {ticket}\t{price} zł")

cart = []
add_another = "t"
while add_another.lower()=='t':
    cart.append(display_menu(prices))
    add_another = input("Czy chcesz dodać kolejny bilet (t/n)? ")
register_payment(cart)
input("Drukowanie biletów. Proszę czekać...")
display_cart(cart)
print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie")