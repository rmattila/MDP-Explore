import graphviz as gv
import wx

# Define the MDP in mdp.py
from mdp import *

class MDPExplore(wx.Frame):

    def __init__(self, parent, title):
        super(MDPExplore, self).__init__(parent, title=title,size=(400, 300))

        # Generate an initial plot of the MDP
        self.hasUI = False
        self.plotMDPGraph(self.generateMDPGraph(0, 0, state_labels()))

        self.initUI()
        self.hasUI = True

        self.Centre()
        self.Show()

    def initUI(self):
        self.panel = wx.Panel(self)

        # Components
        self.mdp_image = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap('./img/mdp.png', wx.BITMAP_TYPE_ANY))

        self.sc_time = wx.SpinCtrl(self.panel, value='0')
        self.sc_time.SetRange(0, 10e4)

        controls = [str(x) for x in range(0, number_of_controls())]
        self.cob_control = wx.ComboBox(self.panel, choices=controls, style=wx.CB_READONLY)

        self.chb_probs = wx.CheckBox(self.panel, label='Show probabilities')
        self.chb_probs.SetValue(True)

        # Bind events
        self.sc_time.Bind(wx.EVT_SPINCTRL, self.updateMDPPlot)
        self.cob_control.Bind(wx.EVT_COMBOBOX, self.updateMDPPlot)
        self.chb_probs.Bind(wx.EVT_CHECKBOX, self.updateMDPPlot)

        # Sizers
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        vboxl = wx.BoxSizer(wx.VERTICAL)
        vboxr = wx.BoxSizer(wx.VERTICAL)

        # Create the layout
        vboxl.Add(self.mdp_image, 1, wx.EXPAND|wx.ALL, 5)

        vboxr.Add(wx.StaticText(self.panel, label='Time:'))
        vboxr.Add(self.sc_time, 0, wx.ALL, 5)

        vboxr.Add(wx.StaticText(self.panel, label='Control:'))
        vboxr.Add(self.cob_control, 0, wx.ALL, 5)

        vboxr.Add(self.chb_probs, 0, wx.TOP, 10)

        self.hbox.Add(vboxl, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5)
        self.hbox.Add(vboxr, 0, wx.ALL, 5)

        self.panel.SetSizer(self.hbox)
        self.hbox.Fit(self)
        self.panel.Layout()

    def updateMDPPlot(self, e):
        self.plotMDPGraph(self.generateMDPGraph(int(self.cob_control.GetValue()), self.sc_time.GetValue(), state_labels()))
        self.mdp_image.SetBitmap(wx.Bitmap('./img/mdp.png', wx.BITMAP_TYPE_ANY))
        self.hbox.Fit(self)
        print "Updated plot"

    def generateMDPGraph(self, u, k, labels):
        line_width = 5.0

        if u > number_of_controls():
            print "ERROR: %i is not a valid control action!" % u
            u = 0

        mdp = gv.Digraph(format='png')

        # Create the nodes in the graph
        for i in range(0, number_of_states()):
            if i in labels:
                if not self.hasUI or self.chb_probs.GetValue():
                    mdp.node(str(i), str(i) + ':' + labels[i])
                else:
                    mdp.node(str(i), labels[i])
            else:
                mdp.node(str(i), 'Node %i' % i)

        # Add edges
        for i in range(0, number_of_states()):
            psum = 0.0
            for j in range(0, number_of_states()):
                p = TProb(i, j, k, u)

                if TProb(i, j, k, u) > 0:
                    if not self.hasUI or self.chb_probs.GetValue():
                        mdp.edge(str(i), str(j), '%.2f' % p, {'penwidth':str(line_width * p)})
                    else:
                        mdp.edge(str(i), str(j), None, {'penwidth':str(line_width * p)})

                    psum += p

            if psum != 1.0:
                print "WARNING: The transition matrix has a row (%i) that does not sum to one!" % i

        return mdp

    def plotMDPGraph(self, mdp):
        filename = mdp.render(filename='img/mdp')
        print "Graph of MDP was rendered to " + filename

def main():
    app = wx.App()
    MDPExplore(None, title='MDP-Explore 0.2')
    app.MainLoop()

if __name__ == '__main__':
    main()

