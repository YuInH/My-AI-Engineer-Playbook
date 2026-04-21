from fastapi import FastAPI

# Step 1: Initialize FastAPI application
app = FastAPI()

# Step 2: Defining a GET endpoint at the root URL ("/")
@app.get("/")
def root():
    # Step 3: Return the correct greeting
    return {"message": "Hello AI Engineer"}