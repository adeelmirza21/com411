import data.dicts.simple_dict as simple_dict

def display_keys(data):
    print("keys")
    for key in data:
        print(key)
    print()

def display_values(data):
    print("values")
    for value in data.values():
        print(value)
    print()

def display_items(data):
  print("items:")
  for key, value in data.items():
    print(f"{key}: {value}")
  print()

def run():
    data = simple_dict.pattern()
    print(f"dictionary:\n{data}")

    display_keys(data)
    display_values(data)
    display_items(data)

run()






