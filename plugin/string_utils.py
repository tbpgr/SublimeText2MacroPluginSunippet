# -*- coding: utf-8 -*-
import re
class StringUtils:
  @classmethod
  def to_camel(cls, value, capitalize): 
    if (value == None):
      return None
    ret = value.lower()

    words = re.split("[\s_]", ret)
    words = map(lambda x: x.capitalize(), words)
    if (capitalize == False):
      words[0] = words[0].lower()

    return "".join(words)

  @classmethod
  def to_snake(cls, value, upper): 
    if (value == None):
      return None
    if (value == ""):
      return ""

    ret = re.sub(r'([\s|A-Z])', "_\\1",value)
    ret = re.sub(r'([\s])', "",ret)
    ret = re.sub(r'^_', "",ret)
    if (upper):
      ret = ret.upper()
    else:
      ret = ret.lower()
    return ret
