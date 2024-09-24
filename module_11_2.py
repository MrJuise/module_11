'''
Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
'''


def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes_obj = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods_obj = [method for method in dir(obj) if callable(getattr(obj, method))]
    module_obj = introspection_info.__module__
    info = {
        'type': type_obj,
        'attributes': attributes_obj,
        'methods': methods_obj,
        'module': module_obj
    }
    return info


number_info = introspection_info(42)
print(number_info)
