phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist.insert(5,plist.pop(7))
remove_list = ['D', "'", 'i', '!']
for letter in plist:
    if letter in remove_list:
        plist.remove(letter)
plist.pop()
plist.insert(2, plist.pop(4))
plist.pop()
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)