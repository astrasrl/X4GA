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
from wx import Panel as wxPanel
from wx.lib import masked

from awc.controls.linktable import LinkTable
from awc.controls.datectrl import DateCtrl
from awc.controls.textctrl import TextCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.checkbox import CheckBox, RCheckBox
from awc.controls.radiobox import RadioBox

from anag.basetab import WorkZoneNotebook

from anag.lib import LinkTableMagazz, LinkTableDocMagazz, LinkTableMovMagazz

from Env import Azienda
bt = Azienda.BaseTab

import stormdb as adb


class TipiValoreRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=["U", "M"])

class TipoProdRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=('S', 'T'))

class AnniChoice(wx.Choice):
    
    anni = []
    
    def __init__(self, *args, **kwargs):
        wx.Choice.__init__(self, *args, **kwargs)
        g = adb.DbTable(bt.TABNAME_PROGIA, 'progia', fields=None)
        g.AddGroupOn('progia.anno')
        g.AddCountOf('1.0')
        g.AddOrder('progia.anno', adb.ORDER_DESCENDING)
        g.Retrieve()
        for g in g:
            self.Append(str(g.anno))
            self.anni.append(g.anno)
        if self.GetCount()>0:
            self.SetSelection(0)
    
    def GetSelectedAnno(self):
        if self.anni:
            return self.anni[self.GetSelection()]
        return None


class GridRiepPanel(wx.Panel):
    
    def __init__(self, parent, id, pos, size, style):
        g = adb.DbTable(bt.TABNAME_PROGIA, 'progia', fields=None)
        g.AddGroupOn('progia.id_magazz')
        g.AddCountOf('1.0')
        g.AddOrder('progia.anno', adb.ORDER_DESCENDING)
        g.Retrieve()
        size = (size[0], 60+22*g.RowsCount())
        wx.Panel.__init__(self, parent, id, pos, size, style)

class TipoValoreRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=('Q','D','N'))

class TipOrdRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=("C","D"))

class TipoGiacenzaRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=("T","Z","P","N"))



# Window functions

ID_WORKZONE = 14000

def ConsolidaCostiFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = WorkZoneNotebook( parent, ID_WORKZONE, wx.DefaultPosition, [200,160], 0 )
    item1 = item2
    
    item3 = wx.Panel( item2, -1 )
    ConsolidaCostiGeneraFunc(item3, False)
    item2.AddPage( item3, "Consolida" )

    item4 = wx.Panel( item2, -1 )
    ConsolidaCostiEliminaFunc(item4, False)
    item2.AddPage( item4, "Elimina costi già consolidati" )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 14001
ID_ANNO = 14002
ID_LINE = 14003
ID_DATGIAC = 14004
ID_BTNSTART = 14005
ID_WARNING = 14006

def ConsolidaCostiGeneraFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "CONSOLIDAMENTO COSTI PRODOTTI", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetFont( wx.Font( 12, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

    item2 = wx.StaticText( parent, ID_TEXT, 
        "Questa funzione consolida i costi dei prodotti al momento dell'elaborazione,\n"
        "in modo tale che la prossima movimentazione di carico/scarico non influisca\n"
        "sul costo/prezzo dei prodotti coinvolti, al fine di poter agevolmente inserire\n"
        "le quantità di giacenza rilevate per le operazioni di chiusura del magazzino.",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Anno di riferimento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = NumCtrl(parent, ID_ANNO, integerWidth=4, groupDigits=False, allowNegative=False); item5.SetName("anno")
    item3.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item3, 0, wx.ALIGN_CENTER, 5 )

    item6 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, 
        "Verranno inoltre consolidate le giacenze relative ad ogni magazzino gestito,\n"
        "per avere il riscontro con le quantità rilevate che si andranno ad inserire.",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item8 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item9 = wx.StaticText( parent, ID_TEXT, "Determina le giacenze al:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.Add( item9, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item10 = DateCtrl( parent, ID_DATGIAC, "", wx.DefaultPosition, [70,-1], 0 )
    item10.SetName( "datgiac" )
    item8.Add( item10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11 = wx.Button( parent, ID_BTNSTART, "Avvia", wx.DefaultPosition, wx.DefaultSize, 0 )
    item11.SetName( "btnstart" )
    item8.Add( item11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item8, 0, wx.ALIGN_CENTER, 5 )

    item12 = wx.StaticText( parent, ID_WARNING, "-", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.SetForegroundColour( wx.RED )
    item12.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item12.SetName( "warning" )
    item0.Add( item12, 0, wx.ALIGN_BOTTOM|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 6 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ANNOCANC = 14007
ID_BTNCANC = 14008
ID_WARNCANC = 14009

def ConsolidaCostiEliminaFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "ELIMINAZIONE COSTI CONSOLIDATI", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetFont( wx.Font( 12, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

    item2 = wx.StaticText( parent, ID_TEXT, 
        "Questa funzione elimina i costi dei prodotti consolidati relativamente ad\n"
        "un anno, nonché tutte le giacenze rilevate facenti capo allo stesso anno\n"
        "di riferimento.\n"
        "\n"
        "Eseguire solo nei seguenti casi:\n"
        "\n"
        " - Ciclo di lavoro per la chiusura annuale di magazzino terminato, ovvero \n"
        "   giacenze rilevate già inserite per tutti i magazzini gestiti e movimenti di\n"
        "   giacenzia iniziale generati.\n"
        "\n"
        " - Rielaborazione costi in caso di consolidamento già effettuato ma errato.\n"
        "",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Anno di riferimento da eliminare:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item5 = NumCtrl(parent, ID_ANNOCANC, integerWidth=4, groupDigits=False, allowNegative=False); item5.SetName("annocanc")
    item3.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item6 = wx.Button( parent, ID_BTNCANC, "Avvia eliminazione", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.SetName( "btncanc" )
    item3.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item3, 0, wx.ALIGN_CENTER, 5 )

    item7 = wx.StaticText( parent, ID_WARNCANC, "-", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetForegroundColour( wx.RED )
    item7.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item7.SetName( "warncanc" )
    item0.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_MAGAZZ = 14010
ID_TOTQTACON = 14011
ID_TOTVALCON = 14012
ID_TOTQTAFIS = 14013
ID_TOTVALFIS = 14014
ID_TIPORD = 14015
ID_TIPVAL = 14016
ID_TIPGIACON = 14017
ID_TIPGIAFIS = 14018
ID_BTNESTRAI = 14019
ID_PANGRID = 14020
ID_BTNLIST = 14021

def EditGiacenzeFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item4 = wx.StaticBox( parent, -1, "Magazzino e periodo" )
    item3 = wx.StaticBoxSizer( item4, wx.HORIZONTAL )
    
    item5 = wx.StaticText( parent, ID_TEXT, "Giacenze del magazzino:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item5, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item6 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item7 = LinkTableMagazz(parent, ID_MAGAZZ, 'magazz')
    item6.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6.Add( [ 200, 1 ] , 0, wx.ALIGN_CENTER, 5 )

    item6.AddGrowableCol( 0 )

    item3.Add( item6, 0, wx.ALIGN_CENTER, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "per l'anno:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item8, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item9 = NumCtrl(parent, ID_ANNO, integerWidth=4, groupDigits=False, allowNegative=False); item9.SetName("anno")
    item3.Add( item9, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item11 = wx.StaticBox( parent, -1, "Totali" )
    item10 = wx.StaticBoxSizer( item11, wx.VERTICAL )
    
    item12 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item13 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item13, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Quantità:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "Valore:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item16 = wx.StaticText( parent, ID_TEXT, "G.Contabili:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item16, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item17 = NumCtrl(parent, ID_TOTQTACON, integerWidth=12, fractionWidth=bt.MAGQTA_DECIMALS, groupDigits=True, allowNegative=False); item17.SetEditable(False); item17.SetName("totqtacon")
    item12.Add( item17, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item18 = NumCtrl(parent, ID_TOTVALCON, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, groupDigits=True, allowNegative=False); item18.SetEditable(False); item18.SetName("totvalcon")
    item12.Add( item18, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item19 = wx.StaticText( parent, ID_TEXT, "G.Fisiche:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item19, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item20 = NumCtrl(parent, ID_TOTQTAFIS, integerWidth=12, fractionWidth=bt.MAGQTA_DECIMALS, groupDigits=True, allowNegative=False); item20.SetEditable(False); item20.SetName("totqtafis")
    item12.Add( item20, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item21 = NumCtrl(parent, ID_TOTVALFIS, integerWidth=12, fractionWidth=bt.VALINT_DECIMALS, groupDigits=True, allowNegative=False); item21.SetEditable(False); item21.SetName("totvalfis")
    item12.Add( item21, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item10.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item2.AddGrowableCol( 0 )

    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item22 = TipOrdRadioBox( parent, ID_TIPORD, "Ordinamento", wx.DefaultPosition, wx.DefaultSize, 
        ["Codice","Descrizione"] , 1, wx.RA_SPECIFY_COLS )
    item22.SetName( "tipord" )
    item1.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item23 = TipiValoreRadioBox( parent, ID_TIPVAL, "Valorizzazione", wx.DefaultPosition, wx.DefaultSize, 
        ["Costo ultimo","Costo medio"] , 1, wx.RA_SPECIFY_COLS )
    item23.SetName( "tipval" )
    item1.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item24 = TipoGiacenzaRadioBox( parent, ID_TIPGIACON, "G.Contab:", wx.DefaultPosition, wx.DefaultSize, 
        ["Tutto","Zero","Posit.","Negat."] , 1, wx.RA_SPECIFY_COLS )
    item24.SetName( "tipgiacon" )
    item1.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item25 = TipoGiacenzaRadioBox( parent, ID_TIPGIAFIS, "G.Rilev:", wx.DefaultPosition, wx.DefaultSize, 
        ["Tutto","Zero","Posit.","Negat."] , 1, wx.RA_SPECIFY_COLS )
    item25.SetName( "tipgiafis" )
    item1.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item26 = wx.Button( parent, ID_BTNESTRAI, "Estrai giacenze", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.SetName( "btnestrai" )
    item1.Add( item26, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item1.AddGrowableCol( 4 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item27 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item28 = wx.StaticText( parent, ID_TEXT, "Giacenze prodotti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item28.SetForegroundColour( wx.BLUE )
    item0.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item29 = wx.Panel( parent, ID_PANGRID, wx.DefaultPosition, [800,500], 0 )
    item29.SetName( "pangrid" )
    item0.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item30 = wx.BoxSizer( wx.HORIZONTAL )
    
    item31 = wx.Button( parent, ID_BTNLIST, "Lista giacenze rilevate", wx.DefaultPosition, wx.DefaultSize, 0 )
    item31.SetName( "btnlist" )
    item30.Add( item31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item30, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 3 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TIPOPROD = 14022
ID_TIPOVAL = 14023
ID_STAGCON = 14024
ID_BTNPRINT = 14025

def ListGiacenzeFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = TipoProdRadioBox( parent, ID_TIPOPROD, "Prodotti da stampare", wx.DefaultPosition, wx.DefaultSize, 
        ["Solo i prodotti con giacenza rilevata significativa","Tutti i prodotti visualizzati"] , 1, wx.RA_SPECIFY_COLS )
    item1.SetName( "tipoprod" )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2 = TipoValoreRadioBox( parent, ID_TIPOVAL, "Prodotti con valore", wx.DefaultPosition, wx.DefaultSize, 
        ["Qualsiasi","Solo definito","Solo non definito (vuoto)"] , 1, wx.RA_SPECIFY_COLS )
    item2.SetName( "tipoval" )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticBox( parent, -1, "Giacenze" )
    item3 = wx.StaticBoxSizer( item4, wx.VERTICAL )
    
    item5 = wx.CheckBox( parent, ID_STAGCON, "Stampa anche le giacenze contabili", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetName( "stagcon" )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6 = wx.Button( parent, ID_BTNPRINT, "Avvia la stampa", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.SetName( "btnprint" )
    item0.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANGRIDRIEP = 14026
ID_TIPDOC = 14027
ID_TIPMOV = 14028
ID_DATDOC = 14029
ID_NUMDOC = 14030
ID_BTNGENMOV = 14031

def GeneraMovimentiFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "GENERAZIONE MOVIMENTI DI GIACENZA INIZIALE", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetFont( wx.Font( 12, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

    item2 = wx.StaticText( parent, ID_TEXT, "Questa funzione provvede a generare i movimenti di giacenza iniziale relativamente ad ogni magazzino e prodotto presente nella sezione delle giacenze rilevate.  Verranno inseriiti nei movimenti solo i prodotti corredati di giacenza rilevata non nulla, relativamente all'anno di seguito indicato.", wx.DefaultPosition, [600,40], wx.ST_NO_AUTORESIZE )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item5 = wx.StaticBox( parent, -1, "Periodo giacenze" )
    item4 = wx.StaticBoxSizer( item5, wx.HORIZONTAL )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Anno di riferimento:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.Add( item6, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item7 = AnniChoice( parent, ID_ANNO, wx.DefaultPosition, [60,-1], [], 0 )
    item7.SetName( "anno" )
    item4.Add( item7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item8 = TipiValoreRadioBox( parent, ID_TIPVAL, "Valorizzazione", wx.DefaultPosition, wx.DefaultSize, 
        ["Costo ultimo","Costo medio"] , 1, wx.RA_SPECIFY_ROWS )
    item8.SetName( "tipval" )
    item3.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item9 = wx.Button( parent, ID_BTNSTART, "Analizza", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "btnstart" )
    item3.Add( item9, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item0.Add( item3, 0, wx.ALIGN_CENTER, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Sintesi prodotti presenti nei magazzini", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.SetForegroundColour( wx.BLUE )
    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item11 = GridRiepPanel( parent, ID_PANGRIDRIEP, wx.DefaultPosition, [200,160], wx.SUNKEN_BORDER )
    item11.SetName( "pangridriep" )
    item0.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item13 = wx.StaticText( parent, ID_TEXT, "Documento", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Movimento", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "Data", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5 )

    item16 = wx.StaticText( parent, ID_TEXT, "Num.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.Add( item16, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item17 = LinkTableDocMagazz(parent, ID_TIPDOC, 'id_tipdoc'); item17.Disable()
    item12.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item18 = LinkTableMovMagazz(parent, ID_TIPMOV, 'id_tipmov'); item18.Disable()
    item12.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item19 = DateCtrl( parent, ID_DATDOC, "", wx.DefaultPosition, [70,-1], 0 )
    item19.SetName( "datdoc" )
    item12.Add( item19, 0, wx.ALIGN_CENTER|wx.RIGHT|wx.BOTTOM, 5 )

    item20 = NumCtrl(parent, ID_NUMDOC, integerWidth=5, groupDigits=False, allowNegative=False); item20.SetName("numdoc")
    item12.Add( item20, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item12.AddGrowableCol( 0 )

    item12.AddGrowableCol( 1 )

    item0.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item21 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item22 = wx.Button( parent, ID_BTNGENMOV, "Genera i movimenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item22.SetName( "btngenmov" )
    item22.Enable(False)
    item0.Add( item22, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 4 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
