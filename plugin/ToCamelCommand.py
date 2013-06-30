# -*- coding: utf-8 -*-
import sublime, sublime_plugin
from string_utils import *
 
class ToCamelCommand(sublime_plugin.TextCommand):
  def run(self, edit, **kwargs):
    is_capitalize = False
    if kwargs["capitalize"] is not None:
      is_capitalize = bool(kwargs["capitalize"])

    for region in self.view.sel():
      if not region.empty():
        ret = StringUtils.to_camel(self.view.substr(region), is_capitalize)
        self.view.replace(edit, region, ret)
