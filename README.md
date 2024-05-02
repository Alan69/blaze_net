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
pip install blaze-net
```

Or clone this repository to your local machine:

```bash
git clone https://github.com/Alan69/blaze_net.git
```

## Usage

```python
from blaze_net import BlazeNet
from model import User

app = BlazeNet()

@app.route('/')
def index(request):
    return 'Hello, BlazeNet!'

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

if __name__ == "__main__":
    app.run()
```

## Model

```python
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from blaze_net import BlazeNet

app = BlazeNet()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

Base.metadata.create_all(app.engine)
```

## Documentation
For more information on how to use BlazeNet, please refer to the documentation https://pypi.org/project/blaze-net/.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
