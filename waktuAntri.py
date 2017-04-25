import numpy as np
from openpyxl import Workbook
from openpyxl.styles import Alignment

class waktuAntri:

    def __init__(self, A, S):
        self.A = A
        self.S = S
        self.waktuDatang = np.zeros((100), dtype=int)
        self.mulaiLayanan = np.zeros((100), dtype=int)
        self.selesaiLayanan = np.zeros((100), dtype=int)
        self.waktuMengantri = np.zeros((100), dtype=int)
        self.waktuSistem = np.zeros((100), dtype=int)

    def hitungWaktuAntri(self):

        for i in range(100):
            if i == 0 :
                self.waktuDatang[i] = 0 + self.A[i]
                self.mulaiLayanan[i] = self.waktuDatang[i]
            else :
                self.waktuDatang[i] = self.waktuDatang[i-1] + self.A[i]
                selisih  = self.selesaiLayanan[i-1] - self.waktuDatang[i]

                if selisih < 0 :
                    selisih = 0

                self.mulaiLayanan[i] = self.waktuDatang[i] + selisih

            self.selesaiLayanan[i] = self.mulaiLayanan[i] + self.S[i]

        self.waktuMengantri = self.mulaiLayanan - self.waktuDatang
        self.waktuSistem = self.selesaiLayanan - self.waktuDatang

    def showTabelDES(self, filename):

        wb = Workbook(write_only=False, read_only=False)
        ws = wb.active
        ws.append(['Mobil-ke', 'Waktu datang (detik)', 'Waktu Mulai (detik)', 'Waktu Layanan (detik)', 'Waktu Selesai (detik)',
                   'Waktu Dalam Antrian (detik)', 'Waktu Dalam Sistem (detik)'])

        for i in range(100):
            ws.append([i+1, self.waktuDatang[i], self.mulaiLayanan[i], self.S[i], self.selesaiLayanan[i],
                       self.waktuMengantri[i], self.waktuSistem[i]])

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

    def hitungRataRata(self, filename):

        rataWaktuMengantri = 0.0
        rataWaktuSistem = 0.0

        totalWaktuMengantri = np.sum(self.waktuMengantri)
        totalWaktuSistem = np.sum(self.waktuSistem)

        rataWaktuMengantri = round((float(totalWaktuMengantri) / float(len(self.waktuMengantri))), 2)
        rataWaktuSistem = round((float(totalWaktuSistem) / float(len(self.waktuSistem))), 2)

        f = open(filename, mode='w')

        f.write('Rata-Rata waktu Mobil dalam antrian : ' + repr(rataWaktuMengantri) + ' detik\n')
        f.write('Rata-Rata waktu Mobil dalam bundaran : ' + repr(rataWaktuSistem) + ' detik')

        f.close()

        return rataWaktuSistem, rataWaktuMengantri

