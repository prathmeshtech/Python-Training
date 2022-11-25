import unittest
from src import  leap_year 
'''
To determine whether a year is a leap year, follow these steps:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
'''
# Test cases
    # 1. 2024 -> True
    # 2. 1900 -> False
    # 3. 2000 -> True
    # 4. 2017 -> False
    
class LeapYearTest(unittest.TestCase):


    def test_year_input(self):
        test_data={2024:True, 1900:False, 2000:True , 2017:False}
        for key, value in test_data.items():
            response=leap_year.identify_leap_year(key)
            self.assertEqual(response,value)

if __name__== '__main__':
    unittest.main()
