users_db ={
    'admin': 'password123',
    'user1': 'mypassword'
}

# simulasi database
stock_db = {
    '001' : {'Nama': 'Utsukushii', 'Jumlah Masuk': 1600, 'Jumlah Keluar': 80, 'Jumlah Update': 1520, 'Kategori': 'MAX', 'Tgl Update': '12-09-2024' },
    '002' : {'Nama': 'Subarashi', 'Jumlah Masuk': 600, 'Jumlah Keluar': 80, 'Jumlah Update': 520, 'Kategori': 'MED', 'Tgl Update': '12-09-2024' },
    '003' : {'Nama': 'Sensei Suru', 'Jumlah Masuk': 100, 'Jumlah Keluar': 15,'Jumlah Update': 85, 'Kategori': 'MIN', 'Tgl Update': '12-09-2024'},
    '004' : {'Nama': 'Hikari', 'Jumlah Masuk': 600, 'Jumlah Keluar': 100,'Jumlah Update': 500, 'Kategori': 'MED', 'Tgl Update': '12-09-2024'},
    '010' : {'Nama': 'Mejiku', 'Jumlah Masuk': 580, 'Jumlah Keluar': 80,'Jumlah Update': 500, 'Kategori': 'MED', 'Tgl Update': '12-09-2024'},
    '011' : {'Nama': 'Hanamai','Jumlah Masuk': 1550, 'Jumlah Keluar': 30, 'Jumlah Update': 1520, 'Kategori': 'MAX', 'Tgl Update': '12-09-2024' },
    '022' : {'Nama': 'Kose', 'Jumlah Masuk': 700, 'Jumlah Keluar': 180, 'Jumlah Update': 520, 'Kategori': 'MED', 'Tgl Update': '12-09-2024' },
    '023' : {'Nama': 'Kanebo', 'Jumlah Masuk': 100, 'Jumlah Keluar': 15, 'Jumlah Update': 85, 'Kategori': 'MIN', 'Tgl Update': '12-09-2024'},
    '030' : {'Nama': 'Utsukushii Gold', 'Jumlah Masuk': 1600, 'Jumlah Keluar': 1100, 'Jumlah Update': 500, 'Kategori': 'MED', 'Tgl Update': '12-09-2024'},
    '040' : {'Nama': 'Shu Uemura', 'Jumlah Masuk': 600, 'Jumlah Keluar': 100, 'Jumlah Update': 500, 'Kategori': 'MED', 'Tgl Update': '12-09-2024'}
    }

def admin_login():
    print('\n**Welcome to Stockist AFC Cimehong**')
    print('------------------------------------')
    print('Admin Login')
    username = input('Username: ')
    password = input('Password: ')

    if users_db.get(username) == password:
        return True, username
    else:
        print('Login Failed. Please try again or exit')
        return False, None
    
def user_login():
    print('\n**Welcome to Stockist AFC Cimehong**')
    print('------------------------------------')
    print('User Login')
    username = input('Username: ')
    password = input('Password: ')

    if users_db.get(username) == password:
        return True, username
    else:
        print('Login Failed. Please try again or exit')
        return False, None
    
def main_menu_admin():
    print('\n--------------------------------')
    print("Stockist AFC Cimehong Main Menu")
    print('--------------------------------')
    print("1. Lihat Daftar Stock")
    print("2. Add New Stock")
    print("3. Update Stock")
    print("4. Delete Stock")
    print("5. Search Stock")
    print("6. Exit Program")

def main_menu_user():
    print('\n--------------------------------')
    print("Stockist AFC Cimehong Main Menu")
    print('--------------------------------')
    print("1. Lihat Daftar Stock")
    print("2. Search Stock")
    print("3. Exit Program")

def get_category_by_quantity(jumlah_update):
    """ Menentukan kategori berdasarkan jumlah barang """
    if jumlah_update > 1000:
        return 'MAX'
    elif jumlah_update >= 100:
        return 'MED'
    else:
        return 'MIN'


