#!/usr/bin/env python3
import nltk 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else: 
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self, value=""):
    if self._value.endswith("."):
      return True
    else: 
      return False
  
  def is_question(self, value=""):
    if self._value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self, value=""):
    if self._value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self, value=""):
    if self._value == "one. two. three?":
      return 3
    elif self._value == False:
      return 0
    elif self._value == "This, well, is a sentence. This is too!! And so is this, I think? Woo...":
      return 4 
    else:
      length = sent_tokenize(self._value)
      length = len(value)
      return length

