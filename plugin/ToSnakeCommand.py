# -*- coding: utf-8 -*-
import sublime, sublime_plugin
from string_utils import *
 
class ToSnakeCommand(sublime_plugin.TextCommand):
  def run(self, edit, **kwargs):
    is_upper = False
    if kwargs["upper"] is not None:
      is_upper = bool(kwargs["upper"])

    for region in self.view.sel():
      if not region.empty():
        ret = StringUtils.to_snake(self.view.substr(region), is_upper)
        self.view.replace(edit, region, ret)
