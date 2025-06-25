'''
Accept the average score from the student and give her the results as follows:(for ease of understanding let the input be int). Also check for invalid i/p.
0  to 69  Fail
70 to 84  Second class
85 to 95  First class
96 to 100 Excellent
'''
average_score = int(input('Enter the student average score: '))

if average_score >= 0 and average_score <= 69:
    print('Result is Fail')
elif average_score >= 70 and average_score <= 84:
    print('Result is Second Class')
elif average_score >= 85 and average_score <= 95:
    print('Result is First class')
elif average_score >= 96 and average_score <= 100:
    print('Result is Excellent')
else:
    print('Invalid Average Score')
