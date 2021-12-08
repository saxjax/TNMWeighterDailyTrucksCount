import json
from src.data_processing import DataProcesser


class MIAdapter:
    """
        The Adapter is responsible for serialization and deserialization of the Transport Network Model (TNM) defined in RFC0020.
        It follows the following interface:
            from_json(JSON model)
            to_json(**table_kwargs)
        All Microservices following TNM must have an Adapter implementing this interface.
    """

    def __init__(self, tnm_model):
        self.tnm = tnm_model
        self.meta_data = None
        self.nodes_data = None
        self.vehicle_data = None

    def from_json(self, options=None):
        """
            Converts the TNM to some internal representation.
            In this Creator service, it converts some options (defined in RFC0020) from JSON to a python dictionary.
        """
        if options == None:
            options = {}
        data_processer = DataProcesser()
        df, self.nodes_data, self.meta_data, self.tnm = data_processer.prepare_data_frame(self.tnm)
        return df

    def to_json(self, predicted_weights):
        data_processer = DataProcesser()
        tnm = data_processer.update_tnm_dictionary(self.tnm, predicted_weights, self.nodes_data, self.meta_data)
        return tnm




