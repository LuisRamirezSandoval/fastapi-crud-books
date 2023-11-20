from uvicorn import main

if __name__ == "__main__":
    main.run("app:app", host="0.0.0.0", port=8080, reload=True)
