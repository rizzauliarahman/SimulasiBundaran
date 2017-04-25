from openpyxl import Workbook
from openpyxl.styles import Alignment

def saveRataRata(listWaktuAntri, listWaktuSistem):
    wb = Workbook(write_only=False, read_only=False)
    ws = wb.active
    ws.append(['Replikasi ke-', 'Rata-rata waktu dalam sistem (s)'])

    for i in range(len(listWaktuSistem)) :
        ws.append([i+1, listWaktuSistem[i]])

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

    wb.save('.\Verifikasi\Replikasi_WaktuSistem.xlsx')

    ##############################################################################

    wb = Workbook(write_only=False, read_only=False)
    ws = wb.active
    ws.append(['Replikasi ke-', 'Rata-rata waktu dalam antrian (s)'])

    for i in range(len(listWaktuAntri)):
        ws.append([i + 1, listWaktuAntri[i]])

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

    wb.save('.\Verifikasi\Replikasi_WaktuAntri.xlsx')