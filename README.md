# CURRENTY UNTESTED

# Picroft GPIO trigger

* Pull 3 separate GPIO pins high (3.3v) when listening, "thinking", and when thinking is over and output starts

GPIO pins are:
* 13 - Listening
* 19 - "thinking"
* 26 - Output


Modified from https://github.com/arother/picroft-led which, in turn was modified from https://github.com/andlo/picroft-google-aiy-voicekit-skill

Documentation for GPIO control (gpiozero) can be found at: https://github.com/gpiozero/gpiozero/blob/master/docs/api_output.rst
Documentation for Mycroft triggers can be found at: https://github.com/MycroftAI/documentation/blob/f7961104558f6b97e63ce4029446370980646cd2/docs/mycroft-technologies/mycroft-core/message-types.md
