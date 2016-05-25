import mosaic
import base64

def enc(func):
	def f(s):
		return base64.b64encode(func(s))
	return f

@enc
def dl_osx(baseurl):
	return "{0}{1}/mosaic-{1}-{2}.dmg".format(baseurl, mosaic.__version__, mosaic.__build__)
	# return "{0}1.2/mosaic-1.2.dmg".format(baseurl)


@enc
def dl_win(baseurl):
	return "{0}{1}/mosaic-x64-{1}-{2}.zip".format(baseurl, mosaic.__version__, mosaic.__build__)
	# return "{0}1.2/mosaic-x64-1.2.zip".format(baseurl)

@enc
def readfile(fname):
	with open(fname, 'r') as f:
		return f.read()
@enc
def updateVers(verlist):
	return verlist

updatejson="""{
		"version" 			: '"""+base64.b64encode(str(mosaic.__version__))+"""',
		"build"				: '"""+base64.b64encode(str(mosaic.__build__))+"""',
		"update-versions"	: '"""+updateVers("""["1.0", "1.1", "1.2", "1.3b1"]""")+"""', 
		"changelog"			: '"""+readfile('../README.rst')+"""',
		"dl-w64"			: '"""+dl_win("https://github.com/usnistgov/mosaic/releases/download/v")+"""',	
		"dl-osx"			: '"""+dl_osx("https://github.com/usnistgov/mosaic/releases/download/v")+"""'
	}"""

with open('version.json', 'w') as f:
	 f.write( base64.b64encode( updatejson.replace("'",'"') ) )
