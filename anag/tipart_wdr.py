# -*- coding: iso-8859-15 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: tipart.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid

# Custom source
from anag.basetab import AnagCardPanel

from Env import Azienda
bt = Azienda.BaseTab



# Window functions

ID_ANAGMAIN = 16000

def TipArtCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    item0.AddGrowableCol( 0 )
    
    item1 = AnagCardPanel(parent, -1)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( [ 20, 160 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
