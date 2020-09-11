

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