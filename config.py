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

config.py

Configuration options for the bot

"""

# Server URL (everything before the index.aspx on the game page)
SERVER = "http://prodgame01.lordofultima.com/35/"

# Bot login details
BOT_USERNAME = "username"
BOT_EMAIL = "email"
BOT_PASSWORD = "password"

# Delay between checks (secs)
# A delay is required to meet the 'normal load' section of the rules for tools, so don't set this too low (<1sec).
SPEED = 1

# Connection timeout (secs)
TIMEOUT = 1

# SQLite database location (you need the FULL path)
DB = '/path/to/database.db'

# Continent (for all chat)
CONT = '33'

# Claims expire time (in hours)
CLAIMS_EXPIRY = 72
