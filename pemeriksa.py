def cek_jawaban(
    jawaban_siswa,
    jawaban_benar
):

    return jawaban_siswa == jawaban_benar


def hitung_nilai(
    jumlah_benar,
    jumlah_soal
):

    return (
        jumlah_benar / jumlah_soal
    ) * 100