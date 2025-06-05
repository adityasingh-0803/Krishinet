import time
import random

class BuyerAgent:
    def __init__(self):
        self.max_price = 28  # INR per kg
        self.required_quantity = 80  # in kg

    def view_offer(self, crop, quantity, price):
        print(f"[BuyerAgent] Found offer: {quantity}kg of {crop} at Rs.{price}/kg")
        return price <= self.max_price and quantity >= self.required_quantity

    def make_bid(self):
        bid_price = random.randint(24, self.max_price)
        print(f"[BuyerAgent] Bidding Rs.{bid_price}/kg")
        return bid_price

if __name__ == "__main__":
    agent = BuyerAgent()
    if agent.view_offer("Wheat", 100, 25):
        agent.make_bid()
    else:
        print("[BuyerAgent] Skipping this offer")
