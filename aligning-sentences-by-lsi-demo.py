# coding: utf-8

# Author: Motaz Saad

import sys
from random import shuffle
##################################################################
#Example Usage:
#python aligning-docs-by-lsi-demo.py ~/corpus/uncorporaorg.0.9.p2.ar ~/corpus/uncorporaorg.0.9.p2.en parallel ~/tmp/docs_aligned_by_lsi/ un ~/tmp/docs_aligned_by_lsi/

def usage():
	print 'Usage: ', sys.argv[0], '<source doc file> <target doc file> <model path> <model name> <output path>'
##################################################################

if len(sys.argv) < 6: usage(); sys.exit(2)

'''
This software is a demo aligning comparable documents using interlanguage links. The method is described in 

Motaz Saad. Mining Documents and Sentiments in Cross-lingual Context. PhD thesis, Université de Lorraine, January 2015.
https://sites.google.com/site/motazsite/Home/publications/saad_phd.pdf

'''

import imp
tp = imp.load_source('textpro', 'textpro.py')


def main(argv):
	source_doc_file = sys.argv[1]
	target_doc_file = sys.argv[2]
	model_path = sys.argv[3]
	model_name = sys.argv[4]
	output_path = sys.argv[5]
	
	source_doc = open(source_doc_file).read().decode('utf-8')
	target_doc = open(target_doc_file).read().decode('utf-8')
	
	source_sentences = tp.pretty_print(source_doc).splitlines()
	target_sentences = tp.pretty_print(target_doc).splitlines()
	
	#shuffle(target_sentences) # ;) 
	
	new_source_sent , new_target_sent = tp.align_sentences_lsi(source_sentences, target_sentences, model_path, model_name) 
	
	source_out = open(output_path + 'source-sentences.txt', 'w')
	target_out = open(output_path + 'target-sentences.txt' , 'w')
	print>>source_out, '\n'.join(new_source_sent).encode('utf-8')
	print>>target_out, '\n'.join(new_target_sent).encode('utf-8')

##################################################################


if __name__ == "__main__":
	main(sys.argv)



