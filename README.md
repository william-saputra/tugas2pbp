# PBP F - 2024

###Nama : William Matthew Saputra  
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
  ```python 
    from main.views import edit_product
  ```
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
  ```python
    from main.views import delete_product
  ```  
  ```python
  ...
  path('delete/<uuid:id>', delete_product, name='delete_product'), 
  ...
  ```  

**Kustomisasi halaman login, register, dan tambah product semenarik mungkin.**

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

**Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:**  
  1.  Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.

  Menambahkan kode berikut pada `main.html` untuk menampilkan gambar dan pesan bahwa belum ada product yang terdaftar  
      
  ```python 
    <!-- Product Entries Section -->
    {% if not product_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
      <img src="{% static 'image/empty.png' %}" alt="Empty product" class="w-32 h-32 mb-4"/>
      <p class="text-center text-gray-200 mt-4">Belum ada data produk pada toko.</p>
    </div>
    {% else %}
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
      {% for product_entry in product_entries %}
        {% include 'card_product.html' with product_entry=product_entry %}
      {% endfor %}
    </div>
    {% endif %}
  ```

2. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!)  

Berikut adalah kode `card_product.html`
   ```python 
        {% load humanize %}
        <div class="relative break-inside-avoid">
            <div class="relative bg-[#2d46a2] shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform scale-100 hover:scale-105 transition-transform duration-300">
              
              <!-- Header Section -->
              <div class="bg-[#fef582] text-black-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                <h3 class="font-bold text-xl mb-2">{{ product_entry.product_name }}</h3>
                <p class="font-bold text-green-600">Rp {{ product_entry.price|intcomma }}</p>
              </div>
              
              <!-- Content Section -->
              <div class="p-4">
                
                <!-- Description Title -->
                <p class="font-semibold text-lg mb-2 text-[#fef582]">Description</p>
                <!-- Description Content -->
                <p class="text-white mb-2">
                  {{ product_entry.description }}
                </p>
                
                <!-- Thickness Title -->
                <p class="font-semibold text-lg mb-2 text-[#fef582]">Thickness</p>
                <!-- Thickness Content -->
                <p class="text-white mb-2">
                  {{ product_entry.thickness }} mm
                </p>
        
                <!-- User Rating and Review -->
                <div class="mt-4 text-center">
                  
                  <!-- User Review Title -->
                  <p class="font-semibold mb-2 text-[#fef582]">User Review</p>
                  <!-- User Review Content -->
                  <p class="italic text-white">"{{ product_entry.user_reviews }}"</p>
                  
                  <!-- Display Star Rating -->
                  <div class="flex justify-center items-center mt-2">
                    {% for i in "12345" %}
                      {% if forloop.counter <= product_entry.user_ratings %}
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                          <path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z" />
                        </svg>
                      {% else %}
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                          <path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z" />
                        </svg>
                      {% endif %}
                    {% endfor %}
                  </div>
                </div>
              </div>
              
              <!-- Edit and Delete Buttons -->
              <div class="absolute top-2 right-2 flex space-x-1">
                <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                  </svg>
                </a>
                <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                </a>
              </div>
            </div>
        </div>
   ```  

**Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!**  

Menambahkan kode berikut pada `card_product.html`  untuk membuat tombol _edit_ dan _delete_  
```python
<!-- Edit and Delete Buttons -->
      <div class="absolute top-2 right-2 flex space-x-1">
        <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
        </a>
        <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </div>
```  

**Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.**  

_Navigation bar_ yang responsive terhadap perbedaan ukuran device bisa diimplementasikan karena pemanfaattan **Tailwind CSS**. Atribut seperti `hidden md:flex` dan juga `md:  hidden` mengatur agar _navigation bar_ yang memiliki konten _Home_, Products, _Categories_, dan _Cart_ bisa menampilkan seluruh aspek tersebut pada layar yang lebar dan bisa menampilkan logo hamburger pada layar kecil dan jika di klik akan menjabarkan seluruh isi konten tersebut. Berikut adalah kode _navigation bar_:

