from src.generator import buat_soal
from src.pemeriksa import (
    cek_jawaban,
    hitung_nilai
)
from src.penyimpanan import (
    simpan_hasil
)

JUMLAH_SOAL = 5

benar = 0

for nomor in range(
    1,
    JUMLAH_SOAL + 1
):

    soal, jawaban = buat_soal()

    print(
        f"Soal {nomor}: "
        f"{soal} = ?"
    )

    jawaban_siswa = int(
        input("Jawaban : ")
    )

    if cek_jawaban(
        jawaban_siswa,
        jawaban
    ):

        print("Benar\n")

        benar += 1

    else:

        print(
            f"Salah "
            f"(Jawaban = {jawaban})\n"
        )

nilai = hitung_nilai(
    benar,
    JUMLAH_SOAL
)

hasil = f"""
Jumlah Benar : {benar}
Jumlah Salah : {JUMLAH_SOAL - benar}
Nilai : {nilai}
"""

print(hasil)

simpan_hasil(
    "data/laporan.txt",
    hasil
)