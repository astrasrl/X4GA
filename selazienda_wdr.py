# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: selazienda.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
import version
import images
from awc.controls.button import Button, FlatButton
from awc.controls.textctrl import TextCtrl, TextCtrl_LC
from awc.controls.numctrl import NumCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.checkbox import CheckBox, RCheckBox
from awc.controls.listbox import ListBox

import wx.lib.hyperlink as hl

from X_wdr import AboutPanel


class MyChoice(wx.Choice):
    def GetValue(self):
        return self.GetClientData(self.GetSelection())




# Window functions

ID_TEXT = 11000
ID_CODICE = 11001
ID_NOMEDB = 11002
ID_BTNMIRAGE = 11003
ID_INTESTAZ = 11004
ID_INDIRIZZO = 11005
ID_CAP = 11006
ID_CITTA = 11007
ID_PROVINCIA = 11008
ID_LINE = 11009
ID_CODFISC = 11010
ID_STATO = 11011
ID_PIVA = 11012
ID_ESERCIZIOGG = 11013
ID_ESERCIZIOMM = 11014
ID_ESERCIZIOERR = 11015
ID_CONFACTION1 = 11016
ID_CONFACTION2 = 11017
ID_BTNQUIT = 11018
ID_BTNOK = 11019

def AziendaSetupFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Database" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Codice:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "Nome database:", wx.DefaultPosition, [90,-1], 0 )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item3.Add( [ 10, 10 ] , 0, wx.ALIGN_CENTER, 5 )

    item6 = TextCtrl_LC( parent, ID_CODICE, "", wx.DefaultPosition, [80,-1], 0 )
    item3.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7 = TextCtrl_LC( parent, ID_NOMEDB, "", wx.DefaultPosition, [80,-1], 0 )
    item3.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.Button( parent, ID_BTNMIRAGE, "Acquisizione azienda da Mirage", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetName( "miracqbut" )
    item3.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3.AddGrowableCol( 2 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = wx.StaticBox( parent, -1, "Dati anagrafici Azienda" )
    item9 = wx.StaticBoxSizer( item10, wx.VERTICAL )
    
    item11 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item12 = wx.StaticText( parent, ID_TEXT, "Intestazione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item11.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item13 = TextCtrl( parent, ID_INTESTAZ, "", wx.DefaultPosition, [400,-1], 0 )
    item11.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "Indirizzo:", wx.DefaultPosition, [90,-1], 0 )
    item11.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item15 = TextCtrl( parent, ID_INDIRIZZO, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item11.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item16 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item17 = wx.StaticText( parent, ID_TEXT, "CAP", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item18 = wx.StaticText( parent, ID_TEXT, "Città", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item19 = wx.StaticText( parent, ID_TEXT, "Prov.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item20 = TextCtrl( parent, ID_CAP, "", wx.DefaultPosition, [60,-1], 0 )
    item16.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item21 = TextCtrl( parent, ID_CITTA, "", wx.DefaultPosition, [80,-1], 0 )
    item16.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item22 = TextCtrl( parent, ID_PROVINCIA, "", wx.DefaultPosition, [35,-1], 0 )
    item16.Add( item22, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item16.AddGrowableCol( 1 )

    item11.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 0 )

    item11.AddGrowableCol( 0 )

    item9.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item23 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item9.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item24 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item25 = wx.StaticText( parent, ID_TEXT, "Cod. Fiscale:", wx.DefaultPosition, [90,-1], 0 )
    item24.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP, 5 )

    item26 = wx.StaticText( parent, ID_TEXT, "Stato:", wx.DefaultPosition, [40,-1], 0 )
    item24.Add( item26, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )

    item27 = wx.StaticText( parent, ID_TEXT, "P.IVA:", wx.DefaultPosition, [40,-1], 0 )
    item24.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )

    item28 = TextCtrl( parent, ID_CODFISC, "", wx.DefaultPosition, [100,-1], 0 )
    item24.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item29 = TextCtrl( parent, ID_STATO, "", wx.DefaultPosition, [35,-1], 0 )
    item24.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item30 = TextCtrl( parent, ID_PIVA, "", wx.DefaultPosition, [80,-1], 0 )
    item24.Add( item30, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item24.AddGrowableCol( 0 )

    item24.AddGrowableCol( 2 )

    item9.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item32 = wx.StaticBox( parent, -1, "Esercizio contabile" )
    item31 = wx.StaticBoxSizer( item32, wx.VERTICAL )
    
    item33 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item34 = wx.StaticText( parent, ID_TEXT, "Giorno e mese di inizio dell'esercizio contabile:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item33.Add( item34, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item35 = NumCtrl(parent, ID_ESERCIZIOGG, integerWidth=2, allowNegative=False); item35.SetName('setup_esercizio_startgg')
    item33.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item36 = wx.StaticText( parent, ID_TEXT, "/", wx.DefaultPosition, wx.DefaultSize, 0 )
    item33.Add( item36, 0, wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, 5 )

    item37 = NumCtrl(parent, ID_ESERCIZIOMM, integerWidth=2, allowNegative=False); item37.SetName('setup_esercizio_startmm')
    item33.Add( item37, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item38 = wx.StaticText( parent, ID_ESERCIZIOERR, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item38.SetForegroundColour( wx.RED )
    item38.SetName( "esercizio_err" )
    item33.Add( item38, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item33.AddGrowableCol( 4 )

    item31.Add( item33, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item39 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item40 = wx.StaticText( parent, ID_CONFACTION1, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item40, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item41 = wx.StaticText( parent, ID_CONFACTION2, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item41, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item39.AddGrowableCol( 0 )

    item0.Add( item39, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item42 = wx.BoxSizer( wx.HORIZONTAL )
    
    item43 = wx.Button( parent, ID_BTNQUIT, "Abbandona", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item43, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item44 = wx.Button( parent, ID_BTNOK, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item44.SetDefault()
    item42.Add( item44, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item42, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_INCORSO = 11020
ID_TABELLA = 11021
ID_STATUS = 11022
ID_RECORD = 11023
ID_ERRORS = 11024
ID_PROGRESS = 11025
ID_SPEED = 11026
ID_BTNBREAK = 11027

def ProgressFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_INCORSO, 
        "\n"
        "Acquisizione archivi Mirage in corso...\n"
        "",
        wx.DefaultPosition, [600,-1], wx.ALIGN_CENTRE )
    item1.SetForegroundColour( wx.WHITE )
    item1.SetBackgroundColour( wx.BLUE )
    item1.SetFont( wx.Font( 16, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 10 )

    item0.Add( [ 20, 10 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item2 = wx.StaticText( parent, ID_TABELLA, "*", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.SetFont( wx.Font( 12, wx.ROMAN, wx.NORMAL, wx.BOLD ) )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 10 )

    item3 = wx.StaticText( parent, ID_STATUS, "*", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item0.Add( [ 20, 10 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item4 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item5 = wx.StaticText( parent, ID_TEXT, "Elementi acquisiti:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetFont( wx.Font( 12, wx.ROMAN, wx.NORMAL, wx.BOLD ) )
    item4.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item6 = wx.ListBox( parent, ID_RECORD, wx.DefaultPosition, [-1,160], [], wx.LB_SINGLE|wx.LB_NEEDED_SB )
    item4.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Problemi riscontrati:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetFont( wx.Font( 12, wx.ROMAN, wx.NORMAL, wx.BOLD ) )
    item4.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item8 = wx.ListBox( parent, ID_ERRORS, wx.DefaultPosition, [-1,120], [], wx.LB_SINGLE|wx.LB_HSCROLL|wx.LB_NEEDED_SB )
    item4.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item4.AddGrowableCol( 0 )

    item4.AddGrowableCol( 1 )

    item4.AddGrowableRow( 0 )

    item4.AddGrowableRow( 1 )

    item0.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = wx.Gauge( parent, ID_PROGRESS, 100, wx.DefaultPosition, [100,20], wx.GA_SMOOTH|wx.GA_PROGRESSBAR )
    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item11 = wx.StaticText( parent, ID_SPEED, "*", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item11, 0, wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item12 = wx.Button( parent, ID_BTNBREAK, "Interrompi (ESC)", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item10.AddGrowableCol( 0 )

    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_NEWAZI = 11028
ID_UTENTI = 11029
ID_WKSETUP = 11030

def AdminPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Amministrazione" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.Button( parent, ID_NEWAZI, "&Nuova Azienda", wx.DefaultPosition, [120,-1], 0 )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item4 = wx.Button( parent, ID_UTENTI, "Gestione &Utenti", wx.DefaultPosition, [130,-1], 0 )
    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item5 = wx.Button( parent, ID_WKSETUP, "Setup &Workstation", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.SetName( "wksetup" )
    item1.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CONFERMA = 11031

def UtentiNewAzienda( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, "Seleziona gli utenti che avranno accesso all'azienda:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item2 = wx.CheckListBox( parent, ID_UTENTI, wx.DefaultPosition, [80,160], [], wx.LB_SINGLE )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3 = wx.BoxSizer( wx.HORIZONTAL )
    
    item4 = wx.Button( parent, ID_CONFERMA, "Conferma", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def AziendaDetailsFunc( parent, call_fit = True, set_sizer = True ):
    item1 = wx.StaticBox( parent, -1, "Azienda" )
    item0 = wx.StaticBoxSizer( item1, wx.VERTICAL )
    
    item2 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Cod.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item4.SetFont( wx.Font( 11, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item4.SetName( "azi_codice" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "DB:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item6.SetFont( wx.Font( 11, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item6.SetName( "azi_schema" )
    item2.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item2.AddGrowableCol( 1 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_ABOUT = 11032
ID_USER = 11033
ID_PSWD = 11034
ID_LOGIN = 11035
ID_SERVER = 11036
ID_CHANGEPWD = 11037
ID_SERVERURL = 11038
ID_LISTAZIENDE = 11039
ID_DATAELAB = 11040
ID_BTNAZISEL = 11041
ID_DETAILS = 11042
ID_SETUP = 11043

def SelAziendaFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AboutPanel(parent, ID_ABOUT)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

    item0.Add( [ 20, 10 ] , 0, wx.ALIGN_CENTER, 5 )

    item3 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Utente:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item5 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item6 = TextCtrl_LC( parent, ID_USER, "", wx.DefaultPosition, [50,-1], 0 )
    item6.SetName( "username" )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Password:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item8 = TextCtrl_LC( parent, ID_PSWD, "", wx.DefaultPosition, [50,-1], wx.TE_PASSWORD )
    item8.SetName( "password" )
    item5.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item5.AddGrowableCol( 0 )

    item5.AddGrowableCol( 2 )

    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = Button( parent, ID_LOGIN, "Login", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.SetName( "butlogin" )
    item3.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Server:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item11 = MyChoice( parent, ID_SERVER, wx.DefaultPosition, [400,-1], [], 0 )
    item11.SetName( "server" )
    item3.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item12 = Button( parent, ID_CHANGEPWD, "Cambia password", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.SetName( "butchangepswd" )
    item3.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "URL:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item13, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 10 )

    item14 = wx.StaticText( parent, ID_SERVERURL, "-", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item3.Add( [ 20, 20 ] , 0, wx.ALIGN_CENTER, 5 )

    item15 = wx.StaticText( parent, ID_TEXT, "Aziende:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item15, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.BOTTOM, 5 )

    item16 = wx.Panel( parent, ID_LISTAZIENDE, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER )
    item16.SetName( "aziende" )
    item3.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item17 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item18 = wx.BoxSizer( wx.HORIZONTAL )
    
    item19 = wx.StaticText( parent, ID_TEXT, "Data:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.Add( item19, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.TOP|wx.BOTTOM, 5 )

    item20 = DateCtrl( parent, ID_DATAELAB, "", wx.DefaultPosition, [100,-1], 0 )
    item20.SetName( "dataelab" )
    item18.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item17.Add( item18, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item21 = Button( parent, ID_BTNAZISEL, "Seleziona azienda", wx.DefaultPosition, wx.DefaultSize, 0 )
    item21.SetName( "butazisel" )
    item17.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item22 = wx.Panel(parent, ID_DETAILS); AziendaDetailsFunc(item22)
    item17.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item23 = wx.Panel(parent, ID_SETUP); AdminPanelFunc(item23)
    item17.Add( item23, 0, wx.GROW|wx.RIGHT|wx.BOTTOM, 5 )

    item3.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3.AddGrowableCol( 1 )

    item0.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 3 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_SUPER_CODE = 11044
ID_SUPER_UTENTE = 11045
ID_SUPER_PSW = 11046
ID_SUPER_PSW1 = 11047
ID_SUPER_FLAG = 1
ID_BTN_SUPEROK = 11048

def SuperUser( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, 
        "E' NECESSARIO DEFINIRE ALMENO UN UTENTE \n"
        "CON I DIRITTI DI AMMINISTRATORE",
        wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item2 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Codice", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.TextCtrl( parent, ID_SUPER_CODE, "", wx.DefaultPosition, [40,-1], 0 )
    item3.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Utente", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item6, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.TextCtrl( parent, ID_SUPER_UTENTE, "", wx.DefaultPosition, [150,-1], 0 )
    item3.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Password", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.TextCtrl( parent, ID_SUPER_PSW, "", wx.DefaultPosition, [80,-1], wx.TE_PASSWORD )
    item3.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "Conferma Password", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item11 = wx.TextCtrl( parent, ID_SUPER_PSW1, "", wx.DefaultPosition, [80,-1], wx.TE_PASSWORD )
    item3.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "Amministratore", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item13 = wx.CheckBox( parent, ID_SUPER_FLAG, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.SetValue( True )
    item13.Enable(False)
    item3.Add( item13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3.Add( [ 20, 20 ] , 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.BoxSizer( wx.HORIZONTAL )
    
    item15 = wx.Button( parent, ID_BTN_SUPEROK, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3.Add( item14, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3.AddGrowableCol( 1 )

    item0.Add( item3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_PANGRIDAZI = 11049
ID_CHECKBOX = 11050
ID_BUTTON = 11051

def AziendaCopyFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Le strutture delle tabelle dell'azienda sono state create, ma al momento tutte le tabella sono vuote.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.StaticText( parent, ID_TEXT, "Da qui è possibile inizializzare il database dell'azienda in base ad una azienda di partenza, dalla quale è possibile acquisire le informazioni", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "desiderate.  Selezionare le informazioni da acquisire.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.AddGrowableCol( 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item5 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item6 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item7 = wx.StaticText( parent, ID_TEXT, "Copia dall'azienda:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.SetForegroundColour( wx.BLUE )
    item6.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item8 = wx.Panel( parent, ID_PANGRIDAZI, wx.DefaultPosition, [400,160], wx.SUNKEN_BORDER )
    item6.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item6.AddGrowableCol( 0 )

    item6.AddGrowableRow( 1 )

    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item10 = wx.StaticText( parent, ID_TEXT, "Le seguenti informazioni:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.SetForegroundColour( wx.BLUE )
    item9.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item11 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item12 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item14 = wx.StaticBox( parent, -1, "Contabilità" )
    item13 = wx.StaticBoxSizer( item14, wx.VERTICAL )
    
    item15 = CheckBox( parent, ID_CHECKBOX, "Causali e Registri IVA", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.SetValue( True )
    item15.SetName( "copyconcau" )
    item13.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item16 = CheckBox( parent, ID_CHECKBOX, "Piano dei Conti e classificazioni", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.SetValue( True )
    item16.SetName( "copyconpdc" )
    item13.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item17 = CheckBox( parent, ID_CHECKBOX, "Anagrafiche Clienti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item17.SetValue( True )
    item17.SetName( "copyconcli" )
    item13.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item18 = CheckBox( parent, ID_CHECKBOX, "Anagrafiche Fornitori", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.SetValue( True )
    item18.SetName( "copyconfor" )
    item13.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item19 = CheckBox( parent, ID_CHECKBOX, "Sottoconti Cassa", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.SetValue( True )
    item19.SetName( "copyconcas" )
    item13.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item20 = CheckBox( parent, ID_CHECKBOX, "Banche", wx.DefaultPosition, wx.DefaultSize, 0 )
    item20.SetValue( True )
    item20.SetName( "copyconban" )
    item13.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item21 = CheckBox( parent, ID_CHECKBOX, "Gruppi Scadenzario", wx.DefaultPosition, wx.DefaultSize, 0 )
    item21.SetValue( True )
    item21.SetName( "copycongrs" )
    item13.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item23 = wx.StaticBox( parent, -1, "Magazzino" )
    item22 = wx.StaticBoxSizer( item23, wx.VERTICAL )
    
    item24 = CheckBox( parent, ID_CHECKBOX, "Causali e magazzini", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.SetValue( True )
    item24.SetName( "copymagcau" )
    item22.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item25 = CheckBox( parent, ID_CHECKBOX, "Prodotti, classificazioni e listini", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.SetValue( True )
    item25.SetName( "copymagpro" )
    item22.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item26 = CheckBox( parent, ID_CHECKBOX, "Agenti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.SetValue( True )
    item26.SetName( "copymagage" )
    item22.Add( item26, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item27 = CheckBox( parent, ID_CHECKBOX, "Zone", wx.DefaultPosition, wx.DefaultSize, 0 )
    item27.SetValue( True )
    item27.SetName( "copymagzne" )
    item22.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item28 = CheckBox( parent, ID_CHECKBOX, "Dati trasporto", wx.DefaultPosition, wx.DefaultSize, 0 )
    item28.SetValue( True )
    item28.SetName( "copymagtra" )
    item22.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item30 = wx.StaticBox( parent, -1, "Varie" )
    item29 = wx.StaticBoxSizer( item30, wx.VERTICAL )
    
    item31 = CheckBox( parent, ID_CHECKBOX, "Aliquote IVA", wx.DefaultPosition, wx.DefaultSize, 0 )
    item31.SetValue( True )
    item31.SetName( "copygeniva" )
    item29.Add( item31, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item32 = CheckBox( parent, ID_CHECKBOX, "Valute", wx.DefaultPosition, wx.DefaultSize, 0 )
    item32.SetValue( True )
    item32.SetName( "copygenval" )
    item29.Add( item32, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item33 = CheckBox( parent, ID_CHECKBOX, "Mod. Pagamento e Spese Incasso", wx.DefaultPosition, wx.DefaultSize, 0 )
    item33.SetValue( True )
    item33.SetName( "copygenpag" )
    item29.Add( item33, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item34 = CheckBox( parent, ID_CHECKBOX, "Automatismi vari", wx.DefaultPosition, wx.DefaultSize, 0 )
    item34.SetValue( True )
    item34.SetName( "copygenaut" )
    item29.Add( item34, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item12.AddGrowableCol( 0 )

    item11.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9.AddGrowableCol( 0 )

    item5.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item5.AddGrowableCol( 0 )

    item5.AddGrowableRow( 0 )

    item0.Add( item5, 0, wx.GROW, 5 )

    item35 = wx.BoxSizer( wx.HORIZONTAL )
    
    item36 = wx.Button( parent, ID_BUTTON, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item36.SetName( "btnok" )
    item35.Add( item36, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

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
