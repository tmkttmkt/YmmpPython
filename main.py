import json
from  func import *

#ymmpファイルはjson形式なのでモジュールを使って取り込める
class Ymmp:
    def Field(self):
        self.Layer={"#":0,"##":1,"###":2,"background1":3,"background1":4,"char1":6,"char2":7,"main":8,"sub":9,"char_sub1":11,"char_sub2":12,"title_big":13,"title_small":14}
        self.char_ryk=[]
    def __init__(self,name=""):
        self.data=crete()
        if name!="":
            with open(name, "r",encoding="utf-8-sig") as json_file:
                self.data = json.load(json_file)
        self.Field()
    def write(self,txt=""):
        if txt=="":
            txt="outfile"
        with open(txt, "w") as json_file:
            json.dump(self.data, json_file,indent=4)
    def SetFPS(self,i:int):
        self.data["Timeline"]["VideoInfo"]["FPS"]=i
    def SetWidth(self,i:int):
        self.data["Timeline"]["VideoInfo"]["Width"]=i
    def SetHeight(self,i:int):
        self.data["Timeline"]["VideoInfo"]["Height"]=i
    def SetLength(self,i:int):
        self.data["Timeline"]["Length"]=i
    def SetLength(self):
        return self.data["Timeline"]["Length"]
    def GetFPS(self):
        return self.data["Timeline"]["VideoInfo"]["FPS"]
    def GetWidth(self):
        return self.data["Timeline"]["VideoInfo"]["Width"]
    def GetHeight(self):
        return self.data["Timeline"]["VideoInfo"]["Height"]
    def AllSerifSlice(self,index:int,mae=True):
        if mae:
            for ob in self.data["Timeline"]["Items"]:
                if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                    ob["Serif"]=ob["Serif"][:index]
        else:
            for ob in self.data["Timeline"]["Items"]:
                if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                    ob["Serif"]=ob["Serif"][index:]
    def AllSerifReplace(self,be,af):
        for ob in self.data["Timeline"]["Items"]:
            if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                ob["Serif"]=ob["Serif"].replace(be,af)
    def AllTextSlice(self,index:int,mae=True):
        if mae:
            for ob in self.data["Timeline"]["Items"]:
                if "YukkuriMovieMaker.Project.Items.TextItem" in ob["$type"]:
                    ob["Serif"]=ob["Serif"][:index]
        else:
            for ob in self.data["Timeline"]["Items"]:
                if "YukkuriMovieMaker.Project.Items.TextItem" in ob["$type"]:
                    ob["Serif"]=ob["Serif"][index:]
    def AllTextReplace(self,be,af):
        for ob in self.data["Timeline"]["Items"]:
            if "YukkuriMovieMaker.Project.Items.TextItem" in ob["$type"]:
                ob["Serif"]=ob["Serif"].replace(be,af)
    def AllsetLayer(self,layer=0):
        voice_list=[]
        for ob in self.data["Timeline"]["Items"]:
            if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                voice_list.append(ob)
        voice_list = sorted(voice_list, key=lambda x: x["Frame"])
        frame=0
        for ob in voice_list:
            ob["Frame"]=frame
            frame+=ob["Length"]
            ob["Layer"]=layer
    def AllSerifCount(self,num,flg="IsHidden"):
        n=0
        for ob in self.data["Timeline"]["Items"]:
            if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                if num<count_char(ob["Serif"]):
                    ob[flg]=True
                    n+=1
                    print(n,"aut")
    def SearchSerif(self,txt):
        for ob in self.data["Timeline"]["Items"]:
            if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                if ob["Serif"]==txt:
                    return ob["CharacterName"]
        return None
    def PrintOut(self,dic,name):
        if dic!=None:
            lis=[]
            for ob in self.data["Timeline"]["Items"]:
                if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                    if ob["CharacterName"] in dic:
                        lis.append((ob["Serif"],dic[ob["CharacterName"]],ob["Frame"],ob["Length"]))
                if "YukkuriMovieMaker.Project.Items.TextItem" in ob["$type"]:
                    if "#" in ob["Text"]:
                        lis.append((ob["Text"],ob["Text"].count('#'),ob["Frame"],ob["Length"]))
            lis=sorted(lis, key=lambda x: (x[2],-x[3]))
            name=file_name(name,rast="md")
            with open(name, "w",encoding="utf-8") as file:
                for line in lis:
                    if str==type(line[1]):
                        file.write("{},{:x},{:x}:{}\n".format(line[1],line[2],line[3],line[0]))
                    elif int==type(line[1]):
                        file.write("{}:{:x},{:x}\n".format(line[0],line[1],line[2],line[3]))
        else:
            with open(name, "w",encoding="utf-8") as file:
                for ob in self.data["Timeline"]["Items"]:
                    if "YukkuriMovieMaker.Project.Items.VoiceItem" in ob["$type"]:
                        file.write(ob["Serif"])

    def PrintIn(self,dic,bc,name,CVF=craete_Voice,CTF=craete_Text):
        name=file_name(name,rast="md")
        with open(name, "r",encoding="utf-8") as file:
            list=file.readlines()
            fps=0
            sarpe_flgs=[]
            for line in list:
                line=line[:-1]
                if "#" in line:
                    layer=line.count("#")-1
                    flg=False
                    for sarpe_flg in sarpe_flgs:
                        if layer==sarpe_flg[2]:
                            self.data["Timeline"]["Items"].append(CTF(sarpe_flg[1],frame=sarpe_flg[0],length=fps-sarpe_flg[0],layer=sarpe_flg[2]))
                            del_flg=sarpe_flg
                            flg=True
                            break
                    if flg:
                        sarpe_flgs.remove(del_flg)
                    if ":" in line:
                        mae=line[:line.find(":")]
                        usi=line[line.find(":")+1:]
                        frame,length=usi.split(",")
                        frame=int(frame,16)
                        length=int(length,16)
                    else:
                        sarpe_flgs.append((fps,line,layer))
                        continue
                    from_flg=False
                    for ob in self.data["Timeline"]["Items"]:
                        if "YukkuriMovieMaker.Project.Items.TextItem" in ob["$type"]:
                            if ob["Layer"]==layer:
                                if frame==ob["Frame"] and length==ob["Length"]:
                                    ob["Text"]=mae
                                    from_flg=True
                                    break
                    if not from_flg:
                        self.data["Timeline"]["Items"].append(CTF(mae,frame=frame,length=length,layer=layer))
                else:
                    if ":" in line:
                        mae=line[:line.find(":")]
                        usi=line[line.find(":")+1:]
                        char,frame,length=mae.split(",")
                        frame=int(frame,16)
                        length=int(length,16)
                        from_flg=False
                        for ob in self.data["Timeline"]["Items"]:
                            if "YukkuriMovieMaker.Project.Items.TextItem" in ob["$type"]:
                                if frame==ob["Frame"] and length==ob["Length"]:
                                    if char in dic:
                                        if ob["CharacterName"]==dic[char]:
                                            ob["Frame"]=fps
                                            fps+=length
                                            ob["Serif"]=usi
                                            from_flg=True
                                            break
                                    else:
                                        if ob["CharacterName"]==char:
                                            ob["Frame"]=fps
                                            fps+=length
                                            ob["Serif"]=usi
                                            from_flg=True
                                            break

                        if not from_flg:
                            if char in dic:
                                self.data["Timeline"]["Items"].append(CVF(usi,dic[char],frame=fps,length=length,layer=self.Layer["main"]))
                                fps+=length
                            else:
                                self.data["Timeline"]["Items"].append(CVF(usi,char,frame=fps,length=length,layer=self.Layer["main"]))
                                fps+=length
                    else:
                        self.data["Timeline"]["Items"].append(CVF(line,bc,frame=fps,length=10,layer=self.Layer["main"]))
                        fps+=10

                    
            for sarpe_flg in sarpe_flgs:
                 self.data["Timeline"]["Items"].append(CTF(sarpe_flg[1],frame=sarpe_flg[0],length=fps-sarpe_flg[0],layer=sarpe_flg[2]))
                        




                


#ymmpの台本機能に成形する(ほぼキャラクター名の追加)
class Daihon:
    def __init__(self,file,outfile="output",char="ゆっくり霊夢 (解)") -> None:
        self.file=file_name(file)
        self.output=outfile
        self.charc=char
    def set_output(self,txt):
        self.output=txt
    def craete(self,upfile=None):
        if upfile==None:    
            with open(self.file,"r",encoding='utf-8') as file:
                with open(self.output+".csv","w") as exle:
                    lines=file.readlines()
                    for line in lines:
                        if not("#" in line)and not("#" in line):
                            w=self.charc+","+line
                            exle.write(w)
        else:
            y=Ymmp(name=upfile)
            with open(self.file,"r",encoding='utf-8') as file:
                with open(self.output+".csv","w") as exle:
                    lines=file.readlines()
                    for line in lines:
                        char=y.SearchSerif(line)
                        if not("#" in line)and not("#" in line):
                            if char!=None:
                                w=char+","+line
                            else:
                                w=self.charc+","+line
                            exle.write(w)




