import os
import json

# Nama file untuk menyimpan daftar film
FILE_NAME = 'films.json'

# Fungsi untuk memuat daftar film dari file
def load_films():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan daftar film ke file
def save_films(films):
    with open(FILE_NAME, 'w') as file:
        json.dump(films, file, indent=4)

# Fungsi untuk menampilkan film
def display_film(film, index=None):
    status = "Selesai" if film['selesai'] else "Belum Selesai"
    fav = " (Favorit)" if film['favorit'] else ""
    if index:
        print(f"{index}. {film['nama']} - Rating: {film['rating']}/10 - {status}{fav}")
        print(f"   Genre: {film['genre']}")
        print(f"   Ulasan: {film['ulasan']}")
        print(f"   Rekomendasi: {film['rekomendasi']}")
    else:
        print(f"Nama: {film['nama']}")
        print(f"Rating: {film['rating']}/10")
        print(f"Status: {status}")
        print(f"Favorit: {'Ya' if film['favorit'] else 'Tidak'}")
        print(f"Genre: {film['genre']}")
        print(f"Ulasan: {film['ulasan']}")
        print(f"Rekomendasi: {film['rekomendasi']}")

# Fungsi utama aplikasi
def main():
    films = load_films()
    while True:
        print("\n=== Aplikasi Catatan Film Ditonton ===")
        print("1. Tambah film")
        print("2. Lihat daftar film")
        print("3. Edit film")
        print("4. Hapus film")
        print("5. Keluar")
        choice = input("Pilih opsi (1-5): ").strip()

        if choice == '1':
            nama = input("Masukkan nama film: ").strip()
            if not nama:
                print("Nama film tidak boleh kosong.")
                continue
            try:
                rating = int(input("Masukkan rating (1-10): ").strip())
                if not 1 <= rating <= 10:
                    print("Rating harus antara 1-10.")
                    continue
            except ValueError:
                print("Rating harus angka.")
                continue
            ulasan = input("Masukkan ulasan: ").strip()
            selesai = input("Sudah selesai ditonton? (y/n): ").strip().lower() == 'y'
            favorit = input("Apakah favorit? (y/n): ").strip().lower() == 'y'
            genre = input("Masukkan genre: ").strip()
            rekomendasi = input("Rekomendasi film lain: ").strip()

            film = {
                'nama': nama,
                'rating': rating,
                'ulasan': ulasan,
                'selesai': selesai,
                'favorit': favorit,
                'genre': genre,
                'rekomendasi': rekomendasi
            }
            films.append(film)
            save_films(films)
            print(f"Film '{nama}' berhasil ditambahkan.")

        elif choice == '2':
            if films:
                print("\nDaftar film yang sudah dicatat:")
                for i, film in enumerate(films, 1):
                    display_film(film, i)
            else:
                print("Belum ada film yang dicatat.")

        elif choice == '3':
            if films:
                print("\nDaftar film:")
                for i, film in enumerate(films, 1):
                    print(f"{i}. {film['nama']}")
                try:
                    index = int(input("Masukkan nomor film yang ingin diedit: ")) - 1
                    if 0 <= index < len(films):
                        film = films[index]
                        print("Biarkan kosong untuk tidak mengubah.")
                        nama = input(f"Nama ({film['nama']}): ").strip() or film['nama']
                        try:
                            rating_str = input(f"Rating ({film['rating']}): ").strip()
                            rating = int(rating_str) if rating_str else film['rating']
                            if rating_str and not 1 <= rating <= 10:
                                print("Rating harus antara 1-10.")
                                continue
                        except ValueError:
                            print("Rating harus angka.")
                            continue
                        ulasan = input(f"Ulasan ({film['ulasan']}): ").strip() or film['ulasan']
                        selesai_str = input(f"Selesai (y/n) ({'y' if film['selesai'] else 'n'}): ").strip().lower()
                        selesai = selesai_str == 'y' if selesai_str else film['selesai']
                        favorit_str = input(f"Favorit (y/n) ({'y' if film['favorit'] else 'n'}): ").strip().lower()
                        favorit = favorit_str == 'y' if favorit_str else film['favorit']
                        genre = input(f"Genre ({film['genre']}): ").strip() or film['genre']
                        rekomendasi = input(f"Rekomendasi ({film['rekomendasi']}): ").strip() or film['rekomendasi']

                        film.update({
                            'nama': nama,
                            'rating': rating,
                            'ulasan': ulasan,
                            'selesai': selesai,
                            'favorit': favorit,
                            'genre': genre,
                            'rekomendasi': rekomendasi
                        })
                        save_films(films)
                        print(f"Film '{nama}' berhasil diedit.")
                    else:
                        print("Nomor tidak valid.")
                except ValueError:
                    print("Masukkan nomor yang valid.")
            else:
                print("Belum ada film yang dicatat.")

        elif choice == '4':
            if films:
                print("\nDaftar film:")
                for i, film in enumerate(films, 1):
                    print(f"{i}. {film['nama']}")
                try:
                    index = int(input("Masukkan nomor film yang ingin dihapus: ")) - 1
                    if 0 <= index < len(films):
                        removed = films.pop(index)
                        save_films(films)
                        print(f"Film '{removed['nama']}' berhasil dihapus.")
                    else:
                        print("Nomor tidak valid.")
                except ValueError:
                    print("Masukkan nomor yang valid.")
            else:
                print("Belum ada film yang dicatat.")

        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
