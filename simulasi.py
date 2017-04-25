import waktuKedatanganGenerator
import waktuLayananGenerator
import waktuAntri
import randomGenerator as rand
import saveData as save
import numpy as np

def main():

    listWaktuAntri = []
    listWaktuSistem = []

    for i in range(1, 11):

        rataMengantriPerRep = []
        rataSistemPerRep = []

        for j in range(1, 5):

            a, c, m, seed = rand.randomizeParam()
            kedGen = waktuKedatanganGenerator.generator(a=a, c=c, m=m, seed=seed)
            kedatangan = {}
            kedatangan['x'], kedatangan['U'], kedatangan['A'] = kedGen.generateData()

            kedGen.showTabelWaktuKedatangan(filename='.\Simulasi '+ repr(i) +'\waktuKedatangan_' + repr(j) + '.xlsx')

            a, c, m, seed = rand.randomizeParam()
            layGen = waktuLayananGenerator.generator(a=a, c=c, m=m, seed=seed)
            layanan = {}
            layanan['x'], layanan['U'], layanan['S'] = layGen.generateData()

            layGen.showTabelWaktuLayanan(filename='.\Simulasi '+ repr(i) +'\waktuLayanan_' + repr(j) + '.xlsx')

            DesGen = waktuAntri.waktuAntri(A=kedatangan['A'], S=layanan['S'])
            DesGen.hitungWaktuAntri()
            DesGen.showTabelDES(filename='.\Simulasi '+ repr(i) +'\TabelDES_' + repr(j) + '.xlsx')

            rataSistem, rataMengantri = DesGen.hitungRataRata(filename='.\Simulasi '+ repr(i) + '\RataRata_' + repr(j) + '.txt')

            rataMengantriPerRep.append(rataMengantri)
            rataSistemPerRep.append(rataSistem)

        listWaktuAntri.append(round(np.sum(rataMengantriPerRep) / float(len(rataMengantriPerRep)), 2))
        listWaktuSistem.append(round(np.sum(rataSistemPerRep) / float(len(rataSistemPerRep)), 2))

    save.saveRataRata(listWaktuAntri, listWaktuSistem)


main()
