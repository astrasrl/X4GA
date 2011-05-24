# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: statpdc.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from anag.basetab import AnagCardPanel

from awc.controls.checkbox import CheckBox
from awc.controls.linktable import LinkTable
from awc.controls.attachbutton import AttachmentButton

from Env import Azienda
bt = Azienda.BaseTab

class UnoZeroCheckBox(CheckBox):

    def __init__(self, *args, **kwargs):
        CheckBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=(1,0))



# Window functions

ID_ANAGMAIN = 16000
ID_HIDESEARCH = 16001

def StatPdcCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.StaticBox( parent, -1, "Ricerca sottoconti" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = UnoZeroCheckBox( parent, ID_HIDESEARCH, "Nascondi nelle ricerche i sottoconti con questo status", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "hidesearch" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( [ 20, 150 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
