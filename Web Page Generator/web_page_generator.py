import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # Setting a min window size
        self.master.minsize(795,146)
        # Setting a max window size
        self.master.maxsize(795,146)
        # Setting a title for the GUI window
        self.master.title("Web Page Generator")

        # Creates button to select the default HTML content for HTML page creation
        self.default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        # Position of the default button using grid()
        self.default.grid(row=3, column=3, padx=(10, 0), pady=(10, 10), sticky=E)

        # Creates button to select the entrered content for the HTML page creation
        self.submit = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.submitHTML)
        # Position of the submit button using grid()
        self.submit.grid(row=3, column=4, padx=(10, 0), pady=(10, 10), sticky=W)
        
        # Creates label with instructions
        self.Lbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        # Poitioning the label at the top of entry using grid()
        self.Lbl.grid(row=0, column=0, columnspan=3, padx=(10,10), pady=(10, 10))

        # Creates and empty entry for user input
        self.entry = Entry(self.master, text='',)
        # Positioning entry slot below the label using grid()
        self.entry.grid(row=1, column=0, columnspan=5, padx=(10,10), pady=(10,10), sticky=E+W)

    # Creates function to create an HTML page and open it on the the browser
    def defaultHTML(self):
        # Hardcoded text to display on the page
        htmlText = "Stay tuned for our amazing summer sale!"
        # Creating an html file
        htmlFile = open("index.html", "w")
        # HTML used to create the page 
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # Applying the html written into the html file
        htmlFile.write(htmlContent)
        # Closing the html file
        htmlFile.close()
        # Opening the browser to display the page created
        webbrowser.open_new_tab("index.html")

    # Creates function to create an HTML page and open it on the the browser
    def submitHTML(self):
        # Creating a varible and setting it equal to the custom text entered on the entry widget using get()
        text = self.entry.get()
        # Setting the text to display as the page content
        htmlText = text
        # Creating an html file
        htmlFile = open("index.html", "w")
        # HTML used to create the page 
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        # Applying the html written into the html file
        htmlFile.write(htmlContent)
        # Closing the html file
        htmlFile.close()
        # Opening the browser to display the page created
        webbrowser.open_new_tab("index.html")


if __name__ ==  "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