```python
    <nav class="bg-[#2d46a2] shadow-lg fixed top-0 left-0 z-40 w-screen">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <h1 class="text-2xl font-bold text-center text-white">{{app}}</h1>
          </div>
          <div class="hidden md:flex items-center space-x-4">
            <!-- Navbar items for desktop -->
            <a href="#" class="text-white hover:text-gray-200">Home</a>
            <a href="#" class="text-white hover:text-gray-200">Products</a>
            <a href="#" class="text-white hover:text-gray-200">Categories</a>
            <a href="#" class="text-white hover:text-gray-200">Cart</a>
            {% if user.is_authenticated %}
              <span class="text-gray-300">Welcome, {{ user.username }}</span>
              <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Logout
              </a>
            {% else %}
              <a href="{% url 'main:login' %}" class="text-center bg-[#2d46a2] hover:bg-[#24378c] text-white font-bold py-2 px-4 rounded transition duration-300">
                Login
              </a>
            {% endif %}
          </div>
          <div class="md:hidden flex items-center">
            <button class="mobile-menu-button">
              <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M4 6h16M4 12h16M4 18h16"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
      <!-- Mobile menu -->
      <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
        <div class="pt-2 pb-3 space-y-1 mx-auto">
          <!-- Navbar items for mobile -->
          <a href="#" class="block text-center text-white py-2">Home</a>
          <a href="#" class="block text-center text-white py-2">Products</a>
          <a href="#" class="block text-center text-white py-2">Categories</a>
          <a href="#" class="block text-center text-white py-2">Cart</a>
          {% if user.is_authenticated %}
            <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="block text-center bg-[#2d46a2] hover:bg-[#24378c] text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
              Login
            </a>
          {% endif %}
        </div>
      </div>
    
      <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
      
        btn.addEventListener("click", () => {
          menu.classList.toggle("hidden");
        });
      </script>
    </nav>
```  

**PERTANYAAN**  
**1.   Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**  

Prioritasnya adalah Inline Styles > ID Selector > Class, Attribute, dan Pseudo-class Selectors > Element Selector > Browser Default.  

Inline Styles adalah gaya yang ditulis langsung pada elemen HTML menggunakan atribut `style=""`. Contohnya adalah `<h1 style="color: red;">Judul</h1>`. Prioritas inline style selalu yang tertinggi dan akan menimpa semua jenis CSS lainnya jika tidak ada penggunaan `!important`.  

ID Selector adalah selector yang menggunakan atribut `id` pada elemen HTML. Contohnya adalah `#header { color: blue; }` untuk elemen `<div id="header"></div>`.  

Class, Attribute, dan Pseudo-class Selectors adalah selector yang menggunakan class, atribut, atau pseudo-class seperti `:hover`, `:focus`, dan lainnnya. Class ini dapat diterapkan pada beberapa elemen sekaligus. Contoh implementasinya adalah `.main { font-size: 16px; }`, `[type="text"] { color: green; }`, `:hover { background-color: yellow; }`. 

Element Selector adalah selctor yang hanya menggunakan nama elemen HTML. Contohnya adalah `h1 { color: orange; }` untuk elemen `<h1>`. 

Browser default tidak memiliki gaya khusus yang diterapkan oleh pengguna. Browser akan menggunakan gaya defaultnya untuk elemen HTML, misalnya heading `<h1>` lebih besar dan tebal daripada paragraf `<p>` secara default.  

**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**  

_Responsive design_ menjadi konsep yang penting dalam pengembangan aplikasi web karena secara langsung akan mempengaruhi _user experience_ pada berbagai perangkat dengan perbedaan ukuran layar. Dalam _responsive design_, elemen pada halaman web akan menyesuaikan ukuran dan tata letaknya berdasarkan ukuran layar. Hal ini memastikan agar pengguna bisa mengakses dan berinteraksi dengan aplikasi web secara nyaman. Tidak hanya berhubungan dengan _user experience_, responsive design juga berhubungan dengan beberapa aspek lainnya, salah satunya adalah dengan SEO. Search engine Google menggunakan **_mobile-first indexing_** yang berarti aplikasi web dengan desain responsif akan lebih diutamakan dalam peringkat hasil pencarian, terutama pada pencarian perangkat mobile.  Contoh aplikasi yang belum menggunakan responsive design adalah aren.cs.ui.ac.id yang merupakan aplikasi untuk melakukang penilaian lab matkul SDA, sedangkan aplikasi yang sudah menggunakan responsive design adalah tokopedia.com yang merupakan salah satu _platform_ jual beli terbesar di Indonesia.

