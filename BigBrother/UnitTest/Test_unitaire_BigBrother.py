
import unittest

class Test_BigBrother(unittest.TestCase) :

    def test_ItemValidation_True(self) :
        self.assertEqual(test_ItemValidation(["Vin"], ["Brioche", "Vin", "Eau"]), bool(True))
        self.assertEqual(test_ItemValidation(["Vin"], ["Vin"]), bool(True))

    def test_ItemValidation_False(self) :
        self.assertEqual(test_ItemValidation(["Vin"], ["Brioche", "Pain", "Eau"]), bool(False))
        self.assertEqual(test_ItemValidation(["Vin"], ["Pain"]), bool(false))

    def test_memoryArticle_True(self) :
        self.assertEqual(memoryArticle("Pain", "Vin, Biere, "), "Vin, Biere, Pain")

    def test_CalculateSpendDaySum_True(self) :
        self.assertEqual(calculateSpendDaySum(130, 25), 155)
        self.assertEqual(calculateSpendDaySum(130, 0), 130)
        self.assertEqual(calculateSpendDaySum(0, 25), 25)
        self.assertEqual(calculateSpendDaySum(130, -25), 105)
        self.assertEqual(calculateSpendDaySum(-25, 130), 105)

    def test_HabBuyDay_True(self) :
        self.assertEqual(updateHabBuyDay([0,0,1,0,1,1,0], 2), [0,1,1,0,1,1,0])

if __name__ == '__main__' :
    unittest.main()
