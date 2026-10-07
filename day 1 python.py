.. code:: ipython3

    c = float(input("Enter Celsius: "))
    
    f = (c * 9/5) + 32
    
    print("Fahrenheit: {:.2f}".format(f))


.. parsed-literal::

    Enter Celsius:  2024
    

.. parsed-literal::

    Fahrenheit: 3675.20
    

.. code:: ipython3

    basic = float(input("Enter Basic Salary: "))
    
    hra = basic * 20 / 100
    da = basic * 15 / 100
    pf = basic * 8 / 100
    
    net_salary = basic + hra + da - pf
    
    print("HRA:", hra)
    print("DA:", da)
    print("PF:", pf)
    print("Net Take-Home Salary:", net_salary)


.. parsed-literal::

    Enter Basic Salary:  200000
    

.. parsed-literal::

    HRA: 40000.0
    DA: 30000.0
    PF: 16000.0
    Net Take-Home Salary: 254000.0
    

.. code:: ipython3

    year = int(input("Enter year: "))
    
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")


.. parsed-literal::

    Enter year:  2024
    

.. parsed-literal::

    2024 is a Leap Year
    

.. code:: ipython3

    m1 = float(input("Enter mark 1: "))
    m2 = float(input("Enter mark 2: "))
    m3 = float(input("Enter mark 3: "))
    
    average = (m1 + m2 + m3) / 3
    
    print("Average Percentage:", average)
    
    if average >= 90:
        print("Grade: A+")
    elif average >= 75:
        print("Grade: A")
    elif average >= 50:
        print("Grade: B")
    else:
        print("Grade: Fail")


.. parsed-literal::

    Enter mark 1:  89
    Enter mark 2:  99
    Enter mark 3:  90
    

.. parsed-literal::

    Average Percentage: 92.66666666666667
    Grade: A+
    

.. code:: ipython3

    age = int(input("Enter age: "))
    
    vote = "Eligible" if age >= 18 else "Not Eligible"
    discount = "Eligible" if age >= 60 else "Not Eligible"
    
    print("Voting:", vote)
    print("Senior Citizen Discount:", discount)


.. parsed-literal::

    Enter age:  25
    

.. parsed-literal::

    Voting: Eligible
    Senior Citizen Discount: Not Eligible
    

.. code:: ipython3

    n = int(input("Enter number: "))
    
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


.. parsed-literal::

    Enter number:  25
    

.. parsed-literal::

    25 x 1 = 25
    25 x 2 = 50
    25 x 3 = 75
    25 x 4 = 100
    25 x 5 = 125
    25 x 6 = 150
    25 x 7 = 175
    25 x 8 = 200
    25 x 9 = 225
    25 x 10 = 250
    

.. code:: ipython3

    n = int(input("Enter N: "))
    
    i = 1
    total = 0
    
    while i <= n:
        total = total + i
        i = i + 1
    
    average = total / n
    
    print("Sum:", total)
    print("Average:", average)


.. parsed-literal::

    Enter N:  79
    

.. parsed-literal::

    Sum: 3160
    Average: 40.0
    

.. code:: ipython3

    n = int(input("Enter number: "))
    
    if n < 2:
        print(n, "is not a Prime Number")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(n, "is not a Prime Number")
                break
        else:
            print(n, "is a Prime Number")


.. parsed-literal::

    Enter number:  88
    

.. parsed-literal::

    88 is not a Prime Number
    

.. code:: ipython3

    n = int(input("Enter number: "))
    
    original = n
    reverse = 0
    
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    
    print("Reversed Number:", reverse)
    
    if original == reverse:
        print(original, "is a Palindrome")
    else:
        print(original, "is not a Palindrome")


.. parsed-literal::

    Enter number:  95
    

.. parsed-literal::

    Reversed Number: 59
    95 is not a Palindrome
    

.. code:: ipython3

    code = int(input("Enter HTTP status code: "))
    
    match code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Invalid Status Code")


.. parsed-literal::

    Enter HTTP status code:  68
    

.. parsed-literal::

    Invalid Status Code
    

