from main_pemesanantiket import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import sys
import os

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.row_count = 0

        #PELANGGAN
        self.ui.btn_simpan018.clicked.connect(self.add_to_table018)
        self.ui.btn_hapus018_2.clicked.connect(self.delete_data018)
        self.ui.tabelpelanggan018.cellClicked.connect(self.load_data_to_form018)
        self.ui.btn_edit018.clicked.connect(self.update_data018)
        
        #TRANSAKSI
        self.ui.btn_simpan012.clicked.connect(self.add_to_table012)
        self.ui.btn_hapus012.clicked.connect(self.delete_data012)
        self.ui.tabeltransaksi012.cellClicked.connect(self.load_data_to_form012)
        self.ui.btn_edit012.clicked.connect(self.update_data012)

        #TIKET
        self.ui.btn_simpan019.clicked.connect(self.add_to_table019)
        self.ui.btn_hapus019.clicked.connect(self.delete_data019)
        self.ui.tabeltiket019.cellClicked.connect(self.load_data_to_form019)
        self.ui.btn_edit019.clicked.connect(self.update_data019)

        self.setWindowTitle("Aplikasi Praktikum")
        self.ui.actionpelanggan.triggered.connect(lambda: self.switch_page(self.ui.page))
        self.ui.actiontransaksi.triggered.connect(lambda: self.switch_page(self.ui.page_2))
        self.ui.actiontiket.triggered.connect(lambda: self.switch_page(self.ui.page_3))

    def switch_page(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)

    def messagebox(self, title, message):
     QtWidgets.QMessageBox.warning(self, title, message)
    
    #PELANGGAN
    def add_to_table018(self):
        # "Menambahkan data ke tabel dari inputan teks"
        input_nama = self.ui.nama_txt018.text() 
        input_email = self.ui.email_txt018.text()
        input_noTelp = self.ui.noTelp_txt018.text()
        input_alamat = self.ui.alamat_txt018.text()
        input_tanggallahir = self.ui.tanggallahir_txt018.text()

        if input_nama and input_email: # Pastikan tidak kosong
            self.ui.tabelpelanggan018.insertRow(self.row_count)
            self.ui.tabelpelanggan018.setItem(self.row_count, 0, QtWidgets.QTableWidgetItem(input_nama))
            self.ui.tabelpelanggan018.setItem(self.row_count, 1, QtWidgets.QTableWidgetItem(input_email))
            self.ui.tabelpelanggan018.setItem(self.row_count, 2, QtWidgets.QTableWidgetItem(input_noTelp))
            self.ui.tabelpelanggan018.setItem(self.row_count, 3, QtWidgets.QTableWidgetItem(input_alamat))
            self.ui.tabelpelanggan018.setItem(self.row_count, 3, QtWidgets.QTableWidgetItem(input_tanggallahir))
            self.row_count += 1 # Tambah jumlah baris

            # Kosongkan inputan setelah ditambahkan
            self.ui.nama_txt018.clear()
            self.ui.email_txt018.clear()
            self.ui.noTelp_txt018.clear()
            self.ui.alamat_txt018.clear()
            self.ui.tanggallahir_txt018.clear()

    def delete_data018(self):
        selected_row = self.ui.tabelpelanggan018.currentRow()
        if selected_row >= 0:
            self.ui.tabelpelanggan018.removeRow(selected_row)
            self.row_count -= 1
        else:
            self.messagebox("Peringatan", "Pilih baris yang akan dihapus")
    
    def load_data_to_form018(self):
        selected_row = self.ui.tabelpelanggan018.currentRow()
        if selected_row >= 0:
            nama_item = self.ui.tabelpelanggan018.item(selected_row, 0)
            email_item = self.ui.tabelpelanggan018.item(selected_row, 1)
            noTelp_item = self.ui.tabelpelanggan018.item(selected_row, 2)
            alamat_item = self.ui.tabelpelanggan018.item(selected_row, 3)
            tanggallahir_item = self.ui.tabelpelanggan018.item(selected_row, 4)

            if nama_item and email_item and noTelp_item and alamat_item and tanggallahir_item:
                self.ui.nama_txt018.setText(nama_item.text())
                self.ui.email_txt018.setText(email_item.text())
                self.ui.noTelp_txt018.setText(noTelp_item.text())
                self.ui.alamat_txt018.setText(alamat_item.text())
                self.ui.tanggallahir_txt018.setText(tanggallahir_item.text())

    def update_data018(self):
        selected_row = self.ui.tabelpelanggan018.currentRow()
        if selected_row >= 0:
            nama = self.ui.nama_txt018.text()
            email = self.ui.email_txt018.text()
            noTelp = self.ui.noTelp_txt018.text()
            alamat = self.ui.alamat_txt018.text()
            tanggallahir = self.ui.tanggallahir_txt018.text()


            if nama and email:
                self.ui.tabelpelanggan018.setItem(selected_row, 0, QtWidgets.QTableWidgetItem(nama))
                self.ui.tabelpelanggan018.setItem(selected_row, 1, QtWidgets.QTableWidgetItem(email))
                self.ui.tabelpelanggan018.setItem(selected_row, 2, QtWidgets.QTableWidgetItem(noTelp))
                self.ui.tabelpelanggan018.setItem(selected_row, 3, QtWidgets.QTableWidgetItem(alamat))
                self.ui.tabelpelanggan018.setItem(selected_row, 3, QtWidgets.QTableWidgetItem(tanggallahir))

                # Kosongkan inputan setelah ditambahkan
                self.ui.nama_txt018.clear()
                self.ui.email_txt018.clear()
                self.ui.noTelp_txt018.clear()
                self.ui.alamat_txt018.clear()
                self.ui.tanggallahir_txt018.clear()
            else:
                self.messagebox("Peringatan", "Nama dan noTelp tidak boleh kosong.")
        else:
            self.messagebox("Peringatan", "Pilih baris yang ingin diupdate")

    #TRANSAKSI
    def add_to_table012(self):
        # "Menambahkan data ke tabel dari inputan teks"
        input_nama = self.ui.nama_txt012.text() 
        input_idbayar = self.ui.idbayar_txt012.text()
        input_noRek = self.ui.noRek_txt012.text()
        input_tanggal = self.ui.tanggal_txt012.text()
        input_pembelian = self.ui.pembelian_txt012.text()


        if input_nama and input_idbayar: # Pastikan tidak kosong
            self.ui.tabeltransaksi012.insertRow(self.row_count)
            self.ui.tabeltransaksi012.setItem(self.row_count, 0, QtWidgets.QTableWidgetItem(input_nama))
            self.ui.tabeltransaksi012.setItem(self.row_count, 1, QtWidgets.QTableWidgetItem(input_idbayar))
            self.ui.tabeltransaksi012.setItem(self.row_count, 2, QtWidgets.QTableWidgetItem(input_noRek))
            self.ui.tabeltransaksi012.setItem(self.row_count, 3, QtWidgets.QTableWidgetItem(input_tanggal))
            self.ui.tabeltransaksi012.setItem(self.row_count, 4, QtWidgets.QTableWidgetItem(input_pembelian))
            self.row_count += 1 # Tambah jumlah baris

            # Kosongkan inputan setelah ditambahkan
            self.ui.nama_txt012.clear()
            self.ui.idbayar_txt012.clear()
            self.ui.noRek_txt012.clear()
            self.ui.tanggal_txt012.clear()
            self.ui.pembelian_txt012.clear()

    def delete_data012(self):
        selected_row = self.ui.tabeltransaksi012.currentRow()
        if selected_row >= 0:
            self.ui.tabeltransaksi012.removeRow(selected_row)
            self.row_count -= 1
        else:
            self.messagebox("Peringatan", "Pilih baris yang akan dihapus")
    
    def load_data_to_form012(self):
        selected_row = self.ui.tabeltransaksi012.currentRow()
        if selected_row >= 0:
            nama_transaksi = self.ui.tabeltransaksi012.item(selected_row, 0)
            idbayar_transaksi = self.ui.tabeltransaksi012.item(selected_row, 1)
            noRek_transaksi = self.ui.tabeltransaksi012.item(selected_row, 2)
            tanggal_transaksi = self.ui.tabeltransaksi012.item(selected_row, 3)
            pembelian_transaksi = self.ui.tabeltransaksi012.item(selected_row, 4)

            if nama_transaksi and idbayar_transaksi and noRek_transaksi and tanggal_transaksi and pembelian_transaksi:
                self.ui.nama_txt012.setText(nama_transaksi.text())
                self.ui.idbayar_txt012.setText(idbayar_transaksi.text())
                self.ui.noRek_txt012.setText(noRek_transaksi.text())
                self.ui.tanggal_txt012.setText(tanggal_transaksi.text())
                self.ui.pembelian_txt012.setText(pembelian_transaksi.text())

    def update_data012(self):
        selected_row = self.ui.tabelpelanggan018.currentRow()
        if selected_row >= 0:
            nama = self.ui.nama_txt012.text()
            idbayar = self.ui.idbayar_txt012.text()
            noRek = self.ui.noRek_txt012.text()
            tanggal = self.ui.tanggal_txt012.text()
            pembelian = self.ui.pembelian_txt012.text()

            if nama and idbayar:
                self.ui.tabeltransaksi012.setItem(selected_row, 0, QtWidgets.QTableWidgetItem(nama))
                self.ui.tabeltransaksi012.setItem(selected_row, 1, QtWidgets.QTableWidgetItem(idbayar))
                self.ui.tabeltransaksi012.setItem(selected_row, 2, QtWidgets.QTableWidgetItem(noRek))
                self.ui.tabeltransaksi012.setItem(selected_row, 3, QtWidgets.QTableWidgetItem(tanggal))
                self.ui.tabeltransaksi012.setItem(selected_row, 4, QtWidgets.QTableWidgetItem(pembelian))
                
                # Kosongkan inputan setelah ditambahkan
                self.ui.nama_txt012.clear()
                self.ui.idbayar_txt012.clear()
                self.ui.noRek_txt012.clear()
                self.ui.tanggal_txt012.clear()
                self.ui.pembelian_txt012.clear()
            else:
                self.messagebox("Peringatan", "Nama dan noTelp tidak boleh kosong.")
        else:
            self.messagebox("Peringatan", "Pilih baris yang ingin diupdate")
            
    #TIKET
    def add_to_table019(self):
        # "Menambahkan data ke tabel dari inputan teks"
        input_namaevent = self.ui.namaevent_txt019.text() 
        input_jenisTiket = self.ui.jenistiket_txt019.text()
        input_alamatEvent = self.ui.alamatevent_txt019.text()
        input_idTiket = self.ui.idtiket_txt019.text()
        input_jammulai = self.ui.jammulai_txt019.text()

        if input_namaevent and input_idTiket: # Pastikan tidak kosong
            self.ui.tabeltiket019.insertRow(self.row_count)
            self.ui.tabeltiket019.setItem(self.row_count, 0, QtWidgets.QTableWidgetItem(input_namaevent))
            self.ui.tabeltiket019.setItem(self.row_count, 1, QtWidgets.QTableWidgetItem(input_jenisTiket))
            self.ui.tabeltiket019.setItem(self.row_count, 2, QtWidgets.QTableWidgetItem(input_alamatEvent))
            self.ui.tabeltiket019.setItem(self.row_count, 3, QtWidgets.QTableWidgetItem(input_idTiket))
            self.ui.tabeltiket019.setItem(self.row_count, 4, QtWidgets.QTableWidgetItem(input_jammulai))
            self.row_count += 1 # Tambah jumlah baris

            # Kosongkan inputan setelah ditambahkan
            self.ui.namaevent_txt019.clear()
            self.ui.jenistiket_txt019.clear()
            self.ui.alamatevent_txt019.clear()
            self.ui.idtiket_txt019.clear()
            self.ui.jammulai_txt019.clear()

    def delete_data019(self):
        selected_row = self.ui.tabeltiket019.currentRow()
        if selected_row >= 0:
            self.ui.tabeltiket019.removeRow(selected_row)
            self.row_count -= 1
        else:
            self.messagebox("Peringatan", "Pilih baris yang akan dihapus")
    
    def load_data_to_form019(self):
        selected_row = self.ui.tabeltiket019.currentRow()
        if selected_row >= 0:
            namaevent_item = self.ui.tabeltiket019.item(selected_row, 0)
            jenisTiket_item = self.ui.tabeltiket019.item(selected_row, 1)
            alamatEvent_item = self.ui.tabeltiket019.item(selected_row, 2)
            idTiket_item = self.ui.tabeltiket019.item(selected_row, 3)
            jammulai_item = self.ui.tabeltiket019.item(selected_row, 4)

            if namaevent_item and jenisTiket_item and alamatEvent_item and idTiket_item and jammulai_item:
                self.ui.namaevent_txt019.setText(namaevent_item.text())
                self.ui.jenistiket_txt019.setText(jenisTiket_item.text())
                self.ui.alamatevent_txt019.setText(alamatEvent_item.text())
                self.ui.idtiket_txt019.setText(idTiket_item.text())
                self.ui.jammulai_txt019.setText(jammulai_item.text())

    def update_data019(self):
        selected_row = self.ui.tabeltiket019.currentRow()
        if selected_row >= 0:
            namaevent = self.ui.namaevent_txt019.text()
            jenisTiket = self.ui.jenistiket_txt019.text()
            alamatEvent = self.ui.alamatevent_txt019.text()
            idTiket = self.ui.idtiket_txt019.text()
            jammulai = self.ui.jammulai_txt019.text()

            if namaevent and idTiket:
                self.ui.tabeltiket019.setItem(selected_row, 0, QtWidgets.QTableWidgetItem(namaevent))
                self.ui.tabeltiket019.setItem(selected_row, 1, QtWidgets.QTableWidgetItem(jenisTiket))
                self.ui.tabeltiket019.setItem(selected_row, 2, QtWidgets.QTableWidgetItem(alamatEvent))
                self.ui.tabeltiket019.setItem(selected_row, 3, QtWidgets.QTableWidgetItem(idTiket))
                self.ui.tabeltiket019.setItem(selected_row, 4, QtWidgets.QTableWidgetItem(jammulai))

                # Kosongkan inputan setelah ditambahkan
                self.ui.namaevent_txt019.clear()
                self.ui.jenistiket_txt019.clear()
                self.ui.alamatevent_txt019.clear()
                self.ui.idtiket_txt019.clear()
                self.ui.jammulai_txt019.clear()
            else:
                self.messagebox("Peringatan", "Nama dan ID Tiket tidak boleh kosong.")
        else:
            self.messagebox("Peringatan", "Pilih baris yang ingin diupdate")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.showMaximized()
    sys.exit(app.exec_())
