import graphviz as gv
import wx

# Define the MDP in mdp.py
from mdp import *

def generateMDPGraph(u, k, labels):

    line_width = 5.0

    if u > number_of_controls():
        print "ERROR: %i is not a valid control action!" % u
        u = 0

    mdp = gv.Digraph(format='png')

    # Create the nodes in the graph
    for i in range(0, number_of_states()):
        if i in labels:
            mdp.node(str(i), str(i) + ':' + labels[i])
        else:
            mdp.node(str(i), 'Node %i' % i)

    # Add edges
    for i in range(0, number_of_states()):
        psum = 0.0
        for j in range(0, number_of_states()):
            p = TProb(i, j, k, u)

            if TProb(i, j, k, u) > 0:
                mdp.edge(str(i), str(j), '%.2f' % p, {'penwidth':str(line_width * p)})
                psum += p

        if psum != 1.0:
            print "WARNING: The transition matrix has a row (%i) that does not sum to one!" % i

    return mdp

def plotMDPGraph(mdp):
    filename = mdp.render(filename='img/mdp')
    print "Graph of MDP was rendered to " + filename

class MDPExplore(wx.Frame):

    def __init__(self, parent, title):
        super(MDPExplore, self).__init__(parent, title=title,size=(400, 300))
        self.initUI()
        self.Centre()
        self.Show()

    def initUI(self):

        self.panel = wx.Panel(self)

        # Components
        mdp_image = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('./img/mdp.png', wx.BITMAP_TYPE_ANY))
        btn_redraw = wx.Button(self.panel, label='Redraw')

        sc_time = wx.SpinCtrl(self.panel, value='0')
        sc_time.SetRange(0, 150)

        controls = [str(x) for x in range(0, number_of_controls())]
        cb_control = wx.ComboBox(self.panel, choices=controls, style=wx.CB_READONLY)
        cb_control.Bind(wx.EVT_COMBOBOX, self.OnChangeControl)

        # Bind events
        sc_time.Bind(wx.EVT_SPINCTRL, self.OnChangeTime)

        # Sizers
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        vboxl = wx.BoxSizer(wx.VERTICAL)
        vboxr = wx.BoxSizer(wx.VERTICAL)

        # Create the layout
        vboxl.Add(mdp_image, 1, wx.EXPAND|wx.ALL, 5)
        vboxl.Add(btn_redraw, 0, wx.ALL, 5)

        vboxr.Add(wx.StaticText(self.panel, label='Time:'))
        vboxr.Add(sc_time, 0, wx.ALL, 5)

        vboxr.Add(wx.StaticText(self.panel, label='Control:'))
        vboxr.Add(cb_control, 0, wx.ALL, 5)

        hbox.Add(vboxl, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5)
        hbox.Add(vboxr, 0, wx.ALL, 5)

        self.panel.SetSizer(hbox)
        hbox.Fit(self)
        self.panel.Layout()

    def OnChangeTime(self, e):
        print "TODO: Update graph with new time"

    def OnChangeControl(self, e):
        print "TODO: Update graph with new control"

def main():
    plotMDPGraph(generateMDPGraph(0, 0, state_labels()))

    app = wx.App()
    MDPExplore(None, title='MDP-Explore 0.1')
    app.MainLoop()

if __name__ == '__main__':
    main()
