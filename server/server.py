from concurrent import futures
import grpc
import crud_pb2
import crud_pb2_grpc

class CrudServiceServicer(crud_pb2_grpc.CrudServiceServicer):
    def CreateItem(self, request, context):
        from server import db  # Import db here to avoid circular imports
        db.add_item(request)
        return request

    def ReadItem(self, request, context):
        from server import db  # Import db here to avoid circular imports
        item = db.get_item(request.id)
        if item:
            return item
        context.set_details('Item not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return crud_pb2.Item()

    def UpdateItem(self, request, context):
        from server import db  # Import db here to avoid circular imports
        if request.id in db.items_db:
            db.update_item(request)
            return request
        context.set_details('Item not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return crud_pb2.Item()

    def DeleteItem(self, request, context):
        from server import db  # Import db here to avoid circular imports
        deleted_item = db.delete_item(request.id)
        if deleted_item:
            return request
        context.set_details('Item not found')
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return crud_pb2.ItemId()

    def ListItems(self, request, context):
        from server import db  # Import db here to avoid circular imports
        items = db.list_items()
        item_list = crud_pb2.ItemList()
        item_list.items.extend(items)
        return item_list


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crud_pb2_grpc.add_CrudServiceServicer_to_server(CrudServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()


