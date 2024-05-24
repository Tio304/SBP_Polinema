import numpy as np

# Data input
kriteria = ['C1', 'C2', 'C3', 'C4']
bobot = np.array([25, 30, 25, 20])
type_kriteria = ['Benefit', 'Benefit', 'Benefit', 'Benefit']

alternatif = [
    [90, 81, 89, 77],
    [70, 80, 80, 85],
    [85, 69, 76, 89],
    [95, 80, 83, 83],
    [82, 75, 78, 82],
    [76, 65, 80, 80],
    [72, 88, 75, 86],
    [68, 72, 79, 86]
]


alternatif = np.array(alternatif, dtype=float)


def normalisasi_benefit(matrix):
    return matrix / np.max(matrix, axis=0)

normalisasi = normalisasi_benefit(alternatif)


bobot = bobot / 100
ternormalisasi_berbobot = normalisasi * bobot


nilai_rata_rata = np.mean(ternormalisasi_berbobot, axis=0)
matrix_mabac = ternormalisasi_berbobot + nilai_rata_rata


nilai_s = np.sum(matrix_mabac, axis=1)


alternatif_dengan_skor = list(zip(range(1, len(alternatif) + 1), nilai_s))
alternatif_dengan_skor.sort(key=lambda x: x[1], reverse=True)

print("Peringkat alternatif berdasarkan skor MABAC:")
for kode, skor in alternatif_dengan_skor:
    print(f"D{kode}: {skor:.4f}")
