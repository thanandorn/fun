import unittest
#from metadata_finder import list_instances
from metadata_finder import get_instance_metadata

class TestMetadataFinder(unittest.TestCase):
    def test_metadata_finder(self):
        instance_id = 'i-0938ac5c6e3b344db'
        result = get_instance_metadata(instance_id)
        self.assertEqual(result['InstanceId'], instance_id, 'The result should be ' + instance_id)

if __name__ == '__main__':
    unittest.main()
