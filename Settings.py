# This file is just there to Allow you to disable modifications I made to the
# script so that you can cherry-pick the changes you want


############## GENERAL FEATURES ##############
# If you want implicit arm to be enabled set this to True
ENABLE_AUTO_ARM = True

# If you want to use the Fader 9 as a master fader set this to True
# Will also set Knob 9 to Cue Volume instead of current track pan
FADER_9_IS_MASTER = True

############## TAP BUTTON FEATURES ##############
# If you want to use the Tap button as a shift button set this to True
# if you disable this you cant use the shift functionalities of the Tap button
TAP_SHIFT_MODE = True

# If you want to use the Tap button as a shift button and as Tap button set
# this to True
TAP_DUAL_MODE = False

# If you want to use the Context 0 button that usually switches Track/device mode the track to mute
# it when used with the Tap button set this to True
TAP_CONTEXT_0_IS_MUTE = True

# If you want to use the Context 1 button that usually arms the track to solo
# it when used with the Tap button set this to True
TAP_CONTEXT_1_IS_SOLO = True

# Using Tap as shift button and the Pads will either mute or solo Tracks
# Bank A will mute and Bank B will solo
TAP_PADS_MUTE_SOLO = True

# Using Tap as shift button and rewind and fastforward will switch device
# focus This will only work if you are in Device Control Mode not in Track
# Control Mode
TAP_DEVICE_NAVIGATION = True
############## PART BUTTON FEATURES ##############

# If you want to use double click on the Part button to lock the device set this to True
ENABLE_DOUBLE_PART_DEVICE_LOCK = True


############## PYTHON BASED FEATURES ##############
# If you can run python3 scripts on your system set this to True
I_HAVE_PYTHON_3 = True

# If you are a Mac user
IS_MAC = False

# Port to use for the Python Bridge
PY_PORT = 49200

# Part + TAP Toggles the Wrench on the Plugin (currently has to be opened
# manually first and then closed with the button) The wrench has three modes
# black, grey and blue. The button toggles between grey and blue
PY_TOGGLE_WRENCH = True

# Save your Project! with the Tap + Save Button!!!
PY_SAVE_PROJECT = True

# ############# ENCODER USAGE ############## Use The Main Encoder + keeping
# Part pressed to scroll through the device parameter Banks
ENCODER_DEVICE_BANK = True

# Set this to false if you don't want the encoder to jump to the first bank
# after the last bank
ENABLE_ROUNDTRIP_BANKING_PARAM = True

# Use The Main Encoder + keeping Part pressed to scroll through the track if
# in Track Control Mode
ENCODER_TRACK_BANK = True
ENCODER_TRACK_BANK_TRACKS_PER_CLICK = 4

# Set this to false if you don't want TAP and the encoder to also show the tracks
ENCODER_TRACK_BANK_TAP = True

# Set this to false if you don't want the encoder to jump to the first Tracks
# Page after the last bank
ENABLE_ROUNDTRIP_BANKING_TRACK = False


#Switch encoder and up down buttons for track and scene navigation
SCENE_TRACK_NAVIGATION_SWITCH = True










### DO NOT CHANGE ANYTHING BELOW THIS LINE ###
if not TAP_SHIFT_MODE:
    TAP_DUAL_MODE = False
    TAP_CONTEXT_1_IS_SOLO = False
    TAP_CONTEXT_0_IS_MUTE = False
    TAP_PADS_MUTE_SOLO = False
    TAP_DEVICE_NAVIGATION = False

if not I_HAVE_PYTHON_3:
    PY_TOGGLE_WRENCH = False
    PY_SAVE_PROJECT = False

if not ENCODER_TRACK_BANK:
    ENCODER_TRACK_BANK_TRACKS_PER_CLICK = 8
