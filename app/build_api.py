from fastapi import FastAPI
from mechvent.predict import demo_predict
from mechvent.predict import demo_predict_csv

#importing uvicorn web server to enable developers to reach the api
app = FastAPI() #new api object

#define a root entrypoint using .get decorator
@app.get("/")
def index():
    # load deep learning model

    #model.predict(..)
    return {"welcome": True}


# new endpoint to predict, this endpoint only response to the http get requests
@app.get("/predict_from_csv")
def predict(R:float,
            C:float,
            u_in: float,
            u_out: float
    ):
    return demo_predict_csv(R=R, C=C, u_in=u_in, u_out=u_out)

@app.get("/predict_series_with_id")
def predict(idx:int):

    return demo_predict(idx=idx)
