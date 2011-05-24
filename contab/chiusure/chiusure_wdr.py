# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: chiusure.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc import util

from awc.controls.linktable import LinkTable

from awc.controls.radiobox import RadioBox
from awc.controls.textctrl import TextCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.notebook import Notebook

from Env import Azienda
bt = Azienda.BaseTab

from anag.lib import LinkTableCauContab, LinkTablePdc

from contab.awcontrols import SelEsercizioExChoice


class GeneraMovimentiNotebook(Notebook):

    def __init__(self, parent, *args, **kwargs):
        Notebook.__init__(self, parent, *args, **kwargs)
        parent.workzone = self
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)

    def OnPageChanged(self, event):
        def cn(w, x):
            return w.FindWindowByName(x)
        n = event.GetSelection()
        f = None
        if n == 0:
            f = cn(self.GetParent(), 'esercizio')
        if f:
            wx.CallAfter(lambda: f.SetFocus())
        event.Skip()


class ImportoCtrl(NumCtrl):
    def __init__(self, parent, id, name):
        NumCtrl.__init__(self, parent, id, fractionWidth=bt.VALINT_DECIMALS)
        self.SetName(name)
        self.Disable()

class GeneraMovimentiCalcolaPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        GeneraMovimentiCalcolaFunc(self)


class GeneraMovimentiCalcolaChiusurePanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        GeneraMovimentiCalcolaChiusurePanelFunc(self)

class GeneraMovimentiCalcolaAperturePanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        GeneraMovimentiCalcolaAperturePanelFunc(self)


ChiusuraContabileDescPanelFunc = None

class ChiusuraContabileDescPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        ChiusuraContabileDescPanelFunc(self)

from cfg.dbtables import ProgrEsercizio

class SelEsercizioGenMovChoice(SelEsercizioExChoice):
    def __init__(self, *args, **kwargs):
        SelEsercizioExChoice.__init__(self, *args, **kwargs)
        ese = ProgrEsercizio()
        e = ese.GetEsercizioInCorso()
        self.SetValue(e)

class DataLiquidazioneCtrl(DateCtrl):
    def __init__(self, *args, **kwargs):
        DateCtrl.__init__(self, *args, **kwargs)
        self.SetReadOnly()



# Window functions

ID_TIPOTIT = 10000
ID_TEXT = 10001
ID_ESERCIZIO = 10002
ID_UPDATE = 10003
ID_WORKZONE = 10004

def GeneraMovimentiFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TIPOTIT, "Generazione movimenti di Apertura/Chiusura", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.SetFont( wx.Font( 14, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item2.SetName( "tipotit" )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item4 = wx.StaticBox( parent, -1, "" )
    item3 = wx.StaticBoxSizer( item4, wx.VERTICAL )
    
    item5 = wx.StaticText( parent, ID_TEXT, 
        "Questa funzione provvede a generare le registrazioni necessarie per la chiusura e la riapertura dell'esercizio.  Una volta confermato l'esercizio da \n"
        "elaborare, verranno determinati i saldi di tutti i sottoconti movimentati.\n"
        "\n"
        "CHIUSURA\n"
        "Verrà richiesta la data in cui generare le registrazioni: i sottoconti di tipo patrimoniale saranno chiusi nel sottoconto indicato come bilancio di apertura;\n"
        "i sottoconti di tipo economico saranno chiusi nel sottoconto indicato come profitti e perdite.\n"
        "Il saldo a pareggio verrà quindi girato verso il sottoconto indicato come risultato di esercizio per la chiusura.\n"
        "\n"
        "APERTURA\n"
        "Verrà richiesta la data in cui generare le registrazioni: i sottoconti di tipo patrimoniale saranno riaperti dal sottoconto indicato come bilancio di apertura.\n"
        "Il saldo a pareggio verrà quindi girato verso il sottoconto indicato come risultato di esercizio per l'apertura.",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item7 = wx.StaticBox( parent, -1, "Determinazione dei saldi" )
    item6 = wx.StaticBoxSizer( item7, wx.VERTICAL )
    
    item8 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item9 = wx.StaticText( parent, ID_TEXT, "Determina i saldi relativi all'esercizio:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item10 = wx.StaticText( parent, ID_ESERCIZIO, "-", wx.DefaultPosition, [40,-1], wx.ST_NO_AUTORESIZE )
    item10.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item10.SetName( "esercizio" )
    item8.Add( item10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11 = wx.Button( parent, ID_UPDATE, "Calcola", wx.DefaultPosition, wx.DefaultSize, 0 )
    item11.SetDefault()
    item11.SetName( "update" )
    item8.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8.AddGrowableCol( 2 )

    item6.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item1.AddGrowableCol( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item13 = GeneraMovimentiNotebook( parent, ID_WORKZONE, wx.DefaultPosition, [200,160], 0 )
    item12 = item13
    
    item14 = wx.Panel( item13, -1 )
    GeneraMovimentiTotaliFunc(item14, False)
    item13.AddPage( item14, "Totali" )

    item15 = wx.Panel( item13, -1 )
    GeneraMovimentiSaldiPatFunc(item15, False)
    item13.AddPage( item15, "Stato Patrimoniale" )

    item16 = wx.Panel( item13, -1 )
    GeneraMovimentiSaldiEcoFunc(item16, False)
    item13.AddPage( item16, "Conto Economico" )

    item0.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANGRIDSALPAT = 10005
ID_PRINTPAT = 10006

def GeneraMovimentiSaldiPatFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Sottoconti e saldi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item2 = wx.Panel( parent, ID_PANGRIDSALPAT, wx.DefaultPosition, [200,400], wx.SUNKEN_BORDER )
    item2.SetName( "pangridsalpat" )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3 = wx.BoxSizer( wx.HORIZONTAL )
    
    item4 = wx.Button( parent, ID_PRINTPAT, "Stampa", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "printpat" )
    item3.Add( item4, 0, wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT, 5 )

    item0.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANGRIDSALECO = 10007
ID_PRINTECO = 10008

def GeneraMovimentiSaldiEcoFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Sottoconti e saldi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item2 = wx.Panel( parent, ID_PANGRIDSALECO, wx.DefaultPosition, [200,400], wx.SUNKEN_BORDER )
    item2.SetName( "pangridsaleco" )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3 = wx.BoxSizer( wx.HORIZONTAL )
    
    item4 = wx.Button( parent, ID_PRINTECO, "Stampa", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "printeco" )
    item3.Add( item4, 0, wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT, 5 )

    item0.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANEL = 10009
ID_WARNING = 10010

def GeneraMovimentiTotaliFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = GeneraMovimentiCalcolaPanel( parent, ID_PANEL, wx.DefaultPosition, [200,160], 0 )
    item1.SetName( "pancalc" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.StaticText( parent, ID_WARNING, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.SetFont( wx.Font( 12, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item2.SetName( "warning" )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANCALCHI = 10011
ID_PANCALAPE = 10012

def GeneraMovimentiCalcolaFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = GeneraMovimentiCalcolaChiusurePanel( parent, ID_PANCALCHI, wx.DefaultPosition, [200,50], 0 )
    item1.SetName( "pancalchi" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = GeneraMovimentiCalcolaAperturePanel( parent, ID_PANCALAPE, wx.DefaultPosition, [200,50], 0 )
    item2.SetName( "pancalape" )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_REGCHICAU = 10013
ID_REGCHIDAT = 10014
ID_DESCHIBIL = 10015
ID_REGCHIBIL = 10016
ID_SALCHIBIL = 10017
ID_DESCHIPRP = 10018
ID_REGCHIPRP = 10019
ID_SALCHIPRP = 10020
ID_DESCHIUPE = 10021
ID_REGCHIUPE = 10022
ID_SALCHIUPE = 10023
ID_CHIRIS = 10024

def GeneraMovimentiCalcolaChiusurePanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Chiusure" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item5 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Causale", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Data reg.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item7, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = LinkTableCauContab(parent, ID_REGCHICAU, 'regchicau'); item9.Disable()
    item4.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = DateCtrl( parent, ID_REGCHIDAT, "", wx.DefaultPosition, [80,-1], 0 )
    item10.SetName( "regchidat" )
    item4.Add( item10, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Giroconto su:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item12, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "Saldo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item13, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item14 = wx.StaticText( parent, ID_DESCHIBIL, "Stato Patrimoniale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetName( "deschibil" )
    item4.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item15 = LinkTablePdc(parent, ID_REGCHIBIL, 'regchibil'); item15.Disable()
    item4.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item16 = ImportoCtrl(parent, ID_SALCHIBIL, "salchibil")
    item4.Add( item16, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item17 = wx.StaticText( parent, ID_DESCHIPRP, "Conto Economico:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item17.SetName( "deschiprp" )
    item4.Add( item17, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item18 = LinkTablePdc(parent, ID_REGCHIPRP, 'regchiprp'); item18.Disable()
    item4.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item19 = ImportoCtrl(parent, ID_SALCHIPRP, "salchiprp")
    item4.Add( item19, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item20 = wx.StaticText( parent, ID_DESCHIUPE, "Risultato esercizio:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item20.SetName( "deschiupe" )
    item4.Add( item20, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item21 = LinkTablePdc(parent, ID_REGCHIUPE, 'regchiupe'); item21.Disable()
    item4.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item22 = ImportoCtrl(parent, ID_SALCHIUPE, "salchiupe")
    item4.Add( item22, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item4.AddGrowableCol( 1 )

    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item23 = wx.StaticText( parent, ID_CHIRIS, "", wx.DefaultPosition, [50,-1], wx.ST_NO_AUTORESIZE )
    item23.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item23.SetName( "chiris" )
    item3.Add( item23, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item3.AddGrowableCol( 0 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_REGAPECAU = 10025
ID_REGAPEDAT = 10026
ID_DESAPEBIL = 10027
ID_REGAPEBIL = 10028
ID_SALAPEBIL = 10029
ID_DESAPEUPE = 10030
ID_REGAPEUPE = 10031
ID_SALAPEUPE = 10032
ID_APERIS = 10033
ID_GENERA = 10034

def GeneraMovimentiCalcolaAperturePanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Aperture" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item4 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item5 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Causale", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Data reg.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item7, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = LinkTableCauContab(parent, ID_REGAPECAU, 'regapecau'); item9.Disable()
    item4.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = DateCtrl( parent, ID_REGAPEDAT, "", wx.DefaultPosition, [80,-1], 0 )
    item10.SetName( "regapedat" )
    item4.Add( item10, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Giroconto su:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item12, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "Saldo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item13, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item14 = wx.StaticText( parent, ID_DESAPEBIL, "Stato Patrimoniale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetName( "desapebil" )
    item4.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item15 = LinkTablePdc(parent, ID_REGAPEBIL, 'regapebil'); item15.Disable()
    item4.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item16 = ImportoCtrl(parent, ID_SALAPEBIL, "salapebil")
    item4.Add( item16, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item17 = wx.StaticText( parent, ID_DESAPEUPE, "Risultato esercizio:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item17.SetName( "desapeupe" )
    item4.Add( item17, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item18 = LinkTablePdc(parent, ID_REGAPEUPE, 'regapeupe'); item18.Disable()
    item4.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item19 = ImportoCtrl(parent, ID_SALAPEUPE, "salapeupe")
    item4.Add( item19, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item4.AddGrowableCol( 1 )

    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item20 = wx.StaticText( parent, ID_APERIS, "", wx.DefaultPosition, [50,-1], wx.ST_NO_AUTORESIZE )
    item20.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item20.SetName( "aperis" )
    item3.Add( item20, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item3.AddGrowableCol( 0 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = wx.Button( parent, ID_GENERA, "&Genera movimenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item21.SetName( "genera" )
    item0.Add( item21, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ESERCOLD = 10035
ID_ESERCNEW = 10036

def SovrapposizioneFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TIPOTIT, "Sovrapposizione di esercizi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetFont( wx.Font( 14, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item1.SetName( "tipotit" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item3 = wx.StaticBox( parent, -1, "" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = wx.StaticText( parent, ID_TEXT, 
        "Questa funzione crea un nuovo esercizio contabile, attivando la sovrapposizione con quello in corso:\n"
        "Saranno azzerati i progressivi di stampa del giornale bollato, i progressivi dare/avere del giornale \n"
        "relativi all'esercizio in corso saranno spostati su quello precedente.\n"
        "Non sarà più possibile registrare e/o apportare modifiche a registrazioni con data precedente l'inizio \n"
        "del nuovo esercizio.\n"
        "Le scritture di rettifica al bilancio dovranno essere registrate nel nuovo esercizio, mediante apposite\n"
        "causali che operano nell'esercizio precedente.",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6 = wx.StaticBox( parent, -1, "" )
    item5 = wx.StaticBoxSizer( item6, wx.VERTICAL )
    
    item7 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item8 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item9 = wx.StaticText( parent, ID_TEXT, "Esercizio in corso:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item10 = NumCtrl(parent, ID_ESERCOLD, integerWidth=4, groupDigits=False); item10.SetName('esercold'); item10.SetEditable(False)
    item8.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Nuovo esercizio:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item12 = NumCtrl(parent, ID_ESERCNEW, integerWidth=4, groupDigits=False); item12.SetName('esercnew'); item12.SetEditable(False)
    item8.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item13 = wx.Button( parent, ID_UPDATE, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.SetName( "update" )
    item7.Add( item13, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item5.Add( item7, 0, wx.ALIGN_CENTER, 5 )

    item0.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = wx.StaticText( parent, ID_WARNING, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetForegroundColour( wx.RED )
    item14.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item14.SetName( "warning" )
    item0.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def ChiusuraContabileFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TIPOTIT, "Chiusura contabile", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetFont( wx.Font( 14, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item1.SetName( "tipotit" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item2 = ChiusuraContabileDescPanel( parent, ID_PANEL, wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3 = wx.StaticText( parent, ID_WARNING, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.SetForegroundColour( wx.RED )
    item3.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item3.SetName( "warning" )
    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.Button( parent, ID_UPDATE, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetName( "update" )
    item0.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def ChiusuraContabileNormaleDescPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.StaticText( parent, ID_TEXT, 
        "Questa funzione crea un nuovo esercizio contabile:\n"
        "Saranno azzerati riga, pagina e progressivi di stampa del giornale bollato.",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item5 = wx.StaticBox( parent, -1, "" )
    item4 = wx.StaticBoxSizer( item5, wx.VERTICAL )
    
    item6 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item7 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item8 = wx.StaticText( parent, ID_TEXT, "Esercizio in corso:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item9 = NumCtrl(parent, ID_ESERCOLD, integerWidth=4, groupDigits=False); item9.SetName('esercold'); item9.SetEditable(False)
    item7.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Nuovo esercizio:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item11 = NumCtrl(parent, ID_ESERCNEW, integerWidth=4, groupDigits=False); item11.SetName('esercnew'); item11.SetEditable(False)
    item7.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item4.Add( item6, 0, wx.ALIGN_CENTER, 5 )

    item0.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def ChiusuraContabileSovrapposizioneDescPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.StaticText( parent, ID_TEXT, 
        "Questa funzione chiude la sovrapposizione di esercizio.\n"
        "Saranno azzerati i progressivi dare/avere dell'esercizio precedente del giornale bollato.",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_NUOVOANNO = 10037
ID_DATULIQ = 10038
ID_CREDULIQ = 10039
ID_BUTGENERA = 10040

def ChiusuraIVAFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TIPOTIT, "Chiusura Annuale IVA", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetFont( wx.Font( 14, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item1.SetName( "tipotit" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item3 = wx.StaticBox( parent, -1, "" )
    item2 = wx.StaticBoxSizer( item3, wx.VERTICAL )
    
    item4 = wx.StaticText( parent, ID_TEXT, 
        "Questa funzione provvede a creare i progressivi del credito IVA compensabile\n"
        "per l'anno successivo a quello richiesto, inizializzandoli in base al credito\n"
        "risultate dall'ultima liquidazione dell'anno richiesto.\n"
        "La generazione avrà luogo solo se la data dell'ultima liquidazione effettuata\n"
        "nell'anno selezionato corrisponde all'ultimo giorno dell'anno stesso.",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item2, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6 = wx.StaticBox( parent, -1, "" )
    item5 = wx.StaticBoxSizer( item6, wx.VERTICAL )
    
    item7 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item8 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item9 = wx.StaticText( parent, ID_TEXT, "Genera i progressivi per l'anno:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item10 = NumCtrl(parent, ID_NUOVOANNO, integerWidth=4, groupDigits=False, allowNegative=False); item10.SetName('nuovoanno')
    item8.Add( item10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Ultima liquidazione precedente:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item12 = DataLiquidazioneCtrl( parent, ID_DATULIQ, "", wx.DefaultPosition, [80,-1], 0 )
    item12.SetName( "datuliq" )
    item8.Add( item12, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "Credito da riportare:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item13, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item14 = ImportoCtrl(parent, ID_CREDULIQ, "creduliq")
    item8.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8.AddGrowableCol( 0 )

    item7.Add( item8, 0, wx.ALIGN_CENTER, 5 )

    item15 = wx.Button( parent, ID_BUTGENERA, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.SetName( "butgenera" )
    item7.Add( item15, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item7.AddGrowableCol( 0 )

    item5.Add( item7, 0, wx.ALIGN_CENTER, 5 )

    item16 = wx.StaticText( parent, ID_WARNING, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.SetForegroundColour( wx.RED )
    item16.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item16.SetName( "warning" )
    item5.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

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
