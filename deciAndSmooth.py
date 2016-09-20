import glob # can get list of files in directory
import subprocess # can call terminal commands
import sys

if len(sys.argv) <= 2:
	print 'Include the base directory and output directory when calling this script.'
	print 'For example: python deciAndSmooth.py testinput/ testoutput/'
	sys.exit()

baseDir = sys.argv[1]
outputDir = sys.argv[2]
if not baseDir.endswith('/'):
	baseDir += '/'
if not outputDir.endswith('/'):
	outputDir += '/'

files = glob.glob(baseDir + '*.obj')
command = 'meshlabserver -s test.mlx -i %s -o ' + outputDir + '%s'

with open('test.mlx') as script:
	scriptText = script.read().replace('<Param type="RichFloat" value=".2" name="TargetPerc"/>', '<Param type="RichFloat" value="%f" name="TargetPerc"/>')	
	
for fileName in files:
	numFaces = 0
	with open(fileName) as obj:
		line = obj.readline()
		for line in obj:
			# print line
			if line.startswith('f '):
				numFaces += 1
				
	print 'File: ' + fileName + ', num vertices: ' + str(numFaces)
	shortFileName = fileName.replace(baseDir, '', 1)
	if numFaces > 100:
		with open('newScript.mlx', 'w+') as scriptOutput:
			scriptOutput.write(scriptText % 7.0)
			
		newCommand = command % (fileName, shortFileName)
		print newCommand
		subprocess.call(newCommand)
	else:
		print 'Not running filters for file ' + fileName
