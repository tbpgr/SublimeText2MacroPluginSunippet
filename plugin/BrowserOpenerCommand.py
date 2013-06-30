# -*- coding: utf-8 -*-
import sublime, sublime_plugin
import webbrowser

class BrowserOpenerCommand(sublime_plugin.TextCommand):
  def run(self, edit, **kwargs):
    if kwargs == None:
      kwargs["type"] = "search_google"
    method_name = kwargs["type"]

    region = self.view.sel()[0]
    method = getattr(self, method_name)
    method(self.view.substr(region))

  def google_translate_en_ja(self, word):
    self.open_browser("http://translate.google.co.jp/#en/ja/" + word)

  def google_translate_ja_en(self, word):
    self.open_browser("http://translate.google.co.jp/#ja/en/" + word)

  def search_wikipedia(self, word):
    self.open_browser("http://ja.wikipedia.org/wiki/" + word)

  def search_google(self, word):
    self.open_browser("http://www.google.co.jp/search?aq=f&ix=hca&sourceid=chrome&ie=UTF-8&q=" + word)

  def open_browser(self, url):
    webbrowser.open(url)
