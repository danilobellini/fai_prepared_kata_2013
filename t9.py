# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:09:27 2013

@author: danilo
"""

def t9(msg):
  assert isinstance(msg, str)
  data = {
    "a": "2",
    "b": "22",
    "d": "3",
    "e": "33",
    "g": "4",
    "h": "44",
    "j": "5",
    "k": "55",
    "m": "6",
    "n": "66",
  }
  numbers = []
  for ch in msg:
    numbers.append(data[ch])
  last = "_"
  for idx, number in enumerate(numbers):
    if last == number[-1]:
      numbers[idx] = "_" + number
    last = number[0]
  return "".join(numbers)
  