import time
import random

class FarmerAgent:
    def __init__(self):
        self.crop = "Wheat"
        self.quantity = 100
        self.price_per_kg = 25

    def post_offer(self):
        print(f"[FarmerAgent] Offering {self.quantity}kg of {self.crop} at Rs.{self.price_per_kg}/kg")

    def negotiate(self, bid_price):
        if bid_price >= self.price_per_kg:
            print(f"[FarmerAgent] Accepting bid of Rs.{bid_price}/kg")
        else:
            print(f"[FarmerAgent] Rejecting bid of Rs.{bid_price}/kg")

if __name__ == "__main__":
    agent = FarmerAgent()
    agent.post_offer()
    time.sleep(2)
    agent.negotiate(random.randint(20, 30))
