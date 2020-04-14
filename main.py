from tkinter import *
import tkinter.font as font
import random
from tkinter import messagebox as mb



class GameSetting:

    INSTANCE = None

    @staticmethod
    def getInstance():
        if GameSetting.INSTANCE == None:
            GameSetting()
        
        return GameSetting.INSTANCE
    
    def __init__(self):
        self.pBoard = 30
        self.lBoard = 10
        self.pKotak = 40
        self.lebarPintuKeluar = 3
        self.buildMatrix()
        GameSetting.INSTANCE = self

    def buildMatrix(self):
        self.matrix = [[0 for x in range(self.pBoard)] for y in range(self.lBoard)]
        self.generateBoard()
    
    def generateBoard(self):
        # pagar atas bawah
        for i in range(self.pBoard):
            self.matrix[0][i]=1
            self.matrix[self.lBoard-1][i]=1
        
        # pagar kiri kanan
        for i in range(self.lBoard):
            self.matrix[i][0]=1
            self.matrix[i][self.pBoard-1]=1
        
        # pintu keluar
        self.pintu = random.randint(1, self.lBoard - self.lebarPintuKeluar-1)

        # buat halangan
        for y in range(1,self.lBoard-1):
            for x in range(1, self.pBoard-1):
                if x==1 and y == 1:
                    continue
        
                halangan = random.randint(1, 20)
                if(halangan%5==0):
                    """
                    #case 1
                    temp_x = x-1
                    temp_y = y-1

                    if ( temp_x != 0 and temp_x != self.pBoard-1 and temp_y != 0 and temp_y != self.lBoard-1 ) and self.matrix[temp_y][temp_x]==1:
                        continue
                    
                     #case 2
                    temp_x = x+1
                    temp_y = y-1

                    if (temp_x != 0 and temp_x != self.pBoard-1 and temp_y != 0 and temp_y != self.lBoard-1) and self.matrix[temp_y][temp_x]==1:
                        continue

                     #case 3
                    temp_x = x-1
                    temp_y = y+1

                    if (temp_x != 0 and temp_x != self.pBoard-1 and temp_y != 0 and temp_y != self.lBoard-1) and self.matrix[temp_y][temp_x]==1:
                        continue

                    #case 4
                    temp_x = x-1
                    temp_y = y+1

                    if (temp_x != 0 and temp_x != self.pBoard-1 and temp_y != 0 and temp_y != self.lBoard-1) and self.matrix[temp_y][temp_x]==1:
                        continue
                    """
                    self.matrix[y][x]=1

        for i in range(self.lebarPintuKeluar):
            self.matrix[self.pintu+i][self.pBoard-1]=2



class board(Frame):
    INSTANCE = None

    @staticmethod
    def getInstance():
        if board.INSTANCE == None:
            board()
        
        return board.INSTANCE
    
    def __init__(self):
        pass

    def __init__(self, root):
        super().__init__()
        board.INSTANCE = self
        self.master.title("Shapes")
        self.root = root
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.bind("<Button-1>", self.callback)
        self.draw()
        self.canvas.pack(fill=BOTH, expand=1)
       
    
    def callback(self, event):
        temp_x = int((event.x)/GameSetting.getInstance().pKotak)
        temp_y = int((event.y)/GameSetting.getInstance().pKotak)
        player.getInstance().restart(temp_x, temp_y)
        print("ok")
    
    def draw(self):

        panjang_kotak = GameSetting.getInstance().pKotak    
        for y in range(GameSetting.getInstance().lBoard):
            for x in range(GameSetting.getInstance().pBoard):
                if GameSetting.getInstance().matrix[y][x]==1:
                    self.canvas.create_rectangle(x*panjang_kotak, y*panjang_kotak, x*panjang_kotak+panjang_kotak,  y*panjang_kotak+panjang_kotak, outline="#f11", fill="#f50", width=2)
                elif GameSetting.getInstance().matrix[y][x]==0 :
                    self.canvas.create_rectangle(x*panjang_kotak, y*panjang_kotak, x*panjang_kotak+panjang_kotak,  y*panjang_kotak+panjang_kotak, outline="#f11", fill="#05f", width=2)
                else:
                    self.canvas.create_rectangle(x*panjang_kotak, y*panjang_kotak, x*panjang_kotak+panjang_kotak,  y*panjang_kotak+panjang_kotak, outline="#f11", fill="green", width=2)
                
        player.getInstance().redraw()
        self.canvas.pack(fill=BOTH, expand=1)


