 
import  pdfkit
from PyPDF2 import PdfFileMerger
from weasyprint import HTML
from pathlib import Path 
import glob, os

def pdfConverter(path):
	for filename in glob.iglob('./'+path+'/**', recursive=True):
		if os.path.isfile(filename): # filter dirs
		    
		    if filename.endswith('.html'):
		    	
		    	pdfkit.from_file(filename, (filename[:(len(filename)-4)]+'.pdf'))
		    	
		    	

i = 0
foldPath = './grokking'
for folder in os.listdir('./grokking'):
	for subFolder in os.listdir(foldPath+'/'+folder):	
		merger = PdfFileMerger()	 
		for subSubFolder in os.listdir(foldPath+'/'+folder+'/'+subFolder):
			print(foldPath+'/'+folder+'/'+subFolder+'/'+subSubFolder)
	#		merger.append(open(foldPath+'/'+folder+'/'+subFolder+'/'+subSubFolder, 'rb'))
	#	merger.write('/pdf/'+subFolder+'.'+subSubFolder+".pdf")
	#	merger.close()
				
print(i)

 
