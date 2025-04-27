class SingletonMeta(type):
    """
    Класс Singleton может быть реализован в Python разными способами. Некоторые
    возможные методы включают: базовый класс, декоратор, метакласс. Мы будем использовать
    метакласс, потому что он лучше всего подходит для этой цели..
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Возможные изменения значения аргумента `__init__` не влияют на возвращаемый экземпляр.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
