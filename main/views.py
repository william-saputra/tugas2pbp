from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Leather Store',
        'name': 'William Matthew Saputra',
        'class': 'PBP F',
        'product': 'New Ontario Synthetic Leather',
        'price': 75000,
        'thickness': 1.0,
        'description': 'Ontario memiliki ukuran 1,37 meter x 1 meter dengan ketebalan 0,5 mm.\n'
                        'Beratnya mencapai 350 gram per meter, terbuat dari bahan PVC yang kuat dan tahan lama.\n'
                        'Selain itu, produk ini dilengkapi dengan backing yang berbahan knitted, memberikan dukungan ekstra untuk keawetan dan kenyamanan penggunaannya.',
        'user_reviews': 'Bagus bgt packing bener2 aman bgt Recomend banget nih toko nya ayo guyss buruan order ditoko ini.. Terimakasih.',


        
    }

    return render(request, "main.html", context)