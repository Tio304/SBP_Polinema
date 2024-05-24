import numpy as np

# Data input
kriteria = ['G001', 'G002', 'G003', 'G004', 'G005', 'G006', 'G007', 'G008', 'G009', 'G010', 'G011', 'G012', 'G013', 'G014', 'G015', 'G016', 'G017', 'G018', 'G019', 'G020', 'G021']

# Bobot kriteria, ini perlu disesuaikan dengan data yang diberikan
bobot = np.array([0.4, 0.4, 0.9, 0.7, 0.4, 0.5, 0.5, 0.6, 0.5, 0.6, 0.6, 0.5, 0.5, 0.7, 0.5, 0.5, 0.8, 0.6, 0.6, 0.6, 0.5])

kode_hipotesa = [
    'H1', 'H2', 'H3'
]

kode_variabel = [
    'G001', 'G002', 'G003', 'G004', 'G005', 'G006', 'G007', 'G008', 'G009', 'G010', 
    'G011', 'G015', 'G016', 'G017', 'G018', 'G019', 'G020', 'G021'
]

hipotesa = {
    'H1': ['G001', 'G003', 'G006', 'G009', 'G011', 'G013', 'G015', 'G017', 'G020'],
    'H2': ['G001', 'G004', 'G007', 'G009', 'G011', 'G013', 'G016', 'G018', 'G020'],
    'H3': ['G002', 'G005', 'G008', 'G010', 'G012', 'G014', 'G016', 'G019', 'G021']
}

term_cf = {
    "Tidak": 0,
    "Sedikit Mungkin" : 0.4,
    "Mungkin": 0.5,
    "Kemungkinan Besar": 0.6,
    "Kecil Kepastian": 0.7,
    "Hampir Pasti": 0.8,
    "Pasti": 1
}

user_input = {
     "G001": ["Tingkat Kematian Minimal", "Tidak", 0],
  "G002": ["Tingkat Kematian Optimal", "Mungkin", 0.4],
  "G003": ["Harga Penjualan Mahal", "Tidak", 0],
  "G004": ["Harga Penjualan Normal", "Tidak", 0],
  "G005": ["Harga Penjualan Murah", "Tidak", 0],
  "G006": ["Kondisi Kandang Optimal", "Tidak", 0],
  "G007": ["Kondisi Kandang Layak", "Tidak", 0],
  "G008": ["Kondisi Kandang Minimal", "Tidak", 0],
  "G009": ["Jenis Bibit Dari Pabrik", "Tidak", 0],
  "G010": ["Jenis Bibit Dari Breder lokal", "Tidak", 0],
  "G011": ["Pakan Pabrik", "Tidak", 0],
  "G012": ["Pakan Racikan Peternak", "Tidak", 0],
  "G013": ["Program Vaksinasi Dari Pabrik", "Tidak", 0],
  "G014": ["Program Vaksinasi Dari Peternak", "Tidak", 0],
  "G015": ["Menerapkan Bio Sequrity", "Tidak", 0],
  "G016": ["Tidak Menerapkan Bio Sequrity", "Tidak", 0],
  "G017": ["Presentase Produksi Tinggi", "Tidak", 0],
  "G018": ["Presentase Produksi Normal", "Tidak", 0],
  "G019": ["Presentase Produksi Rendah", "Tidak", 0],
  "G020": ["Musim Normal", "Tidak", 0],
  "G021": ["Musim Pancaroba", "Tidak", 0]
}

pakar_input = {
    "H1": [
        ("G001", "Tingkat Kematian Minimal", 0.4),
        ("G003", "Harga Penjualan Mahal", 0.4),
        ("G006", "Kondisi Kandang Optimal", 0.6),
        ("G009", "Jenis Bibit Dari Pabrik", 0.6),
        ("G011", "Pakan Pabrik", 0.4),
        ("G013", "Program Vaksinasi Dari Pabrik", 0.4),
        ("G015", "Menerapkan Bio Sequrity", 1),
        ("G017", "Presentase Produksi Tinggi", 0.4),
        ("G020", "Musim Normal", 1)
    ],
    "H2": [
        ("G001", "Tingkat Kematian Minimal", 0.4),
        ("G004", "Harga Penjualan Normal", 0.4),
        ("G007", "Kondisi Kandang Layak", 0.6),
        ("G009", "Jenis Bibit Dari Pabrik", 0.4),
        ("G011", "Pakan Pabrik", 0.4),
        ("G013", "Program Vaksinasi Dari Pabrik", 0.6),
        ("G016", "Tidak Menerapkan Bio Sequrity", 0.4),
        ("G018", "Presentase Produksi Normal", 0.6),
        ("G020", "Musim Normal", 0.6)
    ],
    "H3": [
        ("G002", "Tingkat Kematian Optimal", 0.4),
        ("G005", "Harga Penjualan Murah", 0.6),
        ("G008", "Kondisi Kandang Minimal", 1),
        ("G010", "Jenis Bibit Dari Breder lokal", 1),
        ("G012", "Pakan Racikan Peternak", 0.6),
        ("G014", "Program Vaksinasi Dari Peternak", 0.6),
        ("G016", "Tidak Menerapkan Bio Sequrity", 1),
        ("G019", "Presentase Produksi Rendah", 0.6),
        ("G021", "Musim Pancaroba", 0.6)
    ]
}

