#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   article_tagging_program.py
#   Eifu --Sep. 30
#
#
#
#

import MeCab
import csv
import sys
import string
from sets import Set

try:
    tagger = MeCab.Tagger("mecabrc")
except RuntimeError as e:
print ("RuntimeError: ",e)

    outputF = open("output.txt","w");
    inputF = open("input.csv")

    reader = csv.reader(inputF)

    visited = set([])

    for row in reader:

     article_id = row[0];
     tite_column = row[1];
     article_column = row[2];

         if(validation_row_length and has_id(article_id) and has_html_tag(article_column)):

            m = tagger.parseToNode(row[1])

            prsdText = ""
            while m:
               INDEX_OF_WORD_TYPE = 3
                if(m.feature[:INDEX_OF_WORD_TYPE]!="\xe5\x8a\xa9" and
                    m.feature[:INDEX_OF_WORD_TYPE] != "\xe8\xa8\x98" ):
                    # \xe5\x8a\xa9 <= jodoushi no jo, \xe5\xa8\x98 <= kigou no ki
                    prsdText = prsdText + m.surface + " "

                m = m.next

            outputF.write("%s\t%s\n" % (row[0],prsdText))
            visited.add(row[0])



def validation_row_length(row):
    if(row > 2):return true
    else:return false


def has_id(id_column):
  if(article_column[0].isdigit()):return true
  else:return false

def has_html_tag(article_column):
    if first_char =="<":return true
    else:return false
