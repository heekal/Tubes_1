# Admin
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


class Aplikasi:
    def __init__(self, nama, password, jabatan):
        self.nama = nama
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
        
    def sdm_menu(self):
        print('Silakan Pilih Opsi Di Bawah Ini: ')
        print('1. Tambah/Edit Pegawai')
        print('2. Tambah/Edit Gaji Pokok dan Gaji Per Jam')
        print('3. ')