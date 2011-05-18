# -*- coding: iso-8859-15 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: gruart.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid

# Custom source
from anag.basetab import AnagCardPanel, WorkZoneNotebook
from anag.catart import CatArtDialog

from awc.controls.linktable import LinkTable

import awc.controls.windows as aw

from Env import Azienda
bt = Azienda.BaseTab



# Window functions

ID_ANAGMAIN = 16000
ID_WORKZONE = 16001

def GruArtCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    item0.AddGrowableCol( 0 )
    item0.AddGrowableRow( 1 )
    
    item1 = AnagCardPanel(parent)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = WorkZoneNotebook( parent, ID_WORKZONE, wx.DefaultPosition, [200,160], 0 )
    if wx.VERSION >= (2,5,2):
        item2 = item3
    else:
        item2 = wx.NotebookSizer( item3 )
    
    item4 = aw.Panel(item3, -1); item4.SetName('GruArtAnagPage')
    GruArtCardAnagFunc(item4, False)
    item3.AddPage( item4, "Dati anagrafici" )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_LBL_SEARCHRESULTS = 16002
ID_TEXT = 16003
ID_FILT_CATART = 16004

def GruArtSpecSearchFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    item0.AddGrowableCol( 0 )
    item0.AddGrowableRow( 5 )
    
    item1 = wx.StaticText( parent, ID_LBL_SEARCHRESULTS, "Mostra solo i gruppi relativi a:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item1.SetName( "searchresultstitle" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3 = wx.StaticBox( parent, -1, "Selezioni" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = wx.FlexGridSizer( 1, 0, 0, 0 )
    item4.AddGrowableCol( 0 )
    item4.AddGrowableCol( 1 )
    
    item5 = wx.FlexGridSizer( 0, 1, 0, 0 )
    item5.AddGrowableCol( 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Da categoria:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item7 = LinkTable(parent, ID_FILT_CATART); item7.SetDataLink(bt.TABNAME_CATART, None, CatArtDialog); item7.SetName('catart1')
    item5.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item4.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item8 = wx.FlexGridSizer( 0, 1, 0, 0 )
    item8.AddGrowableCol( 0 )
    
    item9 = wx.StaticText( parent, ID_TEXT, "A categoria:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item10 = LinkTable(parent, ID_FILT_CATART); item10.SetDataLink(bt.TABNAME_CATART, None, CatArtDialog); item10.SetName('catart2')
    item8.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item4.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CTRCATART = 16005

def GruArtCardAnagFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    item0.AddGrowableCol( 0 )
    
    item2 = wx.StaticBox( parent, -1, "Classificazione di magazzino" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 2, 0, 0 )
    item3.AddGrowableCol( 1 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Fa parte della categoria:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = LinkTable(parent, ID_CTRCATART ); item5.SetDataLink( bt.TABNAME_CATART, "id_catart", CatArtDialog ); item5.SetObligatory()
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( [ 20, 120 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
