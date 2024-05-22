from dataclasses import dataclass
from typing import *
import unittest

#* Section 1 (Git)
# persnickety

#* Section 2 (Data Definitions)

#* 1)
fahrenheit : TypeAlias = float
f_ex1 : fahrenheit = 30.6
f_ex: fahrenheit = 95
celsius : TypeAlias = float
c_ex1 : celsius = 65
c_ex2 : celsius = 93

#* 2)
price : TypeAlias = float
p_ex1 : 2.5
P_ex2 : 3.5

#* 3)
class price_record:
    def __init__(self, name:str, price: float):
        self.name = name
        self.price = price
    def __eq__(self,other):
        if isinstance(other, price_record):
            if self.name == other.name:
                return self.price == other.price
            else:
                return False
    def __repr__(self):
        return "Price Record(name ={}, price + {}".format(self.name, self.price)


p_ex1 : price_record = price_record("book", 5.5)
P_ex2 : price_record = price_record("pencil", 1.3)

#* 4)

class date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    def __eq__(self, other):
        if isinstance(other, date):
            return self.day == other.day and self.month == other.month and self.year == other.year
        else:
            return False
    def __repr__(self):
        return self.day + "/" + self.month + "/" + self.year

class open_tab:
    def __init__(self, url: str, date: date):
        self.url = url
        self.date = date

    def __eq__(self, other):
        if isinstance(other, open_tab):
            return self.url == other.url and self.date == other.date
        else:
            return False

    def __repr__(self):
        return "url: " + self.url + " was last visited on " + self.date
o_ex1: open_tab = open_tab("www.web.com", date(4,12,2003))
o_ex2: open_tab = open_tab("www.site.com", date(5,5,2009))

#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)

# Purpose statement: A function accepts a price and returns the price with sales tax computed.
def price_sales_tax(price: float) -> price:

#* 2)

# Purpose statement: A function accepts the name of an item and returns the price in the database
def find_price(item_name: str, database: Dict[str, float]) -> Union[float, None]:

#* 3)

# Purpose Statement: A function accepts a string representing a geographic region and a dictionary representing a database of income data.
# The function computes and returns the median income for the specified region if it exists or None if it is not in the database.None
def compute_median_income(region: str, database: Dict[str, List[float]]) -> float:

#* 4)
#Purpose Statement: A function accepts a string representing a geographic region and a dictionary representing a database.
#The function compares two different geographic regions and finds which cities are present in both cities.
def cities_overlap(region: str, database: Dict[str, List[float]]) -> List[str]:

#* Section 4 (Test Cases)

class Section4TestCases(unittest.TestCase):

    #* 1)
    #PS: tests method correctly finds highest value
    def findLargest(self, number1: float, number2: float, number3: float) -> float:
        return number1
    def test_largest(self):
            self.assertEqual(self.findLargest(36, 37, 38), 38)
            self.assertEqual(self.findLargest(-5, 0, 10), 10)
            self.assertEqual(self.findLargest(-3.4, 5.5, 1.2), 5.5)
        pass

    #* 2)
    #PS: tests method finds string
    def find_no_capital(self, word: str) -> bool:
        pass
    def test_capital(self):
        self.assertEqual(self.find_no_capital("hello"), True)
        self.assertEqual(self.find_no_capital("Hey"), False)
        self.assertEqual(self.find_no_capital("nope"), True)

    #* 3)
    #PS: tests method that accepts the name of two states and returns the northernmost one
    def find_northernmost(self, state1: str, state2: str): -> str:
    def test_hemi(self):
        self.assertEqual(self.find_northernmost("Alabama","North Dakota"), "North Dakota")
        self.assertEqual(self.find_northernmost("California","Washington"), "Washington")
    pass

#* Section 5 (Whole Functions)

#* 1)
# Ps: Accept a length in feet and return corresponding length in meters
def length(feet: float) -> float:
    return feet/3.281


#* 2)
# Ps: Develop data definition for Musical Note, which has a pitch in Hz and duration in seconds

class MusicalNote:
    def __init__(self, frequency: int, length: int):
        self.frequency = int
        self.length = int
    def __eq__(self, other):
        if isinstance(other, MusicalNote):
            if self.frequency == other.frequency and self.length == other.length:
                return True
            else:
                return False
    def __repr__(self):
        return "The Musical Note is"+ self.frequency + " " + self.length




#* 3)
#Ps: Function accepts a note and returns a new note that is higher by one octave
def up_one_octave(note: MusicalNote) -> MusicalNote:
    return MusicalNote(note.frequency * 2, note.length)

#* 4)

#* Section 5 Test cases

class Section4TestCases(unittest.TestCase):
    def test_f2m(self):
        self.assertEqual(length(5),1.524)

    def test_MusicalNote(self):
        m_ex1 = MusicalNote(300, 240)
        m_ex2 = MusicalNote(230, 890)
        self.assertEqual(m_ex1, m_ex2)

    def test_octave(self):
        self.assertEqual(up_one_octave(MusicalNote(300,24)), MusicalNote(600,24))

    pass
