from context_engines.weather_engine import WeatherEngine
from context_engines.stock_engine import StockEngine
from context_engines.smart_home_engine import SmartHomeEngine
from decision_units.basic_dmu import BasicDMU
from decision_units.ai_dmu import AIDMU
from action_engine.action_executor import ActionExecutor
import time

if __name__ == "__main__":
    # Initialize components
    weather_engine = WeatherEngine()
    stock_engine = StockEngine()
    smart_home_engine = SmartHomeEngine()
    basic_dmu = BasicDMU()
    ai_dmu = AIDMU()
    action_executor = ActionExecutor()

    print("Starting JARVIS-like Intelligence System...")

    # Real-time loop
    while True:
        print("\n--- Gathering Context ---")
        weather_context = weather_engine.run()
        stock_context = stock_engine.run()
        smart_home_context = smart_home_engine.run()
        combined_context = {**weather_context, **stock_context, **smart_home_context}

        print("\n--- Making Decisions ---")
        basic_decision = basic_dmu.run(combined_context)
        ai_decision = ai_dmu.run(combined_context)

        print("\n--- Executing Actions ---")
        # To test executing decisions, uncomment the following line
        decisions = [
            "Energy usage is high. Dim the lights.",
            "Rain expected tomorrow. Set a reminder to carry an umbrella."
        ]
        action_executor.run(decisions)
        # Uncomment the following line to execute the decisions from the DMUs
        # action_executor.run([basic_decision, ai_decision])

        # Wait for the next cycle
        time.sleep(5)
