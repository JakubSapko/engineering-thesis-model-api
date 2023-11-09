import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("2023-11-01_17-45-10_output.csv")

print(data.columns)

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
x = clf.fit(X, Y)
print(x)
# test = [2500, 88, 2, 2, 432, 8, 0, 1001]

# test = scaler.transform([test])
# print(clf.predict(test))

import ass
with open("test.ass", encoding="utf-16") as f:
    doc = ass.parse(f)
    print(doc)
    print(list(doc.sections.keys()))
    print(doc.events)
    for i in doc.events:
        print(i)
