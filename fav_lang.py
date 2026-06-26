favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'mike', 'emily']

print("The following people should take the favorite languages poll:")
for person in people_to_poll:
    print(person.title())

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())