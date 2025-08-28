# A simple procedural test script, not using unittest.
from agent import find_answer

# Mock knowledge base, same as before.
knowledge_base = [
    "The sun is a star.",
    "The capital of France is Paris.",
    "Elephants are the largest land animals.",
    "The earth revolves around the sun.",
    "Python is a popular programming language."
]

def run_tests():
    """Runs a series of tests and asserts their correctness."""
    print("Running tests...")

    # Test 1: Single Match
    question1 = "What is the capital of France?"
    expected1 = "The capital of France is Paris."
    result1 = find_answer(question1, knowledge_base)
    assert result1 == expected1, f"Test 1 FAILED: Expected '{expected1}', got '{result1}'"
    print("Test 1: Single Match -> PASSED")

    # Test 2: Multiple Matches
    question2 = "sun"
    result2 = find_answer(question2, knowledge_base)
    expected_answers2 = {
        "The sun is a star.",
        "The earth revolves around the sun."
    }
    assert set(result2.split('\n')) == expected_answers2, f"Test 2 FAILED: Got '{result2}'"
    print("Test 2: Multiple Matches -> PASSED")

    # Test 3: No Match
    question3 = "What is the meaning of life?"
    expected3 = "抱歉，我不知道这个问题的答案。"
    result3 = find_answer(question3, knowledge_base)
    assert result3 == expected3, f"Test 3 FAILED: Expected '{expected3}', got '{result3}'"
    print("Test 3: No Match -> PASSED")

    # Test 4: Case-insensitivity
    question4 = "what about python?"
    expected4 = "Python is a popular programming language."
    result4 = find_answer(question4, knowledge_base)
    assert result4 == expected4, f"Test 4 FAILED: Expected '{expected4}', got '{result4}'"
    print("Test 4: Case-insensitivity -> PASSED")

    # Test 5: Empty question
    question5 = "  "
    expected5 = "请输入一个问题。"
    result5 = find_answer(question5, knowledge_base)
    assert result5 == expected5, f"Test 5 FAILED: Expected '{expected5}', got '{result5}'"
    print("Test 5: Empty question -> PASSED")

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    run_tests()
