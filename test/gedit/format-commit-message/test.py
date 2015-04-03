'''
Run the test from terminal:
$ python test/gedit/format-commit-message/test.py
'''

import os
import subprocess
import xml.etree.ElementTree as ElementTree

formatterLocation = './.config/gedit/tools/format-commit-message'
testXmlLocation = './test/gedit/format-commit-message/xml/'

class FormatterFileTest:
	def __init__(self, filename=None):
		self.filename = filename

	def assertEqual(self, expected, actual):
		if expected != actual:
			print '##################################### ' + self.filename
			print '### Message was:'
			print actual
			print '### Expected:'
			print expected
			return False
		return True

	def test(self):
		root = ElementTree.parse(self.filename).getroot()
		message = root.find('message').text.strip()
		expected = root.find('expected').text.strip()
		
		cmd = ['python', formatterLocation]
		process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		formattedMessage = process.communicate(message)[0][:-1]
		return self.assertEqual(expected, formattedMessage)

class FormatterTest:

	def testAll(self):
		successCounter = 0
		failCounter = 0
		failedCases = []
		for filename in os.listdir(testXmlLocation):
			if not filename.endswith('.xml'):
				continue

			success = FormatterFileTest(testXmlLocation + filename).test()
			if not success:
				failedCases.append(filename)
				failCounter = failCounter + 1
			else:
				successCounter = successCounter + 1

		print '#####################################'
		print 'Success: ' + str(successCounter) + ', Failed ' + str(failCounter)
		print failedCases

if __name__ == '__main__':
	FormatterTest().testAll()
