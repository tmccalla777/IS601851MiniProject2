import unittest
from CsvReader.CsvReader import CsvReader, ClassFactory

'''
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('/Tests/Data/Unit Test Square Root.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_objects('person')
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])
        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)
'''

if __name__ == '__main__':
    unittest.main()
