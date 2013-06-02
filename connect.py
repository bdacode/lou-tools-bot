"""

LoU Bot - A chatbot for LoU
Copyright (c) 2011 Adam Tonks (obsessive1)

--

LoU Bot is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

LoU Bot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with LoU Bot.  If not, see <http://www.gnu.org/licenses/>.

---

connect.py

Provides functions for accessing/connecting to the LoU game API

"""

import config, database, json, random, urllib, urllib2

# Retrieves the session from the database, optionally testing it
def get_session(test=False):

    # Get stored session from DB
    session = database.get_setting('session')

    # Test session if required
    # If test fails or no session is found, generate a new one
    if test:
        session = test_session()

    if not session:
        session = new_session()

    return session

# Tests the stored session
def test_session():

    # Make test poll
    test = poll(("PLAYER:",))

    # If player data wasn't returned, then session is invalid
    try:
        if not test[1]['C'] == u'PLAYER':
            session = None
        else:
            session = get_session()
        return session
    except TypeError:
        return None

# Generates a new session ID
def new_session():

    # Build opener with cookies
    o = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    urllib2.install_opener(o)

    # Encode data
    data = urllib.urlencode({'mail':config.BOT_EMAIL,'password':config.BOT_PASSWORD})

    # Do the login...
    r = o.open('https://www.lordofultima.com/en/user/login?destination=%40homepage%3F', data)
    response = r.read()
    r.close()

    # Extract session ID
    s = response.find('Id" value="')
    p = s + 11
    sess = response[p:p+36]

    # Generate session key from session ID
    key = get("OpenSession",{'session':sess,'reset':'false'})
    key = key['i']

    # Save session key to database
    database.set_setting('session',key)

    # Connect session to continent chat
    poll(("CHAT:/c 33",))

    return key


# Retrieves data from a specified endpoint
def get(endpoint,data):

    # Define URL
    url = config.SERVER + "Presentation/Service.svc/ajaxEndpoint/" + endpoint

    # Encode data
    data = json.dumps(data)

    # Replace ## with \f (because I can't get it escaped beforehand for some odd reason)
    data = data.replace('##',r'\f')
    
    # Add URL + data to request
    r = urllib2.Request(url,data)

    # Add extra headers
    r.add_header('Content-Type', 'application/json')
    r.add_header('X-Qooxdoo-Reponse-Type', 'application/json')
    r.add_header('Referer', config.SERVER + 'index.aspx')

    # Make request, decode and return
    r = urllib2.urlopen(r)
    try:
        d = json.loads(r.read())
    except ValueError:
        d = None
    return d

# Runs a poll request
def poll(requests,test=False):

    # Load requests into string
    reqs = ""
    for r in requests:
        reqs += (r + '##')

    # Set up data
    data = {
        'session': get_session(test),
        'requestid': random.randint(0,100),
        'requests': reqs
    }

    # Return result of poll
    return get('Poll', data)
