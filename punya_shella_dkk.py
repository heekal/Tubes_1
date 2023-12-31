# Database
admin = {
    'username' : ['admin1', 'admin2'],
    'password' : ['123', '321']
}

direktur_sdm = {
    'username' : ['sdm1', 'sdm2'],
    'password' : ['123', '321']
}

direktur = {
    'username' : ['direktur1', 'direktur2'],
    'password' : ['123', '321']
}

pegawai = {
    'nip' : [1103223000, 1103223001, 1003223000, 1103223004],
    'nama' : ['haikal', 'luna', 'winatha', 'glenn'],
    'gaji' : {
        'pokok' : [1000, 1000, 250, 250],
        'jam' : [50, 50, 10, 10]
    },
    'jabatan' : ['vice manager', 'manager', 'programmer', 'programmer'],
    'divisi' : ['pejabat', 'pejabat', 'database', 'database']
}

# Parent Class
class Aplikasi:
    def __init__(self, username, password, jabatan):
        self.username = username
        self.password = password
        self.jabatan = jabatan

    def login_menu(self):
        print('Silakan Pilih Jabatan Anda: ')
        print('1. Admin')
        print('2. Direktur SDM')
        print('3. Direktur')

    def admin_menu(self):
        print('Silakan Pilih Opsi Di Bawah Ini: ')
        print('1. Tambah/Edit Direktur SDM')
        print('2. Tambah/Edit Direktur')
        print('3. Keluar')
        
    def sdm_menu(self):
        print('Silakan Pilih Opsi Di Bawah Ini: ')
        print('1. Tambah/Edit Data') # ini bisa edit data pegawai atau gaji
        print('2. Lihat Pegawai') # ini bisa dari bulan atau divisi tapi udah terurut NIP
        print('3. Lihat Divisi') # sekalian tampilin Standar Gaji
        print('4. Lihat Pejabat Kantor')
        print('5. Hitung Total Gaji Yang Perlu Dibayar')
        print('6. Keluar')

    def direktur_menu(self):
        print('Silakan Pilih Opsi Di Bawah Ini: ')
        print('1. Lihat Pegawai')
        print('2. Lihat Pegawai Tertentu') # ini bisa dari bulan atau divisi
        print('3. Lihat Divisi') # tampilin Standar Gaji
        print('4. Lihat Pejabat Kantor')
        print('5. Hitung Total Gaji Yang Perlu Dibayar')
        print('6. Keluar')

    def verifikasi(self):
        if self.nama in self.jabatan['username'] and self.password in self.jabatan['password']:
            return True
        return False
    
class Admin(Aplikasi):
    def __init__(self, username, password, jabatan):
        super().__init__(username, password, jabatan)

    def main_program(self):
        Admin.admin_menu(self)
        opsi = int(input('Pilihan Kamu: '))

        if opsi == 1:
            self.tambah_data(self, direktur_sdm)
        elif opsi == 2:
            self.tambah_data(self, direktur)
        elif opsi == 3:
            return False
        
    def tambah_data(self, tujuan):
        tujuan['username'].append(input('Masukkan Nama Baru: '))
        tujuan['password'].append(input('Masukkan Password Baru :'))
        print('Data Telah Ditambahkan !')

    def edit_data(self, tujuan):
        username_cari = input('Masukkan Username Yang Ingin Di cari : ')
        password_cari = input('Masukkan Password Yang Ingin Di cari : ') 
        for index, username_tersimpan in enumerate(tujuan['username']):
            if username_cari == username_tersimpan:
                print('Data Ditemukan !')
                tujuan['username'][index] = input('Masukkan Username Baru : ')
                tujuan['password'][index] = input('Masukkan Password Baru : ')
                print('Data Berhasil Ditambahkan !')
            else:
                print('Data Tidak Ditemukan !')

class Sumberdaya(Aplikasi):
    def __init__(self, username, password, jabatan):
        super().__init__(username, password, jabatan)

    def main_program(self):
        Sumberdaya.sdm_menu()
        opsi = int(input('Masukkan pilihan kamu'))

        if opsi == 1:
            self.tampil_data()
            data = input('Pilih Data Yang Ingin Diganti : ') # isinya bisa gaji   
            if data == 'gaji':
                gaji_lama = input('Masukkan Nominal Yang Ingin Diganti : ')
                gaji_baru = input('Masukkan Nominal Gaji Yang Baru : ')
                self.edit_gaji(data, gaji_lama, gaji_baru)
            else:
                ganti = input('Pilih Pegawai Yang Ingin Diganti : ')
                self.edit_data(ganti, data)         

    def tampil_data(self):
        self.urut('nip')
        print('Data Pegawai: ') # ini buat lihat semua pegawai
        print("NIP\tNama\tGaji Pokok\tGaji Jam\tJabatan\tDivisi") 
        print("-------\t-------\t-------\t-------\t-------\t-------")
        for i in range(len(pegawai['nip'])):
            print(f"{pegawai['nip'][i]}\t{pegawai['nama'][i]}\t{pegawai['gaji']['pokok'][i]}\t{pegawai['gaji']['jam'][i]}\t{pegawai['jabatan'][i]}\t{pegawai['divisi'][i]}")
    
    def edit_data(self, tujuan, nama):
        if nama in pegawai['nama']: # udah urut NIP
            pegawai['nama'][nama] = input(f'Masukkan {nama} Yang Baru : ')
            print('Data Berhasil Ditambahkan !')
        else:
            print('Data Tidak Ditemukan')

    def edit_gaji(self, gaji, gaji_lama, gaji_baru):
        if gaji in pegawai['gaji']:
            for i, item in enumerate(pegawai['gaji'][gaji]):
                if item == gaji_lama:
                    pegawai['gaji'][gaji][i] = gaji_baru
        else:
            print('Data Tidak Ditemukan !')

    def urut(self, tipe):
        if tipe == 'nip':
            simpan_index = []
            sort_nip = []
            copy_nip = pegawai[tipe]
            for i in range(len(pegawai[tipe])):
                simpan_index.append(i)
            copy_nip.sorted(True)
            for j, item in enumerate(pegawai[tipe]):
                if item == copy_nip[j]:
                    sort_nip.append(j)
            for k,l in sort_nip, range(len(pegawai[tipe])):
                pegawai[tipe].append()