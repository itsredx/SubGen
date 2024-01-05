# importing libraries
from tkinter import *
import tkinter as tk
from tkinter import font, filedialog, messagebox
from PIL import ImageTk, Image
import time
import os
import assemblyai as aai
import time
from moviepy.editor import VideoFileClip


# API key for audio transcription
api_key = "d54427ea7f1740d1b491b67ad5d02d98"


w = Tk()

# Global variables to store the selected audio file and output directory
audio_path = None
output_directory = None


# Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %
           (width_of_window, height_of_window, x_coordinate, y_coordinate))
# w.configure(bg='#ED1B76')
w.overrideredirect(1)  # for hiding titlebar

#Custom Message Box
def message_box():
    M = Tk()
    # Using piece of code from old splash screen
    width_of_window = 427
    height_of_window = 200
    screen_width = M.winfo_screenwidth()
    screen_height = M.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    M.configure(bg='#A065CD')
    M.geometry("%dx%d+%d+%d" %
           (width_of_window, height_of_window, x_coordinate, y_coordinate))
    # M.configure(bg='#ED1B76')
    M.overrideredirect(1)
    
    def des():
        M.destroy()
    
    msg = Label(M,text='Subtitle Generated Successfully', fg='white', bg='#A065CD')
    msg.configure(font=("Game Of Squids", 14, "bold"))
    msg.place(x=45, y=50)
    print(msg.winfo_width)
    Button(M, text='Ok',
        borderwidth=0,
        fg='white',
        bg='#A065CD',
        highlightthickness=0,
        command=des,
        relief="flat",
        width=6).place(x=180, y=170)

    
     
    
