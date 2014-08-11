#Initialize

import sqlite3
import os
from dict import *

#Connect to database in current directory (database must be downloaded elsewhere and placed in current directory)



#table_container = ['dnd_characterclass', 'dnd_characterclassvariant', 'dnd_characterclassvariant_class_skills', 'dnd_characterclassvariantrequiresfeat', 'dnd_characterclassvariantrequiresrace', 'dnd_characterclassvariantrequiresskill', 'dnd_deity', 'dnd_dndedition', 'dnd_domain', 'dnd_domainvariant', 'dnd_domainvariant_deities', 'dnd_feat', 'dnd_feat_feat_categories', 'dnd_featcategory', 'dnd_featrequiresfeat', 'dnd_featrequiresskill', 'dnd_featspecialfeatprerequisite', 'dnd_item', 'dnd_item_aura_schools', 'dnd_item_required_feats', 'dnd_item_required_spells', 'dnd_itemactivationtype', 'dnd_itemauratype', 'dnd_itemproperty', 'dnd_itemslot', 'dnd_language', 'dnd_monster', 'dnd_monster_subtypes', 'dnd_monsterhasfeat', 'dnd_monsterhasskill', 'dnd_monsterspeed', 'dnd_monstersubtype', 'dnd_monstertype', 'dnd_newsentry', 'dnd_race', 'dnd_race_automatic_languages', 'dnd_race_bonus_languages', 'dnd_racefavoredcharacterclass', 'dnd_racesize', 'dnd_racespeed', 'dnd_racespeedtype', 'dnd_racetype', 'dnd_rule', 'dnd_rulebook', 'dnd_skill', 'dnd_skillvariant', 'dnd_specialfeatprerequisite', 'dnd_spell', 'dnd_spell_descriptors', 'dnd_spellclasslevel', 'dnd_spelldescriptor', 'dnd_spelldomainlevel', 'dnd_spellschool', 'dnd_spellsubschool', 'dnd_staticpage', 'dnd_textfeatprerequisite', 'dnd_rules_conditions']

	
class dnd_query():
	
	def __init__(self, q_table):
		self.conn = sqlite3.connect('dnd.sqlite')
		self.c = self.conn.cursor()
		self.conn.text_factory = str
		self.q_table = q_table
#		self.filt_bool = filt_bool
#		self.search_bool = search_bool
#		self.sortby_bool = sortby_bool
#		self.call_term = call_term
#		self.sort_key = sort_key
		self.filter_input = {}
		self.sortby_input = {}
		
		self.filter_dict = filter_dict
		self.sortby_dict = sortby_dict

#		self.default_str = "SELECT dnd_spell.id, dnd_spell.name FROM dnd_spell "
		self.select_str = []
		self.join_str = []
		self.where_str = {}
		self.sortby_str = []
		self.where_li = []
		self.q_str = ""

		self.filt_result = []

	def init_filter(self, **f_param):
		self.filter_input =  f_param
		for i, k in f_param.items():
			self.filter_dict[self.q_table][i]['val'] = k

	def init_sortby(self, **s_param):
		self.sortby_input = s_param
		for j, v in s_param.items():
			self.sortby_dict[self.q_table][j]['val'] = v
		
	def make_filter(self, **kwargs):
		
		for i, v in kwargs.items():
			if kwargs[i]['val'] == None:
				pass
			else:
				self.where_str.update({kwargs[i]['field'] : [kwargs[i]['op'][0], kwargs[i]['op'][1], str(kwargs[i]['val']), kwargs[i]['op'][2]]})
				self.join_str.append(kwargs[i]['join'])
				self.select_str.append(kwargs[i]['field'])
		print 'sp_filt', self.join_str
		print '\n'
		print 'sp_filt', self.where_str
		print '\n'
		print '\n'

	
	def sortby(self, **kwargs):
		sortorder = {}	#USED TO KEEP HIERARCHICAL SORTS IN THE CORRECT ORDER
		for i, k in kwargs.items():
			if kwargs[i]['val'] == None:
				pass
			else:
				self.join_str.append(self.sortby_dict[self.q_table][i]['join'])
				sortorder.update({self.sortby_dict[self.q_table][i]['val'] : self.sortby_dict[self.q_table][i]['field']})
				for o in sorted(sortorder.keys()):
					self.sortby_str.append(sortorder[o])
					self.select_str.append(sortorder[o])


	def submit_query(self):
	
		if len(self.filter_input) > 0:
			self.make_filter(**self.filter_dict[self.q_table])
		else:
			pass
