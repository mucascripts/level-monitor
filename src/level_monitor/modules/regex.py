import re


def get_characters_regex() -> re.Pattern[str]:
    base_start = r"<tr.*>(?:\n)?<td.*<\/td>\n"
    name = r"<td>(?P<name>.*(?!:<\/td>))<\/td>\n"
    level = r"<td>(?P<level>\d*(?!:<\/td>))<\/td>\n"
    resets = r"<td>(?P<resets>\d*(?!:<\/td>))<\/td>\n"
    base_end = r"<\/tr>\n"

    pattern = base_start + name + level + resets + base_end

    return re.compile(pattern)
