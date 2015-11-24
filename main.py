import subprocess
import Tkinter as tk
import os
import xml.etree.ElementTree as etree
import shutil
import sys
from xml.etree.ElementTree import Element


class StartWindow():
    root = tk.Tk()
    isaachealth = tk.StringVar()
    isaacitem = tk.StringVar()
    maggiehealth = tk.StringVar()
    maggieitem = tk.StringVar()

    e1 = tk.Entry(root, textvariable=isaachealth)
    e2 = tk.Entry(root, textvariable = isaacitem)
    e3 = tk.Entry(root, textvariable=maggiehealth)
    e4 = tk.Entry(root, textvariable = maggieitem)
    #background_image=tk.PhotoImage("C:/Users/Ilya/PycharmProjects/isaac/afterbirth.jpg")

    #b2 = tk.Button(root, text="Update XML", command=lambda: ParseXml.isaac.write("players.xml"))
    # v.set("10")

    # v = e1.get()


    # title ="Binding Of Isaac Run Editor"
    # root = Tk()
    # root.title(title)
    # root.geometry("720x1024")
    @classmethod
    def window(self, windowtitle, geometry):
        # print(self.v)








        # root = tk.Tk()
        # e1 = tk.Entry(root)
        # e2 = tk.Entry(root)
        # frame = Tk.Frame(master=root).grid(row=1, column=1)

        self.root.title(windowtitle)
        self.root.geometry(geometry)

        tk.Label(self.root, text="Isaac Health").grid(row=0)
        tk.Label(self.root, text="Isaac Item ").grid(row=1)
        tk.Label(self.root, text="Maggie Health").grid(row=2)
        tk.Label(self.root, text="Maggie Item ").grid(row=3)
        #background_label = tk.Label(self.root, image=self.background_image)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)



        #scrollbar = tk.Scrollbar(self.root)
        #scrollbar.place(relx=.6, rely=.6)
        #listbox = tk.Listbox(self.root)

        #for i in range(0, 200):
        #    listbox.insert(i, 'Hello' + " " + str(i))

        #listbox.config(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=listbox.yview)

        if sys.platform == "linux2":
            path = readconfig.readconfig("pathgame.ini", "r")
            #print path

            b = tk.Button(self.root, text="Launch The Binding Of Isaac",command=lambda: subprocess.call("cd {0}  ./run-x64.sh".format(readconfig.readconfig("pathgame.ini","r")), shell=True))
        else:
            b = tk.Button(self.root, text="Launch The Binding Of Isaac",command=lambda: subprocess.call([readconfig.readconfig("pathgamewin.ini", "r")]))



           #b = tk.Button(self.root, text="Launch The Binding Of Isaac",command=lambda: subprocess.call([readconfig.readconfig("pathgame.ini", "r")]))
           # b = tk.Button(self.root, text="Launch The Binding Of Isaac",command=lambda: subprocess.call(['./home/ilya/.local/share/Steam/steamapps/common/The\ Binding\ of\ Isaac\ Rebirth/run-x64.sh']))





        ParseXml.isaac = etree.parse("players.xml")
        ParseXml.root = ParseXml.isaac


        b.place(relx=.3, rely=.9, anchor="c")
        ParseXml.b2.place(relx=.6, rely=.9, anchor="c")
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)



        #listbox.place(relx=.2, rely=.2, )

        #self.root.mainloop()






        #  root.button = root.Button(root, text='Start Isaac', width=25, command=subprocess.call([readconfig.readconfig("hello.ini","r")]))
        # root.button.pack()