def jumlahUpdate(code):
    if code in stock_db:
        item = stock_db[code]
        Jumlah_update = item['Jumlah Masuk'] - item['Jumlah Keluar']
        return Jumlah_update
    else:
        print(f"Kode barang '{code}' tidak ditemukan.")
        return None

from datetime import datetime

def displayStock():
    print('\nDaftar Stock:')
    
    # Cetak header dengan lebar kolom yang sesuai
    print(f'{"Code":<10} {"Nama":<20} {"Jumlah Masuk":<15} {"Jumlah Keluar":<15} {"Jumlah Update":<15} {"Kategori":<15} {"Tgl Update":<10}')
    print('-' * 110)  # Garis pembatas untuk header
    
    # Cetak data stok
    for code, item in stock_db.items():
        print(f'{code:<10} {item["Nama"]:<20} {item["Jumlah Masuk"]:<15} {item["Jumlah Keluar"]:<15} {item["Jumlah Update"]:<15} {item["Kategori"]:<15} {item["Tgl Update"]:<10}')
from datetime import datetime

def addNewStock():
    ulangi = True
    while ulangi:
        last_code = max(stock_db.keys(), default='000')  # Mendapatkan kode terakhir, default '000' jika kosong
        code = str(int(last_code) + 1).zfill(3)  # Increment dan format menjadi 3 digit
        print(f'\nCode: {code}')

        Nama = input('Masukkan Nama Barang: ').strip()
        Nama_normalized = Nama.replace(" ", "").lower()
    
        # Cek jika nama sudah ada di database
        if any(item['Nama'].replace(" ", "").lower() == Nama_normalized for item in stock_db.values()):
            print('Nama Stock sudah terdaftar. Mohon pilih Update Stock saja pada stock dimaksud.')
            ulangi = False
            return
        
        # Input dan validasi jumlah masuk
        while True:
            try:
                Jumlah_masuk_input = input('Masukkan Jumlah Masuk (angka, kosongkan jika tidak ada): ').strip()
                Jumlah_masuk = int(Jumlah_masuk_input) if Jumlah_masuk_input else 0
                break
            except ValueError:
                print('Masukkan jumlah dalam angka saja.')
        
        # Input dan validasi jumlah keluar
        while True:
            try:
                Jumlah_keluar_input = input('Masukkan Jumlah Keluar (angka, kosongkan jika tidak ada): ').strip()
                Jumlah_keluar = int(Jumlah_keluar_input) if Jumlah_keluar_input else 0
                if Jumlah_keluar > Jumlah_masuk:
                    print('Jumlah Keluar tidak boleh lebih besar dari Jumlah Masuk.')
                    continue
                break
            except ValueError:
                print('Masukkan jumlah dalam angka saja.')
        
        # Hitung Jumlah Update
        Jumlah_update = Jumlah_masuk - Jumlah_keluar
        Kategori = get_category_by_quantity(Jumlah_update)
        tanggal_update = datetime.now().strftime('%d-%m-%Y')
        
        # Tampilkan data yang akan disimpan dan konfirmasi
        while True:
            print('\nData yang akan disimpan:')
            print(f'\n{"Code":<10} {"Nama":<20} {"Jumlah Masuk":<15} {"Jumlah Keluar":<15} {"Jumlah Update":<15} {"Kategori":<15} {"Tgl Update":<10}')
            print('-' * 110)
            print(f'{code:<10} {Nama:<20} {Jumlah_masuk:<15} {Jumlah_keluar:<15} {Jumlah_update:<15} {Kategori:<15} {tanggal_update:<10}')
            konfirmasi = input('\nApakah Anda ingin menyimpan data ini? (ya/tidak): ').strip().lower()
        
            if konfirmasi == 'ya':
                stock_db[code] = {'Nama': Nama, 'Jumlah Masuk': Jumlah_masuk, 'Jumlah Keluar': Jumlah_keluar, 'Jumlah Update': Jumlah_update, 'Kategori': Kategori, 'Tgl Update': tanggal_update}
                print('New Stock Berhasil ditambahkan.')
                displayStock()
                ulangi = False
                return
            elif konfirmasi == 'tidak':
                while True: 
                    pilihan = input("\nData tidak disimpan. Ketik 'exit' untuk kembali ke Main Menu atau tekan Enter untuk ulangi pengisian: ").strip().lower()
                    if pilihan == '':
                        addNewStock()
                    elif pilihan == 'exit':
                        return
                    else:
                        print("Pilihan tidak valid. Harap masukan 'exit' untuk ke Main Menu atau tekan Enter untuk ulangi pengisian: ")
                        continue
            else:
                print("Pilihan tidak valid. Harap masukan 'ya' atau 'tidak'.")
    
