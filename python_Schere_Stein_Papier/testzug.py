import zug
import unittest
class Test_Zug(unittest.TestCase):
	def test_sieger(self):
		for v in zug.Zug.val:
			self.assertEqual(zug.Zug.val.sieger(v,v),0)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.STEIN,zug.Zug.val.SCHERE),1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.STEIN,zug.Zug.val.PAPIER),-1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.STEIN,zug.Zug.val.BRUNNEN),-1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.SCHERE,zug.Zug.val.STEIN),-1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.SCHERE,zug.Zug.val.PAPIER),1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.SCHERE,zug.Zug.val.BRUNNEN),-1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.PAPIER,zug.Zug.val.STEIN),1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.PAPIER,zug.Zug.val.SCHERE),-1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.PAPIER,zug.Zug.val.BRUNNEN),1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.BRUNNEN,zug.Zug.val.STEIN),1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.BRUNNEN,zug.Zug.val.SCHERE),1)
		self.assertEqual(zug.Zug.val.sieger(zug.Zug.val.BRUNNEN,zug.Zug.val.PAPIER),-1)
if __name__=='__main__':
	unittest.main()
