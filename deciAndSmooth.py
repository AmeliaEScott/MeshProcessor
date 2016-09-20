import glob # can get list of files in directory
import subprocess # can call terminal commands
import sys

if len(sys.argv) <= 1:
	print 'Include the base directory when calling this script. For example: deciAndSmooth.py test/'
	sys.exit()

baseDir = sys.argv[1]
if not baseDir.endswith('/'):
	baseDir += '/'


print repr(glob.glob(baseDir + '*.obj'))

files = glob.glob(baseDir + '*.obj')
command = 'meshlabserver -s test.mlx -i %s -o %s'

with open('test.mlx') as script:
	scriptText = script.read().replace('<Param type="RichFloat" value=".2" name="TargetPerc"/>', '<Param type="RichFloat" value="%f" name="TargetPerc"/>')	
	
for fileName in files:
	numVertices = 0
	with open(fileName) as obj:
		line = obj.readline()
		for line in obj:
			print line
			if line.startswith('v '):
				numVertices += 1
				
	print 'File: ' + fileName + ', num vertices: ' + str(numVertices)
	
	#with open('newScript.mlx', 'w+') as scriptOutput:
	#	scriptOutput.write(scriptText % 7.0)
	
	# newCommand = command % (fileName, 'testResults/' + fileName)
	# subprocess.call(newCommand)
