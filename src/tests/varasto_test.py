import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    
    def test_varaston_tilavuus_ei_voi_olla_negatiivinen(self):
        self.varasto = Varasto(-3)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)
    
    def test_varaston_saldo_ei_voi_olla_negatiivinen(self):
        self.varasto = Varasto(10, -3)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
    def test_varastosta_otetaan_liikaa(self):
        self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_varastoon_liian_suuri_lisays(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
    
    def test_varastoon_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
    def test_varastosta_otetaan_negatiivinen_maara(self):
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
    


