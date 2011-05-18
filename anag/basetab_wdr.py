# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: basetab.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc.controls.textctrl import TextCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.attachbutton import AttachmentButton, AutoNotes

import wx

class TextCtrlCD(TextCtrl):
    def Validate(self):
        return True and self.GetValue()



# Window functions

ID_TEXT = 10000
ID_TXT_DESCRIZ = 10001
ID_TXT_CODICE = 10002
ID_TXT_ID = 10003
ID_BTNATTACH = 10004
ID_AUTONOTES = 10005

def AnagCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 2, 0, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Codice:", wx.DefaultPosition, [60,-1], 0 )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 0 )

    item3 = wx.StaticText( parent, ID_TXT_DESCRIZ, "Descrizione:", wx.DefaultPosition, [90,-1], 0 )
    item1.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 0 )

    item4 = wx.StaticText( parent, ID_TEXT, "id", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item1.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item1.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item6 = TextCtrlCD( parent, ID_TXT_CODICE, "", wx.DefaultPosition, [60,-1], 0 )
    item6.SetName( "codice" )
    item1.Add( item6, 0, wx.GROW|wx.RIGHT, 5 )

    item7 = TextCtrlCD( parent, ID_TXT_DESCRIZ, "", wx.DefaultPosition, [300,-1], 0 )
    item7.SetName( "descriz" )
    item1.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item8 = NumCtrl( parent, integerWidth=6, allowNegative=False, groupDigits=False); item8.SetName("id"); item8.SetEditable(False)
    item1.Add( item8, 0, wx.GROW|wx.RIGHT, 5 )

    item9 = AttachmentButton( parent, ID_BTNATTACH, "", wx.DefaultPosition, [90,-1], 0 )
    item9.SetName( "_btnattach" )
    item1.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = AutoNotes(parent, ID_AUTONOTES); item10.SetName('_attach_autotext')
    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def PdcRelAnagCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Codice:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_BOTTOM|wx.LEFT, 5 )

    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Descrizione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_BOTTOM|wx.LEFT|wx.TOP, 5 )

    item5 = AutoNotes(parent, ID_AUTONOTES); item5.SetName('_attach_autotext')
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT, 5 )

    item3.AddGrowableCol( 1 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_BOTTOM, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "(id)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.LEFT, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item7, 0, wx.ALIGN_CENTER, 5 )

    item8 = TextCtrlCD( parent, ID_TXT_CODICE, "", wx.DefaultPosition, [60,-1], 0 )
    item8.SetName( "codice" )
    item1.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item9 = TextCtrlCD( parent, ID_TXT_DESCRIZ, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "descriz" )
    item1.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item10 = NumCtrl(parent, ID_TXT_ID, integerWidth=6, allowNegative=False, groupDigits=False); item10.SetName("id"); item10.SetEditable(False)
    item1.Add( item10, 0, wx.ALIGN_CENTER|wx.LEFT, 5 )

    item11 = AttachmentButton( parent, ID_BTNATTACH, "-allegati-", wx.DefaultPosition, [90,-1], 0 )
    item11.SetName( "_btnattach" )
    item1.Add( item11, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

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
