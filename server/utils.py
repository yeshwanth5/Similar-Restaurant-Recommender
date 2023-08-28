import json
import pickle
import os
import pandas as pd

class utils:

    def __init__(self):
        self.names = None
        self.model = None
        self.data = None
        self.index = None

    def load_artifacts(self):
        script_dir=os.path.dirname(__file__)
        artifacts_path = os.path.join(script_dir,'artifacts')
        with open(f"{artifacts_path}/restaurant_names.json") as f:
            self.names = json.load(f)
        with open(f"{artifacts_path}/restaurant_index.json") as f:
            self.index = json.load(f)
        with open(f"{artifacts_path}/zomato_NearestNeighbour_model.pkl", 'rb') as f:
            self.model = pickle.load(f)
        self.data = pd.read_csv(f"{artifacts_path}/vectorized_data.csv")

    def get_restaurant_names(self):
        self.load_artifacts()
        names_list = list(self.names.values())
        names_list.sort()
        return names_list

    def get_nearest_neighbours(self,restaurant_name):
        print(f"Requested for - {restaurant_name}")
        nearest_neighbours =[]
        self.load_artifacts()
        restaurant_index = self.index.get(restaurant_name)
        print(f"Restaurant index - {restaurant_index}")
        data = self.data.iloc[restaurant_index]
        _, indices = self.model.kneighbors([data])
        for index in indices[0]:
            if self.names.get(str(index))!=restaurant_name:
                nearest_neighbours.append(self.names.get(str(index)))
        return nearest_neighbours