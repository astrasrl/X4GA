# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: util.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Window functions

ID_TEXT = 30200
ID_LISTREF = 30201
ID_LISTDET = 30202
ID_BTNCLOSE = 30203

def RefIntegrityFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item0.Add( [ 20, 10 ] , 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1 = wx.StaticText( parent, ID_TEXT, 
        "Non è possibile eliminare questo elemento, in quanto esso è al momento collegato ad altre tabelle.\n"
        "Fare doppio click su una voce per dettagliare i riferimenti.",
        wx.DefaultPosition, [300,40], 0 )
    item0.Add( item1, 0, wx.GROW|wx.ALL, 5 )

    item2 = wx.ListCtrl( parent, ID_LISTREF, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )
    item0.Add( item2, 0, wx.GROW|wx.ALL, 5 )

    item3 = wx.StaticText( parent, ID_TEXT, "Dettaglio elementi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item4 = wx.ListBox( parent, ID_LISTDET, wx.DefaultPosition, [80,160], [], wx.LB_SINGLE )
    item0.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item5 = wx.Button( parent, ID_BTNCLOSE, "Chiudi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableCol( 1 )

    item0.AddGrowableCol( 2 )

    item0.AddGrowableRow( 1 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
