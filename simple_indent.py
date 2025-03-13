import sublime
import sublime_plugin

class SimpleIndentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("SimpleIndent.sublime-settings")
        open_brackets = settings.get("open_brackets", "{([")
        close_brackets = settings.get("close_brackets", "})]")
        new_line = settings.get("new_line", ",")
        tab_str = settings.get("tab_str", "\t")
        
        view = self.view
        content = view.substr(sublime.Region(0, view.size()))
        bracket_count = 0
        modified_content = ""
        i = 0
        while i < len(content):
            char = content[i]
            if char in open_brackets:
                j = i + 1
                while j < len(content) and content[j].isspace():
                    j += 1
                if j < len(content) and self._is_matching_bracket(char, content[j]):
                    modified_content += char + content[j]
                    i = j
                else:
                    bracket_count += 1
                    modified_content += char + "\n" + tab_str * bracket_count
            elif char in close_brackets:
                bracket_count = max(0, bracket_count - 1)
                modified_content += "\n" + tab_str * bracket_count + char
            elif char in new_line:
                modified_content += char + "\n" + tab_str * bracket_count
            else:
                modified_content += char
            i += 1
        view.replace(edit, sublime.Region(0, view.size()), modified_content)

    def _is_matching_bracket(self, open_bracket, close_bracket):
        brackets = {"{": "}", "(": ")", "[": "]"}
        return brackets.get(open_bracket) == close_bracket
