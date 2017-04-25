import numpy as np
import tabulate

class generator :

    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed
        self.data = np.zeros((101), dtype=float)
        self.x = np.zeros((101), dtype=int)
        self.U = np.zeros((101), dtype=float)

    def generateData(self):

        for i in range(101):
            if i == 0:
                self.x[i] = self.seed
            else :
                self.x[i] = ((self.x[i-1] * self.a) + self.c) % self.m
            self.U[i] = float(self.x[i]) / float(self.m)
            self.data[i] = -100 * np.log((1 - self.U[i]))

        self.U = np.around(self.U, decimals=2)
        self.data = self.data.astype(dtype=int)

        return self.x, self.U, self.data

    def showTabelWaktuKedatangan(self):

        f = open('waktuKedatangan.txt', mode='w')

        tableData = []

        for i in range(1, 101) :
            tableData.append([i, self.x[i], self.U[i], self.data[i]])

        f.write('\n Tabel Waktu antar Kedatangan di Bundaran\n')
        f.write(tabulate.tabulate(tableData, headers=['Mobil ke-','xi','Ui','Ai(s)'], tablefmt='psql', numalign='center'))
        f.write('\n Keterangan : \n')
        f.write('xi : LCG Antar waktu kedatangan\n')
        f.write('Ui : Uniform number\n')
        f.write('Ai : Waktu antar kedatangan')

        f.close()
