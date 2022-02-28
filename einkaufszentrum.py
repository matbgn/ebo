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


def create_an_entry():
    is_juice = bool(random.getrandbits(1))
    article = f'\nJus de {random.sample(fruit, 1)[0]}' if is_juice else f'\n{random.sample(fruit, 1)[0]}'
    print(article)
    base_weight = random.randrange(10, 5000, 10)/1000.0
    multiplicative = random.randint(1, 5)
    print(f'Poids : {multiplicative} x {"{:.3f}".format(base_weight)} {"l." if is_juice else "kg."}')
    price = base_weight * multiplicative * 0.05 * random.randint(10, 100)
    print(f'Prix total : {"{:.3f}".format(price)} CHF')
    print(f'Poids total en {random.choice(("l.", "dl.", "cl.", "ml.")) if is_juice else random.choice(("kg.", "g."))} : ')
    print(f'Prix au kilo : ')
    print("{:.2f}".format(price/base_weight/multiplicative))


for i in range(5):
    create_an_entry()
