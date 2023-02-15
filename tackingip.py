#!/bin/usr/python
import geocoder

#Kode warna
r = "\033[91m" #red
g = "\033[92m" #green
y = "\033[93m" #yellow
c = "\033[96m" #cyan
p = "\033[95m" #pink
w = "\033[37m" #white
b = "\033[94m" #blue

#Banner
banner = """
{}__________________________________________
{}|__  __|      |  ____|   |  _|  |  |  __  |
{}  |  |   __|	|  |   |   |_|  __|  | _____|
{}  |  |  |  |	|  |___|    _  |__|  |  |
{}  |__|__|__|__|______|___|_|____|__|__|
{}----------------------------------------------------
{}|     {}Author {}: {}KobarX                              {}|
{}|     {}Fungsi {}: {}TrackIp                             {}|
{}|     {}Github {}: {}https://https://github.com/KOBARX   {}|
{}----------------------------------------------------
""".format(w,w,r,r,r,w,w,p,b,c,w,w,p,b,c,w,w,p,b,c,w,w)

print(banner)

try:
	while True:
		teks = input(w+"\n["+y+"?"+w+"]"+y+" Masukkan IP Nya Dude: ")

		#Jika user gk nginput
		if teks == "":
			print(w+"["+r+"!"+w+"]"+r+" Masukkan IP yg Bener Laa!")
			break

		scan = geocoder.ipinfo(teks)

		print(r+"\n["+g+"+"+r+"]"+g+" Alamat          "+w+": ", scan.address)
		print(r+"["+g+"+"+r+"]"+g+" Kota            "+w+": ", scan.city)
		print(r+"["+g+"+"+r+"]"+g+" Negara          "+w+": ", scan.country)
		print(r+"["+g+"+"+r+"]"+g+" Hostname        "+w+": ", scan.hostname)
		print(r+"["+g+"+"+r+"]"+g+" IP address      "+w+": ", scan.ip)
		print(r+"["+g+"+"+r+"]"+g+" Latitude        "+w+": ", scan.lat)
		print(r+"["+g+"+"+r+"]"+g+" Longitude       "+w+": ", scan.lng)
		print(r+"["+g+"+"+r+"]"+g+" IP nya valid    "+w+": ", scan.ok)
		print(r+"["+g+"+"+r+"]"+g+" ORG/Jenis Ny    "+w+": ", scan.org)
		print(r+"["+g+"+"+r+"]"+g+" Kode/Postal     "+w+": ", scan.postal)

		ulang = str(input(w+"["+y+"?"+w+"]"+y+" Lacak lagi? [Y/n] "))

		#Tanya user mau ulang apa gk
		if ulang == "Y":
			continue
		else:
			print(w+"["+g+"+"+w+"]"+g+" Ok")
			break

#Jika user memaksa keluar dengan CTRL + C
except KeyboardInterrupt:
	print(w+"["+g+"+"+w+"]"+g+"Bye-bye\n"+w+"["+g+"+"+w+"]"+g+"Makasih Dah Pakee")

