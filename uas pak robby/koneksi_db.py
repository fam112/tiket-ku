import mysql.connector
from mysql.connector import Error

def connect_db():
    """
    Fungsi untuk membuat koneksi ke database MySQL.
    Mengembalikan objek koneksi jika berhasil, atau None jika gagal.
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',  # Ganti dengan IP/hostname server MySQL Anda
            database='nama_database_anda',  # Ganti dengan nama database MySQL Anda
            user='root',       # Ganti dengan username MySQL Anda
            password='password_anda' # Ganti dengan password MySQL Anda
        )
        if conn.is_connected():
            print("Koneksi ke database MySQL berhasil!")
            return conn
    except Error as e:
        print(f"Error saat koneksi ke MySQL: {e}")
        return None

if __name__ == '__main__':
    # Contoh penggunaan:
    connection = connect_db()
    if connection:
        # Lakukan operasi database di sini
        # Contoh: Buat kursor dan jalankan query sederhana
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT VERSION()")
            db_version = cursor.fetchone()
            print(f"Versi MySQL: {db_version}")
        except Error as err:
            print(f"Error saat menjalankan query: {err}")
        finally:
            cursor.close()
            connection.close()
            print("Koneksi database ditutup.")
    else:
        print("Gagal terhubung ke database.")