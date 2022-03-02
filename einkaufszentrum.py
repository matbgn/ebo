import random

fruit = {
    "Abricot",
    "Airelle",
    "Amande",
    "Ananas",
    "Avocat",
    "Banane",
    "Cassis",
    "Cerise",
    "Châtaigne",
    "Citron",
    "Clémentine",
    "Coing",
    "Datte",
    "Figue",
    "fraîche",
    "Fraise",
    "Fraise des bois",
    "Framboise",
    "Fruit de la passion",
    "Grenade",
    "Groseille",
    "Groseille à maquereau",
    "Kaki",
    "Kiwi",
    "Kumquat",
    "Litchi",
    "Mandarine",
    "Mangue",
    "Marron",
    "Melon",
    "Mirabelle",
    "Mûre",
    "Myrtille",
    "Nectarine",
    "Noisette",
    "Noix",
    "Orange",
    "Orange sanguine",
    "Pamplemousse",
    "Papaye",
    "Pastèque",
    "Pêche",
    "Poire",
    "Pomme",
    "Prune",
    "Quetsche",
    "Raisin",
    "Reine-claude",
    "Tomate",
    "Tomate charnue",
    "Tomate",
    "Peretti",
}


def create_an_entry(withAnswers=False):
    is_juice = bool(random.getrandbits(1))
    article = f'Jus de {random.sample(fruit, 1)[0]}' if is_juice else f'{random.sample(fruit, 1)[0]}'
    multiplicative = random.randint(3, 9)
    designation = f'{multiplicative}x {article}'.ljust(38, " ")
    while True:
        base_weight = random.randrange(100, 5000, 100)/1000.0
        price = base_weight * 3
        divider = random.choice((1.5, 2.5, 3, 5))
        weight_denominator = base_weight / divider
        if "{:.3f}".format(weight_denominator)[-1:] == '0' and ("{:.2f}".format(price / divider)[-1:] == '0' or "{:.2f}".format(price / divider)[-1:] == '5'):
            break
    weight_formatting = f'{"{:.3f}".format(base_weight)} {"l." if is_juice else "kg."}'.ljust(9, " ")
    weight_by = random.choice(("dl.", "cl.", "ml.")) if is_juice else "g."
    weight_by_formatting = f'.......... en {weight_by}'.ljust(17, " ")
    price_formatting = f'{"{:.2f}".format(price)} CHF'.ljust(9, " ")
    price_by_formatting = f'.......... CHF / {"{:.3f}".format(weight_denominator)} {"litre" if is_juice else "kilo"}'.ljust(28, " ")
    line_total = f'Total : ............... CHF'
    do_insert_backslash = "" if withAnswers else "\n"
    print(f'{do_insert_backslash}{designation} | {weight_formatting} | {weight_by_formatting} | {price_formatting} | {price_by_formatting} | {line_total}')
    switch = {
        'g.': 1000,
        'dl.': 10,
        'cl.': 100,
        'ml.': 1000,
    }
    if withAnswers:
        answer_print_separator = " "
        weight_by_answer = base_weight * switch.get(weight_by, "Invalid input")
        init_space = "".rjust(56, answer_print_separator)
        weight_by_answer_formatting = "{:.0f}".format(weight_by_answer).ljust(32, answer_print_separator)
        divider_answer_formatting = f'({divider})'.ljust(24, answer_print_separator)
        price_by_answer_formatting = f'{"{:.2f}".format(price / divider).ljust(14, answer_print_separator)}{divider_answer_formatting}'
        total_answer = price * multiplicative
        print(f'{init_space}{weight_by_answer_formatting}{price_by_answer_formatting}{"{:.2f}".format(total_answer)}')

    return total_answer


sum=0
for i in range(5):
    sum += create_an_entry(withAnswers=True)

print(f'{"".rjust(114, " ")}{"".rjust(31, "=")}')
print(f'\n{"".rjust(110, " ")}Grand Total : ............... CHF')
print(f'{"".rjust(128, " ")}{"{:.2f}".format(sum)}')