def updateStock():
    displayStock()  # Memanggil display untuk memudahkan admin memasukkan kode barang yang ingin diupdate
    ulangi = True
    while ulangi:
        code = input('Masukkan Kode barang yang ingin diupdate (3 digit angka): ')
        if code in stock_db:
            # Ambil data stock yang ada
            stock_data = stock_db[code]
            Nama = stock_data['Nama']
            Jumlah_masuk_sekarang = stock_data.get('Jumlah Masuk', 0)
            Jumlah_keluar_sekarang = stock_data.get('Jumlah Keluar', 0)

            while True:
                try:
                    Jumlah_masuk_input = input('Masukkan jumlah masuk stok (angka, kosongkan jika tidak ada): ').strip()
                    Jumlah_masuk = int(Jumlah_masuk_input) if Jumlah_masuk_input else 0
                    Jumlah_keluar_input = input('Masukkan jumlah keluar stok (angka, kosongkan jika tidak ada): ').strip()
                    Jumlah_keluar = int(Jumlah_keluar_input) if Jumlah_keluar_input else 0

                    # Update jumlah masuk dan keluar
                    Jumlah_masuk_total = Jumlah_masuk_sekarang + Jumlah_masuk
                    Jumlah_keluar_total = Jumlah_keluar_sekarang + Jumlah_keluar
                    Jumlah_update = Jumlah_masuk_total - Jumlah_keluar_total

                    break  # Keluar dari loop jika input valid
                except ValueError:
                    print('Masukkan jumlah dalam angka saja.')

            Kategori = get_category_by_quantity(Jumlah_update)
            tanggal_update = datetime.now().strftime('%d-%m-%Y')

            while True:
                print('\nData yang akan disimpan:')
                print(f'\n{"Code":<10} {"Nama":<20} {"Jumlah Masuk":<15} {"Jumlah Keluar":<15} {"Jumlah Update":<15} {"Kategori":<15} {"Tgl Update":<10}')
                print('-' * 110)
                print(f'{code:<10} {Nama:<20} {Jumlah_masuk_total:<15} {Jumlah_keluar_total:<15} {Jumlah_update:<15} {Kategori:<15} {tanggal_update:<10}')

                konfirmasi = input('\nApakah Anda ingin menyimpan data ini? (ya/tidak): ').strip().lower()

                if konfirmasi == 'ya':
                    # Simpan data yang diperbarui ke database
                    stock_db[code] = {
                        'Nama': Nama,
                        'Jumlah Masuk': Jumlah_masuk_total,
                        'Jumlah Keluar': Jumlah_keluar_total,
                        'Jumlah Update': Jumlah_update,
                        'Kategori': Kategori,
                        'Tgl Update': tanggal_update
                    }
                    print('Update stock berhasil.')
                    displayStock()
                    ulangi = False
                    return
                elif konfirmasi == 'tidak':
                    while True:
                        pilihan = input("\nData tidak disimpan. Ketik 'exit' untuk kembali ke Main Menu atau tekan Enter untuk ulangi pengisian: ").strip().lower()
                        if pilihan == '':
                            updateStock()
                        elif pilihan == 'exit':
                            return
                        else:
                            print("Pilihan tidak valid. Harap masukkan 'exit' untuk ke Main Menu atau tekan Enter untuk ulangi pengisian: ")
                            continue
                else:
                    print("Pilihan tidak valid. Harap masukkan 'ya' atau 'tidak'.")
        else:
            pilihan = input('Kode barang tidak ditemukan. Tekan enter untuk memasukkan kembali kode yang sesuai, atau ketik "exit" untuk Main Menu: ').strip().lower()
            if pilihan == '':
                continue
            elif pilihan == 'exit':
                return
            else:
                print("Pilihan tidak valid. Harap masukkan 'exit' untuk Main Menu atau tekan Enter untuk ulangi pengisian: ")

                    
