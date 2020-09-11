import sublime
import sublime_plugin
import json


class FormatJsonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = sublime.Region(0, self.view.size())

        # Get a list of all lines
        lines = self.view.lines(region)

        for line in reversed(lines):
            content = self.view.substr(line)
            content = content.replace("u'", "\"").replace("'", "\"")
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


        # loop the line in reversed order if you want to change content line by line
        # for line in reversed(lines):
        #     # import pdb; pdb.set_trace()
        #     # Here, line should be a region, right ? How to get the content ?
        #     content = self.view.substr(line)
        #     out_line = content + str(len(content))
        #     self.view.replace(edit, line, out_line)


        # self.view.erase_regions('json_errors')
        # selection = "None"
        # for region in self.view.sel():
        #     # If no selection, use the entire file as the selection
        #     # if region.empty() and s.get("use_entire_file_if_no_selection", True):
        #     if region.empty():
        #         selection = sublime.Region(0, self.view.size())
        #         selected_entire_file = True
        #     else:
        #         selection = region
        # sublime.message_dialog(self.view.substr(selection))

            # try:
            #     obj = self.json_loads(self.view.substr(selection))
            #     sublime.message_dialog("JSON is Valid")
            # except Exception:
            #     self.show_exception()
            #     sublime.message_dialog("Invalid JSON")