import os
from app import create_app

if os.environ.get('DASHAPP') == 'production':
    server = create_app(os.environ.get("DASHAPP") or 'development')
else:
    server = create_app(os.environ.get("DASHAPP") or 'development')


if __name__ == '__main__':
    server.run_server(debug=True)