def apply_indention(content, open_brackets, close_brackets, new_line, tab_str):
    bracket_count = 0
    modified_content = ""
    bracket_map = dict(zip(open_brackets, close_brackets))
    i = 0
    while i < len(content):
        char = content[i]
        if char in open_brackets:
            j = next_non_space(content, i)
            if j < len(content) and bracket_map.get(char) == content[j]:
                modified_content += char + content[j]
                i = j
            else:
                bracket_count += 1
                modified_content += char + "\n" + tab_str * bracket_count
        elif char in close_brackets:
            bracket_count = max(0, bracket_count - 1)
            modified_content += "\n" + tab_str * bracket_count + char
        elif char in new_line:
            j = next_non_space(content, i)
            is_next_close = content[j] in close_brackets
            modified_content += char + ("" if is_next_close else "\n" + tab_str * bracket_count)
        else:
            modified_content += char
        i += 1
    return modified_content


def next_non_space(content, i):
    j = i + 1
    while j < len(content) - 1 and content[j].isspace():
        j += 1
    return j
