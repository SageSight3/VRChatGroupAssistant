from PySide6.QtCore import Signal

'''
VRCGA will treat signals as indications of singular specific events
This means should be no question for what they mean to a receiving slot.

For example: 
For whether VRCGA's backend reports that a user's entered login credentials were accepted or denied
by VRChat when querying the VRChat API, we could just have one signal that also passes a boolean value
representing accepted or failed to whatever slot it connects to:

    authCredentialsAccepted = Signal(bool)

However, doing it this way would mean that all slots connected to this signal would need a control flow to figure out
whether the credentials were accepted or not, before knowing what to do.

So, instead, we have two signals to avoid this:
    
    authCredentialsAccepted = Signal()
    authCredentialsDenied = Signal()

By designing our signals with this constraint, we guarantee that whenever we create and implement a new slot,
it will always only handle the events it's being made for.

'''

# VRCGA_GUI_TEST
# temp signal for GUI development
devSignal = Signal(str)

'''
Frontend Local Communication Exclusive signals (FLCE signals)
Signals for communication soley between frontend objects

'''

# Order matters here, 1st str is username, 2nd str is password
loginCreds = Signal(str, str)
twoFACode = Signal(str)
logout = Signal()

'''
Model Information signals (MI signals)

Signals for when the frontend model object's data changes. Not all model data will necessarily
have a signal for when it updates.

These should all be originally emitted from the frontend's model object

'''

authCredsAccepted = Signal()
authCredsDenied = Signal()
twoFACodeAccepted = Signal()
twoFACodeDenied = Signal()
requiresTOTP2fa = Signal()
requiresEmailOTP2fa = Signal()