class player:
    INSTANCE = None

    @staticmethod
    def getInstance():
        if player.INSTANCE == None:
            player()
        return player.INSTANCE

    def __init__(self):
        self.x = 1
        self.y = 1
        self.playing = False
        self.count = 0
        self.fps = 15
        self.canvas =  board.getInstance().canvas
        self.circle = self.canvas.create_rectangle(self.x * GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4) , self.y * GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4), self.x *GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4)*3, self.y*GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4)*3, fill="black")
        player.INSTANCE = self

    
    def redraw(self):
        self.x = 1
        self.y = 1
        self.circle = self.canvas.create_rectangle(self.x * GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4) , self.y * GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4), self.x *GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4)*3, self.y*GameSetting.getInstance().pKotak + int(GameSetting.getInstance().pKotak/4)*3, fill="black")
     

    def restart(self, x =None, y=None):
        if x==None or y ==None:
            pass
        elif GameSetting.getInstance().matrix[y][x]==0:
            self.canvas.move(self.circle, (x-self.x)*GameSetting.getInstance().pKotak, (y-self.y)*GameSetting.getInstance().pKotak)
            self.x = x
            self.y = y
        else:
            x = 1
            y = 1
            self.canvas.move(self.circle, (x-self.x)*GameSetting.getInstance().pKotak, (y-self.y)*GameSetting.getInstance().pKotak)
            self.x = 1
            self.y = 1

        self.dp = [[False for x in range(GameSetting.getInstance().pBoard)] for y in range(GameSetting.getInstance().lBoard)]
        self.dp_val = [[(False, 0) for x in range(GameSetting.getInstance().pBoard)] for y in range(GameSetting.getInstance().lBoard)]
        self.gerak = [[0 for x in range(GameSetting.getInstance().pBoard)] for y in range(GameSetting.getInstance().lBoard)]
    
    def stop(self):
        self.playing = False
        self.count = 0
    
    def play(self):
        
        posible, res = self.cari_jalan(self.y, self.x)
        if posible == False:
            mb.showerror("UDAH NYERAH AJA WKWK", "PATH GAK MUNGKIN BISA SAMPAI FINISH WKWKWWK")
            return

        print("possible : "+str(posible)+" "+str(res))
        self.playing = True
        for y in range(GameSetting.getInstance().lBoard):
            for x in range(GameSetting.getInstance().pBoard):
                print(self.gerak[y][x], end=" ")
            print("\n")
            


    def update(self):
        if self.playing == False :
            return
        self.count += 1
        if self.gerak[self.y][self.x] == 1:
            if self.count%self.fps==0:
                self.y -= 1
            self.canvas.move(self.circle, 0, -1*GameSetting.getInstance().pKotak/self.fps)
        elif self.gerak[self.y][self.x] == 2:
            if self.count%self.fps==0:
                self.y -= 1
                self.x += 1
            self.canvas.move(self.circle, GameSetting.getInstance().pKotak/self.fps, -1*GameSetting.getInstance().pKotak/self.fps)
        elif self.gerak[self.y][self.x] == 3:
            if self.count%self.fps==0:
                self.x+=1
            self.canvas.move(self.circle, GameSetting.getInstance().pKotak/self.fps, 0)
        elif self.gerak[self.y][self.x] == 4:
            if self.count%self.fps==0:
                self.y += 1
                self.x += 1
            self.canvas.move(self.circle, GameSetting.getInstance().pKotak/self.fps, GameSetting.getInstance().pKotak/self.fps)
        elif self.gerak[self.y][self.x] == 5:
            if self.count%self.fps==0:
                self.y += 1
            self.canvas.move(self.circle, 0, GameSetting.getInstance().pKotak/self.fps)
        elif self.gerak[self.y][self.x] == 6:
            if self.count%self.fps==0:
                self.y += 1
                self.x -= 1
            self.canvas.move(self.circle, GameSetting.getInstance().pKotak*-1/self.fps, GameSetting.getInstance().pKotak/self.fps)
        elif self.gerak[self.y][self.x] == 7:
            if self.count%self.fps==0:
                self.x -= 1
            self.canvas.move(self.circle, GameSetting.getInstance().pKotak*-1/self.fps, 0)
        elif self.gerak[self.y][self.x] == 8:
            if self.count%self.fps==0:
                self.y -= 1
                self.x -= 1
            self.canvas.move(self.circle, GameSetting.getInstance().pKotak*-1/self.fps, -1*GameSetting.getInstance().pKotak/self.fps)
         
        print("x :"+str(self.x) + " y :"+str(self.y))
        
        if self.y >= GameSetting.getInstance().pintu and self.y<GameSetting.getInstance().pintu+GameSetting.getInstance().lebarPintuKeluar and self.x == GameSetting.getInstance().pBoard-1:
            self.stop()        
        
    
    def cari_jalan(self, start_y, start_x):

        if start_y>= GameSetting.getInstance().pintu and start_y< (GameSetting.getInstance().pintu + GameSetting.getInstance().lebarPintuKeluar) and start_x==GameSetting.getInstance().pBoard-1:
            self.dp[start_y][start_x]= True
            return (True, 1)
        elif start_x<1 or start_x>=GameSetting.getInstance().pBoard-1 or start_y<1 or start_y>= GameSetting.getInstance().lBoard-1 or GameSetting.getInstance().matrix[start_y][start_x]==1 :
            return (False, 1000000)
        else:
            if self.dp[start_y][start_x] : 
                return self.dp_val[start_y][start_x]

            self.dp[start_y][start_x]= True
            p_atas = GameSetting.getInstance().matrix[start_y-1][start_x]
            p_kanan =  GameSetting.getInstance().matrix[start_y][start_x+1]
            p_bawah =  GameSetting.getInstance().matrix[start_y+1][start_x]
            p_kiri =  GameSetting.getInstance().matrix[start_y][start_x-1]

            best = 1000000
            best_possible = False
            arah = 1
            (possible, res) = self.cari_jalan(start_y-1, start_x)
            if res < best and possible:
                arah=1
                best=res
                best_possible = True
                
            if p_atas!=1 and p_kanan!=1 :
                (possible, res) = self.cari_jalan(start_y-1, start_x+1)
                if res < best and possible:
                    arah=2
                    best=res
                    best_possible = True

            (possible, res) = self.cari_jalan(start_y, start_x+1)
            if res < best and possible:
                arah=3
                best=res
                best_possible = True
            
            if p_bawah!=1 and p_kanan!=1 :
                (possible, res) = self.cari_jalan(start_y+1, start_x+1)
                if res < best and possible:
                    arah=4
                    best=res
                    best_possible = True

            (possible, res) = self.cari_jalan(start_y+1, start_x)
            if res < best and possible:
                arah=5
                best=res
                best_possible = True
            
            if p_bawah!=1 and p_kiri!=1 :
                (possible, res) = self.cari_jalan(start_y+1, start_x-1)
                if res < best and possible:
                    arah=6
                    best=res
                    best_possible = True
            
            (possible, res) = self.cari_jalan(start_y, start_x-1)
            if res < best and possible:
                arah=7
                best=res
                best_possible = True
            
            if p_atas!=1 and p_kiri!=1 :
                (possible, res) = self.cari_jalan(start_y-1, start_x-1)
                if res < best and possible:
                    arah=8
                    best=res
                    best_possible = True
           
            
            self.dp_val[start_y][start_x] = (best_possible, best + 1)
            self.gerak[start_y][start_x]  = arah

            return (best_possible, best + 1)

