class LoadBalancerUnit:
    def run(self, context):
        if context["cpu_usage"] > 80:
            return "Reduce non-critical tasks"
        return "System load is normal"
