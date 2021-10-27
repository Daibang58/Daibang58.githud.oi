import pygame
import random
Som = '?'
Sod = '?'
Castles = '''
                           o                    
                       _---|         _ _ _ _ _ 
                    o   ---|     o   ]-I-I-I-[ 
   _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
   ]-I-I-I-I-[   ---|      |  ---|    |.   | 
    \ `   '_/       |     / \    |    | /^\| 
     [*]  __|       ^    / ^ \   ^    | |*|| 
     |__   ,|      / \  /    `\ / \   | ===| 
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
   |.   | |' |___|_____I___|___I___|---------| 
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\\
'''

Bow ='''
        (
         \
          )
     ##-------->        
          )
         /
        (
'''

Suont = ''' .
           / \
           | |
           | |
           |.|
           |.|
           |:|
           |:|
         `--|--'
            |
            O
'''
Bom = '''
      ______________________________   / |\  | /  .
     /                            / \     \ \ / /
    |                            | ==========  -  - -
     \____________________________\_/     / / \ \
                                        .  / | \  .'''
Winer   = '''

 __      __.___ _______  _____________________ 
/  \    /  \   |\      \ \_   _____/\______   \
\   \/\/   /   |/   |   \ |    __)_  |       _/
 \        /|   /    |    \|        \ |    |   \
  \__/\  / |___\____|__  /_______  / |____|_  /
       \/              \/        \/         \/ '''
Lose  = '''
.____    ________    ______________________________ 
|    |   \_____  \  /   _____/\_   _____/\______   \
|    |    /   |   \ \_____  \  |    __)_  |       _/
|    |___/    |    \/        \ |        \ |    |   \
|_______ \_______  /_______  //_______  / |____|_  /
        \/       \/        \/         \/         \/
''' 

L = 'Vui lòng bấm F5 để chơi lại'








print('Bạn đang ở một lâu đài tối tăm ')
print(Castles)
print('Có phòng 1, 2, 3, 4 các bạn nhớ viết nguyên văn 1 2 3 4')
A = input('Bạn chọn phòng nào: ')
 
