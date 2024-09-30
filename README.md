Nama : William Matthew Saputra  
NPM : 2306165862  
Kelas : PBP F  

Link: https://william-matthew31-tugas2pbp.pbp.cs.ui.ac.id/

<details>
  <summary>Tugas 2</summary>

**TUGAS 2**  
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
</details>

<details>
  <summary>Tugas 3</summary>

**TUGAS 3**  
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


**Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**  
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
**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**  
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

**POSTMAN**

**JSON**  
![image](https://github.com/user-attachments/assets/2bc3c452-ec73-4a21-b39d-0be6c8eaed50)  

**JSON BY ID**  
![image](https://github.com/user-attachments/assets/732802a6-a0bf-423c-a32c-32454d23b9c2)  

**XML**  
![image](https://github.com/user-attachments/assets/c9cbd717-1066-4bc1-aa9e-2e2b7416964e)  

**XML BY ID**  
![image](https://github.com/user-attachments/assets/731d0ec8-eb8e-47d9-8ba4-aa9aaea85a9e)  

</details>

<details>
  <summary>Tugas 4</summary>

**Tugas 4**
  
**Implementasi** 
**Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.** 

Implementasi fungsi `registrasi`, `login`, dan `logout` pada aplikasi Django bertujuan untuk mengatur akses pengguna ke halaman yang di-restrict, seperti halaman utama pada aplikasi. 

Fungsi `register` bertujuan untuk membuat akun pengguna baru agar mereka bisa login dan mengakses halaman yang dibatasi. Fungsi ini ditambahkan pada file `views.py` pada direktori `main`. Untuk tampilan registrasi akan di-handle oleh `register.html` yang berada di direktori `main`. Fungsi ini menggunakan `UserCreationForm` dari Django yang akan menyediakan formulir pendaftaran untuk akun baru. Selanjutnya, pengguna akan mengirimkan data melalui form yang datanya akan divalidasi menggunakan `form.is_valid()`. Jika valid, nantinya akun baru akan disimpan pada `form.save()`. Setelah itu, pengguna akan mendapat pesan berhasil dan akan diarahkan kembali ke halaman `login`.

Mengautentikasi pengguna sehingga mereka bisa login dan mengakses halaman. Fungsi ini ditambahkan pada file `views.py` yang berada pada direktori `main`. Tampilan fungsi ini akan di-handle oleh file `login.html` yang berada pada direktori `main`. Fungsi ini menggunakan `AuthenticationForm` dari Django. Selanjutnya, pengguna akan mengirimkan data form login yang nantinya akan divalidasi. Jika valid, artinya pengguna berhasil diidentifikasi dengan `form.get_user()`. Setelah validasi, fungsi `login(request, user)` digunakan untuk melakukan proses login, menciptakan sesi baru untuk pengguna yang berhasil login.

Fungsi `logout` bertujuan untuk menghapus sesi pengguna yang telah login sehingga mereka tidak bisa mengakses halaman yang dibatasi. Fungsi ini ditambahkan ke file `views.py` yang berada pada direktori `main`. Fungsi ini menggunakan `logout(request)` dari Django yang bisa menghapus sesi pengguna saat ini. Setelah sesi dihapus, pengguna akan diarahkan ke halaman `login` sehingga mereka harus login ulang. Tombol ini ditambahkan ke dalam template `main.html`.  

**Menghubungkan model product dengan user**  
  
Model `Product` dan `User` dihubungkan untuk memetakan kepemilikan user atas product yang dibuatnya. Hal ini dilakukan dengan cara mengimpor model `User` pada `models.py` dilanjutkan dengan menambahkan `ForeignKey` pada model `Product`.

```
class Product(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```  

Kode tersebut berfungsi untuk menghubungkan satu `Product` dengan satu `User` melalui sebuah relationship.  

Selanjutnya kita ubah fungsi `create_product_entry`:
```
def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

Fungsi `create_product_entry` menggunakan `commit=False` untuk mencegah Django langsung menyimpan data ke database setelah form divalidasi. Ini memungkinkan kita memodifikasi objek terlebih dahulu, seperti mengisi field `user` dengan `request.user` yang sedang login. Setelah itu, objek disimpan ke database, menandakan bahwa entri product tersebut milik pengguna yang sedang terautentikasi.  


Selanjutnya ubah value dari `product_entries` dan `context` pada `show_main` menjadi:
```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'product_entries': product_entries
```

Kode tersebut menampilkan `Product` yang terkait dengan pengguna yang sedang login, dengan menyaring objek berdasarkan `User` yang sedang login. Selain itu, `request.user.username` digunakan untuk menampilkan username pengguna di halaman utama.  
  
Setelah itu lakukan migrasi. Dalam proses ini akan ada error yang muncul, pilih `1` dan ketik angka `1` lagi untuk menetapkan user dengan ID `1` pada model yang ada. Setelah itu lakukan import `os` pada `settings.py` dan ganti variabel `DEBUG` dengan kode dibawah ini:  
```
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

**Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.** 

Menampilkan informasi seperti last login pada halaman utama aplikasi akan menggunakan data dari _cookies_. Dengan langkah sebagai berikut:  


1. Tambahkan Import**: Buka `views.py` di subdirektori `main`, dan tambahkan:  
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

2. Menambahkan _Cookie_ `last_login`: Pada fungsi `login_user`, ubah blok kode di if `form.is_valid()` menjadi:  
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

3. Menampilkan last_login di Halaman: Di fungsi show_main, tambahkan kode berikut ke dalam variabel context:  
```
'last_login': request.COOKIES['last_login']
```

4. Hapus _Cookie_ Saat _Logout_: Ubah fungsi `logout_user` menjadi:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
5. Tambahkan ke `main.html`: Setelah tombol _logout_, tambahkan kode berikut untuk menampilkan informasi pada halaman utama aplikasi web:
```
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
  
**PERTANYAAN**  
**1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**  
`HttpResponseRedirect()` adalah respons yang secara eksplisit mengarahkan ulang ke URL tertentu. URL yang diberikan harus ditentukan secara manual. Misalnya, jika kita ingin mengarahkan pengguna ke halaman tertentu harus menulis URL target secara eksplisit, seperti `/home/` atau `/login/`.  

`redirect()` adalah shortcut di Django yang secara internal menggunakan `HttpResponseRedirect()`. Django akan secara otomatis menangani konversi nama view atau nama URL menjadi URL penuh di backend, sehingga penggunaan `redirect()` sangat efisien dalam pengembangan aplikasi berbasis web.  

**2. Jelaskan cara kerja penghubungan model Product dengan User!**  

Model `Product` dan `User` akan dihubungkan menggunakan `ForeignKey` agar setiap produk memiliki pemilik yang jelas. Fungsi `create_product_entry` tidak bisa menyimpan produk baru setelah validasi form, melainkan akan ditambah informasi pemiliknya yaitu user yang sedang login. Nantinya setiap produk akan memiliki kaitan terhadap pengguna yang terautentikasi saat pembuatan.  

Fungsi `show_main` hanya akan menampilkan produk milik pengguna yang sedang login menggunakan filter `Product.objects.filter(user=request.user)`. Setelah perubahan dilakukan, harus dilakukan migrasi database dan jika ada error pilihlah opsi 1 untuk menetapkan `User` dengan ID 1 pada produk yang ada. Selain itu, pengaturan `DEBUG` harus diubah agar bisa aktif di mode development dan mati di mode production menggunakan variabel environment `PRODUCTION`.  

**3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Authentication berfokus pada verifikasi identitas pengguna menggunakan username dan password. Authentication menggunakan fungsi `authenticate()` yang berguna untuk memvalidasi kredensial pengguna. Jika valid nantinya fungsi `login()` akan digunakan untuk membuat sesi dan menyimpan status login pengguna. Session ID kemudian disimpan di cookie untuk mengingat pengguna yang sudah login di setiap request berikutnya.  

Authorization adalah tahap lanjutan dari authentication. Authorization menentukan apa yang bisa pengguna akses. Django mengelola authorization melalui decorators seperti `@login_required` yang berguna untuk memastikan pengguna hanya bisa mengakses halaman tertentu setelah login. Django juga menggunakan `permission_required` untuk membatasi akses berdasarkan batasan tertentu, seperti hanya admin yang dapat mengakses halaman tertentu.  

**4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari _cookies_ dan apakah semua _cookies_ aman digunakan?**  
  
Cara Django mengingat pengguna yang telah login adalah dengan session _cookies_. Session _cookies_ diciptakan Django setelah pengguna login. Isi dari session _cookies_ adalah session ID yang akan digunakan untuk mengaitkan pengguna dengan data pada server. Saat pengguna melakukan request baru, nanti Django dapat memeriksa session ID yang sudah tercipta untuk mengecek apakah sudah melakukan login atau belum.  

Selain untuk mengatur dan melakukan validasi saat pengguna masuk ke sebuah halaman, _cookies_ juga memiliki banyak fungsionalitas lain. Dimulai dari menyimpan preferensi pengguna seperti bahasa default dan juga tema halaman, activity tracking untuk kepentingan analitik, hingga otentikasi untuk melakukan validasi agar pengguna yang meninggalkan halaman tidak perlu untuk melakukan login kembali.  

Meskipun _cookies_ tampaknya memiliki fungsionalitas yang tinggi, tidak semua _cookies_ aman digunakan. Ada beberapa _cookies_ yang tidak dienkripsi sehingga dapat dicuri oleh pihak lain menggunakan serangan man-in-the-middle. Ada juga _cookies_ yang tidak diberi atribut secure maupun tidak menggunakan `HTTPOnly` sehingga jenis-jenis _cookies_ ini sangat mudah disadap dan dapat disalahgunakan untuk mengambil sesi pengguna yang sedang aktif.

![messageImage_1727236854010](https://github.com/user-attachments/assets/1673fa4e-27d9-4535-ac77-7bf06ebe3c81)
![messageImage_1727237066319](https://github.com/user-attachments/assets/4710cd63-83b7-4210-8682-befd6c3ff786)

</details>  
  
<details>
    <summary>Tugas 5</summary>  

**Tugas 5**  
  
**Implementasikan fungsi untuk menghapus dan mengedit product.**  

**A. Edit Product**  
    1. Membuat fungsi edit_product yang menerima parameter request dan id  
    
  ```python  
    def edit_product(request, id):
        product = Product.objects.get(pk=id)
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        context = {'form': form}
        return render(request, "edit_product.html", context)
  ```
          
  2. Melakukan import pada views.py
  ```python
    from django.shortcuts import .., reverse
    from django.http import .., HttpResponseRedirect
  ```
    
  3. Membuat file baru (edit_product.html)  sebagai tampilan dari fitur dari edit product  
  ```python   
    {% extends 'base.html' %}
    {% load static %}
    {% block content %}
    <h1>Edit Product</h1>
    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Product"/>
                </td>
            </tr>
        </table>
    </form>
    {% endblock %}
  ```

  4. Import fungsi edit_product pada urls.py dan menambahkan path ke urlpatterns  
        from main.views import edit_product
  ```python
    ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    ...
  ```

**B. Delete Product**  
    1. Membuat fungsi delete_product dengan parameter request dan id pada views.py  
```python
      def delete_product(request, id):
          product= Product.objects.get(pk = id)
          product.delete()
          # Kembali ke halaman awal
          return HttpResponseRedirect(reverse('main:show_main'))
```  
    
  2. Import fungsi delete_product pada urls.py dan tambahkan path url ke url patterns
        from main.views import delete_product
  ```python
  ...
  path('delete/<uuid:id>', delete_product, name='delete_product'), 
  ...
  ```  

** Kustomisasi halaman login, register, dan tambah product semenarik mungkin.**

**Login**  
<details>
<summary>Kode Login</summary>

  ```python
  {% extends 'base.html' %}
  {% load static %}  <!-- Ensure this line is present -->

  {% block meta %}
  <title>Login</title>
  {% endblock meta %}

  {% block content %}
  <!-- Background Video and Overlay -->
  <div class="relative min-h-screen overflow-hidden">
  
  <!-- Background Video -->
  <video autoplay loop muted playsinline class="absolute top-0 left-0 w-full h-full object-cover z-0" aria-hidden="true">
      <source src="{% static 'video/background.mp4' %}" type="video/mp4">  <!-- This uses the static tag correctly -->
      Your browser does not support the video tag.
  </video>
  
  <!-- Grey Overlay -->
  <div class="absolute top-0 left-0 w-full h-full bg-gray-700 bg-opacity-50 z-10"></div>
  
  <!-- Main Content -->
  <div class="relative z-20 flex items-center justify-center min-h-screen w-screen py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-md w-full space-y-8">
      <div>
          <h2 class="mt-6 text-center text-3xl font-extrabold text-white"> <!-- changed to white -->
          Login to your account
          </h2>
      </div>
      <form class="mt-8 space-y-6" method="POST" action="">
          {% csrf_token %}
          <input type="hidden" name="remember" value="true">
          <div class="rounded-md shadow-sm -space-y-px">
          <div>
              <label for="username" class="sr-only">Username</label>
              <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-[#2d46a2] focus:border-[#2d46a2] focus:z-10 sm:text-sm" placeholder="Username">
          </div>
          <div>
              <label for="password" class="sr-only">Password</label>
              <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-[#2d46a2] focus:border-[#2d46a2] focus:z-10 sm:text-sm" placeholder="Password">
          </div>
          </div>

          <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#2d46a2] hover:bg-[#24378c] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#2d46a2]">
              Sign in
          </button>
          </div>
      </form>

      {% if messages %}
      <div class="mt-4">
          {% for message in messages %}
          {% if message.tags == "success" %}
          <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
              <span class="block sm:inline">{{ message }}</span>
          </div>
          {% elif message.tags == "error" %}
          <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
              <span class="block sm:inline">{{ message }}</span>
          </div>
          {% else %}
          <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
              <span class="block sm:inline">{{ message }}</span>
          </div>
          {% endif %}
          {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
          <p class="text-sm text-gray-300"> <!-- changed to a lighter gray -->
          Don't have an account yet?
          <a href="{% url 'main:register' %}" class="font-medium text-[#4a90e2] hover:text-[#356bb0]"> <!-- changed to a more vibrant blue -->
              Register Now
          </a>
          </p>
      </div>
      </div>
  </div>
  </div>
  {% endblock content %}
  ```
</details>

**Register**  
<details>
  <summary>Kode Register</summary>  
  
  ```python
    {% extends 'base.html' %}
    {% load static %}  <!-- Ensure this line is present -->
    
    {% block meta %}
    <title>Register</title>
    {% endblock meta %}
    
    {% block content %}
    <!-- Background Video and Overlay -->
    <div class="relative min-h-screen overflow-hidden">
      
      <!-- Background Video -->
      <video autoplay loop muted playsinline class="absolute top-0 left-0 w-full h-full object-cover z-0" aria-hidden="true">
        <source src="{% static 'video/background.mp4' %}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      
      <!-- Grey Overlay -->
      <div class="absolute top-0 left-0 w-full h-full bg-gray-700 bg-opacity-50 z-10"></div>
      
      <!-- Main Content -->
      <div class="relative z-20 flex items-center justify-center min-h-screen w-screen py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-md w-full space-y-8 form-style">
          <div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-white">
              Create your account
            </h2>
          </div>
          <form class="mt-8 space-y-6" method="POST">
            {% csrf_token %}
            <input type="hidden" name="remember" value="true">
            <div class="rounded-md shadow-sm -space-y-px">
              {% for field in form %}
                <div class="{% if not forloop.first %}mt-4{% endif %}">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-white">
                    {{ field.label }}
                  </label>
                  <div class="relative">
                    {{ field }}
                    <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                      {% if field.errors %}
                        <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                        </svg>
                      {% endif %}
                    </div>
                  </div>
                  {% if field.errors %}
                    {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                  {% endif %}
                </div>
              {% endfor %}
            </div>
    
            <div>
              <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#2d46a2] hover:bg-[#24378c] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#2d46a2]">
                Register
              </button>
            </div>
          </form>
    
          {% if messages %}
          <div class="mt-4">
            {% for message in messages %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
              <span class="block sm:inline">{{ message }}</span>
            </div>
            {% endfor %}
          </div>
          {% endif %}
    
          <div class="text-center mt-4">
            <p class="text-sm text-white">
              Already have an account?
              <a href="{% url 'main:login' %}" class="font-medium text-[#4a90e2] hover:text-[#24378c]">
                Login here
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
    {% endblock content %}
  ```
</details>

**Tambah Product**  
<details>
  <summary>Kode Tambah Product</summary>  
  
  ```python 
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Create Product</title>
    {% endblock meta %}
    
    {% block content %}
    {% include 'navbar.html' %}
    
    <!-- Background Video and Overlay -->
    <div class="relative min-h-screen overflow-hidden">
      
      <!-- Background Video -->
      <video autoplay loop muted playsinline class="absolute top-0 left-0 w-full h-full object-cover z-0" aria-hidden="true">
        <source src="{% static 'video/background.mp4' %}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      
      <!-- Grey Overlay -->
      <div class="absolute top-0 left-0 w-full h-full bg-gray-700 bg-opacity-50 z-10"></div>
      
      <!-- Main Content -->
      <div class="relative z-20 flex flex-col min-h-screen">
        <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
          <h1 class="text-3xl font-bold text-center mb-8 text-white">Create Product Entry</h1>
        
          <div class="bg-white shadow-md rounded-lg p-6 form-style">
            <form method="POST" class="space-y-6">
              {% csrf_token %}
              {% for field in form %}
                <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                    {{ field.label }}
                  </label>
                  <div class="w-full">
                    {{ field }}
                  </div>
                  {% if field.help_text %}
                    <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                    <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
                </div>
              {% endfor %}
              <div class="flex justify-center mt-6">
                <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                  Create Product Entry
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    {% endblock %}
  ```

</details>




</details>




