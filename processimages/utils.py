from PIL import Image, ExifTags

class ProcessImage:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
        try: 
            self.image = Image.open(self.image_path)
        except:
            raise ValueError("Issues with image")

    def _get_orientation(self):
        if self.image:
            exif = self.image.getexif()
            # exif is a dictionary and key for orientation is 274 (as per the EXIF standard)
            # another way is to use ExifTags
            # if exif:
            #     for key, value in exif.items():
            #         if key in ExifTags.TAGS and ExifTags.TAGS[key] == "Orientation":
            #             return exif[key]
            if exif and 274 in exif:
                return exif[274]
        return None


    def rotate(self):
        rotation_angles = {
            3: 180, 
            6: 270, 
            8: 90 
        }
        orientation = self._get_orientation()
        if orientation in rotation_angles:
            self.image = self.image.rotate(angle=rotation_angles[orientation], expand=True)
        return self


    def resize(self, new_size=(800, 800)):
        self.image.thumbnail(size=new_size, resample=Image.BICUBIC)
        return self


    def save(self):
        self.image.save(fp=self.image_path)
        self.image.close()
        return self


