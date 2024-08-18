import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
from chat import get_response


# Name of the chatbot
bot_name = "Farzad"

class ChatScreen(tk.Canvas):
    def __init__(self, parent):
        # Initialize the Canvas widget
        super().__init__(parent, bg="#F4F5F7")

        # Set the bot's window name
        parent.title(bot_name)  # This sets the title of the Tk window
        
        # Calculate the position to center the window on the screen
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_co = int((screen_width / 2) - (680 / 2))
        y_co = int((screen_height / 2) - (750 / 2)) - 80
        parent.geometry(f"540x750+{x_co}+{y_co}")

        # Load and resize user image
        user_image = Image.open('images/user.png')  # Default user image path
        user_image = user_image.resize((40, 40), Image.LANCZOS)
        self.user_image = ImageTk.PhotoImage(user_image)

        # Load and resize group photo
        global group_photo
        group_photo = Image.open('images/favicon.png')
        group_photo = group_photo.resize((60, 60), Image.LANCZOS)
        group_photo = ImageTk.PhotoImage(group_photo)

        # Initialize attributes for the chat
        self.y = 140
        self.clients_online_labels = {}

        # Create and place a label for the bot's name
        tk.Label(self, text="   ", font="lucida 15 bold", bg="#2C99FF").place(x=4, y=30)
        tk.Label(self, text=bot_name, font="lucida 15 bold", padx=20, fg="#ffffff",
                 bg="#2C99FF", anchor="w", justify="left").place(x=95, y=30, relwidth=1)

        # Display the group photo
        self.create_image(60, 40, image=group_photo)

        # Create a frame to contain the chat area
        container = tk.Frame(self)
        container.place(x=40, y=120, width=450, height=550)
        self.canvas = tk.Canvas(container, bg="#595656")
        self.scrollable_frame = tk.Frame(self.canvas, bg="#595656")

        # Create a window in the canvas to hold the scrollable frame
        scrollable_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure scrolling region for the canvas
        def configure_scroll_region(e):
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        # Resize the scrollable window when the canvas resizes
        def resize_frame(e):
            self.canvas.itemconfig(scrollable_window, width=e.width)

        self.scrollable_frame.bind("<Configure>", configure_scroll_region)

        # Create and pack a vertical scrollbar
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(fill="both", expand=True)

        # Bind resize event and pack the canvas
        self.canvas.bind("<Configure>", resize_frame)

        # Create and place the send button
        send_button = tk.Button(self, text="Send", fg="#ffffff", font="lucida 11 bold", bg="#7d7d7d", padx=10,
                                relief="solid", bd=2, command=self.sent_message_format, height=1)
        send_button.place(x=400, y=680)

        # Create and place the text entry widget
        self.entry = tk.Text(self, font="lucida 10 bold", width=50, height=2,
                             highlightcolor="blue", highlightthickness=1)
        self.entry.place(x=38, y=680)

        # Set focus to the text entry widget
        self.entry.focus_set()

        # Add a welcome message to the chat area
        m_frame = tk.Frame(self.scrollable_frame, bg="#d9d5d4")
        t_label = tk.Label(m_frame, bg="#d9d5d4", text=datetime.now().strftime('%H:%M'), font="lucida 9 bold")
        t_label.pack()
        m_label = tk.Label(m_frame, wraplength=250, text=f"Welcome Stranger!",
                           font="lucida 10 bold", bg="#D5DCF6")
        m_label.pack(fill="x")
        m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

        # Pack the ChatScreen widget to fill the parent window
        self.pack(fill="both", expand=True)

    def sent_message_format(self, event=None):
        # Retrieve the message from the text entry widget
        message = self.entry.get('1.0', 'end-1c')

        if message:
            if event:
                message = message.strip()
            # Clear the text entry widget
            self.entry.delete("1.0", "end-1c")

            # Create a new frame for the sent message
            m_frame = tk.Frame(self.scrollable_frame, bg="#595656")
            m_frame.columnconfigure(0, weight=1)

            # Create and place time label
            t_label = tk.Label(m_frame, bg="#595656", fg="white", text=datetime.now().strftime('%H:%M'),
                               font="lucida 7 bold", justify="right", anchor="e")
            t_label.grid(row=0, column=0, padx=2, sticky="e")

            # Create and place message label
            m_label = tk.Label(m_frame, wraplength=250, text=message, fg="black", bg="#40C961",
                               font="lucida 9 bold", justify="left",
                               anchor="e")
            m_label.grid(row=1, column=0, padx=2, pady=2, sticky="e")

            # Create and place user image label
            i_label = tk.Label(m_frame, bg="#595656", image=self.user_image)
            i_label.image = self.user_image
            i_label.grid(row=0, column=1, rowspan=2, sticky="e")

            m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

            # Update the canvas and scroll to the bottom
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)

            # Schedule the bot message to appear after 1 second
            self.after(100, self.bot_message(message))

    def bot_message(self, msg):
        # Create a mock message for the bot response
        message = get_response(msg)

        # Load and resize bot image
        im = Image.open(f"images/favicon.png")
        im = im.resize((40, 40), Image.LANCZOS)
        im = ImageTk.PhotoImage(im)

        # Create a new frame for the bot's message
        m_frame = tk.Frame(self.scrollable_frame, bg="#595656")
        m_frame.columnconfigure(1, weight=1)

        # Create and place time label
        t_label = tk.Label(m_frame, bg="#595656", fg="white", text=datetime.now().strftime('%H:%M'), font="lucida 7 bold",
                           justify="left", anchor="w")
        t_label.grid(row=0, column=1, padx=2, sticky="w")

        # Create and place message label
        m_label = tk.Label(m_frame, wraplength=250, fg="black", bg="#c5c7c9", text=message, font="lucida 9 bold", justify="left",
                           anchor="w")
        m_label.grid(row=1, column=1, padx=2, pady=2, sticky="w")

        # Create and place bot image label
        i_label = tk.Label(m_frame, bg="#595656", image=im)
        i_label.image = im
        i_label.grid(row=0, column=0, rowspan=2)

        m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="w")

        # Update the canvas and scroll to the bottom
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    chat_screen = ChatScreen(root)
    root.mainloop()
