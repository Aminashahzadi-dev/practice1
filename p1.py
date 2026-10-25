marks = [88, 45, 92, 67, 30, 75]

passed = sum(1 for m in marks if m >= 50)
print("50 ya zyada marks:", passed)
print("Average:", round(sum(marks) / len(marks), 1))
print("Highest:", max(marks))
print("Lowest:", min(marks))
