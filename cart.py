from ownable import set_owner
class Cart:
    from item_manager import show_items

    def __init__(self, owner):
        set_owner(self, owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Insufficient funds in the wallet. Purchase could not be completed.")
        else:
            total_cost = self.total_amount()
            self.owner.wallet.withdraw(total_cost)
        
            print("Purchase completed successfully!")