from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # reruns the web server when the code is changed. Turn this off in production
    

