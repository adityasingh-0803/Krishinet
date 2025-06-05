# agents/transport_agent.py
import time
import random

class TransportAgent:
    def __init__(self):
        self.available = True
        self.base_rate = 8  # INR per km
        self.max_distance = 200  # in km

    def offer_transport(self, distance):
        if not self.available or distance > self.max_distance:
            print("[TransportAgent] Cannot accept this route.")
            return None
        total_cost = self.base_rate * distance
        print(f"[TransportAgent] Offering delivery for Rs.{total_cost} ({distance} km)")
        return total_cost

    def confirm(self):
        print("[TransportAgent] Delivery confirmed. Starting journey...")
        time.sleep(2)
        print("[TransportAgent] Delivery completed successfully.")

if __name__ == "__main__":
    agent = TransportAgent()
    cost = agent.offer_transport(150)
    if cost:
        agent.confirm()