if A == '1':
    print('Bạn đang ở phòng 1')
    print ('Có 1 con quái vật đang ngủ')
    print ('1 : Đánh nhau với quái vật')
    print('2 : Đổi đồ với quái vật ')
    print('3 : Không làm gì cả')
    A1 = input('Bạn chọn gì :')
    if A1 == '1':
        print('Bạn chọn cần chọn vũ khí')
        print('1 : Khiếm',Suont)
        print('2 : Cung' ,Bow)
        print('3 : Bom' , Bom)
        A1V1 = input('Bạn chọn gì :')
        if A1V1 == '1':
            print('Bạn lấy khiếm đánh nó')
            print('Player HP :100')
            print('And dagon HP : 10000')
            print(' 1 : Masic')
            print(' 2 : Use sink of Sun Kongfu')
            print(' 3 : Kệ ')
            print('Bạn chọn chiêu thứ 1')
            print('Masic = 1000 HP')
            print('Dagon use freule')
            print('Freule = 9 999 999 999 999 999 HP')
            print('Your HP -9,999,999,999,999,899 HP')
            print('print Lose lose đi')
            print(L)
        elif A1V1 == '2':
            print('Chưởng tên của Ninja Samurai À nhầm Samurai múa Katana chứ')
            print('Mưa tên')
            print('Mũi tên độc')
            print('200 độ cồn')
            print('Mũi làm bằng kim cương')
            print('Nhúng Axit 50')
            print('Không ai địc nổi ta')
            print('Hahahahahahahahahahahahahahahahah')
            print('Có im mồm ko thì bảo')
            print('Con quái vật ném bạn ra ngoài')
            print('Hết')
            print(L)
        elif A1V1 == '3':
            print('Bom á')
            print('Bạn cho bom vào mồm quái vật')
            print('Bùmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
            print('VVVVVVVVVVVVÀÀÀÀÀÀÀÀÀÀÀÀÀÀÀÀNNNNNNNNNNNNNGGGGGGGGGGGGGGGGGGGGGGG')
            print('Vàng trong mồm quái vật')
            print(L)
            
    elif A1 == '2':
        print('Bạn có ')
        print('1 :Bản đồ')
        print('2 :Sắt rỉ xét')
        print('3 :Thức ăn')
        print('4 :Đài')
        A1V2 = input('Bạn đổ gì :')
        if A1V2 == '1':
            print('Con quái vật đổi cho bạn cái tát và thả')
            print(Lose)
            print('Vui lòng bấm F5 để chơi lại')
            
        elif A1V2 == '2':
            print('Con quái vật chả hiểu cái gì và cho bạn vàng')
            print(Winer)
            print(L)
            
        elif A1V2 == '3':
            print('Con quái vật cho bạn fát kiếm là từ thức ăn !!!')
            print('Đúng là phản chủ mà')
            print(Lose)
            print(L)
            
        elif A1V2 == '4':
            print('Ộp')
            pygame.mixer.init()
            pygame.mixer.music.load("Ms.mp3")
            pygame.mixer.music.play()
            print('Quảy lên nào')
            print('Mission Complete ?')
            print('Quẩy đã rồi thì trò chơi kết thúc bấm F5 để chơi lại')
        
    elif A1 == '3':
        print('Bạn đứng như tượng và hắt xì')
        print('Thành quả là quái vật phạt bạn là cho nó món nào đó')
        print('Bạn cho nó thuốc mê')
        print('Con quái vật lăn ra chết và bạn thắng')
        print(L)
        
    else:
        print('Không có lựa chọn nào tên là',A1,'đâu nhá vui lòng nhấn enter !')
elif A == '2':
    print('Bạn đi vào phòng 2 thấy một kho báu và bạn đếm 1, 2 nè, 3, 4 ,5 ---> 100 và chán')
    print('Chán chỉ có mỗi 100 Đô la và mình có đầy')
    print(Lose)
    print(L)
elif A == '3':
    print('Bạn gặp con nhân sư cược bạn chơi trò chơi đoán số')
    print('Thắng = 100.000.000.000 Đô và thua = làm nô lệ')
    print('1 lần đoán và đoán số nguyên từ 1 đến 3')
    Sod = random.randint(1,3)
    
    Som = input('Bạn đoán số nào:')
        
    if Som == Sod:
        print('Ờ ờ , bạn thua rồi nhá à nhầm bạn thắng')
        print(L)
    else:
        print('Thua là thua đất trời lêu lêu lêu giờ bạn chọn việc gì?')
        print(L)
elif A == '4':
    print('Trong phòng chảng có cái gì và bạn nghe thấy một tiếng ')
    print('Hẹ hé hè hẻ')
    print('M M M M MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    print('MA kìa')
    print('Hó Họ hẹ heo')
    print('MA MÂn BASSHYWBADHSJĐCVBNHJMYHNB VCXSDRFTGHJNBVGFRTYUJKIMNBGVFGTYHJMNHGF')
    print('''
 _______ .______      .______        ______   .______          _  _      ___    _  _    
|   ____||   _  \     |   _  \      /  __  \  |   _  \        | || |    / _ \  | || |   
|  |__   |  |_)  |    |  |_)  |    |  |  |  | |  |_)  |       | || |_  | | | | | || |_  
|   __|  |      /     |      /     |  |  |  | |      /        |__   _| | | | | |__   _| 
|  |____ |  |\  \----.|  |\  \----.|  `--'  | |  |\  \----.      | |   | |_| |    | |   
|_______|| _| `._____|| _| `._____| \______/  | _| `._____|      |_|    \___/     |_|
''')
    print('''print('Bởi vì máy hỏng nên The End''')
    print('The End thật mà')
    print('Kết luận phòng 4 là phòng làm cho hỏng máy tính')
    print('Chưởng cuối')
    print('Số nhị phân')
    print('1010110100101011010101010101010101000010101001101011101010101010101101011010101010001010001010101010101010101010000010101111010101010101010101010110101001010100100110010101010101010100110101010010101010001010111110101010101001011101001')
    print('hỏng máy chưa ?')
    print(L)
else:
    print('Nhớ viết nguyên văn vui lòng nhấn phím F5 để thử lại')
                                                                                        

            