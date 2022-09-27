"""
skill picroft-led
Copyright (C) 2021 Andreas Rother
Modified for multiple outputs by Andrew Martin 2022

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

from gpiozero import DigitalOutputDevice

outA = DigitalOutputDevice(13)
outB = DigitalOutputDevice(19)
outC = DigitalOutputDevice(26)

class PicroftLED(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    def initialize(self):
        try:
            outA.blink(n=1)           
        except outA.error:
            self.log.warning("Can't initialize GPIO - skill will not load")
            self.speak_dialog("error.initialise")
        finally:    
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)
            self.add_event('recognizer_loop:utterance',
                           self.handler_utterance)
            self.add_event('recognizer_loop:audio_output_start',
                           self.handler_audio_output_start)
            self.add_event('recognizer_loop:audio_output_end',
                           self.handler_audio_output_end)
           # self.add_event('recognizer_loop:wakeword',
                         # self.handler_wakeword)
            self.add_event('mycroft.stop',
                           self.handler_mycroft_stop)

    def handler_mycroft_stop(self, message):
        # code to excecute when mycroft.stop message detected...
        outA.off()
        outB.off()
        outC.off()
            
    def handle_listener_started(self, message):
        # code to excecute when active listening begins...
        # light up led
        outA.on()

    def handle_listener_ended(self, message):
        outA.off()
    
    def handler_utterance(self, message):
        outB.on()
    
    def handler_audio_output_start(self, message):
        # start fading led
        outC.on()
        
    def handler_audio_output_end(self, message):
        # stop fading led
        outC.off()
   # def handler_wakeword(self, message):
        # code to excecute when recognizer_loop:wakeword message
       # ledA.pulse(fade_in_time=0.5, fade_out_time=0.5, n=1)
        
def create_skill():
    return PicroftCASELIGHTS()
