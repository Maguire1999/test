# hello2

import os
from tkinter import *
# hello

import tkinter.filedialog
from tkinter.tix import Tk, Control, ComboBox
from tkinter import scrolledtext
import vtk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import _thread
import threading


"""[肺结节检测系统]
一、读取原始文件
    mhd格式的3d肺结节扫描文件
    单张显示、上下翻页
    基本信息文字形式显示
二、三维重建
    三维显示
三、肺部区域分割
    Unet模型预测输出
"""


class App:
    def __init__(self):
        self.root = win         # win
        
        self.ct_root = None     # path of raw ct file
        self.ct_file = None     # raw ct file(.mhd)
        self.index = 0          # current index number of ct slices picture
        self.slices = 0         # total number of ct slices picture
        
        # draw the slice picture of ct , segment of the lung or ill detection
        self.ct_draw_picture = None         # plt draw picture
        self.drawPic_canvas = None          # plt will display in canvas
        
        # area to display the info of the ct file 
        self.info_width,self.info_height = 35,150
        self.info_Frame = Frame(self.root.width = self.info_width ,height=self.info_height,bg = 'white')
        self.info_Frame.pack(side = 'right' ,fill ='y')