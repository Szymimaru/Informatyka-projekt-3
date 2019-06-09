# -*- coding: utf-8 -*-

from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
global list_of_points

list_of_points = [
                ['paris.jpg', 49, 3],
                ['tokyo.jpg', 36, 140],
                ['warszawa.jpg', 52, 21],
                ['partenon.jpg', 38, 44],
                ['giza.jpg', 30, 31],
                ['koloseum.jpg', 42, 12],
                ['lasvegas.jpg', 36, -115],
                ['czarnobyl.jpg', 51, 30],
                ['york.png', 41, -74],
                ['mur.jpg', 40, 116],
                ]
class Form(BoxLayout):
    def draw_marker(self):
        
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text = "{}".format(self.latitude)
        self.search_long.text = "{}".format(self.longitude)
        
    def check_points(self):
        r=1
        if self.my_image.source in ['welcome.jpg']:
            pass
        else:
            if (self.latitude-self.curr_img[1])**2+(self.longitude-self.curr_img[2])**2<=r**2:
                self.my_score.text=str(int(self.my_score.text)+1)
                self.my_button_check.disabled = True
            
    def nastepny(self):
        self.my_button_check.disabled = False
        if len(list_of_points)>=1:
            self.curr_img=list_of_points.pop()
            self.my_image.source = self.curr_img[0]        

class MapViewApp(App):
    pass

MapViewApp().run()