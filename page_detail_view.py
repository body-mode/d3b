from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from d3b_query import dnd_query
from dict import *

#from fixtures import fruit_data_attributes
#from fixtures import fruit_data


page_attributes = \
{'dnd_spell' :
	{
	'Rulebook' : "SELECT dnd_rulebook.name FROM dnd_spell JOIN dnd_rulebook ON dnd_spell.rulebook_id = dnd_rulebook.id WHERE dnd_spell.id =?",
	'Spellschool' : "SELECT dnd_spellschool.name FROM dnd_spell JOIN dnd_spellschool ON dnd_spell.school_id = dnd_spellschool.id WHERE dnd_spell.id =?",
	'Spell Descriptor' : "SELECT dnd_spelldescriptor.name FROM dnd_spell_descriptors JOIN dnd_spell ON dnd_spell_descriptors.spell_id = dnd_spell.id JOIN dnd_spelldescriptor ON dnd_spell_descriptors.spelldescriptor_id = dnd_spelldescriptor.id WHERE dnd_spell.id =?",
	'Class Level' : "SELECT dnd_characterclass.name, dnd_spellclasslevel.level FROM dnd_spellclasslevel LEFT JOIN dnd_spell ON dnd_spellclasslevel.spell_id = dnd_spell.id LEFT JOIN dnd_characterclass ON dnd_spellclasslevel.character_class_id = dnd_characterclass.id WHERE dnd_spell.id =?",
	'Domain' : "SELECT dnd_domain.name, dnd_spelldomainlevel.level FROM dnd_spelldomainlevel LEFT JOIN dnd_spell ON dnd_spelldomainlevel.spell_id = dnd_spell.id LEFT JOIN dnd_domain ON dnd_spelldomainlevel.domain_id = dnd_domain.id WHERE dnd_spell.id =?",
	'Casting Time' : "SELECT casting_time FROM dnd_spell WHERE id=?",
	'Range' : "SELECT range FROM dnd_spell WHERE id=?",
	'Target' : "SELECT target FROM dnd_spell WHERE id=?",
	'Effect' : "SELECT effect FROM dnd_spell WHERE id=?",
	'Area' : "SELECT area FROM dnd_spell WHERE id=?",
	'Duration' : "SELECT duration FROM dnd_spell WHERE id=?",
	'Saving Throw' : "SELECT saving_throw FROM dnd_spell WHERE id=?",
	'Spell Resistance' : "SELECT spell_resistance FROM dnd_spell WHERE id=?",
	'Description': "SELECT description FROM dnd_spell WHERE id=?"}}

		
# Used in list_cascade.py example.
#
class PageDetailView(GridLayout):
	page_txt = StringProperty('', allownone=True)
	
	
	def __init__(self, **kwargs):
		kwargs['cols'] = 2
		self.page_txt = kwargs.get('page_txt', '')
		self.page_id = kwargs.get('page_id', '')
		self.tname = kwargs['tname']
		self.pagequery = dnd_query(self.tname)
		
		super(PageDetailView, self).__init__(**kwargs)
		if self.page_txt:
			self.redraw()
		if self.page_id:
			self.redraw()
		
	def redraw(self, *args):
		self.clear_widgets()
		if self.page_id:
			self.add_widget(Label(text="Name:", halign='left'))
			self.add_widget(Label(text=self.page_txt, halign='left'))
#			self.add_widget(Label(text=self.page_id))			
			for attribute in page_attributes[self.tname].keys():
				db_entry = '\n'.join(', '.join([str(x) for x in i]) for i in self.pagequery.c.execute(page_attributes[self.tname][attribute], (self.page_id,)).fetchall())
				db_lines = len(db_entry.split('\n'))
				self.add_widget(Label(text="{0}:".format(attribute), size_hint_x=0.2, valign='top', size_hint_y=db_lines))
				self.add_widget(Label(text=db_entry, size_hint_x=0.8, valign='top', size_hint_y=db_lines))

	def page_changed(self, list_adapter, *args):
		if len(list_adapter.selection) == 0:
			self.page_txt = None
		else:
			selected_object = list_adapter.selection[0]

			if type(selected_object) is str:
				self.page_txt = selected_object
			else:
				self.page_txt = selected_object.text
				self.page_id = selected_object.id

		self.redraw()
