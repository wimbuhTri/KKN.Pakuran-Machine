import json

def handler(data):
	jsonIfyed = json.loads(data)
	topic = jsonIfyed["topic"]
	when = jsonIfyed["when"]
	what =jsonIfyed["what"]
	who =jsonIfyed["who"]
	where =jsonIfyed["where"]
	why =jsonIfyed["why"]
	return(topic,when,what,who,where,why)

def JSONing(p1,p2,p3):
	final = '{"P1":"%s","P2":"%s","P3":"%s"}'%(p1,p2,p3)
	return final
