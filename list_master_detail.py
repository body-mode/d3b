from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.dictadapter import DictAdapter
import sqlite3
import os
from d3b_query import dnd_query
from dict import *

#from fixtures import fruit_data

from page_detail_view import PageDetailView


class MasterDetailView(GridLayout):
    '''Implementation of an master-detail view with a vertical scrollable list
    on the left (the master, or source list) and a detail view on the right.
    When selection changes in the master list, the content of the detail view
    is updated.
    '''

    def __init__(self, items, **kwargs):
        kwargs['cols'] = 2
        super(MasterDetailView, self).__init__(**kwargs)

        list_item_args_converter = \
                lambda row_index, rec: {'text': rec[1],
                                        'size_hint_y': None,
                                        'height': 25,
										'id' : str(rec[0])}

        dict_adapter = DictAdapter(sorted_keys=[i[0] for i in myquery.query_result],
                                   data=myquery.q_result_dict,
                                   args_converter=list_item_args_converter,
                                   selection_mode='single',
                                   allow_empty_selection=False,
                                   cls=ListItemButton)

        master_list_view = ListView(adapter=dict_adapter,
                                    size_hint=(.3, 1.0))

        self.add_widget(master_list_view)

        detail_view = PageDetailView(
                page_txt=dict_adapter.selection[0].text,
				page_id=dict_adapter.selection[0].id,
                size_hint=(.7, 1.0),
				tname=myquery.q_table)

        dict_adapter.bind(on_selection_change=detail_view.page_changed)
        self.add_widget(detail_view)


if __name__ == '__main__':
	from kivy.base import runTouchApp
	
	print os.getcwd()
	myquery = dnd_query('dnd_spell')
	myquery.init_filter(**{'class': '2'}) #FILTERS SPELLS TO CLERIC CLASS
	myquery.init_sortby(**{'classlevel' : 0, 'rulebook_id' : 1}) #HIERARCHICALLY ORDER BY CLASS LEVEL, THEN RULEBOOK ID
	myquery.submit_query()	

	master_detail = MasterDetailView([i[0] for i in myquery.query_result], width=800)

	runTouchApp(master_detail)
