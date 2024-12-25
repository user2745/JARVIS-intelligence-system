class AlertUnit:
    def run(self, context):
        if context["weather"] == "Rainy":
            return "Notify: Carry an umbrella"
        return "No alerts"
