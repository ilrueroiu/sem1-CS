import wikipedia


def is_page_valid(title):
    try:
        wikipedia.page(title)
    except Exception:
        return False
    return True


def is_language_valid(lang):
    if lang not in wikipedia.languages():
        return False
    return True


def get_max_summary(titles):
    max_summary, name = 0, 0
    for title in titles:
        lengths = len(wikipedia.page(title).summary.split())
        if max_summary <= lengths:
            max_summary = lengths
            name = title
    return max_summary, name


def add_missed_titles(titles):
    new_titles_list = []
    i = 0
    while i + 1 < len(titles):
        new_titles_list.append(titles[i])
        links = wikipedia.page(titles[i]).links
        if titles[i + 1] not in links:
            for link in links:
                new_links = wikipedia.page(link).links
                if titles[i + 1] in new_links:
                    new_titles_list.append(link)
                    break
        i += 1
    new_titles_list.append(titles[-1])
    return new_titles_list


input_data = input().split(', ')
language = input_data.pop(-1)
if not is_language_valid(language):
    print('no results')
else:
    wikipedia.set_lang(language)
    data = get_max_summary(input_data)
    max_s, title = data
    print(max_s, wikipedia.page(title).title)
    print(add_missed_titles(input_data))
