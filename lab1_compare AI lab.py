def comparison_agent(conversation_answer, task_decision):
    state = {
        "conversation_answer": conversation_answer,
        "task_decision": task_decision
    }
    state["conversation_sounds_correct"] = True
    state["task_is_correct"] = task_decision == "Hold"
    return state
test_cases = [
    {
        "name": "Fluent but Incorrect Answer",
        "conversation_answer": "Review because score is 85 and documents are complete",
        "task_decision": "Hold",
        "expected": "Hold"
    },
    {
        "name": "Correct Task Decision",
        "conversation_answer": "Attendance must also be checked",
        "task_decision": "Hold",
        "expected": "Hold"
    }
]
for test in test_cases:
    result = comparison_agent(
        test["conversation_answer"],
        test["task_decision"]
    )
    if result["task_is_correct"]:
        decision = "Hold"
        reason = "Attendance is below 75%, so the student does not meet all conditions"
    else:
        decision = "Review"
        reason = "The task decision is incorrect"
    print("\nTest Case:", test["name"])
    print("Conversation Answer:", result["conversation_answer"])
    print("Expected:", test["expected"])
    print("Actual:", decision)
    print("Reason:", reason)
    print("Test Passed:", decision == test["expected"])
    print()

