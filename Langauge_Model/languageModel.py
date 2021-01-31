#import paho.mqtt.publish as publish
#import paho.mqtt.client as mqtt
import wikipedia
from Langauge_Model import parshingJSON as pharser
wikipedia.set_lang("id")

kalimat1 = None
kalimat2 = None
kalimat3 = None

def doSearch(query):
	try:
		result = wikipedia.summary(query)
		hasil = pharse_WikiResult(result)
		return hasil
	except Exception as EX:
		print("exceotion occur", EX)
		return Exception
		pass
		

def pharse_WikiResult(data):
	global kalimat1,kalimat2,kalimat3
	firstIndex = 0
	secondIndex= 0 
	lastIndex = 0
	index = 0
	for doIndexing in range(3):
		index = data.find(".",index+1)
		if doIndexing == 0:
			firstIndex = index+2
		if doIndexing == 1:
			secondIndex = index+2
		#print(index)
		lastIndex = index
	
	kalimat1 = data[:firstIndex]
	kalimat2 = data[firstIndex:secondIndex]
	kalimat3 = data[secondIndex:lastIndex]
		
	#paragraf = prettyIntro(kalimat1,kalimat2)
def original_WkiResult():
	global kalimat1,kalimat2,kalimat3
	paragraf = kalimat1+kalimat2+kalimat3
	return str(paragraf)

def prettyIntro():
	global kalimat1,kalimat2,kalimat3
	try:
		#hilangkan sebelum koma di kalimat terahir
		index = kalimat2.find(",")
		#kalimat2 = kalimat2[index: ]
		paragraf = kalimat1[:-1]+kalimat2
		return paragraf
	except Exception as EX:
		print("exceotion occur", EX)
		msg = Exception, "cek penulisan topic"
		return str(msg)
		pass
	
#======================================================================================================================
'''
topic = input("topic? ")
when = input("when? ") 
what = input("what? ")
who = input("who? ")
where = input("where? ")
why = input("why? ")
print("\n=====================================================================================================================\n")
#when,what,who,where = "25 Januari", "Pelayanan posyandu", "Bidan kabupaten, warga dusun Jeruk dan Pakuran", "balai desa"
'''
def do_run(data):
	topic,when,what,who,where,why = pharser.handler(data)
	
	paragraf1=("Pada tanggal {} telah dilakukan kegiatan {}. Kegiatan {} dilaksankaan di {} yang diikuti oleh {}.".format(when,what,topic,where,who))
	doSearch(topic)
	#print(original_WkiResult())
	paragraf2=prettyIntro()
	paragraf3=("Tujuan dari dilakukannya kegiatan ini adalah agar {}".format(why))
	return(paragraf1,paragraf2,paragraf3)

