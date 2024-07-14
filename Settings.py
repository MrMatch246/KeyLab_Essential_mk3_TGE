# This file is just there to Allow you to disable modifications I made to the
# script so that you can cherry-pick the changes you want


############## GENERAL FEATURES ##############
# If you want implicit arm to be enabled set this to True
ENABLE_AUTO_ARM = True


#Sets the Speed of the Fast Forward and Rewind Buttons
REWIND_FORWARD_SPEED = 4

# Set this to True if you the Play button to pause/continue on press
# and start from song marker on longer press
ENABLE_PLAY_PAUSE_BUTTON = True


# If you want to use the Context 0 button that usually switches Track/device mode the track to mute
# it when used with the Tap button set this to True
TAP_CONTEXT_0_IS_MUTE = True

# If you want to use the Context 1 button when used with the Tap button to ARM
# set this to True
# False will make it Solo
TAP_CONTEXT_1_IS_ARM = True

#If you want to have the Context button 1 to Solo by default set this to True
CONTEXT_1_IS_SOLO = True

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

# Update the Filesystem/Places with the Tap + Update Button
# Set it to true and the path to a folder you want to update
# This is used for situations like a Google Drive folder in places that doesnt
# trigger an update when changes are synchronized.
# especially useful if you collaborate, and or drag and drop doesnt work due to
# Ableton running as Admin
PY_UPDATE_FILESYSTEM = False
PY_UPDATE_FILESYSTEM_PATH = None

# If you want to Loop the selected area with the Tap + Loop Button
PY_ENABLE_LOOP_SELECTION = True


# Set this to false if you don't want the encoder to jump to the first bank
# after the last bank (only for the device parameter bank)
ENABLE_ROUNDTRIP_BANKING_PARAM = True

ENCODER_TRACK_BANK_TRACKS_PER_CLICK = 1

# Set this to false if you don't want the encoder to jump to the first Tracks
# Page after the last bank
ENABLE_ROUNDTRIP_BANKING_TRACK = False

#Switch encoder and up down buttons for track and scene navigation
SCENE_TRACK_NAVIGATION_SWITCH = True

#Set this to True if you want the encoder to scroll in the opposite direction
#for the Pads
ENCODER_TRACK_DIRECTION_INVERTED = False


### DO NOT CHANGE ANYTHING BELOW THIS LINE ###
if not I_HAVE_PYTHON_3:
    PY_TOGGLE_WRENCH = False
    PY_SAVE_PROJECT = False


