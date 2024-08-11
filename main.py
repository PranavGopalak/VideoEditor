from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load your videos
clip1 = VideoFileClip("Assets/video1.mp4")
clip2 = VideoFileClip("Assets/video2.mp4")

# Define the duration of the crossfade transition (in seconds)
crossfade_duration = 2  # for example, 2 seconds

# Apply crossfadein effect to the second clip
clip2 = clip2.crossfadein(crossfade_duration)

# Combine the videos with a crossfade transition
combined = concatenate_videoclips([clip1, clip2], method="compose", padding=-crossfade_duration)

# Export the combined video
combined.write_videofile("result.mp4", codec="libx264", fps=24)