**3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**  

Margin, border, dan padding adalah tiga elemen penting dari CSS Box Model yang digunakan untuk mengatur ruang di sekitar elemen HTML. Masing-masing memiliki fungsi yang berbeda, berikut adalah ciri - ciri dari setiap elemen dan cara implementasinya.  

  A. Padding  
Padding adalah ruang antara konten dari elemen dan batas (border) elemen tersebut. Artinya, padding membuat jarak antara isi elemen dengan tepi elemen itu sendiri. Padding termasuk bagian dari elemen yang dapat mempengaruhi ukuran elemen secara keseluruhan. Cara implementasi padding adalah dengan menggunakan properti padding seperti `padding-top`, `padding-right`, `padding-bottom`, dan `padding-left`.  
```python
    .example {
      padding: 20px; /* Padding di semua sisi */
    }
    
    .example2 {
      padding: 10px 15px; /* Padding atas/bawah 10px, kiri/kanan 15px */
    }
    
    .example3 {
      padding-top: 10px;
      padding-right: 5px;
      padding-bottom: 15px;
      padding-left: 5px;
    }
``` 

  B. Border
Border adalah garis yang membungkus elemen. Border berada di luar padding dan digunakan untuk memberikan garis pembatas di sekitar elemen. Border dapat diatur tebal, gaya (solid, dashed, dotted), dan warna. Cara implementasi border adalah dengan menggunakan properti border seperti `border-top`, `border-right`, `border-bottom`, dan `border-left`.  
```python
  .example {
    border: 2px solid black; /* Border hitam 2px di semua sisi */
  }
  
  .example2 {
    border-top: 5px dashed blue; /* Border atas dengan garis putus-putus biru */
  }
```  

  C. Margin
Margin adalah ruang di luar border elemen. Margin menentukan jarak antara elemen dengan elemen lainnya di halaman. Margin tidak mempengaruhi ukuran elemen itu sendiri, tetapi mempengaruhi ruang di luar elemen tersebut. Cara implementasi margin adalah dengan menggunakan properti margin seperti `margin-top`, `margin-right`, `margin-bottom`, dan `margin-left`.
```python
    .example {
      margin: 20px; /* Margin di semua sisi */
    }
    
    .example2 {
      margin: 10px 15px; /* Margin atas/bawah 10px, kiri/kanan 15px */
    }
    
    .example3 {
      margin-top: 10px;
      margin-right: 5px;
      margin-bottom: 15px;
      margin-left: 5px;
    }
```  

**4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!** 
 
Flexbox adalah model tata letak satu dimensi yang berguna untuk mengatur elemen dalam baris atau kolom secara fleksibel. Flexbox ideal untuk tata letak linear seperti navbar, form, atau grid sederhana. Contoh properti dari flexbox seperti `flex-direction`, `justify-content`, dan `align-items`.  

Contoh kegunaan:  
    a. Navbar: Menyusun navigasi secara horizontal  
    b. Layout tombol: Mengatur tombol dalam satu baris atau kolom  
    c. Form: Mengatur elemen input dalam form secara rapi  
    
Berikut adalah contoh implementasinya:  
```python
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
    }
```  

Grid Layout adalah model tata letak dua dimensi yang memungkinkan pengaturan elemen memanfaatkan baris dan kolom. Grid cocok untuk layout yang lebih kompleks seperti dashboard atau galeri. Contoh properti dari grid seperti `grid-template-columns`, `grid-template-rows`, dan `grid-area`. Berikut adalah contoh implementasinya.   
Contoh kegunaan:  
  a. Dashboard: Menyusun widget atau komponen secara terstruktur  
  b. Galeri gambar: Mengatur gambar dalam beberapa kolom dan baris  
  c. Halaman web yang kompleks: Menyusun tata letak halaman dengan banyak elemen  

Berikut adalah contoh implementasinya:  
```python
    .container {
      display: grid;
      grid-template-columns: 200px 200px;
      grid-gap: 10px;
    }
```
</details>  

<details>
  <summary>Tugas 6</summary>

## Implementasi

#### Ubahlah kode cards data mood agar dapat mendukung AJAX GET.
1. Mengambil Data Product dengan Fetch API  
Fungsi `getProductEntries()` diubah untuk mendapatkan data produk menggunakan AJAX GET dari endpoint yang menampilkan produk dalam format JSON.  

