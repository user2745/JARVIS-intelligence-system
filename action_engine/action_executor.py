class ActionExecutor:
    def run(self, decisions):
        for decision in decisions:
            if decision:
                print(f"Executing: {decision}")
        print("Actions completed.")
