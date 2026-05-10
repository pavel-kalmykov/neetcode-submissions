class Singleton:
    _instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance._init_value()
        return cls._instance

    def _init_value(self):
        self._value: str | None = None
    
    def getValue(self) -> str | None:
        return self._value

    def setValue(self, value: str):
        self._value = value
