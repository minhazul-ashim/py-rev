class Singer :
    def __init__(self, album) :
        self.album = album;

    def canSing(self) :
        print(f"YES, CAN SING. {self.album} is made by him.");
    
class Painter :
    def __init__(self, name) :
        self.name = name;

    def canPaint(self) :
        print(f"YES, {self.name} CAN PAINT");

class Photographer :
    def __init__(self, camera) :
        self.camera = camera;

    def canTakePhoto(self) :
        print(f"YES, CAN TAKE GOOD PHOTOS with his {self.camera}");

class Artist(Singer, Painter, Photographer) :
    def __init__(self, album, name, camera, ability):
        Singer.__init__(self, album);
        Painter.__init__(self, name);
        Photographer.__init__(self, camera);
        self.ability = ability;
    
    def whatCanDo(self) :
        if(self.ability == "Singing") :
            self.canSing();
        elif (self.ability == "Painting") :
            self.canPaint();
        elif(self.ability == "Photography") :
            self.canTakePhoto();

artist = Artist("Album Meteora", "Dominic Toretto", "Canon", "Photography");
artist2 = Artist("Album Aushomapto", "Brian O Conner", "Nikon", "Painting");
artist3 = Artist("Album Obosheshe", "Riley Gibson", "Fujifilm", "Singing");

artist.whatCanDo();
artist2.whatCanDo();
artist3.whatCanDo();

