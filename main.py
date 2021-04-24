from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from notion.client import NotionClient
from datetime import date
from datetime import datetime
from kivy.uix.image import Image
#from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        img = Image(source='Duende_Loko.png')
        layout = GridLayout(cols=1, row_force_default=True, row_default_height=80, spacing=10, padding=20)
        self.atv = TextInput(text = 'Your activity here')
        submit = Button(text='Submit', on_press=self.submit)
        layout.add_widget(img)
        layout.add_widget(self.atv)
        layout.add_widget(submit)
        return layout

    def submit(self,obj):
        client = NotionClient(token_v2="ed910b280bbd68c1e30b61a36b2be1912fd2f40d342532904360ca2362c828d46a301c6eced6c3bd55fd01f0a37e7942ad21278ff3545b7ea87488c8eee12be70eb8c6ec60f02f4525ff0ae9de34")
        page = client.get_block("https://www.notion.so/Teste-b02f66d6a4144202817709a9c8e376a9")
        cv = client.get_collection_view("https://www.notion.so/e0cff9051ed840ecaa2f5d4ebdd311fa?v=51b7351e537445fc829f8a2a0bf212d3")
        row = cv.collection.add_row()
        row.data = datetime.now().strftime('%d/%m/%Y %H:%M')
        row.atividade = self.atv.text

MainApp().run()
 #   def build(self):
  #      layout = BoxLayout(orientation = 'vertical')
   #     btn1 = Button(text='Page title')
    #    btn1.bind(on_press=self.on_press_button)
     #   btn2 = Button(text='Page title1')
      #  btn2.bind(on_press=self.on_press_button)
       # layout.add_widget(btn1)
        #layout.add_widget(btn2)

        #return layout

        #button = Button(text='Hello from Kivy', font_size=20)
        #button.bind(on_press=self.on_press_button)

        #return button

  #  def on_press_button(self, instance):
 #       print(datetime.now().strftime('%d/%m/%Y %H:%M'))


#if __name__ == '__main__':
    #app = MainApp()
   #pp.run()