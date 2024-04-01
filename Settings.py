# This file is just there to Allow you to disable modifications i made to the script
# so that you can cherry pick the changes you want

#If you want implicit arm to be enabled set this to True
ENABLE_AUTO_ARM = True

#If you want to use the Fader 9 as a master fader set this to True
#Will also set Knob 9 to Cue Volume instead of current track pan
FADER_9_IS_MASTER = True

#If you want to use the Tap button as a shift button set this to True
# if you disable this you cant use the shift functionalities of the Tap button
TAP_SHIFT_MODE = True

#If you want to use the Tap button as a shift button and as Tap button set this to True
TAP_DUAL_MODE = False

#If you want to use the Context 1 button that usually arms the track to solo it when used with the Tap button set this to True
TAP_CONTEXT_1_IS_SOLO = True

#Using Tap as shift button and the Pads will either mute or solo Tracks
# Bank A will mute and Bank B will solo
TAP_PADS_MUTE_SOLO = True

#Using Tap as shift button and rewind and fastforward will switch device focus
# This will only work if you are in Device Control Mode not in Track Control Mode
TAP_DEVICE_NAVIGATION = True



#If you can run python3 scripts on your system set this to True
I_HAVE_PYTHON_3 = True

#If you are a Mac user
IS_MAC = False

#Port to use for the Python Bridge
PY_PORT = 49200

# Part + TAP Toggles the Wrench on the Plugin (currently has to be opened manually first and then closed with the button)
# The wrench has three modes black, grey and blue. The button toggles between grey and blue
PY_TOGGLE_WRENCH = True
















### DO NOT CHANGE ANYTHING BELOW THIS LINE ###
if not TAP_SHIFT_MODE:
    TAP_DUAL_MODE = False
    TAP_CONTEXT_1_IS_SOLO = False
    TAP_PADS_MUTE_SOLO = False
    TAP_DEVICE_NAVIGATION = False


if not I_HAVE_PYTHON_3:
    PY_TOGGLE_WRENCH = False





