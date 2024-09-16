Nama : William Matthew Saputra  
NPM : 2306165862  
Kelas : PBP F  

Link: https://william-matthew31-tugas2pbp.pbp.cs.ui.ac.id/


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**TUGAS 2**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Memuat project django baru**  
Dalam pembuatan proyek Django baru, ada beberapa hal dasar yang harus disiapkan mulai dari penyimpanan lokal, repository pada GitHub hingga hal - hal penting seperti _virtual environment_ dan lainnya. Penyimpanan lokal berguna untuk menyimpan data secara lokal pada penyimpanan komputer, sedangkan _repository_ GitHub adalah ruang penyimpanan secara daring. Data pada penyimpanan lokal nantinya akan di _push_ ke _repository_ GitHub sehingga data bisa diakses oleh pengembang lain sekaligus bisa dilacak perubahannya. Setelah menyiapkan penyimpanan lokal dan _repository_ GitHub, saya membuat dan mengaktifkan _virtual environment_ untuk mengisolasi _package_ dan _dependencies_ dari aplikasi sehingga tidak terjadi konflik dengan versi lain yang terdapat pada komputer. Selanjutnya, saya menyiapkan dependencies yang merupakan sebuah modul untuk fungsionalitas suatu perangkat lunak. _Dependencies_ mencakup _library_, _framework_, ataupun _package_. Pada kasus ini, saya menambahkan _dependencies_ melalui _file_ yang bernama `requirements.txt` yang nantinya akan di _install_ dengan memanfaatkan _virtual environment_. Setelah semua hal sudah siap, saya membuat proyek Django dengan nama `tugas2pbp` dengan perintah `django-admin startproject tugas2pbp .` Sebelum dijalankan, proyek Django harus diatur konfigurasinya pada file `settings.py`. Bagian yang harus diubah adalah `ALLOWED_HOST`, yang merupakan daftar host yang diperbolehkan untuk mengakses aplikasi web. Setelah itu, proyek Django ini bisa di deploy.  
  
**Membuat aplikasi dengan nama `main` pada proyek tersebut**  
Untuk membuat aplikasi dengan nama main pada proyek, saya menggunakan perintah `python manage.py startapp main` sehingga dirketori `main` baru akan terbentuk. Setelah itu saya mendaftarkan aplikasi `main` ke dalam proyek melalui file `settings.py`. Saya menambahkan `main` pada bagian `INSTALLED_APPS` pada file tersebut.  
  
**Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`**  
Routing proyek dilakukan agar aplikasi `main` bisa dibuka melalui web. Routing dilakukan dengan membuat berkas `urls.py` pada direktori `main` yang sudah dibuat sebelumnya. Hal ini dilakukan untuk mengatur rute URL secara spesifik berdasarkan fitur yang ada pada aplikasi. Setelah itu saya menambahkan rute URL menggunakan fungsi _include_ pada berkas `urls.py`  pada direktori proyek untuk mengarahkan routing URL pada tingkat yang lebih luas dan mengarahkannya ke aplikasi.  

**Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib (name, price, description)**  
Saya membuat model pada aplikasi dengan memodifikasi berkas `models.py` pada direktori main. Untuk tugas ini, saya menggunakan _CharField_ untuk atribut `name`, _IntegerField_ untuk atribut `price`, _TextField_ untuk atribut `description`, _DecimalField_ untuk atribut `thickness`, dan juga _TextField_ untuk atribut `user_reviews`. Setelah membuat model sesuai keinginan, saya melakukan migrasi model untuk mengubah struktur tabel data sesuai dengan model yang saya sudah definisikan.  

**Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**  
`views.py` akan ditambahkan fungsi yang mengembalikan data yang diinginkan ke template HTML. Pada tugas ini, saya mengembalikan nama aplikasi, nama pribadi, dan kelas ke template HTML.  

**Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**  
Saya menambahkan rute URL pada `urls.py` untuk mengatur rute URL yang berhubungan dengan aplikasi `main`. Pada kasus ini, URL akan memetakan fungsi yang sudah dibuat pada `views.py`. Hal ini berguna untuk menggunakan fungsi yang sudah dibuat melalui URL tertentu.  

**Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**  
Setelah menyiapkan seluruh komponen yang diperlukan untuk membuat aplikasi, saya melakukan deployment dengan menambahkan URL deployment pada berkasi `settings.py`, dilanjutkan dengan perintah _git add, commit_, dan _push_ perubahan ke GitHub sekaligus ke server PWS. Setelah _deployment_ berhasil, aplikasi bisa diakses melalui internet.  

**Bagan dan penjelasan**  
![PBP William (1)](https://github.com/user-attachments/assets/55e7a8d4-3280-4f35-8e1f-3c94cbfb3773)  
Bagan tersebut menggambarkan flow kerja dari aplikasi Django. Hal ini diawali dengan _request client_ dari pengguna yang akan diterima oleh `urls.py` yang berfungsi untuk menentukan _view_ yang tepat. Setelah itu, request akan diteruskan ke `views.py` yang nantinya akan berinteraksi dengan `models.py` dalam bentuk membaca atau menulis data yang diperlukan oleh database. Setelah proses data, `views.py` akan menerima data dari `main.html` yang berfungsi sebagai _template_ HTML dan bisa melakukan visualisasi data yang sudah diproses menjadi tampilan yang bisa dinikmati pengguna. Proses ini diakhiri dengan `views.py` yang mengirimkan HTTP _response_ berupa HTML yang sudah diproses atau dirender kepada pengguna.

**Bagian Pertanyaan**  
**1. Jelaskan fungsi git dalam pengembangan perangkat lunak!**  
Git adalah sebuah _distributed version control system_ (dVCS) yang berfungsi sebagai mengontrol dan melacak perubahan versi yang terjadi pada suatu proyek. Hal ini memungkinkan pengembang untuk memastikan bahwa setiap perubahan yang terjadi bisa diatur, dipantau, dan dilacak secara menyeluruh. Selain itu, perubahan juga bisa dibandingkan bahkan dibatalkan juga diperlukan. Inilah menjadi salah satu tools yang digunakan developer untuk berkolaborasi dalam menyelesaikan suatu projek. Developer bisa secara bebas bekerja pada bagian yang berbeda secara bersamaan tanpa mengganggu pekerjaan yang lain.  
  
**2. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**  
Framework Django digunakan sebagai permulaan dalam pembelajaran pengembangan perangkat lunak karena Django sendiri yang ramah untuk pengguna baru. Secara teknis, Django sudah dirancang untuk mengatasi beberapa kerumitan yang terjadi dalam pengembangan web. Rancangan ini juga mencakup ekosistem yang besar, baik, sekaligus memiliki keamanan yang terjamin. Selain itu Django bersifat _open-source_ yang memungkinkan pengembang untuk melakukan modifikasi secara luas. Ada banyak versi, dokumentasi, dan sudah dilengkapi dengan komunitas yang besar dan aktif.  
  
**3. Mengapa model pada Django disebut sebagai ORM?**  
Model pada Django disebut sebagai ORM (_Object Relational Mapping_) karena Django menggunakan cara ini untuk memetakan objek Python ke tabel _database_ yang bersifat _relational_. Pengembang dipermudah melalui kehadiran cara ini, karena mereka tidak perlu  untuk berurusan dengan query SQL secara manual untuk berhubungan dengan _database_. Hal ini cukup digantikan dengan menggunakan model di Python yang secara otomatis diubah menjadi operasi _database_.  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**TUGAS 3**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Membuat input form untuk menambahkan objek model pada app sebelumnya.**  
Langakh ini dimulai dengan membuat `forms.py` pada untuk membuat _forms_ yang bisa menerima data baru. Form menggunakan model `Product` yang mencakup field yang relevan. Setelah itu kita perbarui kode `views.py` dengan menambahkan fungsi `product_entry`. Fungsi ini menerima data, memvalidasi input, serta menyimpan data tersebut. Setelah berhasil disimpan maka pengguna akan di _redirect_ ke halaman utama. Lalu `views.py` dan `main.html` dimodifikasi untuk menampilan semua entri produk yang sudah dibuat.  

**Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**  
    1.  **Format XML**  
        Kita perlu menambahkan fungsi `show_xml` yang mengambil seluruh data dari entry `Product` menggunakan `Product.objects.all()`. Lalu kita gunakan fungsi `serializers.serialize("xml", data)` yang mengembalikan hasil dengan tipe XML. 
          
        ```
        def show_xml(request):
            data = MoodEntry.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            ```  
            
   2.  **Format JSON**  
       Fungsi yang akan digunakan adalah `show_json` yang serupa dengan `show_xml`. Nantinya fungsi ini akan mengembalikan hasil dengan tipe JSON.  
         
       ```
       def show_json(request):
            data = MoodEntry.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
       
  3. **XML by ID dan JSON by ID**  
      Fungsi tambahan`show_xml_by_id` dan `show_json_by_id` digunakan untuk mengambil data `Product` menggunakan ID. Query dilakukan menggunakan `data = MoodEntry.objects.filter(pk=id)` untuk mengambil data sesuai ID, lalu diubah menjadi format XML atau JSON sesuai yang dipanggil. Untuk memanggilnya kita bisa menambahkan ID di belakang URL.  
        
      ```
      def show_xml_by_id(request, id):
            data = MoodEntry.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```  
  
      ```
      def show_json_by_id(request, id):
            data = MoodEntry.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```  


** Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**  
URL ditambahkan pada file `urls.py` supaya fungsi - fungsi yang sudah ditambahkan pada `views.py` bisa diakses dan dimanfaatkan.

```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product_entry',create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
  
**Bagian Pertanyaan**  
** Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**  
Data delivery sangat penting dalam pengimplementasian sebuah platform karena data adalah bagian utama dari interaksi antara pengguna dengan sistem. Peran data delivery adalah memastikan agar komunikasi data antara server dan klien bisa berjalan dengan baik. Salah satu contoh dari data delivery yang baik adalah pada aplikasi web dimana klien pengguna bisa mengakses informasi, memasukkan input, hingga menerima respon secara _real time_.  

**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
JSON dan XML memiliki kelebihan dan kekurangannya masing - masing . Namun JSON sering dianggap lebih baik, terutama untuk aplikasi web karena:
  1. Sintaks yang lebih mudah: Sintaks JSON lebih sederhana dan mudah dibaca baik oleh komputer maupun manusia.
  2. Kompatibel dengan JavaScript: JSON adalah turunan dari JavaScript sehingga mudah digunakan dalam aplikasi web tanpa memerlukan parser tambahan.
  3. Efisiensi proses: JSON memiliki struktur dengan basis objek dan array saja sehingga memudahkan proses di berbagai bahasa pemograman.
Dari sudu pandang XML, XMl lebih rumit karena membutuhkan banyak tag yang harus ditulis sehingga ukurannya besar dan lebih lambat dalam melakukan proses.

**Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**
Method `is_valid()` pada form Django berfungsi untuk memvalidasi input data yang dilakukan oleh pengguna ke dalam form. Method ini mencegah data yang tidak valid atau rusak masuk ke dalam sistem, misalnya angka yang di luar rentang, format nama yang salah, dan lainnya.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
`csrf_token` adalah _randomized token_ yang dihasilkan Django untuk melindungi aplikasi dari serangan CSRF. Serangan ini terjadi ketika ada permintaan berbahaya ke server seperti mengubah data penting menggunakan akun pengguna yang sudah terverifikasi. Tanpa `csrf_token` pada form, aplikasi akan rentan terhadap serangan dan bisa disalahgunakan hingga skala besar seperti menggubah data transaksi dan serangan serupa. Dengan menambahkan `csrf_token` kita memastikan bahwa setiap permintaan POST berasal dari sumber yang valid.
