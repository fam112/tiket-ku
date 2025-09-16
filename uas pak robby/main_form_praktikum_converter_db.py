from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QTableWidgetItem
from desain_form_praktikum import Ui_MainWindow
from koneksi_db import connect_db
import sys

class Mainform(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.setWindowTitle("Aplikasi pembelian Tiket")

        self.ui.actionpelanggan.triggered.connect(lambda: self.switch_page(self.ui.page))
        self.ui.actiontransaksi.triggered.connect(lambda: self.switch_page(self.ui.page 2))
        self.ui.actiontiket.triggered.connect(lambda: self.switch_page(self.ui.page 3))
        self.ui.btn_simpan018.clicked.connect(self.add_to_table018)
        self.ui.btn_hapus018_2.clicked.connect(self.delete_data018)
        self.ui.tabelpelanggan018.cellClicked.connect(self.load_data_to_form018)
        self.ui.btn_edit018.clicked.connect(self.update_data018)

        self.load_data_from_db()
    
    def switch_page(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)

    def load_data_from_db(self):
        self.ui.tabelpelanggan018.setRowCount(0)
        conn = connect_db()
        cursor = conn.cursor()    
        cursor.execute("SELECT id_siswa, nama_siswa, alamat_siswa, telp_siswa FROM siswa")
        rows = cursor.fetchall()   
        for row_data in rows:
            row_number = self.ui.tabelpelanggan018.rowCount()
            self.ui.tabelpelanggan018.insertRow(row_number)
            for column, data in enumerate(row_data[1:]):
                self.ui.tabelpelanggan018.setItem(row_number, column, QTableWidgetItem(str(data)))
            self.ui.tabelpelanggan018.setVerticalHeaderItem(row_number, QTableWidgetItem(str(row_data[0])))     
        cursor.close()
        conn.close()

    def add_to_table018(self):
        nama = self.ui.nama_txt018.text()
        email = self.ui.alamat_txt018.text()
        noTelp = self.ui.noTelp_txt018.text()

        if nama and email:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO siswa (nama_siswa, alamat_siswa, telp_siswa) VALUES (%s, %s, %s)",
                           (nama, email, noTelp))
            conn.commit()
            cursor.close()
            conn.close()

            self.load_data_from_db()
            self.ui.nama_txt018.clear()
            self.ui.email_txt018.clear()
            self.ui.noTelp_txt018.clear()
        else:
            self.messagebox("Peringatan", "Nama dan Email tidak boleh kosong.")

    def load_data_to_form018(self):
        selected_row = self.ui.tabelpelanggan018.currentRow()
        if selected_row >= 0:
            nama = self.ui.tabelpelanggan018.item(selected_row, 0).text()
            email = self.ui.tabelpelanggan018.item(selected_row, 1).text()
            noTelp = self.ui.tabelpelanggan018.item(selected_row, 2).text()
            self.ui.nama_txt018.setText(nama)
            self.ui.email_txt018.setText(email)
            self.ui.noTelp_txt018.setText(noTelp)

    def update_data018(self):
        selected_row = self.ui.tabelsiswa.currentRow()
        if selected_row >= 0:
            id_siswa = int(self.ui.tabelsiswa.verticalHeaderItem(selected_row).text())
            nama = self.ui.nama_text.text()
            alamat = self.ui.alamat_txt.toPlainText()
            telp = self.ui.telp_txt.text()

            if nama and alamat:
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute("UPDATE siswa SET nama_siswa=%s, alamat_siswa=%s, telp_siswa=%s WHERE id_siswa=%s",
                               (nama, alamat, telp, id_siswa))
                conn.commit()
                cursor.close()
                conn.close()
                self.load_data_from_db()
                self.ui.nama_text.clear()
                self.ui.alamat_txt.clear()
                self.ui.telp_txt.clear()
            else:
                self.messagebox("Peringatan", "Nama dan Alamat tidak boleh kosong.")
        else:
            self.messagebox("Peringatan", "Pilih baris yang ingin diupdate.")

    def delete_data018(self):
        selected_row = self.ui.tabelsiswa.currentRow()
        if selected_row >= 0:
            id_siswa = int(self.ui.tabelsiswa.verticalHeaderItem(selected_row).text())
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM siswa WHERE id_siswa=%s", (id_siswa,))
            conn.commit()
            cursor.close()
            conn.close()
            self.load_data_from_db()
        else:
            self.messagebox("Peringatan", "Pilih baris yang ingin dihapus.")

    def messagebox(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())







