from config.config import settings

assert settings.key == "value"

print(settings.key)
print(settings.number)

assert settings.number == 1234
assert settings.a_dict.nested.other_level == "nested value"
assert settings['a_boolean'] is False
assert settings.get("DONTEXIST", default=1) == 1

print(f'settings["debug"]: {settings["debug"]}')
