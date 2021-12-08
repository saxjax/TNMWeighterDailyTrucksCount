# import json
# from decimal import Decimal

# class DecimalEncoder(json.JSONEncoder):
#     """
#         Class used to serialize/deserialize which can do decimal numbers.
#     """
#     def default(self, obj):
#         if isinstance(obj, Decimal):
#             return str(obj)
#         return json.JSONEncoder.default(self, obj)

# class Adapter:
#     def __init__(self):
#         """
#             The Adapter constructor.
#             Holds a reference to the tnm model.
#         """
#         self.tnm = {}

#     def from_json(self, input):
#         """
#             Converts the input into a tnm model, and saves the reference in the adapter.
#             This is used in the to_json function to fill in the edge weights.
#         """
#         self.tnm = json.loads(input)
#         return self.tnm

#     def to_json(self, **outputs):
#         """ 
#             Inserts the normalized weights into the tnm model, and serializes it as the output
#         """
#         for key, data in outputs["weights"].items():
#             self.tnm["nodes"][key]["edges"][data["edge_id"]]["weight"] = data["normalized_weight"]
        
#         return json.dumps(self.tnm, cls=DecimalEncoder)
            