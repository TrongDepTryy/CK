import inspect

class SubmissionScorer:
    def __init__(self, problem_description, test_cases):
        self.problem_description = problem_description
        self.test_cases = test_cases

    def score_submission(self, submission_func):
        passed_tests = 0
        total_tests = len(self.test_cases)
        results = []

        for i, (inputs, expected_output) in enumerate(self.test_cases):
            try:
                actual_output = submission_func(*inputs)
                if actual_output == expected_output:
                    passed_tests += 1
                    results.append(f"Test case {i+1}: Passed")
                else:
                    results.append(f"Test case {i+1}: Failed. Expected {expected_output}, but got {actual_output}")
            except Exception as e:
                results.append(f"Test case {i+1}: Error - {str(e)}")

        score = (passed_tests / total_tests) * 100
        return score, results

    def print_results(self, score, results):
        print(f"Problem: {self.problem_description}")
        print(f"Score: {score:.2f}%")
        print("Test Results:")
        for result in results:
            print(result)

# Example problem: Write a function that returns the sum of two numbers
test_cases_add_numbers = [
    ((1, 2), 3),
    ((0, 0), 0),
    ((-1, 1), 0),
    ((100, 200), 300),
    ((-50, -30), -80)
]

problems = {
    "add_numbers": test_cases_add_numbers,
}
problem_description = "Write a function 'add_numbers(a, b)' that returns the sum of two numbers."
scorer = SubmissionScorer(problem_description, problems["add_numbers"])

# Example correct submission
def correct_submission(a, b):
    return a + b

# Example incorrect submission
def incorrect_submission(a, b):
    return a - b

# Score the submissions
print("Scoring correct submission:")
score, results = scorer.score_submission(correct_submission)
scorer.print_results(score, results)

print("\nScoring incorrect submission:")
score, results = scorer.score_submission(incorrect_submission)
scorer.print_results(score, results)

def grade_multiple_functions(student_submission, function_names):
    try:
        # Create a local namespace to execute the submission code
        local_namespace = {}
        exec(student_submission, local_namespace)
        
        results = []
        
        for function_name in function_names:
            # Extract the function from the namespace
            submission_func = local_namespace.get(function_name)
            scorer = SubmissionScorer(problem_description, problems[function_name])

            if submission_func and inspect.isfunction(submission_func):
                score, func_results = scorer.score_submission(submission_func)
                results.append((function_name, score, func_results))
            else:
                results.append((function_name, 0, ["Error: Could not find a function named '{}' in the submission.".format(function_name)]))
        
        return results
    except Exception as e:
        print(f"Error in grading: {str(e)}")
        return []


# Example usage of test_student_submission
student_submission = """
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b
"""

print("\nTesting student submission:")
grade_multiple_functions(student_submission, ["add_numbers", "subtract_numbers", "multiply_numbers"])