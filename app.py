"""
Entry into main app
"""

from dashboard.content import app

server = app.server

# If python running this file as main program, sets __name__ == __main__
if __name__ == '__main__':
    app.run_server(debug=True)