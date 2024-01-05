from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import time
import os
import assemblyai as aai
from moviepy.editor import VideoFileClip

class SubGenApp:
    # Load images and other resources
    img0 = PhotoImage(file="img0.png")

    def __init__(self):
        self.w = Tk()
        self.api_key = "d54427ea7f1740d1b491b67ad5d02d98"
        self.audio_path = None
        self.output_directory = None

        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.w.geometry("427x250")
        self.w.overrideredirect(1)  # for hiding titlebar

    def create_widgets(self):
        # ... Your existing code for widget creation ...

        # Example button creation:
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.transcribe_button_click,
            relief="flat"
        )
        b0.place(x=676.0, y=453.0, width=130, height=51)

    def transcribe_button_click(self):
        audio_path_fn = self.audio_path
        print(audio_path_fn)

        if self.audio_path:
            output_dir = self.output_directory

            # Check if the input file is a video
            is_video = False
            if audio_path_fn.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                is_video = True

            if is_video:
                video_clip = VideoFileClip(audio_path_fn)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(
                    os.path.join(output_dir, f'{os.path.splitext(os.path.basename(audio_path_fn))[0]}.wav'))
                audio_path_fn = os.path.join(output_dir, f'{os.path.splitext(os.path.basename(audio_path_fn))[0]}.wav')

            transcriber = self.AudioTranscriber(self.api_key)
            output_file_path = transcriber.transcribe_audio(audio_path_fn, output_dir)
            print(f"Transcription saved to: {output_file_path}")
            if is_video:
                os.remove(audio_path_fn)

            self.show_success_message()

    def show_success_message(self):
        messagebox.showinfo("Success", "Transcription Successful")

    def pick_file(self, event):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.audio_path = file_path
            print("Selected File:", file_path)
            l1.config(text=self.truncate_text(file_path, 40))

    def pick_path(self, event):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.output_directory = dir_path
            print("Selected Path:", dir_path)
            l0.config(text=self.truncate_text(dir_path, 40))

    def splash_time(self, image_a, image_b, l1x, l2x, l3x, l4x, y, Range):
        # ... Your existing code for the splash animation ...
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

    def run(self):
        self.w.destroy()
        self.new_win()
        self.w.mainloop()

    def new_win(self):
        # Load images and other resources
        img0 = PhotoImage(file="img0.png")

            # Function to handle the transcription process
        def transcribe_button_click():
            audio_path_fn = audio_path
            print(audio_path_fn)
            

            if audio_path:
                output_dir = output_directory
                # You can specify the output directory here


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
                    audio_path_fn, output_dir)
                print(f"Transcription saved to: {output_file_path}")
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

        # Function to handle directory selection using filedialog (used for button command)
        def pick_path_btn():
            dir_path = filedialog.askdirectory()
            if dir_path:
                global output_directory
                output_directory = dir_path
                print("Selected Path:", dir_path)
                l0.config(text=truncate_text(dir_path, max_length))
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
            # ... Your existing code for the second window ...

    class AudioTranscriber:
        def __init__(self, api_key):
            aai.settings.api_key = api_key
            self.transcriber = aai.Transcriber()

        def transcribe_audio(self, audio_path, output_dir="."):
            audio_name = os.path.splitext(os.path.basename(audio_path))[0]
            transcript = self.transcriber.transcribe(audio_path)
            srt_subtitles = transcript.export_subtitles_srt()
            output_file_path = os.path.join(output_dir, f"{audio_name}.srt")

            with open(output_file_path, "w") as srt_file:
                srt_file.write(srt_subtitles)

            return output_file_path

        # ... Add other methods as needed ...



# Create the app and run it
app = SubGenApp()
app.run()
