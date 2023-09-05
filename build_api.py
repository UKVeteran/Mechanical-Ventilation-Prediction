from fastapi import FASTAPI

#importing uvicorn web server to enable developers to reach the api
app = FASTAPI()

#define a root endpoint using .get decorator
@app.get("/")
def index():
    return {"ok": True}







# pip install fastapi
# pip install uvicorn

# python file name and name of the api to browse rootpage
# uvicorn build_api:app --reload
