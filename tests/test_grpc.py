import unittest
import grpc
from google.protobuf import empty_pb2
import crud_pb2
import crud_pb2_grpc
from server.server import CrudServiceServicer
from server import db


class TestCrudService(unittest.TestCase):

    def setUp(self):
        self.service = CrudServiceServicer()
        db.items_db.clear() 

    def test_create_item(self):
        item = crud_pb2.Item(id=1, name="Test Item", description="This is a test.")
        response = self.service.CreateItem(item, None)
        self.assertEqual(response.id, 1)

    def test_read_item(self):
        item = crud_pb2.Item(id=1, name="Test Item", description="This is a test.")
        self.service.CreateItem(item, None)
        request = crud_pb2.ItemId(id=1)
        response = self.service.ReadItem(request, None)
        self.assertEqual(response.name, "Test Item")

    def test_update_item(self):
        item = crud_pb2.Item(id=1, name="Test Item", description="This is a test.")
        self.service.CreateItem(item, None)
        updated_item = crud_pb2.Item(id=1, name="Updated Item", description="Updated description.")
        response = self.service.UpdateItem(updated_item, None)
        self.assertEqual(response.name, "Updated Item")

    def test_delete_item(self):
        item = crud_pb2.Item(id=1, name="Test Item", description="This is a test.")
        self.service.CreateItem(item, None)
        request = crud_pb2.ItemId(id=1)
        response = self.service.DeleteItem(request, None)
        self.assertEqual(response.id, 1)

    def test_list_items(self):
        item1 = crud_pb2.Item(id=1, name="Test Item 1", description="This is a test.")
        item2 = crud_pb2.Item(id=2, name="Test Item 2", description="This is another test.")
        self.service.CreateItem(item1, None)
        self.service.CreateItem(item2, None)
        response = self.service.ListItems(empty_pb2.Empty(), None)
        self.assertEqual(len(response.items), 2)


if __name__ == '__main__':
    unittest.main()