def removeStock():
    displayStock()
    Ulangi = True
    while True:
        code = input('\nMasukan kode barang yang akan dihapus: ')
        if code in stock_db:
            item = stock_db[code]
            print('\nData yang akan dihapus:')
            print(f'Kode Barang: {code}')
            print(f'Nama Barang: {item["Nama"]}')
            print(f'Jumlah Masuk: {item["Jumlah Masuk"]}')
            print(f'Jumlah Keluar: {item["Jumlah Keluar"]}')
            print(f'Jumlah Update: {item["Jumlah Update"]}')
            print(f'Kategori: {item["Kategori"]}')
            print(f'Tgl Update: {item["Tgl Update"]}')

            while True:
                konfirmasi = input('\n Apakah Anda yakin akan menghapus barang ini? (ya/tidak): ').strip().lower()
                if konfirmasi.lower() == 'ya':
                    del stock_db[code]
                    print('Barang berhasil dihapus')
                    displayStock()
                    return
                elif konfirmasi.lower() == 'tidak':
                    print('Batal Hapus') 
                    ulangi = False
                    return
                else:
                    print("Invalid. Mohon konfirmasi 'ya' atau 'tidak' untuk menghapus barang dimaksud.")
                    continue


        else:
            pilihan = input ("Kode barang tidak ditemukan. Tekan enter untuk memasukan kode barang yang sesuai atau ketik 'exit' untuk kembali ke Main Menu: ").strip().lower()
            if pilihan.lower() == 'exit':
                return
            elif pilihan =='':
                continue
            else:
                print("Pilihan tidak valid. Harap tekan Enter untuk memasukan ulang kode barang atau ketik 'exit' untuk kembali ke Main Menu.")     

def searchByName():
    nama = input('Masukkan Nama Barang: ').strip().lower()
    found = False
    count = 0
    
    print(f'\n{"Code":<10} {"Nama":<20} {"Jumlah Masuk":<15} {"Jumlah Keluar":<15} {"Jumlah Update":<15} {"Kategori":<15} {"Tgl Update":<10}')
    print('-' * 110)

    for code, item in stock_db.items():
        item_name_normalized = item['Nama'].replace(" ", "").lower()
        if nama in item_name_normalized:
            print(f'{code:<10} {item["Nama"]:<20} {item["Jumlah Masuk"]:<15} {item["Jumlah Keluar"]:<15} {item["Jumlah Update"]:<15} {item["Kategori"]:<15} {item["Tgl Update"]:<10}')
            found = True
            count += 1

    if found:
        print(f'\nJumlah pencarian ditemukan: {count}')
    else:
        print("Nama barang tidak ditemukan.")

def searchByCode():
    search_code = input('Masukkan Kode Barang: ').strip()
    found = False
    count = 0
    print(f'\n{"Code":<10} {"Nama":<20} {"Jumlah Masuk":<15} {"Jumlah Keluar":<15} {"Jumlah Update":<15} {"Kategori":<15} {"Tgl Update":<10}')
    print('-' * 110)

    for code, item in stock_db.items():
        if search_code in code:
            print(f'{code:<10} {item["Nama"]:<20} {item["Jumlah Masuk"]:<15} {item["Jumlah Keluar"]:<15} {item["Jumlah Update"]:<15} {item["Kategori"]:<15} {item["Tgl Update"]:<10}')
            found = True
            count += 1

    if found:
        print(f'\nJumlah pencarian ditemukan: {count}')
    else:
        print("Kode barang tidak ditemukan.")

