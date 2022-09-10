
class Singleton:
    __instance: 'Singleton' = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


st1 = Singleton()
st2 = Singleton()
print(f'{st1 is st2}')

# уязвимость
Singleton._Singleton__instance = None

st3 = Singleton()
print(f'{st3 is st1}')
