import sqlite3 as sql
from contextlib import closing

dados = [
    ["São Paulo", "SE", "SP", 44411238],
    ["Minas Gerais", "SE", "MG", 20732660],
    ["Rio de Janeiro", "SE", "RJ", 16054524],
    ["Bahia", "NE", "BA", 14136417],
    ["Paraná", "S", "PR", 11433957],
    ["Rio Grande do Sul", "S", "RS", 10880749],
    ["Pernambuco", "NE", "PE", 9058931],
    ["Ceará", "NE", "CE", 8791688],
    ["Pará", "N", "PA", 8116132],
    ["Santa Catarina", "S", "SC", 7610361],
    ["Maranhão", "NE", "MA", 6775152],
    ["Goiás", "CO", "GO", 6950976],
    ["Amazonas", "N", "AM", 4207714],
    ["Espírito Santo", "SE", "ES", 4064052],
    ["Mato Grosso", "CO", "MT", 3658649],
    ["Rio Grande do Norte", "NE", "RN", 3302406],
    ["Alagoas", "NE", "AL", 3127683],
    ["Piauí", "NE", "PI", 3269201],
    ["Distrito Federal", "CO", "DF", 2817068],
    ["Mato Grosso do Sul", "CO", "MS", 2756700],
    ["Paraíba", "NE", "PB", 3999415],
    ["Sergipe", "NE", "SE", 2298696],
    ["Rondônia", "N", "RO", 1581016],
    ["Tocantins", "N", "TO", 1511460],
    ["Acre", "N", "AC", 830026],
    ["Amapá", "N", "AP", 733759],
    ["Roraima", "N", "RR", 636707],
]

print("região estados    minima      maxima       media         total")
print("====== ======= ========== ========== =========== =============")
with sql.connect("brasil.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        for região in cursor.execute("select região, count(*), min(população), max(população), avg(população)," \
        " sum(população)as top from estados group by região having count(*) > 5 order by top  desc"):
            print("{0:6} {1:7} {2:10} {3:10} {4:11.0f} {5:13}".format(*região))
        print("\nbrsil{0:7} {1:10} {2:10} {3:11.0f} {4:13}".format(*cursor.execute("select count(*), min(população), max(população)," \
        " avg(população), sum(população) from estados").fetchone()))