```javascript
async function getProductEntries() {
    return fetch("{% url 'main:show_json' %}") // Mengambil data produk dari endpoint JSON
    .then((res) => res.json()) // Mengubah response ke JSON
}
```
2. Membuat Fungsi untuk Melakukan render Data Produk ke dalam Card  
Setelah mendapatkan data produk, kita perlu merender data tersebut ke dalam bentuk HTML (card). Data ini diambil dari JSON yang diterima dari server. 

```javascript
async function refreshProductEntries() {
    // Menghapus isi kontainer card sebelum me-render ulang
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";

    const productEntries = await getProductEntries(); // Ambil data produk melalui fetch

    let htmlString = "";
    let classNameString = "";

    // Jika data kosong, tampilkan pesan bahwa tidak ada produk
    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/empty.png' %}" alt="Empty product" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada produk di toko.</p>
            </div>
        `;
    } else {
        // Menampilkan data produk dalam bentuk card
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
        productEntries.forEach((item) => {
            const product_name = DOMPurify.sanitize(item.fields.product_name);  // Sanitasi input untuk keamanan XSS
            const description = DOMPurify.sanitize(item.fields.description); // Sanitasi input
            const user_reviews = DOMPurify.sanitize(item.fields.user_reviews);

            htmlString += `
                <div class="relative break-inside-avoid">
                    <div class="relative bg-[#2d46a2] shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform scale-100 hover:scale-105 transition-transform duration-300">
                        <div class="bg-[#fef582] text-black-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                            <h3 class="font-bold text-xl mb-2">${product_name}</h3>
                            <p class="font-bold text-green-600">Rp ${item.fields.price.toLocaleString()}</p>
                        </div>
                        <div class="p-4">
                            <p class="font-semibold text-lg mb-2 text-[#fef582]">Description</p>
                            <p class="text-white mb-2">
                                ${description}
                            </p>
                            <p class="font-semibold text-lg mb-2 text-[#fef582]">Thickness</p>
                            <p class="text-white mb-2">
                                ${item.fields.thickness} mm
                            </p>
                            <div class="mt-4 text-center">
                                <p class="font-semibold mb-2 text-[#fef582]">User Review</p>
                                <p class="italic text-white">"${user_reviews}"</p>
                                <div class="flex justify-center items-center mt-2">
                                    ${[...Array(5)].map((_, i) => i < item.fields.user_ratings
                                      ? `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z"/></svg>`
                                      : `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z"/></svg>`).join('')}
                                </div>
                            </div>
                        </div>
                        <div class="absolute top-2 right-2 flex space-x-1">
                            <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                                </svg>
                            </a>
                            <a href="/delete-product/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                                  <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            `;
        });
    }

    // Menambahkan className dan innerHTML yang baru
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
}

```
3. Memanggil Fungsi Saat Halaman Dimuat  
Fungsi `refreshProductEntries()` harus dipanggil setelah halaman selesai dimuat agar produk bisa langsung tampil.  

```javascript
document.addEventListener("DOMContentLoaded", function () {
    refreshProductEntries(); // Panggil fungsi untuk menampilkan data saat halaman dimuat
});

```

####  Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.

1. Membuat Endpoint yang Mengambil Data Berdasarkan Pengguna yang Logged-in  
Untuk membuat endpoint untuk mengambil data Product berdasarkan pengguna yang sedang logged-in, kita harus melakukan filter pada data Product di `views.py`  

```python
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

2. Menyiapkan AJAX GET untuk Mengambil Data Product  
Snyiapkan Fetch API pada bagian frontend pada `main.html` untuk melakukan permintaan AJAX GET ke endpoint yang sudah dibuat.