# Dont forget to put this back
class ParseXml():
    isaac = etree.parse("players.xml")
    root = isaac
    b2 = tk.Button(StartWindow.root, text="Update XML", command=lambda: ParseXml.isaac.write("players.xml"))



    # root = isaac
    # @classmethod
    def mainparse(self, file, param, ):
        """

        :type self: object
        """
        if os.path.exists(file):

            # isaac = etree.parse(file)




            # root = isaac



            """
            for actor in root.findall('{player}item'):

                item = actor.find ('{player}item')
                print item.text
                print ("hello")
                """
            players = self.root.findall('player')
            for g in players:
                hp = g.get("hp")
                name = g.get("name")

                #if name == ("Isaac"):
                    #g.set("hp", "{0}".format(StartWindow.v.get()))
                    #newstring = g.get("items")
               #     g.set("items", "{0}".format(newstring+StartWindow.t.get()))

             #       self.isaac.write('players.xml')



                # g.get(g,"23")
                # g.set("updated","23")
                # g.set("hp","{0}".format(StartWindow.v.get()))

                # g.set("hp","'27'")
                # g.set("hp", "{0}".format(StartWindow.v.get()))
                #self.isaac.write('players.xml')
                print hp

                # players = isaac.findall('player')
                # print players
                # for neighbor in root.iter('player'):

                #   print(neighbor.attrib)
            #ParseXml.root.mainloop()
            for p in players:


                items = p.get("items")
                name = p.get("name")
                StartWindow.root.mainloop()




                if name == ('Isaac'):




                    #if p.get("items") == "":
                     #   p.set("hp", "{0}".format(StartWindow.isaachealth.get()))
                      #  p.set("items", "{0}".format(StartWindow.isaacitem.get()))
                      #  self.isaac.write('players.xml')
                     #   continue

                    if StartWindow.isaacitem.get() == "" and StartWindow.isaachealth.get() != "":
                        p.set("hp", "{0}".format(StartWindow.isaachealth.get()))
                        self.isaac.write('players.xml')
                        continue
                    if StartWindow.isaachealth.get() == "" and StartWindow.isaacitem.get() != "":
                        newstring1 = p.get("items")
                        p.set("items", "{0}".format(newstring1+","+StartWindow.isaacitem.get()))
                        self.isaac.write('players.xml')
                        continue


                    if (StartWindow.isaachealth.get() == "" and StartWindow.isaacitem.get() == ""):
                        break



                    else:
                        p.set("hp", "{0}".format(StartWindow.isaachealth.get()))
                        newstring1 = p.get("items")
                        p.set("items", "{0}".format(newstring1+","+StartWindow.isaacitem.get()))
                        self.isaac.write('players.xml')
                    continue


                if name == ('Magdalene'):
                    if p.get("items") == "":
                        p.set("hp", "{0}".format(StartWindow.maggiehealth.get()))
                        p.set("items", "{0}".format(StartWindow.maggieitem.get()))
                        self.isaac.write('players.xml')

                    if StartWindow.maggieitem.get() == "":
                        self.isaac.write('players.xml')
                        break



                    else:

                        p.set("hp", "{0}".format(StartWindow.maggiehealth.get()))
                        newstring2 = p.get("items")
                        p.set("items", "{0}".format(newstring2+","+StartWindow.maggieitem.get()))
                        self.isaac.write('players.xml')










                    # print (StartWindow.v)
                    #p.set("hp", "9")
                    # v= StartWindow.v.get()
                   #StartWindow.root.mainloop()
                    #p.set("hp", "{0}".format(StartWindow.v.get()))
                    #newstring = p.get("items")
                    #p.set("items", "{0}".format(newstring+","+StartWindow.t.get()))





                    #self.isaac.write('players.xml')

                p.set(p, "23")
                print items

            """
            for c in players:
                player =  c.find('player')
                print ("{0}".format(player))
                for items in c.findall('//player/@items'):
                    x = c.findall('//player/@items')
                    print (x)
"""



            # for player in c.findall('//player'):
            # player.get("items")



        else:
            print ("file doesnt exist")


class OpenFile():
    def readconfig(self, str, param):
        f = open(str, param)
        # f.readline()
        return f.readline()
        for line in f.readconfig(str, param).readlines():
            return (line)




readconfig = OpenFile()







# print("{0}".format(item))

# for c in players:
#    player = c.find("player").text
#    print("{0}".format(player))




# print(readconfig.readconfig("hello.ini","r"))

# subprocess.call([readconfig.readconfig("hello.ini","r")])
#ParseXml.isaac.write('players.xml')
parsexml = ParseXml()
startgui = StartWindow()
startgui.window("The Binding Of Isaac Editor", ("500x150"))
parsexml.mainparse("players.xml", "a")
#shutil.copy("players.xml", os.path.join(readconfig.readconfig("pathres.ini", "r")))





if sys.platform == "linux2":
    resoureceloc = readconfig.readconfig("pathres.ini","r")
    os.system("cp players.xml " + resoureceloc)
else:
    shutil.copy("players.xml", os.path.join(readconfig.readconfig("pathres.ini", "r")))

#shutil.copy("players.xml",  readconfig.readconfig("pathres.ini", "r"))


# print (startgui.v)
# root = Tk()
# root.title("hello")
# root.geometry("1024x720")


# for line in myobject.readconfig("hello.ini","r").readlines():

#   print (line)
