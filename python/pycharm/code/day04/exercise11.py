"""
    公司有以下員工:
    經理-曹操，劉備，孫權
    技術-曹操，劉備，張飛，關羽
    請計算:
        是經理也是技術的有誰?
        是經理，不是技術的有誰?
        是技術，不是經理的有誰?
        身兼一職的有誰?
"""
# set_manager = {'曹操', '劉備', '孫權'}
# set_technician = {'曹操', '劉備', '張飛', '關羽'}
# print(set_manager & set_technician)
# print(set_manager - set_technician)
# print(set_technician - set_manager)
# print(set_manager ^ set_technician)
# print(len(set_manager | set_technician))

dict_person = {
    "經理": {'曹操', '劉備', '孫權'}
    "技術": {'曹操', '劉備', '張飛', '關羽'}
}
print(dict_person["經理"] & dict_person["技術"])
print(dict_person["經理"] - dict_person["技術"])
print(dict_person["技術"] - dict_person["經理"])
print(dict_person["經理"] ^ dict_person["技術"])
print(len(dict_person["經理"] | dict_person["技術"]))
