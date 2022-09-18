from operator import is_


def multiply_lnk(lst_of_link):
    result, new_lst, is_recursive= 1,[],True
    for link in lst_of_link:
        if link.rest == Link.empty:
            is_recursive = False
        result *= link.first
        new_lst.append(link.rest)
    if is_recursive:
        Link(result, multiply_lnk(new_lst))
    else:
        Link(result)
