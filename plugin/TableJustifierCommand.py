# -*- coding: utf-8 -*-
import sublime, sublime_plugin
from table_justifier import *
 
class TableJustifierCommand(sublime_plugin.TextCommand):
  def run(self, edit, **kwargs):
    if kwargs == None:
      kwargs["separator"] = "|"

    separator = kwargs["separator"]
    ret = ""
    region_of_line = ""
    for region in self.view.sel():
      region_of_line = self.view.line(region)

    justifier = TableJustifier()
    ret = justifier.justify(self.view.substr(region_of_line), separator)

    return self.view.replace(edit, region_of_line, ret)