hitung_cf = {
    "H1": [
        ("G001", "Tingkat Kematian Minimal", 0.4, 0.4),
        ("G003", "Harga Penjualan Mahal", 0.9, 0.4),
        ("G006", "Kondisi Kandang Optimal", 0.5, 0.6),
        ("G009", "Jenis Bibit Dari Pabrik", 0.5, 0.6),
        ("G011", "Pakan Pabrik", 0.6, 0.4),
        ("G013", "Program Vaksinasi Dari Pabrik", 0.5, 0.4),
        ("G015", "Menerapkan Bio Sequrity", 0.5, 1),
        ("G017", "Presentase Produksi Tinggi", 0.8, 0.4),
        ("G020", "Musim Normal", 0.6, 1)
    ],
    "H2": [
        ("G001", "Tingkat Kematian Minimal", 0.4, 0.4),
        ("G004", "Harga Penjualan Normal", 0.7, 0.4),
        ("G007", "Kondisi Kandang Layak", 0.5, 0.6),
        ("G009", "Jenis Bibit Dari Pabrik", 0.5, 0.4),
        ("G011", "Pakan Pabrik", 0.6, 0.4),
        ("G013", "Program Vaksinasi Dari Pabrik", 0.5, 0.6),
        ("G016", "Tidak Menerapkan Bio Sequrity", 0.5, 0.4),
        ("G018", "Presentase Produksi Normal", 0.6, 0.6),
        ("G020", "Musim Normal", 0.6, 0.6)  
    ],
    "H3": [
       ("G002", "Tingkat Kematian Optimal", 0.5, 0.4),
        ("G005", "Harga Penjualan Murah", 0.4, 0.6),
        ("G008", "Kondisi Kandang Minimal", 0.6, 1),
        ("G010", "Jenis Bibit Dari Breder lokal", 0.6, 1),
        ("G012", "Pakan Racikan Peternak", 0.5, 0.6),
        ("G014", "Program Vaksinasi Dari Peternak", 0.7, 0.6),
        ("G016", "Tidak Menerapkan Bio Sequrity", 0.5, 1),
        ("G019", "Presentase Produksi Rendah", 0.6, 0.6),
        ("G021", "Musim Pancaroba", 0.5, 0.6)
    ]
}
# Input dari user
user_input_cf = {key: term_cf[value[1]] for key, value in user_input.items()}

# Input dari pakar
pakar_input_cf = {h: {v[0]: v[2] for v in values} for h, values in pakar_input.items()}

# Matriks keputusan berdasarkan input pakar
matrix_keputusan = np.array([[pakar_input_cf[h].get(k, 0) for k in kriteria] for h in kode_hipotesa])

# Langkah 1: Normalisasi Matriks Keputusan
def normalisasi_benefit(matrix):
    return matrix / np.max(matrix, axis=0)

normalisasi = normalisasi_benefit(matrix_keputusan)

# Langkah 2: Menghitung Bobot Ternormalisasi
ternormalisasi_berbobot = normalisasi * bobot

# Langkah 3: Menghitung Matriks MABAC
nilai_rata_rata = np.mean(ternormalisasi_berbobot, axis=0)
matrix_mabac = ternormalisasi_berbobot + nilai_rata_rata

# Langkah 4: Menghitung Nilai S dan Q
nilai_s = np.sum(matrix_mabac, axis=1)

# Hasil akhir
alternatif_dengan_skor = list(zip(kode_hipotesa, nilai_s))
alternatif_dengan_skor.sort(key=lambda x: x[1], reverse=True)

print("Peringkat hipotesa berdasarkan skor MABAC:")
for kode, skor in alternatif_dengan_skor:
    print(f"{kode}: {skor:.4f}")
