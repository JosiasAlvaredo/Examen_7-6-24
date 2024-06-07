import requests
import json
import os

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_posts(n):
    url = f"https://jsonplaceholder.typicode.com/posts?_limit={n}"
    response = requests.get(url)
    return json.loads(response.text)

def download(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def main():
    contador = 1
    while True:
        try:
            n = int(input("Ingrese la cantidad de post que desea obtener (1-100): "))
            if n < 1 or n > 100:
                raise ValueError
            break
        except ValueError:
            print("Invalido la cantidad de post debe ser un numero entre 1 y 100")

    posts = get_posts(n)
    primos = {}
    no_primos = {}

    for post in posts:
        if is_prime(post["id"]):
            primos[post["id"]] = post
        else:
            no_primos[post["id"]] = post

    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")

    archivos_Primos = f"Downloads/dl{contador}Primes.json"
    archivos_noPrimos = f"Downloads/dl{contador}NotPrimes.json"

    download(primos, archivos_Primos)
    download(no_primos, archivos_noPrimos)

    print("Archivos guardados")

    contador += 1

if __name__ == "__main__":
    main()