class Game:

    def __init__(self, root):
        panjang = GameSetting.getInstance().pBoard*GameSetting.getInstance().pKotak 
        lebar = GameSetting.getInstance().lBoard*GameSetting.getInstance().pKotak + 100
        root.geometry(str(panjang)+"x"+str(lebar))
        myFont = font.Font(size=25)

        self.root = root
        
        self.playingButton = Button(root, text='MULAI', width=int(panjang/3), command=self.mulai)
        self.playingButton["font"]=myFont
        self.playingButton.pack()
        self.playingButton.place(x=0, y=lebar-100, height=100, width=int(panjang/3))

        self.acakButton = Button(root, text='ACAK', width=int(panjang/3), command=self.acak)
        self.acakButton["font"]=myFont
        self.acakButton.pack()
        self.acakButton.place(x=int(panjang/3), y=lebar-100, height=100, width=int(panjang/3))

        self.stopButton = Button(root, text='STOP', width=int(panjang/3), command=self.stop)
        self.stopButton["font"]=myFont
        self.stopButton.pack()
        self.stopButton.place(x=int(panjang/3)*2, y=lebar-100, height=100, width=int(panjang/3))
    
    def mulai(self):
        player.getInstance().restart()
        player.getInstance().play()
    
    def stop(self):
        player.getInstance().stop()
    
    def acak(self):
        GameSetting.getInstance().buildMatrix()
        board.getInstance().draw()
    
    def update(self):
        player.getInstance().update()
        self.root.after(30, self.update)
    
    

        

    
def main():

    root = Tk()
    ex = board(root)
    game = Game(root)
    root.after(30, game.update)
    root.mainloop()
    


if __name__ == '__main__':
    main()


    
    

        


