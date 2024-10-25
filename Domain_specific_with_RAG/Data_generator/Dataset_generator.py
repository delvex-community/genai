import pandas as pd
import os 
coding_data = {
    "Question": [
        "How do you create a Python function to calculate the factorial of a number at Upflairs without using recursion?",
        "How do you implement a custom Python class at Upflairs to handle complex numbers with addition and subtraction?",
        "How do you read a CSV file into a pandas DataFrame and calculate the mean of a specific column in Upflairs' Data Science course?",
        "How do you create a Python decorator at Upflairs that logs the function name before execution?",
        "How do you write a Python program at Upflairs to reverse a string without using built-in reverse functions?",
        "How do you implement a recursive function at Upflairs to find the nth Fibonacci number?",
        "How do you use list comprehension at Upflairs to create a list of even numbers from 1 to 100?",
        "How do you remove duplicates from a list of dictionaries in Python at Upflairs based on a specific key?",
        "How do you implement matrix multiplication at Upflairs using nested loops in Python?",
        "How do you implement a context manager at Upflairs to safely handle opening and closing files?",
        "How do you write a Python function at Upflairs to find the longest word in a given sentence?",
        "How do you implement quicksort at Upflairs using Python's divide-and-conquer approach?",
        "How do you merge two DataFrames in pandas on a common column at Upflairs with an inner join?",
        "How do you write a Python function at Upflairs to check if a string is a palindrome?",
        "How do you use SQL queries with pandas at Upflairs to filter a DataFrame based on a condition?",
        "How do you implement memoization in a recursive function at Upflairs to optimize performance?",
        "How do you create a Python function at Upflairs to calculate the sum of squares of numbers from 1 to n?",
        "How do you implement a binary search algorithm at Upflairs for a sorted list in Python?",
        "How do you handle exceptions at Upflairs while reading a file and catching multiple exceptions in Python?",
        "How do you serialize and deserialize a Python object at Upflairs using the pickle module?",
        "How do you create a lambda function at Upflairs to filter out even numbers from a list?",
        "How do you create a Python generator at Upflairs to generate an infinite sequence of prime numbers?",
        "How do you create a REST API at Upflairs using Flask that handles GET and POST requests?",
        "How do you implement a binary tree at Upflairs using a Python class and perform in-order traversal?"
    ],
    "Answer": [
        "def factorial(n):\n\tresult = 1\n\tfor i in range(1, n + 1):\n\t\tresult *= i\n\treturn result",
        "class Complex:\n\tdef __init__(self, real, imag):\n\t\tself.real = real\n\t\tself.imag = imag\n\tdef __add__(self, other):\n\t\treturn Complex(self.real + other.real, self.imag + other.imag)\n\tdef __sub__(self, other):\n\t\treturn Complex(self.real - other.real, self.imag - other.imag)",
        "import pandas as pd\n df = pd.read_csv('file.csv')\nmean_value = df['column_name'].mean()\nprint(mean_value)",
        "from functools import wraps\n\ndef log_function(func):\n\t@wraps(func)\n\tdef wrapper(*args, **kwargs):\n\t\tprint(f'Function {func.__name__} is running')\n\t\treturn func(*args, **kwargs)\n\treturn wrapper",
        "def reverse_string(s):\n\tresult = ''\n\tfor char in s:\n\t\tresult = char + result\n\treturn result\nprint(reverse_string('Welcome to Upflairs'))",
        "def fibonacci(n):\n\tif n <= 1:\n\t\treturn n\n\telse:\n\t\treturn fibonacci(n-1) + fibonacci(n-2)\nprint(fibonacci(10))",
        "[x for x in range(1, 101) if x % 2 == 0]",
        "seen = set()\nunique_dicts = [d for d in dict_list if d['key'] not in seen and not seen.add(d['key'])]",
        "result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]",
        "class FileManager:\n\tdef __enter__(self):\n\t\tself.file = open('file.txt', 'r')\n\t\treturn self.file\n\tdef __exit__(self, exc_type, exc_val, exc_tb):\n\t\tself.file.close()",
        "def longest_word(sentence):\n\twords = sentence.split()\n\treturn max(words, key=len)\nprint(longest_word('Welcome to Upflairs'))",
        "def quicksort(arr):\n\tif len(arr) <= 1:\n\t\treturn arr\n\tpivot = arr[len(arr) // 2]\n\tleft = [x for x in arr if x < pivot]\n\tmiddle = [x for x in arr if x == pivot]\n\tright = [x for x in arr if x > pivot]\n\treturn quicksort(left) + middle + quicksort(right)",
        "df_merged = pd.merge(df1, df2, on='common_column', how='inner')",
        "def is_palindrome(s):\n\ts = s.lower()\n\treturn s == s[::-1]\nprint(is_palindrome('Upflairs'))",
        "filtered_df = df.query('column_name > 100')\nprint(filtered_df)",
        "def memoize_fibonacci(n, memo={}):\n\tif n in memo:\n\t\treturn memo[n]\n\tif n <= 1:\n\t\treturn n\n\tmemo[n] = memoize_fibonacci(n-1, memo) + memoize_fibonacci(n-2, memo)\n\treturn memo[n]\nprint(memoize_fibonacci(10))",
        "def sum_of_squares(n):\n\treturn sum(x ** 2 for x in range(1, n + 1))\nprint(sum_of_squares(5))",
        "def binary_search(arr, target):\n\tlow, high = 0, len(arr) - 1\n\twhile low <= high:\n\t\tmid = (low + high) // 2\n\t\tif arr[mid] == target:\n\t\t\treturn mid\n\t\telif arr[mid] < target:\n\t\t\tlow = mid + 1\n\t\telse:\n\t\t\thigh = mid - 1\n\treturn -1",
        "try:\n\twith open('file.txt', 'r') as f:\n\t\tdata = f.read()\nexcept (IOError, ValueError) as e:\n\tprint(f'Error occurred: {e}')",
        "import pickle\nobj = MyClass()\nwith open('data.pkl', 'wb') as f:\n\tpickle.dump(obj, f)\nwith open('data.pkl', 'rb') as f:\n\tobj_loaded = pickle.load(f)",
        "filtered_list = list(filter(lambda x: x % 2 == 0, my_list))",
        "def prime_generator():\n\tD = {}\n\tq = 2\n\twhile True:\n\t\tif q not in D:\n\t\t\tyield q\n\t\t\tD[q * q] = [q]\n\t\telse:\n\t\t\tfor p in D[q]:\n\t\t\t\tD.setdefault(p + q, []).append(p)\n\t\tdel D[q]\n\t\tq += 1",
        "from flask import Flask, request\napp = Flask(__name__)\n\n@app.route('/api', methods=['GET', 'POST'])\ndef api():\n\tif request.method == 'GET':\n\t\treturn 'GET request received'\n\telif request.method == 'POST':\n\t\treturn 'POST request received'\n\nif __name__ == '__main__':\n\tapp.run()",
        "class Node:\n\tdef __init__(self, key):\n\t\tself.left = None\n\t\tself.right = None\n\t\tself.val = key\n\ndef inorder(root):\n\tif root:\n\t\tinorder(root.left)\n\t\tprint(root.val)\n\t\tinorder(root.right)"]}

df = pd.DataFrame(coding_data)
data_folder_path = r"D:\Achievements\freelancing\GenerativeAI\Domain_specific_with_RAG\Data"
file_name = "questin_answering.csv"
upflairs_data_file_path = os.path.join(data_folder_path,file_name)
# Saving to CSV
df.to_csv(upflairs_data_file_path, index=False)
print("Successfully written your data into folder : ",upflairs_data_file_path)