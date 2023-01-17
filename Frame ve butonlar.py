from tkinter import *
from time import strftime
from time import *


master = Tk()
master.title("Kullanıcı Arayüzü") #Master penceresine isim verme
canvas = Canvas(master, height=800, width=1800) # Ana Pencere Boyutu ayarlama
canvas.pack()           # pack place grid 3 tane ekleme seçeneği var


#3  tane frame yapısından oluşan bir arayüz tasarladık

frame_ust = Frame(master, bg='#add8e6')
frame_ust.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.1) # rel x ve rel y de framenin_üst nerden başlıcağını gösteriyor
frame_alt_sol = Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.7)
frame_alt_sag = Frame(master, bg='#add8e6')
frame_alt_sag.place(relx=0.32, rely=0.25, relwidth=0.58, relheight=0.7)


def aktif_saat():
    # aktif bir saat fonksiyonu tanımlayarak saat verisini ekrana yazdırmak için kullanıyoruz1
    time_string = strftime("%d/%m/%Y\n%H:%M:%S")
    tarih_saat.config(text=time_string)
    tarih_saat.after(1000,aktif_saat)

# Tarih ve saat
tarih_saat = Label(frame_ust,bg='#add8e6', font="verdana 9 bold")
tarih_saat.pack(pady=10,padx=10, side=RIGHT)
tarih = Label(frame_ust,bg='#add8e6',text="Tarih:\nSaat:", font="verdana 9 bold")
tarih.pack(pady=10,padx=10, side=RIGHT)



Dosya_secme_butonu=Button(frame_alt_sol, text="Dosya seç",height= 5, width=15).pack(pady=10,padx=10, )

Dosya_bilgileri_ayarla=Button(frame_alt_sol, text="Program Veriler Giriş",height= 5, width=15).pack(pady=10,padx=10, )

Başlatma=Button(frame_alt_sol, text="programı başlat",height= 5, width=15).pack(pady=10,padx=10 )

Manuel_Mod=Button(frame_alt_sol, text="Manuel Mod",height= 5, width=15).pack(pady=10,padx=10 )


aktif_saat()
master.mainloop()