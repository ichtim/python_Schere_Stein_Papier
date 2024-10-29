import random
from enum import Enum
from PIL import Image
class Zug:
	class val(Enum):
		STEIN,SCHERE,PAPIER,BRUNNEN=range(4)
		def sieger(self,zug2):
			if self.value==zug2.value:
				return 0
			else:
				s=0
				match 1:
					case 1 if set((self.value,zug2.value))==set((Zug.val.STEIN.value,Zug.val.SCHERE.value)):
						s=Zug.val.STEIN
					case 1 if set((self.value,zug2.value))==set((Zug.val.STEIN.value,Zug.val.PAPIER.value)):
						s=Zug.val.PAPIER
					case 1 if set((self.value,zug2.value))==set((Zug.val.STEIN.value,Zug.val.BRUNNEN.value)):
						s=Zug.val.BRUNNEN
					case 1 if set((self.value,zug2.value))==set((Zug.val.SCHERE.value,Zug.val.PAPIER.value)):
						s=Zug.val.SCHERE
					case 1 if set((self.value,zug2.value))==set((Zug.val.SCHERE.value,Zug.val.BRUNNEN.value)):
						s=Zug.val.BRUNNEN
					case 1 if set((self.value,zug2.value))==set((Zug.val.PAPIER.value,Zug.val.BRUNNEN.value)):
						s=Zug.val.PAPIER
				if s.value==self.value:
					return 1
				else:
					return -1
	loc=[i+'.png'for i in['stein','schere','papier','brunnen']]
	img=[Image.open(i) for i in loc]
#	Züge={i.value:[i.name,j]for (i,j) in zip(val,loc)}
	Züge={i.value:[i.name,j]for (i,j) in zip(val,img)}
	def zufallszug():
		return Zug.val(random.randint(0,3))
