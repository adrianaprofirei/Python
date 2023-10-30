#Ex 1

def set_operations(a, b):
    res = []
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)
    res = [intersection, union, a_minus_b, b_minus_a]
    return res

a = [1, 2, 3, 4, 5, 5]
b = [3, 4, 5, 6 ,7, 8]
print(set_operations(a, b))

# Ex 2
def char_counter(string):
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter


string = "Ana has apples"
print(char_counter(string))


# Ex 3

def dict_compare(a, b):
    if len(a) != len(b):
        return False
    flag = 0
    for key in a:
        if a.get(key) != b.get(key):
            flag = 1
    if flag:
        return False
    return True


dict1 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
dict2 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
dict3 = {'a': 1, 'b': {'c': 2, 'd': [3, 5]}}

print(dict_compare(dict1, dict2))
print(dict_compare(dict1, dict3))


# Ex 4

def build_xml_element(tag, content, **attributes):
    xml_element = f"<{tag}"
    for key, value in attributes.items():
        xml_element += f' {key}="{value}"'
    xml_element += f">{content}</{tag}>"
    return xml_element


print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))


# Ex 5

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix):
                return False
            if middle not in value[1:-1]:
                return False
            if not value.endswith(suffix):
                return False
        else:
            return False

    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid"
}
print(validate_dict(rules, dictionary))

rules = {("key1", "start", "middle", "end"), ("key2", "abc", "def", "ghi")}
dictionary = {
    "key1": "startmiddleend",
    "key2": "abc def ghi",
    "key3": "this is not valid"
}
print(validate_dict(rules, dictionary))


# Ex 6

def unique_duplicates_counter(list):
    counter = len(list)
    unique = set(list)
    unique_counter = len(unique)
    duplicate_counter = counter - unique_counter
    return unique_counter, duplicate_counter


list = [1, 2, 3, 3, 3, 4, 4, 5]
print(unique_duplicates_counter(list))


# Ex 7

def operations(*set):
    dict = {}
    for i in range(len(set)):
        for j in range(i + 1, len(set)):
            set_a = set[i]
            set_b = set[j]
            key = f"{set_a} | {set_b}"
            dict[key] = set_a | set_b
            key = f"{set_a} & {set_b}"
            dict[key] = set_a & set_b
            key = f"{set_a} - {set_b}"
            dict[key] = set_a - set_b
            key = f"{set_b} - {set_a}"
            dict[key] = set_b - set_a
    return dict


set_a = {1, 2}
set_b = {2, 3}
print(operations(set_a, set_b))


# Ex 10

def loop(mapping):
    visited = set()
    res = []
    current_key = mapping.get("start", None)
    while current_key is not None and current_key not in visited:
        res.append(current_key)
        visited.add(current_key)
        current_key = mapping.get(current_key, None)

    return res


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(loop(mapping))


# Ex 11

def my_function(*posargs, **keywordargs):
    count = 0
    keyword_values = set(keywordargs.values())
    for arg in posargs:
        if arg in keyword_values:
            count += 1
    return count


print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
