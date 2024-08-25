from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pycaw.constants import CLSID_MMDeviceEnumerator, IID_IAudioEndpointVolume

def set_volume(volume_level):
    # Get default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Set volume level (volume_level should be between 0.0 and 1.0)
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def get_volume():
    # Get current volume level
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    currentVolume = volume.GetMasterVolumeLevelScalar()
    return currentVolume

# Example usage:
set_volume(0.5)  # Set volume to 50%
print("Current volume:", get_volume())
