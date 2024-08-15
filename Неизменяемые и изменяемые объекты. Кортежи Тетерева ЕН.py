immutable_var = [1.0, 2, "three", True, [1, 2, 3]]
print(immutable_var)
# immutable_var[0] = 3  # TypeError: 'tuple' object does not support item assignment
# изменить назначение элементов кортежа после того, как он создан, нельзя, потому что это его главное свойство
mutable_list = [1.0, 2, "three", True, [1, 2, 3]]
mutable_list[0] = 'rose'
print(mutable_list)