```javascript
async function getProductEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }

  async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const productEntries = await getProductEntries(); // Adjust the fetch function accordingly
    let htmlString = "";
    let classNameString = "";

    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">No product data available in the leather store.</p>
            </div>
        `;
    } else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
        productEntries.forEach((item) => {
          const product_name = DOMPurify.sanitize(item.fields.product_name); 
          const description = DOMPurify.sanitize(item.fields.description);
          const user_reviews = DOMPurify.sanitize(item.fields.user_reviews);

            htmlString += `
            <div class="relative break-inside-avoid">
              <div class="relative bg-[#2d46a2] shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform scale-100 hover:scale-105 transition-transform duration-300">
                
                <!-- Header Section -->
                <div class="bg-[#fef582] text-black-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                  <h3 class="font-bold text-xl mb-2">${item.fields.product_name}</h3> <!-- Display product name dynamically -->
                  <p class="font-bold text-green-600">Rp ${item.fields.price.toLocaleString()}</p> <!-- Format price to include commas -->
                </div>
                
                <!-- Content Section -->
                <div class="p-4">
                  
                  <!-- Description Title -->
                  <p class="font-semibold text-lg mb-2 text-[#fef582]">Description</p>
                  <!-- Description Content -->
                  <p class="text-white mb-2">
                    ${item.fields.description}
                  </p>
                  
                  <!-- Thickness Title -->
                  <p class="font-semibold text-lg mb-2 text-[#fef582]">Thickness</p>
                  <!-- Thickness Content -->
                  <p class="text-white mb-2">
                    ${item.fields.thickness} mm
                  </p>

                  <!-- User Rating and Review -->
                  <div class="mt-4 text-center">
                    
                    <!-- User Review Title -->
                    <p class="font-semibold mb-2 text-[#fef582]">User Review</p>
                    <!-- User Review Content -->
                    <p class="italic text-white">"${item.fields.user_reviews}"</p>
                    
                    <!-- Display Star Rating -->
                    <div class="flex justify-center items-center mt-2">
                      ${[...Array(5)].map((_, i) => i < item.fields.user_ratings
                        ? `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z"/></svg>`
                        : `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z"/></svg>`).join('')}
                    </div>
                  </div>
                </div>
                
                <!-- Edit and Delete Buttons -->
                <div class="absolute top-2 right-2 flex space-x-1">
                  <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                  </a>
                  <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/>
                    </svg>
                  </a>
                </div>
              </div>
          </div>

            `;
        });
    }
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
}
```
####  Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.

1. Kode HTML Modal untuk Product Entry  
Kode berikut adalah implementasi modal (Tailwind) pada `main.html`.
```html
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
  <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
    <!-- Modal header -->
    <div class="flex items-center justify-between p-4 border-b rounded-t">
      <h3 class="text-xl font-semibold text-gray-900">
        Add New Product Entry
      </h3>
      <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
        </svg>
        <span class="sr-only">Close modal</span>
      </button>
    </div>
    <!-- Modal body -->
    <div class="px-6 py-4 space-y-6 form-style">
      <form id="productEntryForm">
        <div class="mb-4">
          <label for="product_name" class="block text-sm font-medium text-gray-700">Product Name</label>
          <input type="text" id="product_name" name="product_name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter your product name" required>
        </div>
        <div class="mb-4">
          <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
          <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Describe the product" required></textarea>
        </div>
        <div class="mb-4">
          <label for="price" class="block text-sm font-medium text-gray-700">Price (in Rupiah)</label>
          <input type="number" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product price" required>
        </div>
        <div class="mb-4">
          <label for="thickness" class="block text-sm font-medium text-gray-700">Thickness (mm)</label>
          <input type="number" id="thickness" name="thickness" step="0.01" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
        </div>
        <div class="mb-4">
          <label for="user_reviews" class="block text-sm font-medium text-gray-700">User Reviews</label>
          <textarea id="user_reviews" name="user_reviews" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter user reviews"></textarea>
        </div>
        <div class="mb-4">
          <label for="user_ratings" class="block text-sm font-medium text-gray-700">User Ratings (1-10)</label>
          <input type="number" id="user_ratings" name="user_ratings" min="1" max="10" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
        </div>
      </form>
    </div>
    <!-- Modal footer -->
    <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
      <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
      <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
    </div>
  </div>
</div>
```

2. JavaScript untuk Menampilkan dan Menyembunyikan Modal  
Tailwind yang digunakan adalah _vanilla Tailwind CSS_ sehingga tidak ada _class_ modal yang built-in. karena itu perlu ditambahkan beberapa fungsi di bawah ini pada `main.html`.  
```javascript
<script>
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
</script>
```  

3. Tombol untuk Membuka Modal  
```hTML
<!-- Tombol untuk membuka modal product entry dengan AJAX -->
<button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
  Add New Product by AJAX
</button>

```

