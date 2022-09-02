import imageio
from random import *
from io import BytesIO
from PIL import Image,ImageDraw,ImageFont,ImageFilter

class gif_captcha(object):
    def __init__(self,width=150,height=50,code_count=4,font_size=32,point_count=300,line_count=3,frame_count=30):
        self.width=width
        self.height=height
        self.code_count=code_count
        self.font_size=font_size
        self.point_count=point_count
        self.line_count=line_count
        self.frame_count=frame_count

    @staticmethod
    def get_random_color():
        c1,c2,c3=randint(0,255),randint(0,255),randint(0,255)
        return c1,c2,c3

    def get_captcha(self):
        list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        captcha_str=''.join(sample(list,4))
        bg_color=self.get_random_color()
        params=[1-float(randint(1,2))/100,
            0,0,0,
            1-float(randint(1,2))/100,
            float(randint(1,2))/500,
            0.001,
            float(randint(1,1))/500,
        ]

        frame_list=[]
        for _ in range(self.frame_count):
            image=Image.new('RGB',(self.width,self.height),bg_color)
            draw=ImageDraw.Draw(image)
            font=ImageFont.truetype('simsun.ttc',size=self.font_size)
            for i,code in enumerate(captcha_str):
                v=randint(5-3,5+3)# 竖直抖动
                x=randint(10-3,10+3)# 水平抖动
                draw.text((x+i*30,v),code,self.get_random_color(),font=font)
            for i in range(self.line_count):
                x1,y1=(randint(0,self.width),randint(0,self.width))
                x2,y2=(randint(0,self.height),randint(0,self.height))
                draw.line([(x1,y1),(x2,y2)],fill=self.get_random_color())
            for i in range(self.point_count):
                x,y=randint(0,self.width),randint(0,self.height)
                draw.point([x,y],fill=self.get_random_color())
                # 扩大噪点
                # x=randint(0,self.width)
                # y=randint(0,self.height)
                # draw.arc((x,y,x+4,y+4),0,90,fill=self.get_random_color())

            # 斜体
            image=image.transform((self.width,self.height),Image.PERSPECTIVE,params)
            # 滤镜
            # image=image.filter(ImageFilter.EDGE_ENHANCE_MORE)

            f=BytesIO()
            image.save(f,"png")
            data=f.getvalue()
            f.close()

            data=imageio.imread(data,format="png")
            frame_list.append(data)
        return frame_list,captcha_str

def main():
    img=gif_captcha()
    frame_list,captcha_str=img.get_captcha()
    imageio.mimsave("captcha.gif",frame_list,'gif',duration=0.3)
    print(f'验证码"{captcha_str}"已生成至当前目录/captcha.gif')

if __name__=="__main__":
    main()