"""
Example: Agent evolution after runtime failure

This example demonstrates:
1. Initial agent execution
2. A runtime failure
3. Agent evolution triggered by failure
4. Improved behavior after evolution
"""

from hive import Agent, Goal

goal = Goal(
    description="Answer questions accurately using provided context"
)

agent = Agent(goal=goal)

print("=== First run (expected to fail) ===")
try:
    agent.run(
        input_text="Answer using external data that is unavailable"
    )
except Exception as e:
    print("Failure occurred:", e)

print("\n=== Agent evolves based on failure ===")
agent.evolve(reason="Missing data source caused failure")

print("\n=== Second run (post-evolution) ===")
result = agent.run(
    input_text="Answer using only the given prompt context"
)

print("Final output:", result)