4. AJAX untuk Menambahkan Product Entry  
Berikut adalah kode yang digunakan untuk mengirimkan data produk baru menggunakan AJAX setelah pengguna mengisi form di modal

```javascript
<script>
  function addProductEntry() {
    // Menggunakan fetch untuk mengirim data produk dengan metode POST
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => refreshProductEntries()) // Refresh list produk setelah sukses menambahkan
    .catch(error => console.error('Error:', error));

    // Reset form dan sembunyikan modal setelah data dikirim
    document.getElementById("productEntryForm").reset(); 
    hideModal();

    return false;
  }

  // Event listener untuk menangkap submit form dan menjalankan fungsi addProductEntry
  document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProductEntry();
  });
</script>
```

####  Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
**Buat Fungsi View untuk Menambahkan Product Baru**  
Berikut adalah fungsi view untuk menambahkan produk baru ke dalam basis data. Fungsi ini akan memproses permintaan AJAX dan menyimpan produk yang baru ke dalam model Product.  


```python
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    thickness = strip_tags(request.POST.get("thickness"))
    user_reviews = strip_tags(request.POST.get("user_reviews"))
    user_ratings = strip_tags(request.POST.get("user_ratings"))
    user = request.user

    new_product = Product(
        product_name=product_name, price=price,
        description=description, thickness=thickness,
        user_reviews=user_reviews, user_ratings=user_ratings,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
```

#### Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
Import fungsi dan tambahkan jalur routing baru di `urls.py` untuk bisa mengakses fungsi view yang baru saja dibuat.
```python
from main.views import ..., add_product_entry_ajax

urlpatterns = [
  ...
  # URL untuk menambahkan produk baru via AJAX
  path('add-product-entry-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
  ...
]
```
####  Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.  
```javascript
document.getElementById("productEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();  // Mencegah form reload halaman
    addProductEntry();  // Panggil fungsi AJAX
});

```

####  Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.  

Buat fungsi `refreshProductEntries()` untuk menampilkan produk-produk terbaru secara dinamis pada halaman utama. Fungsi ini akan dipanggil setelah data berhasil ditambahkan.

```javascript
async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const productEntries = await getProductEntries(); // Adjust the fetch function accordingly
    let htmlString = "";
    let classNameString = "";

    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">No product data available in the leather store.</p>
            </div>
        `;
    } else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
        productEntries.forEach((item) => {
          const product_name = DOMPurify.sanitize(item.fields.product_name); 
          const description = DOMPurify.sanitize(item.fields.description);
          const user_reviews = DOMPurify.sanitize(item.fields.user_reviews);

            htmlString += `
            <div class="relative break-inside-avoid">
              <div class="relative bg-[#2d46a2] shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform scale-100 hover:scale-105 transition-transform duration-300">
                
                <!-- Header Section -->
                <div class="bg-[#fef582] text-black-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                  <h3 class="font-bold text-xl mb-2">${item.fields.product_name}</h3> <!-- Display product name dynamically -->
                  <p class="font-bold text-green-600">Rp ${item.fields.price.toLocaleString()}</p> <!-- Format price to include commas -->
                </div>
                
                <!-- Content Section -->
                <div class="p-4">
                  
                  <!-- Description Title -->
                  <p class="font-semibold text-lg mb-2 text-[#fef582]">Description</p>
                  <!-- Description Content -->
                  <p class="text-white mb-2">
                    ${item.fields.description}
                  </p>
                  
                  <!-- Thickness Title -->
                  <p class="font-semibold text-lg mb-2 text-[#fef582]">Thickness</p>
                  <!-- Thickness Content -->
                  <p class="text-white mb-2">
                    ${item.fields.thickness} mm
                  </p>

                  <!-- User Rating and Review -->
                  <div class="mt-4 text-center">
                    
                    <!-- User Review Title -->
                    <p class="font-semibold mb-2 text-[#fef582]">User Review</p>
                    <!-- User Review Content -->
                    <p class="italic text-white">"${item.fields.user_reviews}"</p>
                    
                    <!-- Display Star Rating -->
                    <div class="flex justify-center items-center mt-2">
                      ${[...Array(5)].map((_, i) => i < item.fields.user_ratings
                        ? `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z"/></svg>`
                        : `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927a1 1 0 011.902 0l1.454 4.473a1 1 0 00.95.69h4.702c.97 0 1.371 1.24.588 1.81l-3.808 2.718a1 1 0 00-.364 1.118l1.454 4.473c.296.911-.755 1.668-1.539 1.118L10 14.347l-3.808 2.718c-.784.55-1.835-.207-1.539-1.118l1.454-4.473a1 1 0 00-.364-1.118L2.935 9.9c-.784-.57-.382-1.81.588-1.81h4.702a1 1 0 00.95-.69l1.454-4.473z"/></svg>`).join('')}
                    </div>
                  </div>
                </div>
                
                <!-- Edit and Delete Buttons -->
                <div class="absolute top-2 right-2 flex space-x-1">
                  <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                  </a>
                  <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/>
                    </svg>
                  </a>
                </div>
              </div>
          </div>

            `;
        });
    }
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
}

```

