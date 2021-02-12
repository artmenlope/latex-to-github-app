# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:14:50 2020
@author: artmenlope
"""


# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk               # Python 3
import urllib                      # To convert the LaTeX code to HTML
from PIL import Image, ImageTk
from io import BytesIO
from cairosvg import svg2png



class Application:
    
    def __init__(self, root):
    
        self.root = root
        self.txt_width = 50
        self.txt_height = 5
        self.latex_width = self.txt_width
        self.latex_height = 5*self.txt_height
        self.canvas_width = 100 #6*self.txt_width
        self.canvas_height = 50 #10*self.latex_height

        self.root.title("Convert LaTeX code to HTML readable by Github.")
        self.root.resizable(True, True)
        
        self.create_widgets()
        self.create_buttons()
        self.create_scrollbars()
        self.make_grid()
        self.configure_rowsCols()
        self.make_menu()
        
        self.root.focus_force() # Focus on the main app's window as soon as the app starts running.
        
        
    def create_widgets(self):
        
        # Create the widgets
        
        # Top LaTeX widget
        self.l1 = tk.Label(self.root, text="Write your LaTeX code (math mode):")
        self.entry = tk.Text(self.root, width=self.latex_width, height=self.latex_height, wrap=tk.NONE)
        self.entry.focus_set() # Allow writing in the LaTeX widget as soon as the app is open.
        
        # HTML output widget
        self.l2 = tk.Label(self.root, text="The HTML result is:")
        self.output_html = tk.Text(self.root, width=self.txt_width, height=self.txt_height, wrap=tk.CHAR)
        
        # Github url output widget
        self.l3 = tk.Label(self.root, text="The GitHub URL result is:")
        self.output_gith = tk.Text(self.root, width=self.txt_width, height=self.txt_height, wrap=tk.CHAR)
        
        # Image output canvas
        self.l4 = tk.Label(self.root, text="Image:")
        self.output_img = tk.Canvas(self.root, bg="white", width=self.canvas_width, height=self.canvas_height)

        self.right_click_menus() # Create right click mouse copy-cut-paste menus for the text widgets.
        
        return
    
    
    def create_buttons(self):
        
        # Create the buttons.
        
        self.button = tk.Button(self.root, text="Convert LaTeX code", width=20)
        
        self.activate_img = tk.IntVar(value=1) # value=1 -> checkbutton checked by default.
        self.checkbutton = tk.Checkbutton(self.root, text=" View image\n(requires internet connection).", justify=tk.LEFT,
                                          variable=self.activate_img, onvalue=1, offvalue=0)
        
        # Button activation
        self.button.configure(command=self.encodeLaTeX)
        
        return
    
    
    def create_scrollbars(self):
        
        # Latex widget scrollbar
        # Horizontal scroll 
        self.entry_scroll_x = tk.Scrollbar(self.root, orient="horizontal", command=self.entry.xview)
        # Vertical scroll 
        self.entry_scroll_y = tk.Scrollbar(self.root, orient="vertical", command=self.entry.yview)
        # Configure
        self.entry.configure(yscrollcommand=self.entry_scroll_y.set, xscrollcommand=self.entry_scroll_x.set)
 
        # HTML widget scrollbar
        self.root.scrollbar_html = tk.Scrollbar(self.root)
        self.output_html.config(yscrollcommand=self.root.scrollbar_html.set)
        self.root.scrollbar_html.config(command=self.output_html.yview)

        # Github widget scrollbar
        self.root.scrollbar_gith = tk.Scrollbar(self.root)
        self.output_gith.config(yscrollcommand=self.root.scrollbar_gith.set)
        self.root.scrollbar_gith.config(command=self.output_gith.yview)
                
        # Image scrollbar
        # Horizontal scroll 
        self.output_img_scroll_x = tk.Scrollbar(self.root, orient="horizontal", command=self.output_img.xview)
        # Vertical scroll 
        self.output_img_scroll_y = tk.Scrollbar(self.root, orient="vertical", command=self.output_img.yview)
        # Configure
        self.output_img.configure(yscrollcommand=self.output_img_scroll_y.set, xscrollcommand=self.output_img_scroll_x.set)
        self.output_img.configure(scrollregion=self.output_img.bbox("all"))
        
        return
    
    
    def make_grid(self):
        
        #Positioning the widgets
        
        # Top LaTeX widget
        self.l1.grid(row=1, column=1, padx=20, pady=(20,0), sticky="w")
        self.entry.grid(row=2, column=1, rowspan=6, columnspan=2, padx=(20,0), pady=(10,0), sticky="wens")
        
        # Buttons
        self.button.grid(row=9, column=1, rowspan=1, columnspan=1, padx=(0,0), pady=(25,0))
        self.checkbutton.grid(row=9, column=2, rowspan=1, columnspan=1, padx=(0,40), pady=(25,0))
        
        # HTML output widgetd
        self.l2.grid(row=1, column=5, padx=(10,0), pady=(20,0), sticky="w")
        self.output_html.grid(row=2, column=5, columnspan=2, padx=(10,0), pady=(10,10), sticky="wens")
        
        # Github url output widget
        self.l3.grid(row=3, column=5, padx=(10,0), pady=(10,0), sticky="w")
        self.output_gith.grid(row=4, column=5, columnspan=2, padx=(10,0), pady=(0,10), sticky="wens")
        
        # Image output canvas
        self.l4.grid(row=5, column=5, padx=(10,0), pady=(5,0), sticky="w")
        self.output_img.grid(row=6, column=5, rowspan=4, columnspan=2, padx=(10,0), pady=0, sticky="wens")

        # Scrollbars
        
        # Latex widget scrollbar
        # Horizontal scroll 
        self.entry_scroll_x.grid(row=8, column=1, rowspan=1, columnspan=2, padx=(20,0), pady=(0,10), sticky="ewn")
        # Vertical scroll 
        self.entry_scroll_y.grid(row=2, column=3, rowspan=6, columnspan=1, pady=(10,0), sticky="nsw")
        
        # HTML widget scrollbar
        self.root.scrollbar_html.grid(row=2, column=7, rowspan=1, columnspan=1, padx=(0,10), pady=(10,10), sticky="nsw")

        # Github widget scrollbar
        self.root.scrollbar_gith.grid(row=4, column=7, rowspan=1, columnspan=1, padx=(0,10), pady=(0,10),  sticky="nsw")
        
        # Image scrollbar
        # Horizontal scroll 
        self.output_img_scroll_x.grid(row=10, column=5, columnspan=2, padx=(10,0), pady=(0,15), sticky="ewn")
        # Vertical scroll 
        self.output_img_scroll_y.grid(row=6, column=7, rowspan=4, padx=(0,10), pady=0, sticky="nsw")
        
        return
    
    
    def encodeLaTeX(self):
        
        self.string = self.entry.get("1.0",tk.END)
        self.encoded_string = urllib.parse.quote(str(self.string).encode("utf-8"), safe="~()*!.\"")
        self.github_url = "https://render.githubusercontent.com/render/math?math=" + self.encoded_string
        self.result = '<img src="' + self.github_url + '">'
    
        self.output_html.delete('1.0', tk.END)
        self.output_html.insert(tk.END, str(self.result))
        
        self.output_gith.delete('1.0', tk.END)
        self.output_gith.insert(tk.END, str(self.github_url))
        
        state = self.activate_img.get()
        if state == 1:
            self.show_image()
        else:
            self.output_img.delete("all") # Delete all possible images in the output_img canvas.
        
        return
    
    
    def show_image(self):
        
        try:
            self.page = urllib.request.urlopen(self.github_url).read()
            self.img_data = self.page
            self.img_data = svg2png(bytestring=self.img_data, write_to=None)
            self.img_data = Image.open(BytesIO(self.img_data))
            
            #####
            self.check_canvas_dimensions() 
            #####
            
            self.image = ImageTk.PhotoImage(self.img_data)
            
            self.root.image=self.image # to prevent the image garbage collected.
            
            self.output_img.create_image((10,10), image=self.root.image, anchor="nw")
            self.output_img.update() # Refresh (optional)
            
        except urllib.error.HTTPError: # Error while rendering the image using Github.
            tk.messagebox.showerror(title="HTTPError", message="An error occurred while trying to show the image.\n\nPlease, check for typos in your LaTeX code.")
            raise # Show the exception in the terminal too.
            
        return
    
    
    def check_canvas_dimensions(self):
        
        self.img_width, self.img_height = self.img_data.size
        
        # Reset scrollregion in case that the canvas it is already displaying a big image.    
        self.output_img.config(scrollregion=(0, 0, self.canvas_width, self.canvas_height))
        
        if self.img_width > self.canvas_width or self.img_height > self.canvas_height:
            
            self.new_width  = max([1.1*self.img_width, self.canvas_width])
            self.new_height = max([1.2*self.img_height, self.canvas_height])
            
            self.output_img.config(scrollregion=(0, 0, int(self.new_width)+1, int(self.new_height)+1)) # The numbers for scrollregion must be integers.
            
        return
    
    
    def configure_rowsCols(self):
        
        for i in range(0,7+1):
            self.root.grid_columnconfigure(i,weight=1)
        # self.root.grid_columnconfigure(3,weight=0) # LaTeX horizontal scrollbar
        
        for i in range(0,10+1):
            self.root.grid_rowconfigure(i,weight=1)
        # self.root.grid_rowconfigure(8,weight=0) # LaTeX vertical scrollbar
        
        return
    
    
    def make_menu(self):
        
        # Creating Menubar 
        self.menubar = tk.Menu(self.root) 
        self.root.config(menu=self.menubar)  # Asign it to the window
        
        # Adding options menu
        self.help = tk.Menu(self.menubar, tearoff=0) # tearoff=0 -> once clicked, show menu (even without mouse over it) until clicked again.
        self.help.add_command(label ='Documentation', command = self.docs_window) 
        self.menubar.add_cascade(label ='Help', menu=self.help) 
        # options.add_separator() 
        
        return
    
    def right_click_menus(self):
        
        """
        Create a right click mouse menu on each text widget with 
        the copy, cut and paste options.
        
        References: 
            https://stackoverflow.com/q/8449053
            https://gist.github.com/kai9987kai/f8b34c5538613d2786be8ab1b273e1ca
        """
        
        # Right click menu on the text entry widget.
        
        rClickMenu_entry = tk.Menu(self.entry, tearoff=0) # Create the menu.
        rClickMenu_entry.add_command(label="Copy", 
                                     accelerator="Ctrl+C", # Show the command's shortcut together with the label.
                                     command=lambda: self.entry.event_generate('<Control-c>')) # Define the command.
        rClickMenu_entry.add_separator() # Add vertical space between the two labels.
        rClickMenu_entry.add_command(label="Cut", 
                                     accelerator="Ctrl+X", # Show the command's shortcut together with the label.
                                     command=lambda: self.entry.event_generate('<Control-x>')) # Define the command.
        rClickMenu_entry.add_separator() # Add vertical space between the two labels.
        rClickMenu_entry.add_command(label="Paste", 
                                     accelerator="Ctrl+V", # Show the command's shortcut together with the label.
                                     command=lambda: self.entry.event_generate('<Control-v>')) # Define the command.
    
        def show_rClickMenu_entry(event):
            rClickMenu_entry.tk_popup(event.x_root, event.y_root, 0)

        self.entry.bind("<Button-3>", show_rClickMenu_entry)
        
        
        # Right click menu on the HTML output widget.
        
        rClickMenu_HTML = tk.Menu(self.output_html, tearoff=0)
        rClickMenu_HTML.add_command(label="Copy", 
                                    accelerator="Ctrl+C", 
                                    command=lambda: self.output_html.event_generate('<Control-c>'))
        rClickMenu_HTML.add_separator()
        rClickMenu_HTML.add_command(label="Cut", 
                                    accelerator="Ctrl+X", 
                                    command=lambda: self.output_html.event_generate('<Control-x>'))
        rClickMenu_HTML.add_separator()
        rClickMenu_HTML.add_command(label="Paste", 
                                    accelerator="Ctrl+V", 
                                    command=lambda: self.output_html.event_generate('<Control-v>'))
    
        def show_rClickMenu_HTML(event):
            rClickMenu_HTML.tk_popup(event.x_root, event.y_root, 0)

        self.output_html.bind("<Button-3>", show_rClickMenu_HTML)
        
        
        # Right click menu on the Github url output widget.
        
        rClickMenu_gith = tk.Menu(self.output_gith, tearoff=0)
        rClickMenu_gith.add_command(label="Copy", 
                                    accelerator="Ctrl+C", 
                                    command=lambda: self.output_gith.event_generate('<Control-c>'))
        rClickMenu_gith.add_separator()
        rClickMenu_gith.add_command(label="Cut", 
                                    accelerator="Ctrl+X", 
                                    command=lambda: self.output_gith.event_generate('<Control-x>'))
        rClickMenu_gith.add_separator()
        rClickMenu_gith.add_command(label="Paste", 
                                    accelerator="Ctrl+V", 
                                    command=lambda: self.output_gith.event_generate('<Control-v>'))
    
        def show_rClickMenu_gith(event):
            rClickMenu_gith.tk_popup(event.x_root, event.y_root, 0)

        self.output_gith.bind("<Button-3>", show_rClickMenu_gith)
        
        
        return
        
        
    def docs_window(self): # new window definition
    
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title('Documentation')
        # self.new_window.geometry("500x500") 
        self.new_window.resizable(True, True)
        self.new_window.focus_force() # Focus on the docs window as soon as the window is opened.
        
        self.docs_width = 80
        self.docs_height = 30
        self.docs_text_widget = tk.Text(self.new_window, width=self.docs_width, height=self.docs_height, wrap=tk.WORD)
        self.docs_text_widget.configure(borderwidth=0, background='gray95')
        # self.docs_text_widget.configure(font=("Helvetica", 10))
        self.docs_text_widget.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Blue color text tag.
        blue_tag = "color-" + "blue"
        self.docs_text_widget.tag_configure(blue_tag, foreground="medium blue")
        
        self.docs_text_widget.delete('1.0', tk.END)
        self.docs_text_widget.insert(tk.END, str(
            "This is a small app for converting LaTeX code to a format readable by GitHub's Markdown using source URLs."+"\n\n"+\
            "It was inspired by the solutions provided by Alexander Rodin (username: a-rodin) at:"+"\n\n"+\
            "\thttps://gist.github.com/a-rodin/fef3f543412d6e1ec5b6cf55bf197d7b"+"\n\n"+\
            u"\u25A0"+' You can write your LaTeX formula in the frame under the label "Write yout LaTeX code:". '+\
            'Pressing the "Convert LaTeX code" left button under the LaTeX input frame a HTML code is generated. This code can be pasted into a GitHub README.md file so the desired formula can be generated. ' "\n"+\
            "It is asumed that the input is already in math mode. You can also start writing in the LaTeX frame as soon as the app is opened."+"\n\n"+\
            u"\u25A0"+' The frame under the "The HTML result is:" label is where the resulting HTML code will be shown. The code will have the following form:'+"\n\n"
            ))
        
        self.docs_text_widget.insert(tk.END, str(
            '<img src="https://render.githubusercontent.com/render/math?math=--Formatted formula here--">'+"\n\n"
            ), blue_tag)
        
        self.docs_text_widget.insert(tk.END, str(
            u"\u25A0"+' The frame under the "The GitHub URL result is:" label will show the URL for GitHub to render the math formula. '+\
            "You can paste this URL in the adress bar of your web browser to view the resulting formula. "+\
            "This URL is already inside the HTML code and has the following aspect:"+"\n\n"))
        
        self.docs_text_widget.insert(tk.END, str(
            "https://render.githubusercontent.com/render/math?math=--Formatted formula here--"+"\n\n"
            ), blue_tag)
        
        self.docs_text_widget.insert(tk.END, str(
            u"\u25A0"+" In this app you can also view the result from the URL if internet connection is available. "+\
            'Keeping the "View image" checkbutton below the input frame checked, the formula can ve viewed on '+\
            'the "Image:" canvas on the lower right.'+"\n\n"+\
            u"\u274F"+" For further reference on this application see the following GitHub repository:"+"\n\n"+\
            "\thttps://github.com/artmenlope/LaTeX-to-GitHub-app"+"\n\n"+\
            "This project is licensed under the terms of the MIT license."))
            
        
        # Docs right y-scrollbar
        self.root.docs_scroll_y = tk.Scrollbar(self.new_window, orient='vertical')
        self.docs_text_widget.config(yscrollcommand=self.root.docs_scroll_y.set)
        self.root.docs_scroll_y.config(command=self.docs_text_widget.yview)
        self.root.docs_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)    
        
        return 
    

#Setting up the GUI window
root = tk.Tk()
Application(root) 
root.mainloop()
