# -*- coding: utf-8 -*-

import re

with open ("noricum.html", "r") as myfile:
    clauss=myfile.read().replace('\n', '')

list = re.findall(r"<p><b>Belegstelle:</b>\s(.*?)&nbsp;", clauss)

for x in list:
    # zu unterscheiden sind 2 Fälle:
    # 1. Zeile beginnt mit  <script language="JavaScript">
    # 2. Zeile enthält nur Lit-Verweis

    # in beiden Fällen muss nach folgendem Muster gesucht werden (=> HDNummer)
    #  <a href="partner.php?param=HD042088" target="_blank">
    #
    eintrag = x.strip()
    if re.match("^.script",eintrag): 
      lit = re.search("\)..>(.*?)</a>",eintrag)
      litVerweise = lit.group(1)
      hdnr = re.search("HD\d\d\d\d\d\d",eintrag)
      if hdnr:
        hdnr = hdnr.group()
      else:
        hdnr = ""
      print litVerweise + "\t" + hdnr 
    else:
      hdnr = re.search("HD\d\d\d\d\d\d",eintrag)
      lit = re.search("(.*?)\s<a",eintrag)
      if lit:
        litVerweise = lit.group(1)
      else:
      	litVerweise = eintrag
      if hdnr:
        print litVerweise + "\t" + hdnr.group() 
      else:
      	print litVerweise 


