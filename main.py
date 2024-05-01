from blaze_net import BlazeNet
from model import User

app = BlazeNet()

@app.route('/')
def index(request):
    return app.template_env.get_template('index.html').render()

@app.route('/json-reponce/')
def json_reponce(request):
    # Create a session
    session = app.Session()

    # Query all users from the database
    users = session.query(User).all()
    user_dicts = []
    for user in users:
        user_dict = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        user_dicts.append(user_dict)
    # Close the session
    session.close()
    return app.json_response(user_dicts)

# Run the app
if __name__ == '__main__':
    app.run()