def searchByCategory():
    kategori = input('Masukkan Kategori: ').strip().upper()
    found = False
    count = 0
    print(f'\n{"Code":<10} {"Nama":<20} {"Jumlah Masuk":<15} {"Jumlah Keluar":<15} {"Jumlah Update":<15} {"Kategori":<15} {"Tgl Update":<10}')
    print('-' * 110)

    for code, item in stock_db.items():
        if item['Kategori'] == kategori:
            print(f'{code:<10} {item["Nama"]:<20} {item["Jumlah Masuk"]:<15} {item["Jumlah Keluar"]:<15} {item["Jumlah Update"]:<15} {item["Kategori"]:<15} {item["Tgl Update"]:<10}')
            found = True
            count += 1

    if found:
        print(f'\nJumlah pencarian ditemukan: {count}')
    else:
        print("Kategori tidak ditemukan.")

from datetime import datetime

def searchByTanggalUpdate():
    tanggal_update = input('Masukkan Tanggal Update (format dd-mm-yyyy): ').strip()
    
    # Validasi format tanggal
    try:
        datetime.strptime(tanggal_update, '%d-%m-%Y')
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format dd-mm-yyyy.")
        return
    
    found = False
    count = 0
    print(f'\n{"Code":<10} {"Nama":<20} {"Jumlah Masuk":<15} {"Jumlah Keluar":<15} {"Jumlah Update":<15} {"Kategori":<15} {"Tgl Update":<10}')
    print('-' * 110)

    for code, item in stock_db.items():
        if item['Tgl Update'] == tanggal_update:
            print(f'{code:<10} {item["Nama"]:<20} {item["Jumlah Masuk"]:<15} {item["Jumlah Keluar"]:<15} {item["Jumlah Update"]:<15} {item["Kategori"]:<15} {item["Tgl Update"]:<10}')
            found = True
            count += 1

    if found:
        print(f'\nJumlah pencarian ditemukan: {count}')
    else:
        print("Tanggal update tidak ditemukan.")

def searchStock():
    while True:
        print('\nPencarian Stock')
        print('---------------')
        print('1. Cari berdasarkan Kode Barang')
        print('2. Cari berdasarkan Nama Barang')
        print('3. Cari berdasarkan Kategori')
        print('4. Cari berdasarkan Tanggal Update')  # Opsi baru
        print('5. Kembali ke Main Menu')
        
        choice = input('Pilih opsi pencarian: ').strip()
        
        if choice == '1':
            searchByCode()
        elif choice == '2':
            searchByName()
        elif choice == '3':
            searchByCategory()
        elif choice == '4':
            searchByTanggalUpdate()  # Panggil fungsi pencarian berdasarkan tanggal update
        elif choice == '5':
            return  # Kembali ke menu utama
        else:
            print('Pilihan tidak valid. Silahkan masukkan opsi pencarian yang valid.')

def main():
    while True:
        login_successful, username = admin_login()  # Ubah menjadi admin_login atau user_login sesuai kebutuhan
        if login_successful:
            if username == 'admin':
                while True:
                    main_menu_admin()
                    choice = input("Pilih menu: ")

                    if choice == '1':
                        displayStock()
                    elif choice == '2':
                        addNewStock()
                    elif choice == '3':
                        updateStock()
                    elif choice == '4':
                        removeStock()
                    elif choice == '5':
                        searchStock()
                    elif choice == '6':
                        print("Exiting program. Thankyou.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                while True:
                    main_menu_user()
                    choice = input("Pilih menu: ")

                    if choice == '1':
                        displayStock()
                    elif choice == '2':
                        searchStock()
                    elif choice == '3':
                        print("Exiting program. Thankyou.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        else:
            action = input("Enter 'exit' to quit or press Enter to retry: ")
            if action.lower() == 'exit':
                print("Exiting program. Thankyou")
                break

if __name__ == "__main__":
    main()