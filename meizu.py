import os, sys

print ("\033[1;32mMasukkan Username & Password Bro..")

print ("\033[1;32msilahkan hubungi RR ")

username = 'roni'      

password = 'qwerty1234'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mOk sipp masuuk.....", 

			sys.exit()



		else:

			print "\033[1;32mMaaf Masukkan password salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Masukkan Username salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
