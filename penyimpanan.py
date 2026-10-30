def simpan_hasil(
    file,
    hasil
):

    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(hasil)