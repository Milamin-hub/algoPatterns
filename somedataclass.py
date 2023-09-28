from dataclasses import dataclass
from pprint import pprint


@dataclass
class SomeData:
    name: str
    age: int

dt = SomeData('John', 27)

pprint(SomeData.__dict__)