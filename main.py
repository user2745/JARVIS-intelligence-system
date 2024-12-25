from context_engines.weather_engine import WeatherEngine
from context_engines.system_engine import SystemEngine
from decision_units.load_balancer_unit import LoadBalancerUnit
from decision_units.alert_unit import AlertUnit
from action_engine.action_executor import ActionExecutor
import time

# System loop
if __name__ == "__main__":
    # Initialize components
    weather_engine = WeatherEngine()
    system_engine = SystemEngine()
    load_balancer = LoadBalancerUnit()
    alert_unit = AlertUnit()
    action_executor = ActionExecutor()

    print("Starting Generic Intelligence System...")

    # Real-time loop
    while True:
        print("\n--- Gathering Context ---")
        weather_context = weather_engine.run()
        system_context = system_engine.run()
        print(f"Weather Context: {weather_context}")
        print(f"System Context: {system_context}")

        # Combine all context
        combined_context = {**weather_context, **system_context}

        print("\n--- Making Decisions ---")
        load_decision = load_balancer.run(combined_context)
        alert_decision = alert_unit.run(combined_context)
        print(f"Load Decision: {load_decision}")
        print(f"Alert Decision: {alert_decision}")

        print("\n--- Executing Actions ---")
        action_executor.run([load_decision, alert_decision])

        # Simulate real-time processing interval
        time.sleep(5)
