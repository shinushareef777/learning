from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Inventory:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.quantity_on_hand * self.unit_price
    


inv = Inventory('Books', 25.0, 5)
inv.name = 'Pen'
print(inv)