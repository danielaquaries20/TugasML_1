class Rekening:
    def __init__(self):
        self.__saldo = 0

    def kredit(self, jumlah):
        if jumlah < 0:
            print("Gagal Kredit, Jumlah tidak bisa kurang dari 0")
            return

        self.__saldo += jumlah

    def debit(self, jumlah):
        if jumlah > self.__saldo:
            print("Gagal Debit, Jumlah melebihi Saldo!")
            return

        if jumlah < 0:
            print("Gagal Debit, Jumlah tidak bisa kurang dari 0")
            return

        self.__saldo -= jumlah

    def cetakSaldo(self):
        print("Saldo saat ini " + str(self.__saldo))


bniBudi = Rekening()

bniBudi.kredit(9999999)
bniBudi.cetakSaldo()
bniBudi.debit(100000)
