# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: spesometro_2013.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc.controls.linktable import LinkTable
from awc.controls.textctrl import TextCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.checkbox import CheckBox, RCheckBox
from awc.controls.radiobox import RadioBox

import anag.lib as alib

from Env import Azienda
bt = Azienda.BaseTab

class AcquistiVenditeCorrispettiviRadioBox(RadioBox):
    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=["A", "V", "C", "T"])


class TipValoriRadioBox(RadioBox):
    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=["M", "T"])



# Window functions

ID_ACQVENCOR = 10000
ID_TEXT = 10001
ID_ANNO = 10002
ID_DATA1 = 10003
ID_DATA2 = 10004
ID_SOLO_ANAG_ALL = 10005
ID_LINE = 10006
ID_ESCLUDI_BLA = 10007
ID_ESCLUDI_BLS = 10008
ID_SOLO_CAUS_ALL = 10009
ID_BUTUPDATE = 10010
ID_REGSPY = 10011
ID_GRIDPANEL = 10012
ID_TOTANADES = 10013
ID_TOTANAIMP = 10014
ID_TOTANAIVA = 10015
ID_TOTANATOT = 10016
ID_TIPVALORI = 10017
ID_MAXAZI = 10018
ID_MAXPRI = 10019
ID_WARNING = 10020
ID_BUTESTRAI = 10021
ID_BUTGENERA = 10022

def SpesometroPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = AcquistiVenditeCorrispettiviRadioBox( parent, ID_ACQVENCOR, "Tipo", wx.DefaultPosition, wx.DefaultSize, 
        ["Acquisti","Vendite","Corrisp.","TUTTO"] , 2, wx.RA_SPECIFY_ROWS )
    item2.SetName( "acqvencor" )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item4 = wx.StaticBox( parent, -1, "Periodo" )
    item3 = wx.StaticBoxSizer( item4, wx.VERTICAL )
    
    item5 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Anno:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.ALIGN_CENTER|wx.BOTTOM, 5 )

    item7 = NumCtrl(parent, ID_ANNO, integerWidth=4, fractionWidth=0, groupDigits=False); item7.SetName('anno')
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Registrazioni dal:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item9 = DateCtrl( parent, ID_DATA1, "", wx.DefaultPosition, [80,-1], 0 )
    item9.SetName( "data1" )
    item5.Add( item9, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item5.Add( [ 2, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item5.Add( [ 20, 2 ] , 0, wx.ALIGN_CENTER, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "al:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item11 = DateCtrl( parent, ID_DATA2, "", wx.DefaultPosition, [80,-1], 0 )
    item11.SetName( "data2" )
    item5.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item13 = wx.StaticBox( parent, -1, "Anagrafiche" )
    item12 = wx.StaticBoxSizer( item13, wx.VERTICAL )
    
    item14 = wx.CheckBox( parent, ID_SOLO_ANAG_ALL, "Solo in allegato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetValue( True )
    item14.SetName( "solo_anag_all" )
    item12.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item15 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item12.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item16 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item17 = wx.StaticText( parent, ID_TEXT, "Escludi blacklist:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.Add( item17, 0, wx.ALIGN_CENTER|wx.RIGHT, 5 )

    item18 = wx.CheckBox( parent, ID_ESCLUDI_BLA, "Anagr.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.SetName( "escludi_bla" )
    item16.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item16.Add( [ 2, 2 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item19 = wx.CheckBox( parent, ID_ESCLUDI_BLS, "Stato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.SetName( "escludi_bls" )
    item16.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item16.AddGrowableCol( 1 )

    item12.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item21 = wx.StaticBox( parent, -1, "Causali" )
    item20 = wx.StaticBoxSizer( item21, wx.VERTICAL )
    
    item22 = wx.CheckBox( parent, ID_SOLO_CAUS_ALL, "Solo in allegato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item22.SetValue( True )
    item22.SetName( "solo_caus_all" )
    item20.Add( item22, 0, wx.ALIGN_CENTER, 5 )

    item1.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item23 = wx.Button( parent, ID_BUTUPDATE, "Aggiorna", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.SetDefault()
    item23.SetName( "butupdate" )
    item1.Add( item23, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item24 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item25 = wx.StaticText( parent, ID_TEXT, "Elenco transazioni", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.SetForegroundColour( wx.BLUE )
    item25.SetName( "gridtitle" )
    item24.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item26 = RCheckBox( parent, ID_REGSPY, "Reg.Spy", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.SetName( "regspy" )
    item24.Add( item26, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item24.AddGrowableCol( 0 )

    item0.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item27 = wx.Panel( parent, ID_GRIDPANEL, wx.DefaultPosition, [900,300], wx.SUNKEN_BORDER )
    item27.SetName( "gridpanel" )
    item0.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item28 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item29 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item30 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item32 = wx.StaticBox( parent, -1, "Totali anagrafica" )
    item31 = wx.StaticBoxSizer( item32, wx.VERTICAL )
    
    item33 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item34 = wx.StaticText( parent, ID_TEXT, "Anagrafica", wx.DefaultPosition, [250,-1], wx.ST_NO_AUTORESIZE )
    item33.Add( item34, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item35 = wx.StaticText( parent, ID_TEXT, "Tot.Operazioni", wx.DefaultPosition, wx.DefaultSize, 0 )
    item33.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item36 = wx.StaticText( parent, ID_TEXT, "Tot.Imposta", wx.DefaultPosition, wx.DefaultSize, 0 )
    item33.Add( item36, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item37 = wx.StaticText( parent, ID_TEXT, "Tot.Op.+IVA", wx.DefaultPosition, wx.DefaultSize, 0 )
    item33.Add( item37, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item38 = wx.StaticText( parent, ID_TOTANADES, "-", wx.DefaultPosition, [250,30], wx.ST_NO_AUTORESIZE )
    item38.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item38.SetName( "totanades" )
    item33.Add( item38, 0, wx.LEFT|wx.RIGHT, 5 )

    item39 = wx.StaticText( parent, ID_TOTANAIMP, "0", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item39.SetName( "totanaimp" )
    item33.Add( item39, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 5 )

    item40 = wx.StaticText( parent, ID_TOTANAIVA, "0", wx.DefaultPosition, wx.DefaultSize, 0 )
    item40.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item40.SetName( "totanaiva" )
    item33.Add( item40, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 5 )

    item41 = wx.StaticText( parent, ID_TOTANATOT, "0", wx.DefaultPosition, wx.DefaultSize, 0 )
    item41.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item41.SetName( "totanatot" )
    item33.Add( item41, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 5 )

    item33.Add( [ 1, 1 ] , 0, wx.ALIGN_CENTER, 5 )

    item33.Add( [ 120, 1 ] , 0, wx.ALIGN_CENTER, 5 )

    item33.Add( [ 120, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 0 )

    item33.Add( [ 120, 1 ] , 0, wx.ALIGN_CENTER|wx.ALL, 0 )

    item31.Add( item33, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item30.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item42 = TipValoriRadioBox( parent, ID_TIPVALORI, "Valori", wx.DefaultPosition, wx.DefaultSize, 
        ["Solo eccedenti i massimali","Tutte le operazioni"] , 1, wx.RA_SPECIFY_COLS )
    item42.SetName( "tipvalori" )
    item30.Add( item42, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item44 = wx.StaticBox( parent, -1, "Massimali" )
    item43 = wx.StaticBoxSizer( item44, wx.VERTICAL )
    
    item45 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item46 = wx.StaticText( parent, ID_TEXT, "Aziende:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item45.Add( item46, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item47 = NumCtrl(parent, ID_MAXAZI, integerWidth=10, fractionWidth=2); item47.SetName('maxazi'); item47.Disable()
    item45.Add( item47, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item48 = wx.StaticText( parent, ID_TEXT, "Privati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item45.Add( item48, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item49 = NumCtrl(parent, ID_MAXPRI, integerWidth=10, fractionWidth=2); item49.SetName('maxpri'); item49.Disable()
    item45.Add( item49, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item43.Add( item45, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item30.Add( item43, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item30.AddGrowableCol( 0 )

    item29.Add( item30, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item50 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item29.Add( item50, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item51 = wx.StaticText( parent, ID_WARNING, "-", wx.DefaultPosition, wx.DefaultSize, 0 )
    item51.SetForegroundColour( wx.RED )
    item51.SetFont( wx.Font( 12, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item51.SetName( "warning" )
    item29.Add( item51, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item29.AddGrowableCol( 0 )

    item28.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item53 = wx.StaticBox( parent, -1, "Azioni" )
    item52 = wx.StaticBoxSizer( item53, wx.VERTICAL )
    
    item54 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item55 = wx.Button( parent, ID_BUTESTRAI, "&Estrai", wx.DefaultPosition, wx.DefaultSize, 0 )
    item55.SetName( "butestrai" )
    item55.Enable(False)
    item54.Add( item55, 0, wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item56 = wx.Button( parent, ID_BUTGENERA, "Genera file", wx.DefaultPosition, wx.DefaultSize, 0 )
    item56.SetName( "butgenera" )
    item54.Add( item56, 0, wx.ALIGN_RIGHT|wx.BOTTOM, 5 )

    item52.Add( item54, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

    item28.Add( item52, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item28.AddGrowableCol( 0 )

    item0.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CAUSALE = 10023
ID_DATREG = 10024
ID_NUMDOC = 10025
ID_DATDOC = 10026
ID_PANGRIDBODY = 10027

def RegSpyPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Causale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3 = alib.LinkTableCauContab(parent, ID_CAUSALE, 'id_caus'); item3.Disable()
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "Registrazione del:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item5 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item6 = DateCtrl( parent, ID_DATREG, "", wx.DefaultPosition, [80,-1], 0 )
    item6.SetName( "datreg" )
    item6.Enable(False)
    item5.Add( item6, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Documento num.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item8 = TextCtrl( parent, ID_NUMDOC, "", wx.DefaultPosition, [80,-1], 0 )
    item8.SetName( "numdoc" )
    item8.Enable(False)
    item5.Add( item8, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "del:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item9, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item10 = DateCtrl( parent, ID_DATDOC, "", wx.DefaultPosition, [80,-1], 0 )
    item10.SetName( "datdoc" )
    item10.Enable(False)
    item5.Add( item10, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Contenuto della registrazione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item11.SetForegroundColour( wx.BLUE )
    item0.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item12 = wx.Panel( parent, ID_PANGRIDBODY, wx.DefaultPosition, [700,160], wx.SUNKEN_BORDER )
    item12.SetName( "pangridbody" )
    item0.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_RAGSOC = 10028
ID_COMUNE = 10029
ID_PROV = 10030
ID_CODFISC = 10031
ID_PIVA = 10032
ID_BUTGEN = 10033

def GeneraFileFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Dati del soggetto obbligato alla presentazione" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Denominazione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )

    item4 = TextCtrl( parent, ID_RAGSOC, "", wx.DefaultPosition, [400,-1], 0 )
    item4.SetName( "ragsoc" )
    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item5 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Comune:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Prov:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item8 = TextCtrl( parent, ID_COMUNE, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetName( "comune" )
    item5.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item9 = TextCtrl( parent, ID_PROV, "", wx.DefaultPosition, [40,-1], 0 )
    item9.SetName( "prov" )
    item5.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item5.AddGrowableCol( 0 )

    item1.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item11 = wx.StaticText( parent, ID_TEXT, "Cod.Fiscale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "P.IVA:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item13 = TextCtrl( parent, ID_CODFISC, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.SetName( "codfisc" )
    item10.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item14 = TextCtrl( parent, ID_PIVA, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetName( "piva" )
    item10.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10.AddGrowableCol( 0 )

    item10.AddGrowableCol( 1 )

    item1.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = wx.Button( parent, ID_BUTGEN, "Genera file", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.SetName( "butgen" )
    item0.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

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
