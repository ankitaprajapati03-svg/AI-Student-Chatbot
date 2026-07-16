import pandas as pd
import joblib
import sqlite3

model = joblib.load("model.pkl")

vectorizer = joblib.load("vectorizer.pkl")

data = pd.read_csv("dataset.csv")


def get_response(user_input):

    user_vector = vectorizer.transform([user_input])

    predicted_intent = model.predict(user_vector)[0]

    response = data[data["Intent"] == predicted_intent]["Response"].iloc[0]

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute(

        "INSERT INTO chat_history(question,response) VALUES (?,?)",

        (user_input,response)

    )

    connection.commit()

    connection.close()

    return response