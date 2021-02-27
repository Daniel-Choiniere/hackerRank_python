# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60],
}

query_name = "Malika"

student_query = students[query_name]

total = 0;
for score in student_query:
    total += score

average = total / 3

print("{:.2f}".format(average))