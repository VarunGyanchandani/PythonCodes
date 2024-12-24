def combinationSum(candidates, target):
    result = []

    def backtrack(start, target, path):
        # If we hit the target, add the current path to result
        if target == 0:
            result.append(path)
            return
        # Explore further candidates
        for i in range(start, len(candidates)):
            if candidates[i] > target:  # No need to continue if the candidate is greater than target
                continue
            # Choose the current candidate and recurse with the same index (we allow repetition)
            backtrack(i, target - candidates[i], path + [candidates[i]])

    # Start the backtracking with index 0, target, and an empty path
    backtrack(0, target, [])

    return result

print(combinationSum([2,3,6,7],7))