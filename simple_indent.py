import sublime
import sublime_plugin
from .apply_indention import apply_indention


class SimpleIndentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("SimpleIndent.sublime-settings")
        open_brackets = settings.get("open_brackets", "{([")
        close_brackets = settings.get("close_brackets", "})]")
        new_line = settings.get("new_line", ",")
        tab_str = settings.get("tab_str", "\t")
        view = self.view
        content = view.substr(sublime.Region(0, view.size()))
        modified_content = apply_indention(content, open_brackets, close_brackets, new_line, tab_str)
        view.replace(edit, sublime.Region(0, view.size()), modified_content)
