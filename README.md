# Moni-test-App

Minimal proyect with CRUD + Api connection + Flask + SQLAlchemy + SQLite 

## Installation

Local 

Use the package manager [pip3](https://pip.pypa.io/en/stable/) and [venv](https://pypi.org/project/virtualenv/) to install all the requirements.

```bash
cd moni-test-app
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt
```


Pull from Docker-Hub
```bash
docker pull fluzko/moni-test-app:latest
```

Create via Dockerfile
```bash
cd moni-test-app
docker build -t moni-test-app .
```

## Usage

Local -> localhost:4000/
```bash
python3 run.py
```

Docker -> localhost:7000/
```bash
sudo docker run -it -p 7000:4000 -d moni-test-app
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
