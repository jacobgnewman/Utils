import sys
from youtube_transcript_api import YouTubeTranscriptApi
video_id = sys.argv[1]
vt = YouTubeTranscriptApi.get_transcript(video_id)
dialog =  " ".join(list(map(lambda x: x["text"], vt)))
print(dialog)