# new window to open
def new_win():
    api_key = "d54427ea7f1740d1b491b67ad5d02d98"

    # Create a class for handling audio transcription
    class AudioTranscriber:
        def __init__(self, api_key):
            aai.settings.api_key = api_key
            self.transcriber = aai.Transcriber()

        def transcribe_audio(self, audio_path,active_button_value, output_dir="."):
            print('All good from AudioTranscriber')

            # Get the base name of the audio file without extension
            audio_name = os.path.splitext(os.path.basename(audio_path))[0]

            # Transcribe the audio
            transcript = self.transcriber.transcribe(audio_path)

            print(active_button_value)

            # Conditional logic for generating different output formats
            if active_button_value == 1:  # SRT format
                output_format = "srt"
            elif active_button_value == 2:  # VTT format
                output_format = "vtt"
            else:  # Default to plain text format
                output_format = "txt"

            # Generate and save the output file
            if output_format == "srt":
                subtitles = transcript.export_subtitles_srt()
                output_file_path = os.path.join(output_dir, f"{audio_name}.srt")
            elif output_format == "vtt":
                subtitles = transcript.export_subtitles_vtt()  # Assuming a method for VTT export exists
                output_file_path = os.path.join(output_dir, f"{audio_name}.vtt")
            else:
                subtitles = transcript.text  # Assuming plain text transcript is available
                output_file_path = os.path.join(output_dir, f"{audio_name}.txt")

            with open(output_file_path, "w") as output_file:
                output_file.write(subtitles)

            return output_file_path


    
    
    # Function to handle the transcription process
    def transcribe_button_click():
        audio_path_fn = audio_path
        print(audio_path_fn)
        

        if audio_path:
            output_dir = output_directory
              # You can specify the output directory here
            global button_value
            print(button_value)


            # Check if the input file is a video
            is_video = False
            # Add more video extensions if needed
            if audio_path_fn.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                is_video = True

            if is_video:
                
                # Get the base name of the audio file without extension
                audio_name = os.path.splitext(os.path.basename(audio_path_fn))[0]
                # Convert the video to audio
                
                video_clip = VideoFileClip(audio_path_fn)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(
                    os.path.join(output_dir, f'{audio_name}.wav'))
                audio_path_fn = os.path.join(output_dir, f'{audio_name}.wav')
                
             

                # Transcribe the audio
            # Replace 'api_key' with your actual API key
            transcriber = AudioTranscriber(api_key)
            output_file_path = transcriber.transcribe_audio(
                audio_path_fn, button_value, output_dir)
            print(f"Transcription saved to: {output_file_path}")
            #print(active_button_value)
            if is_video:
                # Delete the temporary audio file
                os.remove(audio_path_fn)
            
            message_box()
                
            


            

    # Function to show a success message using a messagebox
    def show_success_message():
        messagebox.showinfo("Success", "Transcription Successful")

    # Function to center the Tkinter window on the screen

    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    # Function to truncate text and add ellipsis if it's too long
    def truncate_text(text, max_length):
        print(len(text))
        if len(text) > max_length:
            return "..." + text[-max_length:]
        else:
            return text

    # Maximum length for text truncation
    max_length = 40

    # Function to handle file selection using filedialog
    def pick_file(event):
        file_path = filedialog.askopenfilename()
        if file_path:
            global audio_path
            audio_path = file_path
            print("Selected File:", file_path)
            l1.config(text=truncate_text(file_path, max_length))

    # Function to handle file selection using filedialog (used for button command)
    def pick_file_btn():
        file_path = filedialog.askopenfilename()
        if file_path:
            global audio_path
            audio_path = file_path
            print("Selected File:", file_path)
            l1.config(text=truncate_text(file_path, max_length))

    # Function to handle directory selection using filedialog
    def pick_path(event):
        dir_path = filedialog.askdirectory()
        if dir_path:
            global output_directory
            output_directory = dir_path
            print("Selected Path:", dir_path)
            l0.config(text=truncate_text(dir_path, max_length))
    def btn_clicked():
        print("Button Clicked")

    # Function to handle directory selection using filedialog (used for button command)
    def pick_path_btn():
        dir_path = filedialog.askdirectory()
        if dir_path:
            global output_directory
            output_directory = dir_path
            print("Selected Path:", dir_path)
            l0.config(text=truncate_text(dir_path, max_length))

    def create_toggle_button(root, image1, image2, value):
        """Creates a toggle button with image switching and state tracking."""
        photo1 = tk.PhotoImage(file=image1)
        photo2 = tk.PhotoImage(file=image2)
        button = tk.Button(
            root,
            image=photo1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: toggle_button(button, photo1, photo2, value)
        )
        button.image_on = photo1
        button.image_off = photo2
        button.value = value
        return button

    def toggle_button(button, image_on, image_off, value):
        global button_value
        button_value = value
        """Toggles the button's image and updates other buttons accordingly."""
        if button.config('image')[-1] == image_on:
            button.config(image=image_off)
            global active_button_value
            active_button_value = value
            print("Active Value:" + str(active_button_value))
        else:
            button.config(image=image_on)
            active_button_value = value
            print("Active Value:" + str(active_button_value))
        

            # Set other buttons to "off" state
            for other_button in toggle_buttons:
                if other_button != button:
                    other_button.config(image=other_button.image_off)
            
    # Create the main Tkinter window
    window = Tk()

    # Center the window on the screen
    center_window(window, 1000, 600)

    # Set window title and background color
    window.title("SubGen")
    window.configure(bg="#a065cd")

    # Create a Canvas for additional layout elements
    canvas = Canvas(
        window,
        bg="#a065cd",
        height=600,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    # Load images for buttons
    background_img = PhotoImage(file="background.png")
    background = canvas.create_image(
        467.0,
        300.0,
        image=background_img)
    img0 = PhotoImage(file="img0.png")
    img1 = PhotoImage(file="img1.png")
    img2 = PhotoImage(file="img2.png")
    image_a = ImageTk.PhotoImage(file='c2.png')
    image_b = ImageTk.PhotoImage(file='c1.png')

    # Create a button to trigger audio transcription
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=transcribe_button_click,
        relief="flat")
    b0.place(
        x=676.0, y=453.0,
        width=130,
        height=51)

    # Create a button to select an audio file
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=pick_file_btn,
        relief="flat")
    b1.place(
        x=566.0, y=231.0,
        width=354,
        height=51)

    toggle_buttons = []
    

    # Create and place the toggle buttons
    button1 = create_toggle_button(window, "img02.png", "img01.png", 1)
    button1.place(x = 767, y = 143,
        width = 73,
        height = 28)
    toggle_buttons.append(button1)

    button2 = create_toggle_button(window, "img04.png", "img03.png", 2)
    button2.place(x = 684, y = 143,
        width = 73,
        height = 28)
    toggle_buttons.append(button2)

    button3 = create_toggle_button(window, "img05.png", "img06.png", 3)
    button3.place(x = 601, y = 143,
        width = 73,
        height = 28)
    toggle_buttons.append(button3)

    # Set the initial state of the first button to "on"
    toggle_buttons[0].config(image=toggle_buttons[0].image_on)
    toggle_buttons[1].config(image=toggle_buttons[1].image_off)
    toggle_buttons[2].config(image=toggle_buttons[2].image_off)
    active_button_value = toggle_buttons[0].value
    print(active_button_value)

    # Create a button to select an output directory
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=pick_path_btn,
        relief="flat")
    b2.place(
        x=561.0, y=340.0,
        width=355,
        height=51)

    img6 = PhotoImage(file = f"img6.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b6.place(
        x = 929, y = 536,
        width = 44,
        height = 44)

    # Create labels to display selected file and path
    l0 = Label(
        text='',
        bg='#CC96F5',
        justify="left",
        anchor="w",
        fg='white',
        font=("Arial", 10))
    l0.place(x=583.0, y=350.0,
             width=280,
             height=30)
    l0.bind("<Button-1>", pick_path)

    l1 = Label(
        text='',
        bg='#CC96F5',
        justify="left",
        anchor="w",
        fg='white',
        font=("Arial", 10))
    l1.place(x=583.0, y=241.0,
             width=280,
             height=30)
    l1.bind("<Button-1>", pick_file)

    # animate_labels(window, image_a, image_b, 708, 728, 748, 768, 410, Range)

    # Make the window non-resizable
    window.resizable(False, False)

    # Start the Tkinter event loop
    window.mainloop()


