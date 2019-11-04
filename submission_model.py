import numpy as np
import pandas as pd
import sys


class Model:
    def run(self, data):

        """
        data: dict, {name: pd.DataFrame}
        """
        friends = data['friends.csv']
        likes = data['likes.csv']
        users_groups = data['users_groups.csv']
        users_train = data['users_train.csv']
        groups = data['groups.csv']
        posts = data['posts.csv']
        users_test = data['users_test.csv']

        x = users_test["uid"]
        pred = pd.DataFrame({
            "uid": x,
            "is_leader": np.ones(len(x)),
        })

        return pred

