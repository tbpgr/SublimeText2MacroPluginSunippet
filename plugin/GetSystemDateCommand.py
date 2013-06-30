# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import datetime
import locale
 
class GetSystemDateCommand(sublime_plugin.TextCommand):
  def run(self, edit, **kwargs):
    if kwargs == None:
      kwargs["format"] = "yyyymmdd"

    date = datetime.datetime.today()
    ret = ""

    format = kwargs["format"]
    if format == "yyyy/mm/dd hh:mi:ss":
      ret =  '%04d/%02d/%02d %02d:%02d:%02d' % (date.year, date.month, date.day, date.hour, date.minute, date.second)
    elif format == "yyyy/mm/dd":
      ret = '%04d/%02d/%02d' % (date.year, date.month, date.day)
    elif format == "yyyymmdd":
      ret = '%04d%02d%02d' % (date.year, date.month, date.day)
    else:
      return ""

    return self.view.insert(edit, self.view.sel()[0].a, ret)
