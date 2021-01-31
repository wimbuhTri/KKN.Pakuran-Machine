def testNone(data):
	try:
		if len(data) > 1:
			print("ok")
		else:
			print("no")
	except Exception as EX:
		print("exceotion occur")
		print(EX)
		pass