# Generic Intelligence System

## Overview
The Generic Intelligence System is a modular and real-time intelligence framework that gathers context from multiple sources, evaluates decisions, and executes actions autonomously. It simulates how intelligence systems operate by combining **Contextual Engines**, **Decision-Making Units (DMUs)**, and an **Action Engine** into one cohesive system.

### Features
- **Contextual Engines**: Gather real-time data from APIs (e.g., weather, system performance).
- **Decision-Making Units**: Analyze context and make decisions based on predefined logic.
- **Action Engine**: Executes decisions and performs actions based on outputs.
- **Real-Time Operation**: Continuously processes live data in an autonomous loop.
- **Modular Design**: Easy to add new contextual engines, decision units, or actions.

---

## How It Works

### Workflow
1. **Gather Context**:
   - Contextual engines fetch data from APIs.
   - Example: Weather and system performance data.

2. **Make Decisions**:
   - Decision units evaluate context to generate actionable insights.
   - Example: Reduce system load if CPU usage is high.

3. **Execute Actions**:
   - The action engine carries out the decisions.
   - Example: Notify the user or adjust system settings.

---

### Example Run

#### Input
- Weather API returns `{'weather': 'Rainy'}`.
- System API returns `{'cpu_usage': 85, 'memory_usage': 45}`.

#### Output
```plaintext
--- Gathering Context ---
Weather Context: {'weather': 'Rainy'}
System Context: {'cpu_usage': 85, 'memory_usage': 45'}

--- Making Decisions ---
Load Decision: Reduce non-critical tasks
Alert Decision: Notify: Carry an umbrella

--- Executing Actions ---
Executing: Reduce non-critical tasks
Executing: Notify: Carry an umbrella
Actions completed.



# Notes:  The code is deceptively simple, but this is a real-life framework for complex intelligence systems that take contextual information, think through different decisions and take action.  tldr: this thing 'thinks' & does 'stuff', autonomously.