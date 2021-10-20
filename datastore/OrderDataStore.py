from C1_order_system.datamodel import Order


class OrderDataStore:
    """
    class that defines a container to hold Order objects and
    provide functions to access, filter and query data
    """

    def __init__(self):
        """
        Constructor
        """
        # print(f'OrderDataStore singleton instantiated')
        pass

    def size(self) -> int:
        return 0

    def find_all_orders(self) -> []:
        return []

    def filter(self, _filter_func: bool) -> [Order]:
        return []
