import tkinter as tk
root = tk.Tk()
from pytube import YouTube
l1=tk.Label(root,text='paste your youtube video link here \nto download video')
e1=tk.Entry(root)


def download_youtube_video(video_url, save_path='./'):
    try:
        # Create a YouTube object for the given URL
        yt = YouTube(video_url)

        # Get the highest resolution stream (you can customize this)
        stream = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        stream.download(output_path=save_path)

        l3=tk.Label(root,text=f"Video '{yt.title}' downloaded successfully to {save_path}")
        l3.grid(row=3,column=1)
    except Exception as e:
        l3=tk.Label(root,text=f"An error occurred: {str(e)}")
def download():
    l4=tk.Label(root,text="Thanks For DOWNLOAD ...")
    l4.grid(row=1,column=1)

    if __name__ == "__main__":
        youtube_url = e1.get()
        
        download_path = './'
        

        download_youtube_video(youtube_url, download_path)

b1=tk.Button(root,text='DOWNLOAD',command=download)
b1.grid(row=0,column=2)




l1.grid(row=0,column=0)
e1.grid(row=0,column=1)



root.mainloop()