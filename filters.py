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

filters.py

A space to put any custom filters etc. This is an empty file, so it's licence is fairly redundant.

"""

import bot, database, random, re

def process(text,sender,chatroom):

    # CXX response
    rg = re.compile('(C)(\\d+)',re.IGNORECASE|re.DOTALL)
    m = rg.search(text)
    if m:
        bot.output('C'+m.group(2)+'? I think some idiots must live there.',chatroom)

    # !fight response
    if text.find('!fight') > -1:
        n = random.randint(1,9)
        fightee = text.split(' ',1)[1]
        if n < 4:
            bot.output('On this day, '+sender+' fought '+fightee+', and '+sender+' came out victorious!',chatroom)
        elif n < 7:
            bot.output('On this day, '+sender+' fought '+fightee+', and '+fightee+' came out victorious!',chatroom)
        elif n < 9:
            bot.output('On this day, '+sender+' fought '+fightee+', and obsessive1 came out victorious!',chatroom)
        else:
            bot.output('On this day, '+sender+' fought '+fightee+', and God came out victorious!',chatroom)

    # !tickle response
    if text.find('!tickle') > -1:
        n = random.randint(1,9)
        ticklee = text.split(' ',1)[1]
        if n < 4:
            bot.output(sender+' tickled '+ticklee+' until they parped in their pants.',chatroom)
        elif n < 7:
            bot.output(sender+' tickled '+ticklee+' with their you know what.',chatroom)
        elif n < 9:
            bot.output(sender+' got kicked in the face tickling '+ticklee+'.',chatroom)
        else:
            bot.output(sender+' was killed by a freak serial tickler named '+ticklee,chatroom)

    # !shoot-er
    if text.find('!shoot') > -1:
        leader = 'becaz'
        shootee = text.split(' ',1)[1]
        if shootee.lower() == leader.lower():
            bot.output('Who dare shoot the Monkey high priest! :o',chatroom)
            bot.output(sender+' died at the wrath of '+leader+'.',chatroom)
        else:
            bot.output(sender+' killed '+shootee+'. :(',chatroom)

    # parp response
    if text.find('parp') > -1:
        n = random.randint(1,4)
        if n == 1:
            bot.output(sender+' parped in their pants. Probably best to stay away for a while.',chatroom)
        elif n == 2:
            bot.output(sender+' parped a wet one.',chatroom)
        elif n == 3:
            bot.output(sender+' parped lightening.',chatroom)
        else:
            bot.output(sender+' parped like a boss.',chatroom)

    # add claim
    if text.find('!claim') > -1 and chatroom == 'A':
        try:
            arg = text.split(' ',1)[1]
            xy = arg.split(':',1)
            x = xy[0]
            y = xy[1]
            if len(x) > 3 or len(y) > 3:
                raise IndexError
            if database.check_claim(x,y):
                bot.output('City already claimed by ' + database.check_claim(x,y) + ". :(")
            else:
                database.add_claim(x,y,sender)
                bot.output(x + ':' + y + ' successfully claimed!')
        except IndexError:
            bot.output('Looks like you made a typo.')

    # check claim
    if text.find('!check') > -1 and chatroom == 'A':
        try:
            arg = text.split(' ',1)[1]
            xy = arg.split(':',1)
            x = xy[0]
            y = xy[1]
            if len(x) > 3 or len(y) > 3:
                raise IndexError
            if database.check_claim(x,y):
                bot.output(x + ':' + y + ' is claimed by ' + database.check_claim(x,y) + " :(")
            else:
                bot.output(x + ':' + y + ' is not claimed yet!')
        except IndexError:
            bot.output('Looks like you made a typo.')