#!/usr/bin/python



from parse.kth_extract.pdfssa4met import kthextract

import os, sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))+"/.."  # This is your Project Root

download_dir = ROOT_DIR + "/Source"


def main(argv=None):

	if argv is None:
		argv = sys.argv[1:]

	print 'Preperation for parse module start'
	#path = os.getcwd()
	#print path
	#os.chdir(path)
	os.chdir('/home/maguire/connecting_silos/connecting_silos_kththesis_TCOMK_CINTE/polls/src/parse/kth_extract/pdfssa4met')
	print os.getcwd()
	print 'Preperation for the parse module done'
	print  argv[0]

	if argv[0].endswith(".pdf"):
		#if "-" in argv[0]:
			   print argv[0]
			   #source = os.path.join(download_dir, file)
			   #destination = os.path.join(download_dir, file.replace("-", "_"))
			   #os.rename(source, destination)
			   #file = file.replace("-", "_")
			   #pdf_locl_path = os.path.()
			   print "found pdf file: " + argv[0]

			   kthextract.main([argv[0], 0]) #0 for thesis, 1 for proposal
			   print 'Done with parse module'
			   print 'Whole process done'


if __name__ == '__main__':
    main()
