a = 1
b = 2

try:
    for c in (a, d):
        print(c)

except TypeError as e:
    print(f'TypeError: {e}')

except NameError as e:
    exc = e
    print(f'NameError: {e}')

else:
    print('Success!')

finally:
    print('use it for connections')


# >>> exc
# NameError("name 'd' is not defined")
# >>>
# >>> type(exc)
# <class 'NameError'>
# >>>
# >>> exc.__dict__
# {}
# >>>
# >>> dir(exc)
# ['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'name', 'with_traceback']
# >>>
# >>> exc.args
# ("name 'd' is not defined",)
# >>>
# >>> exc.name
# 'd'
# >>>
# >>> exc.__traceback__
# <traceback object at 0x000002D8D4DF9A80>
# >>>
# >>> tb = exc.__traceback__
# >>>
# >>> type(tb)
# <class 'traceback'>
# >>>
# >>> dir(tb)
# ['tb_frame', 'tb_lasti', 'tb_lineno', 'tb_next']
# >>>
# >>> print(f'\n{tb.tb_frame = }\n\n{type(tb.tb_frame) = }\n')

# tb.tb_frame = <frame at 0x000002D8D4929C40, file 'D:\\...\\scripts\\exceptions1.py', line 19, code <module>>

# type(tb.tb_frame) = <class 'frame'>

# >>> print(f'\n{tb.tb_lasti = }\n\n{type(tb.tb_lasti) = }\n')

# tb.tb_lasti = 14

# type(tb.tb_lasti) = <class 'int'>

# >>> print(f'\n{tb.tb_lineno = }\n\n{type(tb.tb_lineno) = }\n')

# tb.tb_lineno = 5

# type(tb.tb_lineno) = <class 'int'>

# >>> print(f'\n{tb.tb_next = }\n\n{type(tb.tb_next) = }\n')

# tb.tb_next = None

# type(tb.tb_next) = <class 'NoneType'>
