import random
from typing import Optional, Iterable, Tuple, Any, List, Union


class Character:

    def __init__(self, armor: int, power: int):
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


c1 = Character(10, 20)
c1.hit(20)

price: Optional[int]
price = 10
price = None


def rsndom_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)


price_container1: Tuple[int, str, Any] = (1, 'str', 2)
price_container2: Tuple[int, ...] = (1, 2, 3, 4)

list1: List[Union[int, str]] = [1, 2, 3, 'w']
