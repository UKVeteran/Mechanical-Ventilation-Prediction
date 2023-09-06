from fastapi import FastAPI


#importing uvicorn web server to enable developers to reach the api
app = FastAPI() #new api object

#define a root entrypoint using .get decorator
@app.get("/")
def index():
    # load deep learning model

    #model.predict(..)
    return {"ok": True}

# new endpoint to predict, this endpoint only response to the http get requests
@app.get("/predict")
def predict(R,C, u_in, u_out):

    # step 1 bring the model  and return prediction
    # step 2 make sure you are returning right value to calculate since the
    # inputs will be received as strings
    return { "pressure": int(R)*int(C)*float(u_in)*int(u_out)}




# pip install fastapi
# pip install uvicorn

# python file name and name of the api to browse rootpage
# uvicorn build_api:app --reload
