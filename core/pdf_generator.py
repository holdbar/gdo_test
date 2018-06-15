#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id$
#
# Basic starter:
# Create some simple text, vector graphics and image output
#
# required software: PDFlib/PDFlib+PDI/PPS 9
# required data: none
#
from __future__ import unicode_literals, print_function

from sys import exc_info
from traceback import print_tb
from PDFlib.PDFlib import *
"""
x = 55
center = 140
y = 80
yoff = 15 

p = PDFlib()
"""
def generate_pdf(answers, x=55,center=140,y=80,yoff=15,p=PDFlib()):

    try:
        # This means we must check return values of load_font() etc.
        p.set_option("errorpolicy=return")
        p.begin_document("form.pdf", "")
        p.begin_page_ext(0, 0, "width=a4.width height=a4.height topdown")

        # Setting font properties
        italicfont = p.load_font("Courier-Oblique", "unicode", "")
        if italicfont == -1:
            raise PDFlibException("Error: " + p.get_errmsg())
        boldfont = p.load_font("Courier-Bold", "unicode", "")
        if boldfont == -1:
            raise PDFlibException("Error: " + p.get_errmsg())
        regularfont = p.load_font("Courier", "unicode", "")
        if regularfont == -1:
            raise PDFlibException("Error: " + p.get_errmsg())

        # head (1 row)
        p.fit_textline("NOTICE: THIS DOCUMENT CONTAINS SENSITIVE DATA.", 
                        x, 
                        y, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # cause number (3 row)
        p.fit_textline("Cause Number: ", 
                        center*1.25, 
                        y+yoff*3, 
                        "fontname={Courier} embedding fontsize=11 encoding=unicode")
        p.fit_textline("                            ", 
                        center*1.25+90, 
                        y+yoff*3, 
                        "underline=true fontname={Courier} embedding fontsize=11 encoding=unicode")
        p.fit_textline("   {}".format(answers.get('cause_number')), 
                        center*1.25+90, 
                        y+yoff*3, 
                        "fontname={Courier} embedding fontsize=11 encoding=unicode")
        # in the matter (4 row)
        p.fit_textline("IN THE MATTER OF THE MARRIAGE OF", 
                        x, 
                        y+yoff*4, 
                        "fontname={Courier-Bold} embedding fontsize=11 encoding=unicode")
        # court number (4.5 row)
        p.fit_textline("In the: ", 
                        center*2.8, 
                        y+yoff*4.5, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                 ", 
                        center*2.8+45, 
                        y+yoff*4.5, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format(answers.get('court_number')), 
                        center*2.8+45, 
                        y+yoff*4.5, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("(Court Number)",
                        center*2.8+50, 
                        y+yoff*4.5+10, 
                        "fontname={Courier-Oblique} embedding fontsize=7 encoding=unicode")
        # petitioner (6 row)
        p.fit_textline("Petitioner: ", 
                        x, 
                        y+yoff*6, 
                        "fontname={Courier-Bold} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                                              ", 
                        x+65, 
                        y+yoff*6, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format(answers.get('your_name')), 
                        x+65, 
                        y+yoff*6, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("Print first, middle and last name of the spouse who field for divorce.",
                        x+25, 
                        y+yoff*6+10, 
                        "fontname={Courier-Oblique} embedding fontsize=7 encoding=unicode")
        # and (8 row)
        p.fit_textline("And", center*1.5, y+yoff*8, "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # respondent (10 row)
        p.fit_textline("Respondent: ", 
                        x, 
                        y+yoff*10, 
                        "fontname={Courier-Bold} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                                              ", 
                        x+65, 
                        y+yoff*10, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format(answers.get('spouse_name')), 
                        x+65, 
                        y+yoff*10, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("Print first, middle and last name of other spouse.",
                        x+65, 
                        y+yoff*10+10, 
                        "fontname={Courier-Oblique} embedding fontsize=7 encoding=unicode")
        # county (10 row)
        p.fit_textline("                 ", 
                        center*2.8, 
                        y+yoff*10, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format(answers.get('county')), 
                        center*2.8, 
                        y+yoff*10,
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("County, Texas ", 
                        center*3.5, 
                        y+yoff*10, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # and interest (12 row)
        p.fit_textline("ADD IN THE INTEREST OF:", 
                        x, 
                        y+yoff*12, 
                        "fontname={Courier-Bold} embedding fontsize=11 encoding=unicode")
        #checkbox (7 row)
        p.fit_textline(" ", 
                        center*2.8, 
                        y+yoff*7, 
                        "fontname={Courier} fontsize=12 encoding=unicode boxsize={10 10} fitmethod=auto showborder")
        p.fit_textline("District Court", 
                        center*2.85+10, 
                        y+yoff*7-1, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        #checkbox (8 row)
        p.fit_textline(" ", 
                        center*2.8, 
                        y+yoff*8, 
                        "fontname={Courier} fontsize=12 encoding=unicode boxsize={10 10} fitmethod=auto showborder")
        p.fit_textline("County Court at Law", 
                        center*2.85+10, 
                        y+yoff*8-1, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        #vertical line (7 row)
        p.fit_textline("                ", 
                        center*2.8, 
                        y+yoff*7, 
                        "underline=true fontname={Courier} fontsize=12 encoding=unicode \
                        boxsize={0 50} position={right top} orientate=east")
        # list of children 1-3 (13 row)
        # 1
        p.fit_textline("1. ", x, y+yoff*13, "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                           ", 
                        x+10, 
                        y+yoff*13, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format("" if answers.get('children').get('0') is None else answers.get('children').get('0')), 
                        x+10, 
                        y+yoff*13, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # 2
        p.fit_textline("2. ", x+x*3, y+yoff*13, "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                           ", 
                        x+x*3+10, 
                        y+yoff*13, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format("" if answers.get('children').get('1') is None else answers.get('children').get('1')), 
                        x+x*3+10, 
                        y+yoff*13, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # 3
        p.fit_textline("3. ", x+x*6, y+yoff*13, "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                           ", 
                        x+x*6+10, 
                        y+yoff*13, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format("" if answers.get('children').get('2') is None else answers.get('children').get('2')), 
                        x+x*6+10, 
                        y+yoff*13, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # list of children 4-6 (14 row)
        # 4
        p.fit_textline("4. ", x, y+yoff*14, "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                           ", 
                        x+10, 
                        y+yoff*14, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format("" if answers.get('children').get('3')  is None else answers.get('children').get('3')), 
                        x+10, 
                        y+yoff*14, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # 5
        p.fit_textline("5. ", x+x*3, y+yoff*14, "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                           ", 
                        x+x*3+10, 
                        y+yoff*14, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format("" if answers.get('children').get('4') is None else answers.get('children').get('4')), 
                        x+x*3+10, 
                        y+yoff*14, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")
        # 6
        p.fit_textline("6. ", x+x*6, y+yoff*14, "fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("                           ", 
                        x+x*6+10, 
                        y+yoff*14, 
                        "underline=true fontname={Courier} embedding fontsize=9 encoding=unicode")
        p.fit_textline("   {}".format("" if answers.get('children').get('5') is None else answers.get('children').get('5')), 
                        x+x*6+10, 
                        y+yoff*14, 
                        "fontname={Courier} embedding fontsize=9 encoding=unicode")

        p.end_page_ext("")
        p.end_document("")

    except PDFlibException:
        print("PDFlib exception occurred:\n[%d] %s: %s" %
        ((p.get_errnum()), p.get_apiname(),  p.get_errmsg()))
        print_tb(exc_info()[2])

    except Exception:
        print("Exception occurred: %s" % (exc_info()[0]))
        print_tb(exc_info()[2])

    finally:
        p.delete()
