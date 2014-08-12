from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty

#from fixtures import fruit_data_attributes
#from fixtures import fruit_data

fruit_data_attributes = ['(gram weight/ ounce weight)',
                         'Calories',
                         'Calories from Fat',
                         'Total Fat',
                         'Sodium',
                         'Potassium',
                         'Total Carbo-hydrate',
                         'Dietary Fiber',
                         'Sugars',
                         'Protein',
                         'Vitamin A',
                         'Vitamin C',
                         'Calcium',
                         'Iron']

fruit_data_attribute_units = ['(g)',
                              '(%DV)',
                              '(mg)',
                              '(%DV)',
                              '(mg)',
                              '(%DV)',
                              '(g)',
                              '(%DV)',
                              '(g)(%DV)',
                              '(g)',
                              '(g)',
                              '(%DV)',
                              '(%DV)',
                              '(%DV)',
                              '(%DV)']

# Used in list_cascade.py example.
#
class PageDetailView(GridLayout):
    page_id = StringProperty('', allownone=True)

    def __init__(self, **kwargs):
        kwargs['cols'] = 2
        self.page_id = kwargs.get('page_id', '')
        super(PageDetailView, self).__init__(**kwargs)
        if self.page_id:
            self.redraw()

    def redraw(self, *args):
        self.clear_widgets()
        if self.page_id:
            self.add_widget(Label(text="Name:", halign='right'))
            self.add_widget(Label(text=self.page_id))
            for attribute in fruit_data_attributes:
                self.add_widget(Label(text="{0}:".format(attribute),
                                      halign='right'))
 #               self.add_widget(
 #                   Label(text=str(fruit_data[self.fruit_name][attribute])))

    def page_changed(self, list_adapter, *args):
        if len(list_adapter.selection) == 0:
            self.page_id = None
        else:
            selected_object = list_adapter.selection[0]

            if type(selected_object) is str:
                self.page_id = selected_object
            else:
                self.page_id = selected_object.text

        self.redraw()
