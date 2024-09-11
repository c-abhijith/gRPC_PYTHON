import grpc
import crud_pb2
import crud_pb2_grpc
from google.protobuf import empty_pb2


def run():
    # Ensure to specify the port correctly, e.g., 'localhost:50051'
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = crud_pb2_grpc.CrudServiceStub(channel)

        # Create an item
        item = crud_pb2.Item(id=2, name="Item 1", description="This is the first item.")
        response = stub.CreateItem(item)
        print("Item created:", response)

        # Read the item
        response = stub.ReadItem(crud_pb2.ItemId(id=1))
        print("Item read:", response)

        # Update the item
        updated_item = crud_pb2.Item(id=1, name="Updated Item", description="Updated description.")
        response = stub.UpdateItem(updated_item)
        print("Item updated:", response)

        # List all items
        response = stub.ListItems(empty_pb2.Empty())
        print("Item list:", response.items)

        # Delete the item
        response = stub.DeleteItem(crud_pb2.ItemId(id=1))
        print("Item deleted:", response)


if __name__ == '__main__':
    run()
