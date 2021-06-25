"""
skill picroft-led
Copyright (C) 2021 Andreas Rother

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from mycroft import MycroftSkill
from mycroft.messagebus.message import Message

from gpiozero import PWDLED

led = PWMLED(12)

class PicroftLED(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    def initialize(self):
        try:
            led.blink(n=1)           
        except led.error:
            self.log.warning("Can't initialize GPIO - skill will not load")
            self.speak_dialog("error.initialise")
        finally:    
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)
            self.add_event('recognizer_loop:utterance',
                           self.handle_utterance)
    
    def handle_listener_started(self, message):
        # code to excecute when active listening begins...
        # light up led
        led.on()

    def handle_listener_ended(self, message):
        # start fading led
        led.pulse()

    def handle_utterance(self, message):
        # stop fading led
        led.off()
            
def create_skill():
    return PicroftLED()
