import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression



def train(users, posts):
    valid_users = np.unique(users['uid'])
    posts = posts[posts['from_id'].isin(valid_users)]
    posts['text'] = posts['text'].apply(str)
    data = posts.groupby(['from_id'], sort=True).agg({'text': ' '.join,
                                                      'comments': 'sum',
                                                      'likes': 'sum',
                                                      'reposts': 'sum'})
    users.index = users.uid
    users.drop('uid', axis=1, inplace=True)
    data['is_leader'] = users.loc[data.index]['is_leader']
    X = data.drop('is_leader', axis=1)
    Y = data['is_leader'].values
    
    tfidf = TfidfVectorizer()
    model = LogisticRegression()

    model.fit(tfidf.fit_transform(X['text']), Y)
    return model, tfidf

def predict(users, posts, model, tfidf):
    valid_users = np.unique(users['uid'])
    posts = posts[posts['from_id'].isin(valid_users)]
    posts['text'] = posts['text'].apply(str)
    data = posts.groupby(['from_id'], sort=True).agg({'text': ' '.join,
                                                      'comments': 'sum',
                                                      'likes': 'sum',
                                                      'reposts': 'sum'})
    data['pred'] = model.predict(tfidf.transform(data['text']))
    return data


class Model:
    def run(self, data):
        """
        data: dict with {name: pd.DataFrame}
        Method returns dataframe with predictions.
        """
        train_users = data['users_train.csv']
        test_users = data['users_test.csv']
        posts = data['posts.csv']
        model, tfidf = train(train_users.copy(), posts.copy())
        data_preds = predict(test_users.copy(), posts.copy(), model, tfidf)
        x = test_users["uid"]
        pred = pd.DataFrame({
            "uid": x,
            "is_leader": np.zeros(len(x)),
        })
        pred.index = pred.uid
        pred.loc[data_preds.index, 'is_leader'] = data_preds['pred']
        return pred.reset_index(drop=True)
