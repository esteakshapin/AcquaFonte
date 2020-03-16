class myFileList(listofimgs):
    def __init__(self, listofimgs):
        self.myheldimgs = listofimgs

    def releaseimgs(self):
        return self.myheldimgs

    def addimg(self, imgtype):
        self.myheldimgs.append(imgtype)
