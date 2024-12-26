class BasicDMU:
    def run(self, context):
        if context["energy_usage"] > 400:
            return "Turn off non-essential devices"
        return "No immediate action"
