from .. import app



@app.get("/login")
def login():
    return "login"

@app.post("/login")
def login_post():
    return "login"

@app.get("/logout")
def logout():
    return "logout"

@app.get("/register")
def register():
    return "register"

@app.post("/register")
def register_post():
    return "register"