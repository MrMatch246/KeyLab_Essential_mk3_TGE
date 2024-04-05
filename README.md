# Arturia Keylab Essential MK3 TGE
------------------------------------

Modified the Scripts for the Arturia KeyLab Essential Mk3 to add all the easy fixes and the cool features that arturia just overlooked! 
As i am more of an Arrangement Person, please let me know if there is anything in the session direction that would be useful! 
Or anything! I am open to suggestions and will try to implement them as best as i can!

## Current Features (You can choose which to use):

- Fader 9 Controls Master in Tracks Mode (context button 0) and current track in device mode
  - Knob 9 Controls Prehear Volume in Tracks Mode (context button 0) and current track Panning in device mode

- You can set Rewind and FastForward Speed in the Settings.py file (currently set to 4 instead of 1)

- Play Button can work as Play/Pause Button

- Enabled Auto Arm

- Pressing the TAP button doubles as holding a Shift Button that unlocks the following options:  

    - TAP + Rewind / FastForward = previous/next device in chain

    - TAP + Context button 0 (The one that switches Track/Device mode) now MUTEs the Current Track
     
    - TAP + Context button 1 (The one that Arms the current Track) now SOLOs the Current Track
      - You can also Switch the Solo and Arm functionality so that a plain press of the button will solo the track and a press with TAP will arm the track.

    - TAB + PAD Bank A = Mute Tracks

    - TAB + PAD Bank B = Solo Tracks

    - TAP + Main Encoder at any Time shows Mute/Solo Pads as well as Scrolling through Tracks in steps of 4
    
- Double Click the Part Button to Lock the Device
    
- Part + Main Encoder In Device Mode = Scrolls through the Parameter Banks
  - Popup shows selected Device and Bank Number and first and last parameter of the bank
  
- Part + Main Encoder In Mixer Mode scrolls through the Track Banks
  - Bank A : Track Selection
    - They can be clicked to select the track and their color will match the track color.
    - They scroll up and down 4 tracks per encoder click (you will see what i mean).
    - Popup shows selected Track Group and first and last track name of the group
  - Bank B : Track Arming
    - Similar to the Solo/Mute Pads but for Arming Tracks
    - They scroll up and down 4 devices per encoder click (you will see what i mean).

  (TAP/Shift can be used as either both, only Shift mode or only TAP mode)

- ### If you have python3 running (should work on windows and mac) :
  - TAP + Part button Toggles Plugin Window (Wrench Icon) 
    - You need to have the windows opened before you can toggle close them (Ctrl + Alt + P)
  - TAP + Save Saves the current project!!!!!!! (Ctrl + S)
  
  - TAP + Loop loops the current selection (Ctrl + L)
-------------------------


# Install:

- Download the repo as zip  
    ![image](https://github.com/MrMatch246/KeyLab_Essential_mk3_TGE/assets/50702646/10d56113-c67d-4d25-a660-16fdd33b7992) 


- Go into Live

  ![image](https://github.com/MrMatch246/Launchkey_MK3_TGE/assets/50702646/5290bc01-4248-4e5d-9a44-b5f9a80c7d3c)

- then 

  ![image](https://github.com/MrMatch246/Launchkey_MK3_TGE/assets/50702646/559af2d9-a063-437a-b2fe-77be1f838203)

- open "Remote Scripts" in finder/explorer.
  - if there is no "Remote Scripts" folder, create one in the "User Library" folder

- Close Live

- Unzip the downloaded file and copy the "KeyLab_Essential_mk3_TGE" folder into the "Remote Scripts" folder
- Start Live and select it 

  ![image](https://github.com/MrMatch246/KeyLab_Essential_mk3_TGE/assets/50702646/a3a87514-af62-4248-8688-7fcafd98aeb9)

  - Device settings should look like this:

    ![image](https://github.com/MrMatch246/KeyLab_Essential_mk3_TGE/assets/50702646/187ef3db-4d02-4608-b62f-8691b9d2b66a)  
    With input and output set to "KeyLab Essential mk3 MIDI" and the control surface set to "KeyLab Essential mk3 TGE"
    the third row is "KeyLab Essential mk3 ALV" as input and "KeyLab Essential mk3 DINTHRU" as output without the control surface set


IMPORTANT!
The Bank Button should show the assignment of the pads (Solo/Mute) But depending on the Bank selection on startup this might be inverted (cant change that, hardware problem)
If that is the case, double click te bank button to switch its color
