# from distutils.command.build_scripts import first_line_re
# from queue import Empty


# def mutable_link():
#     content = Empty
#     def dispath(method , value = None):
#         nonlocal content
#         if method == 'len':
#             return len_link(content)
#         elif method == 'getitem':
#             return getitem_link(content)
#         elif method  == 'append_link':
#             content = link(content, value)
#         elif method == 'pop_link':
#             f = first(content )
#             content = rest(content)
#             return f
#         elif method == 'str':
#             return join_link(content , ',')
#     return dispath

# def to_mutable_link(scoure):
#     the_link = mutable_link()
#     for s in reversed(scoure):
#         the_link('append_link', s)
#     return the_link

# list_a = [1,2,3,4]
# link_a = to_mutable_link(list_a)
# print(type(link_a))
# print(link_a('str'))
def dictionary(content = []):
    def getitem(key):
        match = [s for s in content if s[0] == key]
        if len(match ) == 1:
            return match[0][1]
    def appenditem(key, value):
        nonlocal content
        non_match = [s for s in content if s[0]!= key]
        content = non_match + [[key,value]]
    def dispath(method,key = None, value =None):
        if method == 'getitem':
            return getitem(key)
        elif method == 'appenditem':
            return appenditem(key, value)
    return dispath

d = dictionary()
d('appenditem','ws',6)
d('appenditem','wzy','zn')
d('appenditem','lyf','emo')
print(d('getitem','lyf'))