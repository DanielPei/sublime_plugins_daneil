import sublime
import sublime_plugin
import json


class ReplaceJsonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())

        # Get a list of all lines
        lines = self.view.lines(region)

        for line in reversed(lines):
            content = self.view.substr(line)
            content = content.replace("'", "\"")
            self.view.replace(edit, line, content)



class CombineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        result = list()
        # Get the whole document as a region.
        region = sublime.Region(0, self.view.size())

        # Get a list of all lines
        lines = self.view.lines(region)

        for line in lines:
            result.append(self.view.substr(line).strip())

        self.view.replace(edit, region, json.dumps(result, ensure_ascii = False))
