class Singleton:
    _instance = None

    def __new__(self):

        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance


def singleton(myClass):
    instances = {}

    def get_instance(*args, **kwargs):
        if myClass not in instances:
            print("!")
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return get_instance
