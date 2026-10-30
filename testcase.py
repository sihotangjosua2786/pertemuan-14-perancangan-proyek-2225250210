from src.pemeriksa import *

assert cek_jawaban(
    5,
    5
) == True

assert cek_jawaban(
    4,
    5
) == False

assert hitung_nilai(
    5,
    5
) == 100

assert hitung_nilai(
    3,
    5
) == 60

print(
    "Semua test PASS"
)