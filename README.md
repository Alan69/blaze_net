# BlazeNet

BlazeNet is a Python web framework inspired by Flask. It provides a simple and lightweight solution for building web applications.

## Features

- Routing: Define routes and associate them with view functions.
- Templating: Render HTML templates using Jinja2.
- Database Integration: Integrate SQLAlchemy for database operations.
- Easy to Use: Simple and intuitive API for developing web applications.

## Installation

You can install BlazeNet using pip:

```bash
pip install blaze_net

```bash
from blaze_net import BlazeNet

app = BlazeNet()

@app.route('/')
def index():
    return 'Hello, BlazeNet!'

if __name__ == '__main__':
    app.run()

## Documentation
For more information on how to use BlazeNet, please refer to the documentation.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
