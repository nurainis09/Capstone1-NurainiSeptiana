# Capstone1-NurainiSeptiana
# Stockist AFC Cimehong: Sistem Manajemen Inventaris

Portofolio Capstone Module 1 Purwadhika Job Connector Data Science Batch 26

Selamat datang di **Sistem Manajemen Inventaris Stockist AFC Cimehong**. Sistem ini memungkinkan pengguna untuk mengelola data stok dengan efisien melalui fitur-fitur untuk menambah, memperbarui, menghapus, dan mencari item stok. Sistem ini mendukung dua peran pengguna, yaitu admin dan pengguna, masing-masing dengan akses yang berbeda.

## Fitur

### Fungsi Admin
- Melihat Daftar Stok
- Menambah Stok Baru
- Memperbarui Stok yang Ada
- Menghapus Stok
- Mencari Stok

### Fungsi Pengguna
- Melihat Daftar Stok
- Mencari Stok

  #### Sub Menu 1: Melihat Daftar Stock (Read)
  Sub Menu ini menampilkan daftar stock barang dengan format data koleksi berupa dictionary
  dengan deskripsi data sebagai berikut:
  - Kode barang (terdiri dari 3 kombinasi angka)
  - Nama Barang (str)
  - Jumlah masuk (int)
  - Jumlah keluar (int)
  - Jumlah update (int/merupakan pengurangan dari jumlah masuk dan jumlah keluar)
  - Tanggal Update (date time) -- secara otomatis tergenerate sesuai tanggal update

  #### Sub Menu 2 : Menambah Stock Baru (Create)
  Sub Menu ini berfungsi menambah stock baru (dengan nama baru dan kode barang auto-generate). Pada sub menu ini, tidak dimungkinkan menambahkan stock baru dengan nama yang sudah ada sebelumnnya. Jika menambah stock baru dengan yang sama, maka akan muncul notifikasi untuk dapat menggunakan fitur Update Stock (memperbarui nama stock yang sudah ada)

  #### Sub Menu 3 : Memperbarui Stock yang ada (Update)
  Sub Menu ini berfungsi memperbarui stock yang sudah terdaftar sebelumnya. Berfungsi memasukan jumlah masuk dan keluar yang akan mempengaruhi jumlah stock yang sudah ada sebelumnya. fitur ini memungkinkan untuk input Jumlah Masuk 0 maupun Jumlah Keluar 0 (salah 1 bisa bernilai 0).

  #### Sub Menu 4 : Menghapus Stock (Delete)
  Sub Menu ini berfungsi menghapus stock yang sudah terdaftar sebelumnya, dan memanggil stock berdasarkan kode barangnya.

  #### Sub Menu 5 : Mencari Stock (Search)
  Sub Menu ini berfungsi untuk mencari stock yang sudah terdaftar berdasarkan kode, nama, kategori dan tanggal update.

  #### Sub Menu 6 : Exiting Program (Exit)
  Sub Menu ini berfungsi untuk keluar dari program.




