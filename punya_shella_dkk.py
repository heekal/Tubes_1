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
    'nip' : [110322300, 1103223001, 1003223000],
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
        print('2. Lihat Semua Pegawai')
        print('3. Lihat Pegawai Tertentu') # ini bisa dari bulan atau divisi
        print('4. Lihat Divisi') # tampilin Standar Gaji
        print('5. Lihat Pejabat Kantor')
        print('6. Hitung Total Gaji Yang Perlu Dibayar')
        print('7. Keluar')

    def direktur_menu(self):
        print('Silakan Pilih Opsi Di Bawah Ini: ')
        print('1. Lihat Semua Pegawai')
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

    def main_menu(self):
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
        password_cari = input('Masukkan Password Baru : ')
        if username_cari in tujuan['username'] and password_cari in tujuan['password']:
            