def hitung_bmi(berat, tinggi):

    hasil = int(berat) / (float(tinggi) * float(tinggi))

    print(hasil)

    if(hasil < 17.0):
        print("anda sangat kurus")
    if(hasil >= 17.0 and hasil < 18.0):
        print("anda cukup kurus")
    if(hasil > 18.0 and hasil < 25.0):
        print("anda normal")
    if(hasil > 25.0 and hasil < 27.0):
        print("anda cukup gemuk")
    if(hasil > 27.0):
        print("anda obesitas")
    
