#!/usr/bin/python3
"""unit tests for the Amenity class"""

import unittest
import models
from models.amenity import Amenity
from datetime import datetime
from time import sleep
import os


class Test_Amenity(unittest.TestCase):
    """test casess for the Amenity class"""

    def setUp(self):
        """set up the environ before each test case"""
        self.amenity = Amenity()

    def tearDown(self):
        """clean up the test environ after each test case if needed"""
        self.amenity = None

    def test_init_with_arguments(self):
        """test initialization with arguments"""
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        self.amenity = Amenity(**data)

        # Verify that the attributes are set correctly
        self.assertEqual(self.amenity.id, '123')
        self.assertEqual(self.amenity.created_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.amenity.updated_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(self.amenity.name, 'Test')

    def test_init_without_arguments(self):
        """test Initialization without Arguments"""
        self.amenity = Amenity()

        # Verify that the attributes are set correctly
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)
        self.assertEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_args(self):
        """Test unused args"""
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_with_kwargs(self):
        """test with kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        am = Amenity(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(am.id, "123")
        self.assertEqual(am.created_at, date)
        self.assertEqual(am.updated_at, date)

    def test_kwargs_None(self):
        """test kwargs with  None"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_with_args_and_kwargs(self):
        """ TestING with both args and kwargs"""
        date = datetime.now()
        tform = date.isoformat()
        am = Amenity(id="123", created_at=tform, updated_at=tform)
        self.assertEqual(am.id, "123")
        self.assertEqual(am.created_at, date)
        self.assertEqual(am.updated_at, date)

    def test_attrubutes_initialization(self):
        """Tests Initialization of attributes"""
        self.assertEqual(self.amenity.name, "")
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_id_is_str(self):
        """Check the id data type"""
        self.assertEqual(str, type(Amenity().id))

    def test_id_is_unique(self):
        """TestING if ids generated are unique"""
        user1 = Amenity()
        user2 = Amenity()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at_datetime(self):
        """checks if the attribute is a datetime Object"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_created_at_timestamp(self):
        """CheckING if the timestamp is different"""
        user1 = Amenity()
        sleep(0.05)
        user2 = Amenity()
        self.assertLess(user1.created_at, user2.created_at)

    def test_updated_at_datetime(self):
        """Checkss if attribute is a datetime Object"""
        self.assertEqual(datetime, type(Amenity(). updated_at))

    def test_updated_at_timestamp(self):
        """Checkss if the timestamp is different"""
        user1 = Amenity()
        sleep(0.05)
        user2 = Amenity()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_instance_storage(self):
        """Checks if storage and retrival were a success"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test__str__(self):
        """Testss the String Representation"""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.__str__(), am2.__str__())

    def test_str_method(self):
        """Testss the strING method"""
        amenity_string = str(self.amenity)
        self.assertIn("[Amenity]", amenity_string)
        self.assertIn("id", amenity_string)
        self.assertIn("created_at", amenity_string)
        self.assertIn("updated_at", amenity_string)

    def test_save(self):
        """Testss the effectivity of timestamp Updates"""
        am = Amenity()
        sleep(0.1)
        update = am.updated_at
        am.save()
        self.assertLess(update, am.updated_at)

    def test_two_saves(self):
        """Tests the effectivity of different timestamps Updates"""
        am = Amenity()
        sleep(0.1)
        upadte1 = am.updated_at
        am.save()
        update2 = am.updated_at
        self.assertLess(upadte1, update2)
        sleep(0.1)
        am.save()
        self.assertLess(update2, am.updated_at)

    def test_save_updates_file(self):
        """Tests that Updates are Updated and stored correctly"""
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_save_method(self):
        """Tests the save Method"""
        updated_at_1 = self.amenity.updated_at
        self.amenity.save()
        updated_at_2 = self.amenity.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_to_dict(self):
        """Testss the expected Output"""
        expected_dict = {
            'id': self.amenity.id,
            'created_at': self.amenity.created_at.isoformat(),
            'updated_at': self.amenity.updated_at.isoformat(),
            '__class__': 'Amenity'
        }
        self.assertEqual(self.amenity.to_dict(), expected_dict)

    def test_to_dict_type(self):
        """Verifies the class returns a Dictionary"""
        am = Amenity()
        self.assertTrue(dict, type(am.to_dict()))

    def test_different_to_dict(self):
        """Tests that the class produces two(2) different dictionary for different instancess"""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertNotEqual(am1.to_dict(), am2.to_dict())

    def test_to_dict_has_correct_keys(self):
        """Testss that the dictionary contain the right key"""
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("__class__", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())

    def test_to_dict_created_at_format(self):
        """Checkss the ISO formatted str"""
        am = self.amenity.to_dict()
        created_at = am["created_at"]
        self.assertEqual(created_at, self.amenity.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """Checkss the ISO formatted str"""
        am = self.amenity.to_dict()
        updated_at = am["updated_at"]
        self.assertEqual(updated_at, self.amenity.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()

