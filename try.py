import unittest
import xmlrunner

def runner(output='python_test_xml'):
	return xmlrunner.XMLTestRunner(
		output=output
	)
	
def find_test():
	return unittest.TestLoader().discover('pystache')

if __name__=='__main__':
	runner().run(find_tests())