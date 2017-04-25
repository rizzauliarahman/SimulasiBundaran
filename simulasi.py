import waktuKedatanganGenerator
import waktuLayananGenerator
import numpy as np

def main():
    kedGen = waktuKedatanganGenerator.generator(a=29, c=5, m=196, seed=27)
    kedatangan = kedGen.generateData()

    kedGen.showTabelWaktuKedatangan()

    layGen = waktuLayananGenerator.generator(a=21, c=7, m=200, seed=25)
    layanan = layGen.generateData()

    layGen.showTabelWaktuLayanan()

main()
