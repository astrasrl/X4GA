# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: helpsys.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
import awc.layout.images as images
import awc.controls.images as awcimg
import awc.layout.imgfac as imgfac

fac = imgfac.WebBrowserImagesFactory()

from awc.controls.textctrl import TextCtrl
from awc.controls.button import FlatBitmapButton as BitmapButton
from awc.controls.button import FlatButton
from awc.controls.radiobox import RadioBox
from awc.controls.linktable import LinkTable

ID_SEARCHGRID = wx.NewId()

class SearchPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        AnagToolbarSearchFunc(self)

class SSVToggleButton(wx.ToggleButton):

    def __init__(self, *args, **kwargs):
        wx.ToggleButton.__init__(self, *args, **kwargs)
        self.SetValue(True)

class CopyFromRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=('U', 'S'))



# Window functions

ID_BUTPREVIOUS = 12000
ID_BUTNEXT = 12001
ID_BUTHOME = 12002
ID_BUTWORLD = 12003
ID_HTMLPANEL = 12004

def HelpHtmlFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = BitmapButton(parent, ID_BUTPREVIOUS, fac.getWebPreviousBitMap()); item2.SetName('butprev'); item2.SetToolTipString("Richiama la pagina precedente")
    item1.Add( item2, 0, wx.ALIGN_CENTER, 5 )

    item3 = BitmapButton(parent, ID_BUTNEXT, fac.getWebNextBitMap()); item3.SetName('butnext'); item3.SetToolTipString("Richiama la pagina seguente")
    item1.Add( item3, 0, wx.ALIGN_CENTER, 5 )

    item4 = BitmapButton(parent, ID_BUTHOME, fac.getWebHomeBitMap()); item4.SetName('buthome'); item4.SetToolTipString("Richiama la pagina principale")
    item1.Add( item4, 0, wx.ALIGN_CENTER, 5 )

    item5 = BitmapButton(parent, ID_BUTWORLD, fac.getWebWorldBitMap()); item5.SetName('butbrow'); item5.SetToolTipString("Apre la pagina con il browser web")
    item1.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 3 )

    item0.Add( item1, 0, wx.GROW, 5 )

    item6 = wx.Panel( parent, ID_HTMLPANEL, wx.DefaultPosition, [800,600], wx.SUNKEN_BORDER )
    item6.SetName( "htmlpanel" )
    item0.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
