import pandas as pd 
coding_data = {
    "Question": [
        "How do you print 'Hello, World!' in Python?",
        "How do you create a for loop that iterates from 1 to 5 in Python?",
        "How you can print 10 times 'welcome  at upflairs'?",
        "How do you check if a number is even in Python?",
        "How do you define a class in python?",
        "How do you create a list of squares from 1 to 5 using list comprehension?",
        "How do you reverse a string in Python?",
        "How do you open a file and read its contents in Python?",
        "How do you remove an item from a list in Python?",
        "How do you find the maximum value in a list in Python?",
        "How do you sort a list in Python?"
    ],
    "Answer": [
        "print('Hello, World!')",
        "for i in range(1, 6):\n\tprint(i)",
        "for i in range(0, 10):\n\tprint('welcome at upflairs')",
        "if number % 2 == 0:\n\tprint('Even')",
        "class Upflairs:\n\tdef __init__(self, name):\n\t\tself.name = name",
        "[x**2 for x in range(1, 6)]",
        "'hello'[::-1]",
        "with open('upflairs.txt', 'r') as file:\n\tcontents = file.read()",
        "my_list.remove('upflairs')",
        "max(my_list)",
        "my_list.sort()"
    ]
}

# Creating a DataFrame for coding examples
coding_df = pd.DataFrame(coding_data)


# Saving the updated DataFrame to a new CSV file
updated_csv_file_path = 'question.csv'
coding_df.to_csv(updated_csv_file_path, index=False)
print("data file generated : ",updated_csv_file_path)