## Pertanyaan
### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web! 
a. **Usability: Memodifikasi Halaman Tanpa Perlu Memuat Ulang (UI Lebih Cepat)**  
JavaScript meningkatkan _user experience_ dengan memungkinkan perubahan pada halaman secara _real-time_ tanpa harus memuat ulang seluruh halaman. Misalnya, saat  mengisi formulir, JavaScript bisa langsung menerapkan perubahan tanpa perlu memuat ulang halaman. Hal ini membuat interaksi antara pengguna dengan web menjadi lebih lancar dan mengurangi penundaan waktu akibat muat ulang.

b. **Efficiency: Melakukan Perubahan Kecil dengan Cepat Tanpa Menunggu Server**   
Dengan JavaScript, perubahan kecil bisa dilakukan langsung di browser tanpa perlu mengirim permintaan ke server. Misalnya, validasi input form, melakukan filter hasil pencarian, atau memperbarui konten secara dinamis bisa dilakukan tanpa harus menunggu respon dari server. hal ini akan mengurangi beban pada server dan jaringan, sehingga interaksi terasa lebih cepat dan responsif.  

c. **Event-Driven: Merespons Tindakan Pengguna Seperti Klik dan Tekan Tombol**  
JavaScript memungkinkan aplikasi web untuk merespons tindakan pengguna seperti klik atau hover dengan cepat. Misalnya, fitur seperti dropdown, modal popup, atau tooltip bisa muncul segera setelah pengguna melakukan aksi tertentu. Respon cepat ini membuat aplikasi terasa lebih interaktif dan menarik, sehingga dapat meningkatkan _user ecperience_.

### 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

Fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`adalah untuk menunggu hingga proses pemanggilan API atau permintaan jaringan selesai dan hasilnya tersedia sebelum melanjutkan eksekusi kode selanjutnya. `await` digunakan dalam konteks fungsi `async` untuk membuat kode asinkron terlihat seperti kode sinkron, sehingga lebih mudah dipahami dan ditulis.

Jika `await` tidak digunakan , `fetch()` akan mengembalikan Promise yang belum selesai (_pending promise_), dan eksekusi kode akan berlanjut sebelum permintaan jaringan selesai. Artinya, kode setelah pemanggilan `fetch()` akan dieksekusi tanpa menunggu hasil `fetch()`, yang bisa menyebabkan masalah jika data yang dibutuhkan belum tersedia.

### 3. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST?  
Decorator `@csrf_exempt` digunakan pada view yang akan menerima permintaan POST via AJAX agar Django tidak memeriksa keberadaan token CSRF (_Cross-Site Request Forgery_) pada request tersebut. Secara default, Django mengharuskan setiap permintaan POST untuk menyertakan token CSRF sebagai mekanisme keamanan untuk mencegah serangan CSRF.

### 4.  Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (_backend_) juga. Mengapa hal tersebut tidak dilakukan di _frontend_ saja?  

Pembersihan data input tidak cukup dilakukan di frontend backend tetap harus menangani validasi dan pembersihan data untuk alasan keamanan. Frontend akan berada di sisi pengguna dan bisa dimodifikasi atau dilewati, memungkinkan pengguna untuk mengirimkan data berbahaya seperti script untuk XSS atau SQL Injection. Oleh karena itu, backend mharus memastikan kembali agar data valid dan aman yang diproses.

</details>