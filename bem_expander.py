import sublime, sublime_plugin
import re, sys, os

if sys.version < '3':
  from src.src_two.scss_expand import SCSSExpand
else:
  from .src.src_three.scss_expand import SCSSExpand

class BemexpanderCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    curpos = self.view.sel()[0].begin()
    rowcol = self.view.rowcol(curpos)
    target = self.view.text_point(rowcol[0] + 2, rowcol[1])
    expander = SCSSExpand(target, self.view.substr, '\n')
    status = expander.coalesce_rule()
    self.view.insert(edit, curpos, '// {{ ' + status + ' }}')