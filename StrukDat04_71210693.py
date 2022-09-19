import json

with open('mahasiswa.json','r') as datafile:
    data = json.load(datafile)

data_s = dict()
n = int(input('Masukan jumlah mahasiswa baru : '))
for i in range(0, n):
    list_hobi = []
    nama = input('Masukan nama Anda : ')
    x = int(input('Masukan Jumlah hobi : '))
    for j in range(0,x):
        hobi = input(f'Masukan Hobi ke-{j+1} : ')
        list_hobi.append(hobi)
    prestasi = input('Masukan Prestasi Anda: ')
    print('=== Data berhasil ditambahkan ===')
    print()
    data_s[nama] = [{"Biodata" : {"Hobi": list_hobi, "Prestasi" : prestasi}}]

data.update(data_s)

with open('mahasiswa.json','w') as datafile:
    json.dump(data, datafile)