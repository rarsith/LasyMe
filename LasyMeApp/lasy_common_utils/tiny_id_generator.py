from bson import ObjectId


class TinyCustomIDGenerator:
    def gen_id(self):
        hex_id = str(ObjectId())
        int_id = int(hex_id, 10)
        return int_id
