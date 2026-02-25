import os
import json
import random

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

# Fungsi untuk menampilkan film dengan hiasan
def display_film(film, index=None):
    status = "✅ Selesai" if film['selesai'] else "⏳ Belum Selesai"
    fav = " ❤️ (Favorit)" if film['favorit'] else ""
    stars = "⭐" * (film['rating'] // 2) + "☆" * (film['rating'] % 2)
    if index:
        print(f"{index}. 🎥 {film['nama']} - Rating: {stars} ({film['rating']}/10) - {status}{fav}")
        print(f"   📅 Ditonton: {film.get('tanggal', 'Tidak diketahui')}")
        print(f"   🎭 Genre: {film['genre']}")
        print(f"   💬 Ulasan: {film['ulasan']}")
        print(f"   🎯 Rekomendasi: {film['rekomendasi']}")
    else:
        print(f"🎥 Nama: {film['nama']}")
        print(f"⭐ Rating: {stars} ({film['rating']}/10)")
        print(f"📊 Status: {status}")
        print(f"❤️ Favorit: {'Ya' if film['favorit'] else 'Tidak'}")
        print(f"📅 Ditonton: {film.get('tanggal', 'Tidak diketahui')}")
        print(f"🎭 Genre: {film['genre']}")
        print(f"💬 Ulasan: {film['ulasan']}")
        print(f"🎯 Rekomendasi: {film['rekomendasi']}")

# Fungsi untuk menghasilkan rekomendasi otomatis berdasarkan genre
def generate_recommendation(films, genre, current_name):
    similar_films = [f for f in films if f['genre'].lower() == genre.lower() and f['rating'] >= 7 and f['nama'].lower() != current_name.lower()]
    if similar_films:
        rec = random.choice(similar_films)
        return f"Berdasarkan genre '{genre}', coba '{rec['nama']}' (Rating: {rec['rating']}/10) - film serupa yang belum ditonton."
    return "Belum ada film serupa dengan rating tinggi yang belum ditonton."

# Fungsi untuk statistik
def show_statistics(films):
    if not films:
        print("📊 Belum ada data film.")
        return
    total = len(films)
    avg_rating = sum(f['rating'] for f in films) / total
    completed = sum(1 for f in films if f['selesai'])
    favorites = sum(1 for f in films if f['favorit'])
    genres = {}
    for f in films:
        genres[f['genre']] = genres.get(f['genre'], 0) + 1
    top_genre = max(genres, key=genres.get) if genres else "Tidak ada"
    print("📊 === Statistik Film ===")
    print(f"🎬 Total Film: {total}")
    print(f"⭐ Rata-rata Rating: {avg_rating:.1f}/10")
    print(f"✅ Film Selesai: {completed}")
    print(f"❤️ Film Favorit: {favorites}")
    print(f"🎭 Genre Terbanyak: {top_genre}")

# Fungsi untuk cari berdasarkan genre
def search_by_genre(films, genre):
    results = [f for f in films if genre.lower() in f['genre'].lower()]
    if results:
        print(f"🔍 Film dengan genre '{genre}':")
        for i, film in enumerate(results, 1):
            display_film(film, i)
    else:
        print(f"❌ Tidak ada film dengan genre '{genre}'.")

# Fungsi untuk filter film
def filter_films(films, filter_type):
    if filter_type == 'favorit':
        results = [f for f in films if f['favorit']]
        title = "❤️ Film Favorit"
    elif filter_type == 'selesai':
        results = [f for f in films if f['selesai']]
        title = "✅ Film Selesai"
    elif filter_type == 'belum':
        results = [f for f in films if not f['selesai']]
        title = "⏳ Film Belum Selesai"
    elif filter_type == 'bagus':
        results = [f for f in films if f['rating'] >= 8]
        title = "⭐ Film Rating Bagus (≥8)"
    elif filter_type == 'kurang':
        results = [f for f in films if f['rating'] < 8]
        title = "😕 Film Rating Kurang (<8)"
    else:
        return
    if results:
        print(f"📋 {title}:")
        for i, film in enumerate(results, 1):
            display_film(film, i)
    else:
        print(f"❌ Tidak ada {title.lower()}.")

# Fungsi untuk pencarian lanjutan
def search_advanced(films, query):
    results = [f for f in films if query.lower() in f['nama'].lower() or query.lower() in f['genre'].lower() or query.lower() in f['ulasan'].lower()]
    if results:
        print(f"🔍 Hasil pencarian untuk '{query}':")
        for i, film in enumerate(results, 1):
            display_film(film, i)
    else:
        print(f"❌ Tidak ada film yang cocok dengan '{query}'.")

# Fungsi untuk mengurutkan film
def sort_films(films, sort_by):
    if sort_by == 'nama':
        sorted_films = sorted(films, key=lambda x: x['nama'].lower())
    elif sort_by == 'rating':
        sorted_films = sorted(films, key=lambda x: x['rating'], reverse=True)
    elif sort_by == 'tanggal':
        sorted_films = sorted(films, key=lambda x: x.get('tanggal', '0000-00-00'), reverse=True)
    else:
        return films
    return sorted_films

# Fungsi untuk rekomendasi acak
def random_recommendation(films):
    candidates = [f for f in films if f['favorit'] or f['rating'] >= 8]
    if candidates:
        rec = random.choice(candidates)
        print("🎲 Rekomendasi Acak:")
        display_film(rec)
    else:
        print("❌ Belum ada film favorit atau rating tinggi untuk direkomendasikan.")

# Fungsi untuk top film
def top_films(films, n=5):
    sorted_films = sorted(films, key=lambda x: x['rating'], reverse=True)
    top = sorted_films[:n]
    if top:
        print(f"🏆 Top {n} Film Berdasarkan Rating:")
        for i, film in enumerate(top, 1):
            display_film(film, i)
    else:
        print("❌ Belum ada film.")

# Fungsi utama aplikasi
def main():
    films = load_films()
    print("🎬 Selamat datang di Movie Check! 🎬")
    while True:
        print("\n" + "="*50)
        print("🍿 === Menu Movie Check === 🍿")
        print("1. ➕ Tambah film")
        print("2. 👀 Lihat daftar film")
        print("3. ✏️  Edit film")
        print("4. 🗑️  Hapus film")
        print("5. 🔍 Cari berdasarkan genre")
        print("6. 📊 Lihat statistik")
        print("7. 🎯 Lihat rekomendasi")
        print("8. 🔧 Filter film")
        print("9. 🔎 Pencarian lanjutan")
        print("10. 🔀 Urutkan daftar")
        print("11. 🎲 Rekomendasi acak")
        print("12. 🏆 Top 5 film")
        print("13. 🚪 Keluar")
        choice = input("Pilih opsi (1-13): ").strip()

        if choice == '1':
            nama = input("🎥 Masukkan nama film: ").strip()
            if not nama:
                print("❌ Nama film tidak boleh kosong.")
                continue
            # Hitung jumlah film dengan nama yang sama yang sudah selesai ditonton
            count = sum(1 for f in films if f['nama'].lower() == nama.lower() and f['selesai'])
            favorit_auto = count >= 3 and rating > 8
            if favorit_auto:
                print(f"❤️ Karena film '{nama}' sudah ditonton {count} kali dan mendapat rating >8, otomatis ditandai sebagai favorit!")
            try:
                rating = int(input("⭐ Masukkan rating (1-10): ").strip())
                if not 1 <= rating <= 10:
                    print("❌ Rating harus antara 1-10.")
                    continue
            except ValueError:
                print("❌ Rating harus angka.")
                continue
            ulasan = input("💬 Masukkan ulasan: ").strip()
            selesai = input("✅ Sudah selesai ditonton? (y/n): ").strip().lower() == 'y'
            if not favorit_auto:
                favorit = input("❤️ Apakah favorit? (y/n): ").strip().lower() == 'y'
            else:
                favorit = True
            genre = input("🎭 Masukkan genre: ").strip()
            tanggal = input("📅 Masukkan tanggal ditonton (YYYY-MM-DD): ").strip()
            # Rekomendasi otomatis
            rekomendasi = generate_recommendation(films, genre, nama)

            film = {
                'nama': nama,
                'rating': rating,
                'ulasan': ulasan,
                'selesai': selesai,
                'favorit': favorit,
                'genre': genre,
                'tanggal': tanggal,
                'rekomendasi': rekomendasi
            }
            films.append(film)
            save_films(films)
            print(f"✅ Film '{nama}' berhasil ditambahkan!")

        elif choice == '2':
            if films:
                print("\n📋 Daftar film yang sudah dicatat:")
                for i, film in enumerate(films, 1):
                    display_film(film, i)
            else:
                print("❌ Belum ada film yang dicatat.")

        elif choice == '3':
            if films:
                print("\n📋 Daftar film:")
                for i, film in enumerate(films, 1):
                    print(f"{i}. 🎥 {film['nama']}")
                try:
                    index = int(input("✏️ Masukkan nomor film yang ingin diedit: ")) - 1
                    if 0 <= index < len(films):
                        film = films[index]
                        print("💡 Biarkan kosong untuk tidak mengubah.")
                        nama = input(f"🎥 Nama ({film['nama']}): ").strip() or film['nama']
                        try:
                            rating_str = input(f"⭐ Rating ({film['rating']}): ").strip()
                            rating = int(rating_str) if rating_str else film['rating']
                            if rating_str and not 1 <= rating <= 10:
                                print("❌ Rating harus antara 1-10.")
                                continue
                        except ValueError:
                            print("❌ Rating harus angka.")
                            continue
                        ulasan = input(f"💬 Ulasan ({film['ulasan']}): ").strip() or film['ulasan']
                        selesai_str = input(f"✅ Selesai (y/n) ({'y' if film['selesai'] else 'n'}): ").strip().lower()
                        selesai = selesai_str == 'y' if selesai_str else film['selesai']
                        favorit_str = input(f"❤️ Favorit (y/n) ({'y' if film['favorit'] else 'n'}): ").strip().lower()
                        favorit = favorit_str == 'y' if favorit_str else film['favorit']
                        genre = input(f"🎭 Genre ({film['genre']}): ").strip() or film['genre']
                        rekomendasi = input(f"🎯 Rekomendasi ({film['rekomendasi']}): ").strip() or film['rekomendasi']

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
                        print(f"✅ Film '{nama}' berhasil diedit!")
                    else:
                        print("❌ Nomor tidak valid.")
                except ValueError:
                    print("❌ Masukkan nomor yang valid.")
            else:
                print("❌ Belum ada film yang dicatat.")

        elif choice == '4':
            if films:
                print("\n📋 Daftar film:")
                for i, film in enumerate(films, 1):
                    print(f"{i}. 🎥 {film['nama']}")
                try:
                    index = int(input("🗑️ Masukkan nomor film yang ingin dihapus: ")) - 1
                    if 0 <= index < len(films):
                        removed = films.pop(index)
                        save_films(films)
                        print(f"✅ Film '{removed['nama']}' berhasil dihapus!")
                    else:
                        print("❌ Nomor tidak valid.")
                except ValueError:
                    print("❌ Masukkan nomor yang valid.")
            else:
                print("❌ Belum ada film yang dicatat.")

        elif choice == '5':
            genre = input("🔍 Masukkan genre yang dicari: ").strip()
            search_by_genre(films, genre)

        elif choice == '6':
            show_statistics(films)

        elif choice == '7':
            if films:
                print("\n🎯 Rekomendasi Film:")
                for film in films:
                    if film['rekomendasi']:
                        print(f"🎥 {film['nama']}: {film['rekomendasi']}")
            else:
                print("❌ Belum ada film untuk direkomendasikan.")

        elif choice == '8':
            print("🔧 Pilih filter:")
            print("1. ❤️ Favorit")
            print("2. ✅ Selesai")
            print("3. ⏳ Belum Selesai")
            print("4. ⭐ Rating Bagus (≥8)")
            print("5. 😕 Rating Kurang (<8)")
            filter_choice = input("Pilih (1-5): ").strip()
            if filter_choice == '1':
                filter_films(films, 'favorit')
            elif filter_choice == '2':
                filter_films(films, 'selesai')
            elif filter_choice == '3':
                filter_films(films, 'belum')
            elif filter_choice == '4':
                filter_films(films, 'bagus')
            elif filter_choice == '5':
                filter_films(films, 'kurang')
            else:
                print("❌ Pilihan tidak valid.")

        elif choice == '9':
            query = input("🔎 Masukkan kata kunci pencarian: ").strip()
            search_advanced(films, query)

        elif choice == '10':
            print("🔀 Pilih pengurutan:")
            print("1. 📝 Nama")
            print("2. ⭐ Rating")
            print("3. 📅 Tanggal (terbaru ke terlama)")
            sort_choice = input("Pilih (1-3): ").strip()
            if sort_choice == '1':
                sorted_list = sort_films(films, 'nama')
            elif sort_choice == '2':
                sorted_list = sort_films(films, 'rating')
            elif sort_choice == '3':
                sorted_list = sort_films(films, 'tanggal')
            else:
                print("❌ Pilihan tidak valid.")
                continue
            print("\n📋 Daftar film yang diurutkan:")
            for i, film in enumerate(sorted_list, 1):
                display_film(film, i)

        elif choice == '11':
            random_recommendation(films)

        elif choice == '12':
            top_films(films)

        elif choice == '13':
            print("👋 Terima kasih telah menggunakan Movie Check! Sampai jumpa! 🎬")
            break

        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
