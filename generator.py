import random


def buat_soal():

    angka1 = random.randint(1, 20)
    angka2 = random.randint(1, 20)

    operator = random.choice(["+", "-"])

    if operator == "+":
        jawaban = angka1 + angka2
    else:
        jawaban = angka1 - angka2

    soal = f"{angka1} {operator} {angka2}"

    return soal, jawaban