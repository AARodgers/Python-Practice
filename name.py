name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#called f-strings or formatted strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

# to add a tab use \t
print("\tPython")

#to add a new line use \n
print("Languages:\nPython\nC\nRuby")

#to strip whitespace on righthand side use .rstrip(), this is temporary so need to reassign
# variable to make it permanent
# strip whitespace from left side use .lstrip()
# to strip whitespace from both sides use .strip()
favorite_language = "python  "
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
print(favorite_language)

# to remove a prefix like https:// use .removeprefix('prefix')
nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)
