# animals
a = input()
b = input()
c = input()

animals = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

print(animals[a][b][c])
