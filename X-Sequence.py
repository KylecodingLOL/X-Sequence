def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def X(n, a, b, m):
    if n == 0:
        return 1
    prev = X(n-1, a, b, m)
    curr = (collatz(n) + a * prev) * (fibonacci(collatz(n)) + b * prev) % m
    return curr

params_list = [
    {'a': 70, 'b': 50, 'm': 50},
    {'a': 30, 'b': 60, 'm': 100},
    {'a': 10, 'b': 20, 'm': 40},
]

starting_point = 7
steps = 30

results_dict = {}

for params in params_list:
    a_value = params['a']
    b_const = params['b']
    m_const = params['m']
    n = starting_point
    results = []
    
    print(f"Running for a = {a_value}, b = {b_const}, m = {m_const}...")
    
    for step in range(steps):
        result = X(n, a_value, b_const, m_const)
        print(f"Step {step + 1}: X({n}) = {result}")
        results.append(result)
        n = collatz(n)
    
    results_dict[f"a = {a_value}, b = {b_const}, m = {m_const}"] = results

print("Final Results:")
print(results_dict)
