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

bot.py

Functions to do the actual bot stuff

"""

import connect, database, filters

# Processes a message
def process(raw):

    # Check the message is from the right chat channel
    if raw['c'] == '@A' or raw['c'] == 'privatein' or (raw['c'] == '@C' and raw['m'][:1] == '!'):

        # Save sender name if whispering
        database.set_setting('lastwhisper',raw['s'][1:])

        # Filter out the text and the sender
        text = raw['m']
        sender = raw['s'][1:]

        # Run through filters file
        filters.process(text,sender,raw['c'][1:])

        # Query the database for any matching filters
        db = database.get_db()
        r = db.execute("select * from filters where ? like search",(text,))

        # Loop through results
        for out in r:

            # Replace sender and arg with correct values
            out = out[1].replace('{{sender}}', sender)
            try:
                out = out.replace('{{arg}}', text.split(' ',1)[1])
            except IndexError:
                pass
            output(out,raw['c'][1:])


    return True

# Outputs given message to alliance chat
def output(message,chatroom='A'):
    if chatroom == 'C':
        connect.poll(("CHAT:" + message,),True)
    elif chatroom == 'rivatein':
        connect.poll(("CHAT:/w " + database.get_setting('lastwhisper') + ' ' + message,),True)
    else:
        connect.poll(("CHAT:/a " + message,),True)
    return True

# Checks for any new messages
def check():
    r = connect.poll(("CHAT:",),True)
    try:
        r[1]
    except (IndexError, TypeError):
        return False

    for msg in r[1]['D']:
        process(msg)
        
    return True
