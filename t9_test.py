# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:10:07 2013

@author: danilo
"""

from t9 import t9

def test_one_letter():
  assert t9("a") == "2"
  assert t9("d") == "3"
  assert t9("g") == "4"
  assert t9("j") == "5"
  assert t9("m") == "6"

def test_two_letters():
  assert t9("b") == "22"
  assert t9("e") == "33"
  assert t9("h") == "44"
  assert t9("k") == "55"
  assert t9("n") == "66"
