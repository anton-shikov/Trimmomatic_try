#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:07:28 2018

@author: anton
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trimmomatic_try')
    parser.add_argument('-isq', help='Input sequence', metavar='Str',type=str)
    parser.add_argument('-hd', help='Input Headcrop parameter', metavar='Int',type=int, default = 0)
    parser.add_argument('-tl', help='Input Tailcrop parameter', metavar='Int',type=int, default = 0)
    parser.add_argument('-wn', help='Input Sliding clip size', metavar='Int',type=int, default = 5)
    parser.add_argument('-th', help='Input quality ', metavar='Int',type=int, default = 0)
    parser.add_argument('-osq', help='Output sequence', metavar='Str',type=str)
    args = parser.parse_args()
    inseq=args.isq
    head=args.hd
    tail=args.tl
    win=args.wn
    thres=args.th
    outseq=args.osq
    record_outlist = []
    def crop (rec):
        return(rec[head-1:len(str(rec.seq))-tail])
    def slide_win (rec):
        star=0
        for i in range(len(rec.letter_annotations["phred_quality"])+1-win):
           meanq=sum(rec.letter_annotations["phred_quality"][star:star+win])/win
           if meanq<thres:
               rec = rec[0:star]
           star+=1
           if len(rec)<2:
               pass
           else: 
               return(rec)
    for record in SeqIO.parse(inseq, 'fastq'): 
        if not (slide_win(crop(record)) is None):
            record_outlist.append(slide_win(crop(record)))
    SeqIO.write(record_outlist, outseq, 'fastq')
