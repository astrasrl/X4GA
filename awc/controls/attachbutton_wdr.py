# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: attachbutton.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
import wx

import awc.controls.images as images
from awc.controls.radiobox import RadioBox
from awc.controls.checkbox import RCheckBox
from awc.controls.notebook import Notebook

class ValueRadioBox(RadioBox):
    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=(5,1,2,3,4))


class VoicePlayerPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        VoicePlayerFunc(self)


class VoicePlayerDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        recorder = kwargs.pop("display_connect", False)
        wx.Dialog.__init__(self, *args, **kwargs)
        if recorder:
            p = wx.Panel(self, -1)
            AttachVoiceFunc(p)
        else:
            p = VoicePlayerPanel(self)
        s = wx.BoxSizer( wx.VERTICAL )
        s.Add(p, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5)
        self.SetSizer(s)
        s.SetSizeHints(self)
        if recorder:
            c = self.FindWindowByName('attach_voice')
            c.Enable(False)
            self.Bind(wx.EVT_BUTTON, self._OnStore, c)
    
    def _OnVoiceRecord(self, event):
        self.VoiceRecord()
    
    def _OnVoicePlay(self, event):
        try:
            self.VoicePlay(self.filename)
        except:
            pass
    
    def _OnVoiceStop(self, event):
        self._voice_play = False
        self._voice_rec = False
    
    def _OnStore(self, event):
        self._voice_play = False
        self._voice_rec = False
        self.EndModal(1)
    
    def _OnQuit(self, event):
        self._voice_play = False
        self._voice_rec = False

from awc.controls.textctrl import TextCtrl, TextCtrl_LC



# Window functions

ID_TEXT = 10000
ID_TEXTCTRL = 10001
ID_ATTACH_SPECS = 10002

def AttachButtonDetailsFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Dettagli allegato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wx.StaticBox( parent, -1, "Descrizione" )
    item3 = wx.StaticBoxSizer( item4, wx.HORIZONTAL )
    
    item5 = TextCtrl_LC( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [500,-1], 0 )
    item5.SetName( "description" )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

    item2.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2.AddGrowableCol( 0 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = Notebook( parent, ID_ATTACH_SPECS, wx.DefaultPosition, wx.DefaultSize, 0 )
    item6 = item7
    
    item8 = wx.Panel( item7, -1 )
    AttachNoteFunc(item8, False)
    item7.AddPage( item8, "Annotazione" )

    item9 = wx.Panel( item7, -1 )
    AttachFileFunc(item9, False)
    item7.AddPage( item9, "Documento" )

    item10 = wx.Panel( item7, -1 )
    AttachUrlFunc(item10, False)
    item7.AddPage( item10, "Pagina WEB" )

    item0.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ICON_WEB = 10003
ID_ATTACH_URL = 10004

def AttachUrlFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Allega indirizzo Internet", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticBitmap(parent, ID_ICON_WEB, images.getWeb32Bitmap())
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "URL:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item2.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = TextCtrl_LC( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item5.SetName( "url" )
    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.Button( parent, ID_ATTACH_URL, "Allega URL", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.SetDefault()
    item6.SetName( "attach_url" )
    item2.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.AddGrowableCol( 2 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ICON_FILE = 10005
ID_SEARCHFILE = 10006
ID_ATTACH_FILE = 10007

def AttachFileFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Allega documento", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticBitmap(parent, ID_ICON_FILE, images.getImage32Bitmap())
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "File:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item2.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = TextCtrl_LC( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], 0 )
    item5.SetName( "file" )
    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.Button( parent, ID_SEARCHFILE, "...", wx.DefaultPosition, [20,-1], 0 )
    item6.SetName( "search_file" )
    item2.Add( item6, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item7 = wx.Button( parent, ID_ATTACH_FILE, "Allega file", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetDefault()
    item7.SetName( "attach_file" )
    item2.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.AddGrowableCol( 2 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ICON_SCANNER = 10008
ID_CHANGE_TWAIN = 10009
ID_ATTACH_TWAIN = 10010

def AttachTwainFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Acquisizione TWAIN (scanner, fotocamera, ecc.)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticBitmap(parent, ID_ICON_SCANNER, images.getScanner32Bitmap())
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "Sorgente:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item2.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = TextCtrl( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,-1], wx.TE_READONLY )
    item5.SetName( "twain_source" )
    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.Button( parent, ID_CHANGE_TWAIN, "Cambia...", wx.DefaultPosition, [60,-1], wx.NO_BORDER )
    item6.SetName( "change_twain" )
    item2.Add( item6, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item7 = wx.Button( parent, ID_ATTACH_TWAIN, "Allega scansione", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetDefault()
    item7.SetName( "attach_twain" )
    item2.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.AddGrowableCol( 2 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_GRID_CONTAINER = 10011
ID_COUNTERS = 10012
ID_SAVE_MODIF = 10013

def AttachGridFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.Panel( parent, ID_GRID_CONTAINER, wx.DefaultPosition, [800,400], wx.SUNKEN_BORDER )
    item1.SetName( "grid_container" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_COUNTERS, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetName( "counters" )
    item2.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.Button( parent, ID_SAVE_MODIF, "Salva modifiche", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "save_modif" )
    item2.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.AddGrowableCol( 0 )

    item2.AddGrowableCol( 1 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ICON_AUDIO = 10014
ID_VOICEPLAYER = 10015
ID_ATTACH_VOICE = 10016

def AttachVoiceFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Allega nota vocale", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.StaticBitmap(parent, ID_ICON_AUDIO, images.getAudio32Bitmap())
    item2.Add( item3, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item4 = VoicePlayerPanel(parent)
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item5 = wx.Button( parent, ID_ATTACH_VOICE, "Allega nota vocale", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetDefault()
    item5.SetName( "attach_voice" )
    item2.Add( item5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2.AddGrowableCol( 1 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_VOICE_PLAY = 10017
ID_VOICE_RECORD = 10018
ID_VOICE_STOP = 10019
ID_VOICE_POSITION = 10020
ID_VOICE_PROGRESS = 10021

def VoicePlayerFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.Button( parent, ID_VOICE_PLAY, "play", wx.DefaultPosition, [30,-1], 0 )
    item2.SetName( "voice_play" )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item3 = wx.Button( parent, ID_VOICE_RECORD, "rec", wx.DefaultPosition, [30,-1], 0 )
    item3.SetName( "voice_record" )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item4 = wx.Button( parent, ID_VOICE_STOP, "stop", wx.DefaultPosition, [30,-1], 0 )
    item4.SetName( "voice_stop" )
    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item5 = wx.BoxSizer( wx.VERTICAL )
    
    item6 = wx.StaticText( parent, ID_TEXT, "tempo:", wx.DefaultPosition, [40,-1], wx.ALIGN_RIGHT )
    item5.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = wx.StaticText( parent, ID_VOICE_POSITION, "", wx.DefaultPosition, [40,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item7.SetName( "voice_position" )
    item5.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item1.Add( item5, 0, wx.ALIGN_BOTTOM, 5 )

    item8 = wx.Gauge( parent, ID_VOICE_PROGRESS, 100, wx.DefaultPosition, [100,-1], wx.GA_SMOOTH|wx.GA_PROGRESSBAR )
    item8.SetName( "voice_progress" )
    item1.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.AddGrowableCol( 4 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ICON_TEXT = 10022
ID_AUTOTEXT = 10023
ID_ATTACH_NOTE = 10024

def AttachNoteFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Allega annotazione", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item1.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item3 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item4 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item5 = wx.StaticBitmap(parent, ID_ICON_TEXT, images.getText32Bitmap())
    item4.Add( item5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Nota:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item4.Add( item6, 0, wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = RCheckBox( parent, ID_AUTOTEXT, "AutoText", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetName( "autotext" )
    item3.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALL, 5 )

    item3.AddGrowableRow( 1 )

    item2.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item8 = TextCtrl_LC( parent, ID_TEXTCTRL, "", wx.DefaultPosition, [80,60], wx.TE_MULTILINE )
    item8.SetName( "note" )
    item2.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.Button( parent, ID_ATTACH_NOTE, "Allega Nota", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetDefault()
    item9.SetName( "attach_note" )
    item2.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2.AddGrowableCol( 1 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ICON_DOCUMENT = 10025

def AttachSpyFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticBitmap(parent, ID_ICON_DOCUMENT, images.getText20Bitmap()); item1.SetName('spy_bitmap')
    item0.Add( item1, 0, wx.ALIGN_CENTER, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
