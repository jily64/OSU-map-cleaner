import os
import json

with open("info.json", "r", encoding="utf-8") as f:
    data = json.load(f)
os.system('cls')
print("Made By jily64")
print("tg: @Oily_Oaff")
print("ds: oily_oaf")
a = input("\nPress Enter to start")

class OsuCleaner:
    def __init__(self, data):
        self.data = data
        self.all_dirs = os.listdir(data["path"])

    def clean_similar(self):
        print("\n---cleaning duplicates---\n")
        files = []
        for dir in self.all_dirs:
            for file in os.listdir(self.data["path"]+'/'+dir):
                if file.endswith(".osu"):
                    files.append(dir+"/"+file)

        last_file = None
        current_file = None
        count_dup = 0
        indicise = 0
        for i in files:
            try:
                last_file_text = None
                current_file_text = None
                last_file = files[indicise]
                current_file = files[indicise+1]
                with open(self.data["path"] + "/" + last_file) as f:
                    last_file_text = f.read()
                with open(self.data["path"] + "/" + current_file) as f:
                    current_file_text = f.read()

                if last_file_text == current_file_text:
                    os.remove(self.data["path"]+"/"+last_file)
                    #print(self.data["path"]+"/"+last_file)
                    count_dup +=1
                else:
                    pass
                indicise+=1
            except:
                pass
        if count_dup != 0:
            print(f"{count_dup} duplicates have been deleted")
        else:
            print("No duplicates found")

    def video_cleaner(self):
        video_count = 0
        print("\n---cleaning videos---\n")
        for dir in self.all_dirs:
            try:
                os.listdir(self.data["path"]+"/"+dir+" [no video]")
                for i in os.listdir(self.data["path"]+"/"+dir):
                    os.remove(self.data["path"]+"/"+dir+"/"+i)
                os.removedirs(self.data["path"]+"/"+dir)
                #os.remove(self.data["path"]+"/"+dir)
                video_count+=1
            except:
                pass

        if video_count != 0:
            print(f"{video_count} videos have been deleted")
        else:
            print("No videos found")


try:
    cleaner = OsuCleaner(data)
    if data["clean_similar_maps"]:
        cleaner.clean_similar()
    elif data["clear_video"]:
        cleaner.video_cleaner()
except Exception as e:
    print(e)

print("\nProgram finished\nThanks for using our soft!")
a = input("Press Enter to close this window")
