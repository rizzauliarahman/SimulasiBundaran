import numpy as np
import tabulate
from openpyxl import Workbook
from openpyxl.styles import Alignment

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

        self.x = self.x[1:]
        self.U = self.U[1:]
        self.data = self.data[1:]

        return self.x, self.U, self.data

    def showTabelWaktuLayanan(self, filename):

        wb = Workbook(write_only=False, read_only=False)
        ws = wb.active
        ws.append(['Mobil ke-', 'LCG Number', 'Angka Uniform', 'Waktu Layanan (detik)'])

        for i in range(100) :
            ws.append([i+1, self.x[i], self.U[i], self.data[i]])

        for col in ws.columns:
            max_length = 0
            column = col[0].column
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                    cell.alignment = Alignment(horizontal='center')
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column].width = adjusted_width

        wb.save(filename)

        # f.write('\n Tabel Waktu di Bundaran\n')
        # f.write(tabulate.tabulate(tableData, headers=['Mobil ke-','yi','Ui','Si(s)'], tablefmt='psql', numalign='center'))
        # f.write('\n Keterangan : \n')
        # f.write('yi : LCG waktu layanan\n')
        # f.write('Ui : Uniform number\n')
        # f.write('Si : Waktu layanan')