Frame(w, width=427, height=250, bg='#A065CD').place(x=0, y=0)
label1 = Label(w, text='SUBGEN', fg='white', bg='#A065CD')  # decorate it
# You need to install this font in your PC or try another one
label1.configure(font=("Game Of Squids", 24, "bold"))
label1.place(x=140, y=90)

label2 = Label(w, text='Loading...', fg='white', bg='#A065CD')  # decorate it
label2.configure(font=("Calibri", 10))
label2.place(x=8, y=228)


# making animation

image_a = ImageTk.PhotoImage(Image.open('c2.png'))
image_b = ImageTk.PhotoImage(Image.open('c1.png'))
image_1 = ImageTk.PhotoImage(Image.open('d1.png'))
image_2 = ImageTk.PhotoImage(Image.open('d2.png'))
image_3 = ImageTk.PhotoImage(Image.open('d3.png'))
image_4 = ImageTk.PhotoImage(Image.open('d4.png'))
image_5 = ImageTk.PhotoImage(Image.open('d5.png'))

d1 = Label(w, image=image_1, border=0, relief=SUNKEN,
           bg='#A065CD').place(x=15, y=125)
d2 = Label(w, image=image_2, border=0, relief=SUNKEN,
           bg='#A065CD').place(x=0, y=10)
d3 = Label(w, image=image_3, border=0, relief=SUNKEN,
           bg='#A065CD').place(x=285, y=180)
d4 = Label(w, image=image_4, border=0, relief=SUNKEN,
           bg='#A065CD').place(x=350, y=0)
d5 = Label(w, image=image_5, border=0, relief=SUNKEN,
           bg='#A065CD').place(x=180, y=-10)


def splash_time(w, image_a, image_b, l1x, l2x, l3x, l4x, y, Range):
    for i in range(Range):  # 5 loops
        l1 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=l1x, y=y)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l2x, y=y)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l3x, y=y)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l4x, y=y)
        w.update_idletasks()
        time.sleep(0.2)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l1x, y=y)
        l2 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=l2x, y=y)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l3x, y=y)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l4x, y=y)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l1x, y=y)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l2x, y=y)
        l3 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=l3x, y=y)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l4x, y=y)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l1x, y=y)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l2x, y=y)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=l3x, y=y)
        l4 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=l4x, y=y)
        w.update_idletasks()
        time.sleep(0.5)


splash_time(w, image_a, image_b, 180, 200, 220, 240, 145, 3)




w.destroy()
new_win()
w.mainloop()