#		if len(self.search_input) > 0:
#			self.search_tables(self.call_term)
#			pass
#		else:
#			pass
		if len(self.sortby_input) > 0:
			self.sortby(**self.sortby_dict[self.q_table])
		else:
			pass
		
		self.select_str = list(set(', '.join(self.select_str).split(', ')))
		self.join_str = list(set(self.join_str))
		self.sortby_str = list(set(self.sortby_str))
#		print join_str
		
		for k, v in self.where_str.iteritems():
			self.where_li.append(k + str(v[0]) + str(v[1]) + str(v[2]) + str(v[3]))
#		
		self.where_li = list(set(self.where_li))
		
		if len(self.select_str) > 0:
			self.select_query = "SELECT %s.id, %s.name, " % (self.q_table, self.q_table) + ', '.join(self.select_str) + " FROM %s" % (self.q_table)
		else:
			self.select_query = "SELECT %s.id, %s.name FROM %s" % (self.q_table, self.q_table, self.q_table)
		self.join_query = ' '.join(self.join_str)
		self.where_query = "WHERE " + ' AND '.join(self.where_li)
		self.sortby_query = "ORDER BY " + ', '.join(self.sortby_str)
		
		print 'SELECT'
		print self.select_query, '\n'
		print 'JOIN'
		print self.join_query, '\n'
		print 'WHERE'		
		print self.where_query, '\n'
		print 'SORTBY'
		print self.sortby_query, '\n\n'
		
		self.q_str = '  '.join([self.select_query, self.join_query, self.where_query, self.sortby_query])
		print self.q_str
		self.query_result = self.c.execute(self.q_str).fetchall()
		for i in self.query_result:
			print i
