import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("2023-11-01_17-45-10_output.csv")
data_raw = pd.read_csv("2023-11-01_17-45-10_output.csv")
data.drop(
    ["cardId", "ord", "deckName", "note", "mod", "dictionary_form", "definitions"],
    inplace=True,
    axis=1,
)

data["target"] = data["interval"].apply(lambda x: 1 if x >= 21 else 0)

Y = data["target"].to_numpy()
data.drop(["target"], inplace=True, axis=1)
X = data.to_numpy()
scaler = StandardScaler()
scaler = scaler.fit(X)
X = scaler.transform(X)
clf = MLPClassifier(
    solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1
)
clf = clf.fit(X, Y)
# test = [2500, 88, 2, 2, 432, 8, 0, 1001]

# test = scaler.transform([test])

import ass

from sudachipy import tokenizer, dictionary

mode = tokenizer.Tokenizer.SplitMode.A
tokenizer_obj = dictionary.Dictionary().create()


list_of_sets = []
with open("test2.ass", encoding="utf-16") as f:
    doc = ass.parse(f)
    for i in doc.events[2:]:
        if isinstance(i, ass.line.Dialogue):
            x = {m.surface() for m in tokenizer_obj.tokenize(i.text, mode)}
            list_of_sets.append(x)

temp = set.union(*list_of_sets)

predicted_words = clf.predict(X)
data["fitting_result"] = predicted_words
known_words = data.loc[data["fitting_result"] == 1]

res = data_raw.loc[data_raw.index.isin(known_words.index)]
words = set(res["dictionary_form"].to_numpy())
common_words = words.intersection(temp)

print(common_words)
print(len(common_words))
print(temp)
print(len(temp))

print("--------------------")
print(len(common_words)/len(temp))

