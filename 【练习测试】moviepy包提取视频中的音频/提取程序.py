def pause():
	from os import system
	system("pause")
输入文件名 = "Frozen World.mp4"
输出文件名 = "Frozen World.mp3"

print("开始生成")
print("")
print("")
print("-----------------------------------------------")
print("")
print("")
import moviepy.editor

视频 = moviepy.editor.VideoFileClip(输入文件名)
音频 = 视频.audio
音频.write_audiofile(输出文件名)

print("")
print("")
print("-----------------------------------------------")
print("")
print("")
pause()