#			self.join_str = []
#			self.where_str = {}
#			self.sortby_str = []
#			self.where_li = []
#			self.q_str = ""
#			self.where_query = ""
#			self.join_query = ""
#			self.sortby_query = ""		

	def get_spell(self, i):
		print '\n'
		print self.c.execute("SELECT name FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print '-----------------------'
		print "Rulebook: ", self.c.execute("SELECT dnd_rulebook.name FROM dnd_spell JOIN dnd_rulebook ON dnd_spell.rulebook_id = dnd_rulebook.id WHERE dnd_spell.id =?", (i,)).fetchall()
		print "School: ", self.c.execute("SELECT dnd_spellschool.name FROM dnd_spell JOIN dnd_spellschool ON dnd_spell.school_id = dnd_spellschool.id WHERE dnd_spell.id =?", (i,)).fetchall()
		print "Descriptor: ", self.c.execute("SELECT dnd_spelldescriptor.name FROM dnd_spell_descriptors JOIN dnd_spell ON dnd_spell_descriptors.spell_id = dnd_spell.id JOIN dnd_spelldescriptor ON dnd_spell_descriptors.spelldescriptor_id = dnd_spelldescriptor.id WHERE dnd_spell.id =?", (i,)).fetchall()
		print '\n'
		'''if f['dnd_spell']['sub_school_id'].ix[i] == 'NaN':
			pass
		else:
			print f['dnd_spellsubschool']['name'].ix[f['dnd_spell']['sub_school_id'].ix[i]]'''
		print self.c.execute("SELECT dnd_characterclass.name, dnd_spellclasslevel.level FROM dnd_spellclasslevel LEFT JOIN dnd_spell ON dnd_spellclasslevel.spell_id = dnd_spell.id LEFT JOIN dnd_characterclass ON dnd_spellclasslevel.character_class_id = dnd_characterclass.id WHERE dnd_spell.id =?", (i,)).fetchall()
		print self.c.execute("SELECT dnd_domain.name, dnd_spelldomainlevel.level FROM dnd_spelldomainlevel LEFT JOIN dnd_spell ON dnd_spelldomainlevel.spell_id = dnd_spell.id LEFT JOIN dnd_domain ON dnd_spelldomainlevel.domain_id = dnd_domain.id WHERE dnd_spell.id =?", (i,)).fetchall()
		print '\n'		
		print "Casting Time: ", self.c.execute("SELECT casting_time FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print "Range: ", self.c.execute("SELECT range FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print "Target: ", self.c.execute("SELECT target FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print "Effect: ", self.c.execute("SELECT effect FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print "Area: ", self.c.execute("SELECT area FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print "Duration: ", self.c.execute("SELECT duration FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print "Saving Throw: ", self.c.execute("SELECT saving_throw FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print "Spell Resistance: ", self.c.execute("SELECT spell_resistance FROM dnd_spell WHERE id=?", (i,)).fetchall()
		print '\n'
		print self.c.execute("SELECT description FROM dnd_spell WHERE id=?", (i,)).fetchall()
	
	
	def get_characlass(self, i):
		print '\n'
		print self.c.execute("SELECT dnd_characterclass.name FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		print '-----------------------'
		print "Rulebook: ", self.c.execute("SELECT dnd_rulebook.name FROM dnd_characterclassvariant JOIN dnd_rulebook ON dnd_characterclassvariant.rulebook_id = dnd_rulebook.id JOIN dnd_characterclass ON dnd_characterclassvariant.character_class_id = dnd_characterclass.id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		print "Page ", self.c.execute("SELECT dnd_characterclassvariant.page FROM dnd_characterclassvariant JOIN dnd_characterclass ON dnd_characterclassvariant.character_class_id = dnd_characterclass.id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		print '\n'
		#print "Adventures: "
		#print "Characteristics: "
		print "Alignment: ", self.c.execute("SELECT dnd_characterclassvariant.alignment FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		#print "Religion: "
		#print "Background: "
		#print "Races: "
		#print "Other Classes: "
		#print "Role: "
		print "Hit Die: ", self.c.execute("SELECT dnd_characterclassvariant.hit_die FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		print "Skill Points: ", self.c.execute("SELECT dnd_characterclassvariant.skill_points FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		print "Class Skills"
		print '\n'
		print "Advancement: \n", self.c.execute("SELECT dnd_characterclassvariant.advancement_html FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		print '\n'
		print "Class Features: \n", self.c.execute("SELECT dnd_characterclassvariant.class_features FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
		print '\n'
		print "Starting Gold: ", self.c.execute("SELECT dnd_characterclassvariant.starting_gold FROM dnd_characterclass JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id WHERE dnd_characterclass.id =?", (i,)).fetchall()
	
	def get_feat(self, i):
		print '\n'
		print self.c.execute("SELECT name FROM dnd_feat WHERE id=?", (i,)).fetchall()
		print '-----------------------'
		print '\n'
		print "Feat Category: "
		print self.c.execute("SELECT dnd_featcategory.name FROM dnd_feat_feat_categories JOIN dnd_feat ON dnd_feat_feat_categories.feat_id = dnd_feat.id JOIN dnd_featcategory ON dnd_feat_feat_categories.featcategory_id = dnd_featcategory.id WHERE dnd_feat.id =?", (i,)).fetchall()
		print '\n'
		print "Rulebook: ", self.c.execute("SELECT dnd_rulebook.name FROM dnd_feat JOIN dnd_rulebook ON dnd_feat.rulebook_id = dnd_rulebook.id WHERE dnd_feat.id =?", (i,)).fetchall()
		print '\n'
		print 'Benefit:'
		print self.c.execute("SELECT benefit FROM dnd_feat WHERE id=?", (i,)).fetchall()
		print '\n'
		print 'Normal:'
		print self.c.execute("SELECT normal FROM dnd_feat WHERE id=?", (i,)).fetchall()
		print '\n'
		print 'Special:'
		print self.c.execute("SELECT special FROM dnd_feat WHERE id=?", (i,)).fetchall()
		print '\n'
		print 'Description:'
		print self.c.execute("SELECT description FROM dnd_feat WHERE id=?", (i,)).fetchall()
		print '\n'
		print 'Requirements: '
		print '\n'
		print 'Required Feats:'
		print self.c.execute("SELECT dnd_feat.name, dnd_featrequiresfeat.additional_text FROM dnd_featrequiresfeat JOIN dnd_feat ON dnd_featrequiresfeat.required_feat_id = dnd_feat.id WHERE dnd_featrequiresfeat.source_feat_id =?", (i,)).fetchall()
		print '\n'
		print 'Required Skills:'
		print self.c.execute("SELECT dnd_skill.name, dnd_featrequiresskill.min_rank FROM dnd_featrequiresskill JOIN dnd_skill ON dnd_featrequiresskill.skill_id = dnd_skill.id JOIN dnd_feat ON dnd_featrequiresskill.feat_id = dnd_feat.id WHERE dnd_featrequiresskill.feat_id =?", (i,)).fetchall()
		print '\n'
		print 'Special Requirements:'
		print self.c.execute("SELECT dnd_specialfeatprerequisite.name, dnd_featspecialfeatprerequisite.value_1, dnd_featspecialfeatprerequisite.value_2 FROM dnd_featspecialfeatprerequisite JOIN dnd_feat ON dnd_featspecialfeatprerequisite.feat_id = dnd_feat.id JOIN dnd_specialfeatprerequisite ON dnd_featspecialfeatprerequisite.special_feat_prerequisite_id = dnd_specialfeatprerequisite.id WHERE dnd_featspecialfeatprerequisite.feat_id =?", (i,)).fetchall()
	
	def get_skill(self, i):
		print '\n'
		print self.c.execute("SELECT name FROM dnd_skill WHERE id=?", (i,)).fetchall()
		print '-----------------------'
		print '\n'
		print "Rulebook: ", self.c.execute("SELECT dnd_rulebook.name, dnd_skillvariant.page FROM dnd_skillvariant JOIN dnd_rulebook ON dnd_skillvariant.rulebook_id = dnd_rulebook.id WHERE dnd_skillvariant.skill_id =?", (i,)).fetchall()
		print '\n'
		print "Key Ability:"
		print self.c.execute("SELECT base_skill FROM dnd_skill WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Trained Only:"
		if self.c.execute("SELECT trained_only FROM dnd_skill WHERE id=?", (i,)).fetchall()[0] == 1:
			print "Yes"
		else:
			print "No"
		print '\n'
		print "Armor Check Penalty:"
		if self.c.execute("SELECT armor_check_penalty FROM dnd_skill WHERE id=?", (i,)).fetchall()[0] == 1:
			print "Yes"
		else:
			print "No"
		print '\n'
		print "Description:"
		print self.c.execute("SELECT dnd_skillvariant.description FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		print '\n'
		print "Check:"
		print self.c.execute("SELECT dnd_skillvariant.check_html FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		print '\n'
		print "Action:"
		print self.c.execute("SELECT dnd_skillvariant.action FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		print '\n'
		print "Try again:"
		print self.c.execute("SELECT dnd_skillvariant.try_again FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		print '\n'
		print "Special:"
		print self.c.execute("SELECT dnd_skillvariant.special FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		print '\n'
		print "Synergy:"
		print self.c.execute("SELECT dnd_skillvariant.synergy FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		print '\n'
		print "Restriction:"
		print self.c.execute("SELECT dnd_skillvariant.restriction FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		print '\n'
		print "Untrained:"
		print self.c.execute("SELECT dnd_skillvariant.untrained FROM dnd_skillvariant JOIN dnd_skill ON dnd_skillvariant.skill_id = dnd_skill.id WHERE dnd_skill.id =?", (i,)).fetchall()
		
	def get_race(self, i):
		print '\n'
		print self.c.execute("SELECT name FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '-----------------------'
		print '\n'
		print self.c.execute("SELECT dnd_rulebook.name, dnd_race.page FROM dnd_race JOIN dnd_rulebook ON dnd_race.rulebook_id = dnd_rulebook.id WHERE dnd_race.id =?", (i,)).fetchall()
		print '\n'
		'''print "Race Type: ", f['dnd_racetype']['name'].ix[f['dnd_race']['race_type_id'].ix[i]]
		print "Base Hit Die Size: ", f['dnd_racetype']['hit_die_size'].ix[f['dnd_race']['race_type_id'].ix[i]]
		print "Base Attack Type: ", f['dnd_racetype']['base_attack_type'].ix[f['dnd_race']['race_type_id'].ix[i]]
		print "Base Fort Save: ", f['dnd_racetype']['base_fort_save_type'].ix[f['dnd_race']['race_type_id'].ix[i]]
		print "Base Reflex Save: ", f['dnd_racetype']['base_reflex_save_type'].ix[f['dnd_race']['race_type_id'].ix[i]]
		print "Base Will Save: ", f['dnd_racetype']['base_will_save_type'].ix[f['dnd_race']['race_type_id'].ix[i]]'''
		print '\n'
		#"Personality"
		#"Physical Description"
		#"Relations"
		#"Alignment"
		#"Lands"
		#"Religion"
		#"Language"
		#"Names"
		#"Adventurers"
		print "Ability Adjustment:"
		print '\n'
		print "STR ", self.c.execute("SELECT str FROM dnd_race WHERE id=?", (i,)).fetchall()
		print "DEX ", self.c.execute("SELECT dex FROM dnd_race WHERE id=?", (i,)).fetchall()
		print "CON ", self.c.execute("SELECT con FROM dnd_race WHERE id=?", (i,)).fetchall()
		print "INT ", self.c.execute("SELECT int FROM dnd_race WHERE id=?", (i,)).fetchall()
		print "WIS ", self.c.execute("SELECT wis FROM dnd_race WHERE id=?", (i,)).fetchall()
		print "CHA ", self.c.execute("SELECT cha FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Level Adjustment", self.c.execute("SELECT level_adjustment FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Size:", self.c.execute("SELECT dnd_racesize.name FROM dnd_race JOIN dnd_racesize ON dnd_race.size_id = dnd_racesize.id WHERE dnd_race.id =?", (i,)).fetchall()
		print "Space: ", self.c.execute("SELECT space FROM dnd_race WHERE id=?", (i,)).fetchall()
		print "Reach: ", self.c.execute("SELECT reach FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Description:"
		print self.c.execute("SELECT description FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Racial Traits:"
		print self.c.execute("SELECT racial_traits FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Combat:"
		print self.c.execute("SELECT combat FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Natural Armor:"
		print self.c.execute("SELECT natural_armor FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'	
		print "Hit Dice Count"
		print self.c.execute("SELECT racial_hit_dice_count FROM dnd_race WHERE id=?", (i,)).fetchall()
	
	def get_monster(self, i):
		print '\n'
		print self.c.execute("SELECT name FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '-----------------------'
		print '\n'
		print self.c.execute("SELECT dnd_rulebook.name, dnd_monster.page FROM dnd_monster JOIN dnd_rulebook ON dnd_monster.rulebook_id = dnd_rulebook.id WHERE dnd_monster.id =?", (i,)).fetchall()
		print self.c.execute("SELECT dnd_monstertype.name FROM dnd_monster JOIN dnd_monstertype ON dnd_monster.type_id = dnd_monstertype.id WHERE dnd_monster.id =?", (i,)).fetchall()
		print '\n'	
		print '\n'
		print "Hit Dice:", self.c.execute("SELECT hit_dice FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Initiative:", self.c.execute("SELECT initiative FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Speed:", self.c.execute("SELECT dnd_monsterspeed.speed FROM dnd_monster JOIN dnd_monsterspeed ON dnd_monster.type_id = dnd_monsterspeed.id WHERE dnd_monster.id =?", (i,)).fetchall()
		print "Armor Class:", self.c.execute("SELECT armor_class FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Touch Armor Class:", self.c.execute("SELECT touch_armor_class FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Flat-footed Armor Class:", self.c.execute("SELECT flat_footed_armor_class FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Base Attack:", self.c.execute("SELECT base_attack FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Grapple:", self.c.execute("SELECT grapple FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Attack:", self.c.execute("SELECT attack FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Full Attack:", self.c.execute("SELECT full_attack FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Special Attacks:", self.c.execute("SELECT special_attacks FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'	
		print "Size:", self.c.execute("SELECT dnd_racesize.name FROM dnd_monster JOIN dnd_racesize ON dnd_monster.size_id = dnd_racesize.id WHERE dnd_monster.id =?", (i,)).fetchall()
		print "Space: ", self.c.execute("SELECT space FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Reach: ", self.c.execute("SELECT reach FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Special Qualities:", self.c.execute("SELECT special_qualities FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'	
		print "Fortitude Save:", self.c.execute("SELECT fort_save, fort_save_extra FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Reflex Save:", self.c.execute("SELECT reflex_save, reflex_save_extra FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "Will Save:", self.c.execute("SELECT will_save, will_save_extra FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Ability Scores:"
		print '\n'
		print "STR ", self.c.execute("SELECT str FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "DEX ", self.c.execute("SELECT dex FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "CON ", self.c.execute("SELECT con FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "INT ", self.c.execute("SELECT int FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "WIS ", self.c.execute("SELECT wis FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print "CHA ", self.c.execute("SELECT cha FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Skills:", self.c.execute("SELECT dnd_skill.name FROM dnd_monsterhasskill JOIN dnd_skill ON dnd_monsterhasskill.skill_id = dnd_skill.id JOIN dnd_monster ON dnd_monsterhasskill.monster_id = dnd_monster.id WHERE dnd_monster.id =?", (i,)).fetchall()
		print '\n'
		print "Feats:", self.c.execute("SELECT dnd_feat.name FROM dnd_monsterhasfeat JOIN dnd_feat ON dnd_monsterhasfeat.feat_id = dnd_feat.id JOIN dnd_monster ON dnd_monsterhasfeat.monster_id = dnd_monster.id WHERE dnd_monster.id =?", (i,)).fetchall()
		print '\n'
		print "Environment:", self.c.execute("SELECT environment FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Organization:"
		print self.c.execute("SELECT organization FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Challenge Rating:", self.c.execute("SELECT challenge_rating FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Treasure:"
		print self.c.execute("SELECT treasure FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Alignment:", self.c.execute("SELECT alignment FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Advancement:", self.c.execute("SELECT advancement FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Level Adjustment:", self.c.execute("SELECT level_adjustment FROM dnd_race WHERE id=?", (i,)).fetchall()
		print '\n'
		print '\n'
		print "Description:"
		print self.c.execute("SELECT description FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Combat:"
		print self.c.execute("SELECT combat FROM dnd_monster WHERE id=?", (i,)).fetchall()
		print '\n'
	
	def get_item(self, i):
		print '\n'
		print self.c.execute("SELECT name FROM dnd_item WHERE id=?", (i,)).fetchall()
		print '-----------------------'
		
		print "Rulebook: ", self.c.execute("SELECT dnd_rulebook.name, dnd_item.page FROM dnd_item JOIN dnd_rulebook ON dnd_item.rulebook_id = dnd_rulebook.id WHERE dnd_item.id =?", (i,)).fetchall()
		print '\n'
		print "Type: ", self.c.execute("SELECT type FROM dnd_item WHERE id=?", (i,)).fetchall()
		print "Price: ", self.c.execute("SELECT price_gp FROM dnd_item WHERE id=?", (i,)).fetchall()
		print "Item Level: ", self.c.execute("SELECT item_level FROM dnd_item WHERE id=?", (i,)).fetchall()
		print "Properties: ", self.c.execute("SELECT dnd_itemproperty.name FROM dnd_item JOIN dnd_itemproperty ON dnd_item.property_id = dnd_itemproperty.id WHERE dnd_item.id =?", (i,)).fetchall()
		print "Body Slot: ", self.c.execute("SELECT dnd_itemslot.name FROM dnd_item JOIN dnd_itemslot ON dnd_item.body_slot_id = dnd_itemslot.id WHERE dnd_item.id =?", (i,)).fetchall()
		print "Caster Level: ", self.c.execute("SELECT caster_level FROM dnd_item WHERE id=?", (i,)).fetchall()
		print "Aura: ", self.c.execute("SELECT dnd_itemauratype.name, dnd_item.aura_dc FROM dnd_item JOIN dnd_itemauratype ON dnd_item.aura_id = dnd_itemauratype.id WHERE dnd_item.id =?", (i,)).fetchall()
		print "Aura School: ", self.c.execute("SELECT dnd_spellschool.name FROM dnd_item_aura_schools JOIN dnd_item ON dnd_item_aura_schools.item_id = dnd_item.id JOIN dnd_spellschool ON dnd_item_aura_schools.spellschool_id = dnd_spellschool.id WHERE dnd_item.id =?", (i,)).fetchall()
		print "Activation: ", self.c.execute("SELECT dnd_itemactivationtype.name FROM dnd_item JOIN dnd_itemactivationtype ON dnd_item.activation_id = dnd_itemactivationtype.id WHERE dnd_item.id =?", (i,)).fetchall()
		print "Weight: ", self.c.execute("SELECT weight FROM dnd_item WHERE id=?", (i,)).fetchall()
		print "Visual Description: ", self.c.execute("SELECT visual_description FROM dnd_item WHERE id=?", (i,)).fetchall()
		print "Description: ", self.c.execute("SELECT description FROM dnd_item WHERE id=?", (i,)).fetchall()
	#	print "Relic Power: ",
	#	print "Lore: ",
		print "Prerequisites: "
		print '\n'
		print "Required Feats: ", self.c.execute("SELECT dnd_feat.name FROM dnd_item_required_feats JOIN dnd_item ON dnd_item_required_feats.item_id = dnd_item.id JOIN dnd_feat ON dnd_item_required_feats.feat_id = dnd_feat.id WHERE dnd_item.id =?", (i,)).fetchall()	
		print "Required Spells: ", self.c.execute("SELECT dnd_spell.name FROM dnd_item_required_spells JOIN dnd_item ON dnd_item_required_spells.item_id = dnd_item.id JOIN dnd_spell ON dnd_item_required_spells.spell_id = dnd_spell.id WHERE dnd_item.id =?", (i,)).fetchall()
		print "Synergy Prerequisites: ",
	#	print "Extra Prerequisites: ", self.c.execute("SELECT required_extra FROM dnd_item WHERE id=?", (i,)).fetchall()
		print '\n'
		print "Cost to Create: ", self.c.execute("SELECT cost_to_create FROM dnd_item WHERE id=?", (i,)).fetchall()
		print '\n'			
			
#### EXAMPLE ####


myquery = dnd_query('dnd_spell')
myquery.init_filter(**{'class': '2'}) #FILTERS SPELLS TO CLERIC CLASS
myquery.init_sortby(**{'classlevel' : 0, 'rulebook_id' : 1}) #HIERARCHICALLY ORDER BY CLASS LEVEL, THEN RULEBOOK ID
myquery.submit_query()

#myquery.init_filter(**{'rulebook_id' : '6', 'class': '2'})
