filter_dict = \
{
	'dnd_spell' :
	{
		'rulebook_id' :
		{
			'val' : None,
			'field' : 'dnd_spell.rulebook_id',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'class' :
		{
			'val' : None,
			'field' : 'dnd_spellclasslevel.character_class_id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_spellclasslevel ON dnd_spell.id = dnd_spellclasslevel.spell_id"
		},
		
		'domain' :
		{
			'val' : None,
			'field' : 'dnd_spelldomainlevel.domain_id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_spelldomainlevel ON dnd_spell.id = dnd_spelldomainlevel.spell_id"
		},
		
		'classlevel' :
		{
			'val' : None,
			'field' : 'dnd_spellclasslevel.level',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_spellclasslevel ON dnd_spell.id = dnd_spellclasslevel.spell_id"
		},
		
		'domlevel' :
		{
			'val' : None,
			'field' : 'dnd_spelldomainlevel.level',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_spelldomainlevel ON dnd_spell.id = dnd_spelldomainlevel.spell_id"
		},
		
		'effect' :
		{
			'val' : None,
			'field' : 'dnd_spell.effect',
			'op' : [" LIKE ", "'%", "%'"],
			'join' : ""
		},
		
		'school_id' :
		{
			'val' : None,
			'field' : 'dnd_spell.school_id',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'sub_school_id' :
		{
			'val' : None,
			'field' : 'dnd_spell.sub_school_id',
			'op' : ["=", "", ""],
			'join' : ""
		},	
		
		'casting_time' :
		{
			'val' : None,
			'field' : 'dnd_spell.casting_time',
			'op' : [" LIKE ", "'%", "%'"],
			'join' : ""
		},
		
		'range' :
		{
			'val' : None,
			'field' : 'dnd_spell.range',
			'op' : [" LIKE ", "'%", "%'"],
			'join' : ""
		},
		
		'verbal_component' :
		{
			'val' : None,
			'field' : 'dnd_spell.verbal_component',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'somatic_component' :
		{
			'val' : None,
			'field' : 'dnd_spell.somatic_component',
			'op' : ["=", "", ""],
			'join' : ""
		},		

		'material_component' :
		{
			'val' : None,
			'field' : 'dnd_spell.material_component',
			'op' : ["=", "", ""],
			'join' : ""
		},		

		'arcane_focus_component' :
		{
			'val' : None,
			'field' : 'dnd_spell.material_component',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'divine_focus_component' :
		{
			'val' : None,
			'field' : 'dnd_spell.material_component',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'xp_component' :
		{
			'val' : None,
			'field' : 'dnd_spell.material_component',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'saving_throw' :
		{
			'val' : None,
			'field' : 'dnd_spell.saving_throw',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'descriptor' :
		{
			'val' : None,
			'field' : 'dnd_spell_descriptors.spelldescriptor_id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_spell_descriptors ON dnd_spell.id = dnd_spell_descriptors.spell_id"
		},	
		
		'spell_resistance' :
		{
			'val' : None,
			'field' : 'dnd_spell.spell_resistance',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'description' :
		{
			'val' : None,
			'field' : 'dnd_spell.description',
			'op' : [" LIKE ", "'%", "%'"],
			'join' : ""
		}
	},
	
	
	'dnd_characterclass' :
	{
		'rulebook_id' :
		{
			'val' : None,
			'field' : 'dnd_characterclassvariant.rulebook_id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id"
		},
		
		'alignment' :
		{
			'val' : None,
			'field' : 'dnd_characterclassvariant.alignment',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id"
		},

		'hit_die' :
		{
			'val' : None,
			'field' : 'dnd_characterclassvariant.hit_die',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id"
		},
		
		'skill_points':
		{
			'val' : None,
			'field' : 'dnd_characterclassvariant.skill_points',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id"
		}
		
	},

	
	'dnd_feat' :
	{
		'rulebook_id' :
		{
			'val' : None,
			'field' : 'dnd_feat.rulebook_id',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'feat_category':
		{
			'val' : None,
			'field' : 'dnd_feat_feat_categories.featcategory_id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_feat_feat_categories ON dnd_feat.id = dnd_feat_feat_categories.feat_id JOIN dnd_featcategory ON dnd_feat_feat_categories.featcategory.id = dnd_featcategory.id"
		}

	},
	
	
	'dnd_skill' :
	{
		'rulebook_id':
		{
			'val' : None,
			'field' : 'dnd_skillvariant.rulebook_id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_skillvariant ON dnd_skill.id = dnd_skillvariant.skill_id"
		},

		'key_ability': 
		{
			'val' : None,
			'field' : 'dnd_skill.base_skill',
			'op' : ["=", "", ""],
			'join' : ""
		}
	},


	'dnd_race' : 
	{
		'rulebook_id':
		{
			'val' : None,
			'field' : 'dnd_race.rulebook_id',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'str':
		{
			'val' : None,
			'field' : 'dnd_race.str',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'dex':
		{
			'val' : None,
			'field' : 'dnd_race.dex',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'con':
		{
			'val' : None,
			'field' : 'dnd_race.con',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'int':
		{
			'val' : None,
			'field' : 'dnd_race.int',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'wis':
		{
			'val' : None,
			'field' : 'dnd_race.wis',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'cha':
		{
			'val' : None,
			'field' : 'dnd_race.cha',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'level_adj':
		{
			'val' : None,
			'field' : 'dnd_race.level_adj',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'size':
		{
			'val' : None,
			'field' : 'dnd_racesize.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_racesize ON dnd_race.size_id = dnd_racesize.id"
		},

		'space':
		{
			'val' : None,
			'field' : 'dnd_race.space',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'reach':
		{
			'val' : None,
			'field' : 'dnd_race.reach',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'speed':
		{
			'val' : None,
			'field' : 'dnd_monsterspeed.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_monsterspeed ON dnd_race.id = dnd_monsterspeed.race_id"
		},		
		
		'natural_armor':
		{
			'val' : None,
			'field' : 'dnd_race.natural_armor',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'hit_dice_count':
		{
			'val' : None,
			'field' : 'dnd_race.racial_hit_dice_count',
			'op' : ["=", "", ""],
			'join' : ""
		},
	},

	'dnd_monster' :
	{
		'rulebook_id':
		{
			'val' : None,
			'field' : 'dnd_monster.rulebook_id',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'type':
		{
			'val' : None,
			'field' : 'dnd_monstertype.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_monstertype ON dnd_monster.type_id = dnd_monstertype.id"
		},
		
		'challenge_rating':
		{
			'val' : None,
			'field' : 'dnd_monster.challenge_rating',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'hit_dice':
		{
			'val' : None,
			'field' : 'dnd_monster.hit_dice',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'initiative':
		{
			'val' : None,
			'field' : 'dnd_monster.initiative',
			'op' : ["=", "", ""],
			'join' : ""
		},		
		
		'speed':
		{
			'val' : None,
			'field' : 'dnd_monsterspeed.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_monsterspeed ON dnd_monster.type_id = dnd_monsterspeed.type_id"
		},
		
		'armor_class':
		{
			'val' : None,
			'field' : 'dnd_monster.armor_class',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'size': 
		{
			'val' : None,
			'field' : 'dnd_racesize.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_racesize ON dnd_monster.size_id = dnd_racesize.id"
		},
		
		'space': 
		{
			'val' : None,
			'field' : 'dnd_monster.space',
			'op' : ["=", "", ""],
			'join' : ""
		},
		'reach': 
		{
			'val' : None,
			'field' : 'dnd_monster.reach',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'str': 
		{
			'val' : None,
			'field' : 'dnd_monster.str',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'dex': 
		{
			'val' : None,
			'field' : 'dnd_monster.dex',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'con': 
		{
			'val' : None,
			'field' : 'dnd_monster.con',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'int': 
		{
			'val' : None,
			'field' : 'dnd_monster.int',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'wis': 
		{
			'val' : None,
			'field' : 'dnd_monster.wis',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'cha': 
		{
			'val' : None,
			'field' : 'dnd_monster.cha',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'environment': 
		{
			'val' : None,
			'field' : 'dnd_monster.environment',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'alignment': 
		{
			'val' : None,
			'field' : 'dnd_monster.alignment',
			'op' : ["=", "", ""],
			'join' : ""
		}
	},
	
	'dnd_item' :
	{
		'rulebook_id':
		{
			'val' : None,
			'field' : 'dnd_item.rulebook_id',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'type': 
		{
			'val' : None,
			'field' : 'dnd_item.type',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'price': 
		{
			'val' : None,
			'field' : 'dnd_item.price_gp',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'item_level': 
		{
			'val' : None,
			'field' : 'dnd_item.item_level',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'properties': 
		{
			'val' : None,
			'field' : 'dnd_itemproperty.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_itemproperty ON dnd_item.property_id = dnd_itemproperty.id"
		},
		
		'body_slot': 
		{
			'val' : None,
			'field' : 'dnd_item.body_slot_id',
			'op' : ["=", "", ""],
			'join' : ""
		},		
		
		'caster_level': 
		{
			'val' : None,
			'field' : 'dnd_item.caster_level',
			'op' : ["=", "", ""],
			'join' : ""
		},

		'aura': 
		{
			'val' : None,
			'field' : 'dnd_item.aura_id',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'aura_dc':
		{
			'val' : None,
			'field' : 'dnd_item.aura_dc',
			'op' : ["=", "", ""],
			'join' : ""
		},
		
		'aura_school': 
		{
			'val' : None,
			'field' : 'dnd_item_aura_schools.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_item_aura_schools ON dnd_item.id = dnd_item_aura_schools.item_id"
		},
		
		'activation': 
		{
			'val' : None,
			'field' : 'dnd_itemactivationtype.id',
			'op' : ["=", "", ""],
			'join' : "JOIN dnd_itemactivationtype ON dnd_item.activation_id = dnd_itemactivationtype.id"
		}
		
	}
 }


sortby_dict = \
{
	'dnd_spell' :
	{
		'classlevel':
		{
			'field' : "dnd_spellclasslevel.character_class_id, dnd_spellclasslevel.level",
			'join' : "JOIN dnd_spellclasslevel ON dnd_spell.id = dnd_spellclasslevel.spell_id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'domlevel':
		{
			'field' : "dnd_spelldomainlevel.domain_id, dnd_spelldomainlevel.level",
			'join' : "JOIN dnd_spelldomainlevel ON dnd_spell.id = dnd_spelldomainlevel.domain_id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},	
		'spelldescriptor':
		{
			'field' : "dnd_spelldescriptor.name",
			'join' : "JOIN dnd_spell_descriptors ON dnd_spell.id = dnd_spell_descriptors.spell_id JOIN dnd_spelldescriptor ON dnd_spell_descriptors.spelldescriptor_id = dnd_spelldescriptor.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'rulebook_id':
		{
			'field' : "dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_spell.rulebook_id = dnd_rulebook.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'name' :
		{
			'field' : "dnd_spell.name",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'school_id':
		{
			'field' : "dnd_spellschool.name",
			'join' : "JOIN dnd_spellschool ON dnd_spell.school_id = dnd_spellschool.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		}
	},

	'dnd_characterclass' :
	{
		'rulebook_id':
		{
			'field' : "dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_characterclass.rulebook_id = dnd_rulebook.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'name' :
		{
			'field' : "dnd_characterclass.name",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'alignment':
		{
			'field' : "dnd_characterclassvariant.alignment",
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'hit_die':
		{
			'field' : "dnd_characterclassvariant.hit_die",
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'skill_points':
		{
			'field' : "dnd_characterclassvariant.skill_points",
			'join' : "JOIN dnd_characterclassvariant ON dnd_characterclass.id = dnd_characterclassvariant.character_class_id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		}
	},
	
	'dnd_feat' :
	{
		'rulebook_id':
		{
			'field' : "dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_feat.rulebook_id = dnd_rulebook.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'name' :
		{
			'field' : "dnd_feat.name",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'feat_category':
		{
			'field' : "dnd_featcategory.name",
			'join' : "JOIN dnd_feat_feat_categories ON dnd_feat.id = dnd_feat_feat_categories.feat_id JOIN dnd_featcategory ON dnd_feat_feat_categories.featcategory.id = dnd_featcategory.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		}
	},
	
	'dnd_skill' :
	{
		'rulebook_id':
		{
			'field' : "dnd_rulebook.id",
			'join' : "JOIN dnd_skillvariant ON dnd_skill.id = dnd_skillvariant.skill_id JOIN dnd_rulebook ON dnd_skillvariant.rulebook_id = dnd_rulebook.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'name' :
		{
			'field' : "dnd_skill.name",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'base_skill' :
		{
			'field' : "dnd_skill.base_skill",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		}
	},

	'dnd_race' : 
	{
		'rulebook_id':
		{
			'field' : "dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_race.rulebook_id = dnd_rulebook.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'name' :
		{
			'field' : "dnd_race.name",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'str' :
		{
			'field' : "dnd_race.str",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'dex' :
		{
			'field' : "dnd_race.dex",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'con' :
		{
			'field' : "dnd_race.con",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'int' :
		{
			'field' : "dnd_race.int",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'wis' :
		{
			'field' : "dnd_race.wis",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'cha' :
		{
			'field' : "dnd_race.cha",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'level_adjustment' :
		{
			'field' : "dnd_race.level_adjustment",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'size' :
		{
			'field' : "dnd_race.size",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'space' :
		{
			'field' : "dnd_race.space",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'reach' :
		{
			'field' : "dnd_race.reach",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'natural_armor' :
		{
			'field' : "dnd_race.natural_armor",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'racial_hit_dice_count' :
		{
			'field' : "dnd_race.racial_hit_dice_count",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		}
	},
	
	'dnd_monster' :
	{
		'rulebook_id':
		{
			'field' : "dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_monster.rulebook_id = dnd_rulebook.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'name' :
		{
			'field' : "dnd_monster.name",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'challenge_rating' :
		{
			'field' : "dnd_monster.challenge_rating",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'size' :
		{
			'field' : "dnd_racesize.order",
			'join' : "JOIN dnd_racesize on dnd_monster.size_id = dnd_racesize.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'type' :
		{
			'field' : "dnd_monstertype.name",
			'join' : "JOIN dnd_monstertype on dnd_monster.type_id = dnd_monstertype.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'hit_dice' :
		{
			'field' : "dnd_monster.hit_dice",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'armor_class' :
		{
			'field' : "dnd_monster.armor_class",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'base_attack' :
		{
			'field' : "dnd_monster.base_attack",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'space' :
		{
			'field' : "dnd_monster.space",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'reach' :
		{
			'field' : "dnd_monster.reach",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'fort_save' :
		{
			'field' : "dnd_monster.fort_save",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'reflex_save' :
		{
			'field' : "dnd_monster.reflex_save",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'will_save' :
		{
			'field' : "dnd_monster.reflex_save",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'str' :
		{
			'field' : "dnd_monster.str",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'dex' :
		{
			'field' : "dnd_monster.dex",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'con' :
		{
			'field' : "dnd_monster.con",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None			
		},
		'int' :
		{
			'field' : "dnd_monster.int",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'wis' :
		{
			'field' : "dnd_monster.wis",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'cha' :
		{
			'field' : "dnd_monster.cha",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'environment' :
		{
			'field' : "dnd_monster.environment",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'organization' :
		{
			'field' : "dnd_monster.organization",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'level_adjustment' :
		{
			'field' : "dnd_monster.level_adjustment",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		}
	},

	'dnd_item' :
	{
		'rulebook_id':
		{
			'field' : "dnd_rulebook.id",
			'join' : "JOIN dnd_rulebook ON dnd_item.rulebook_id = dnd_rulebook.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},		
		'name' :
		{
			'field' : "dnd_item.name",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},		
		'type' :
		{
			'field' : "dnd_item.type",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},		
		'price' :
		{
			'field' : "dnd_item.price_gp",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},		
		'item_level' :
		{
			'field' : "dnd_item.item_level",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'property' :
		{
			'field' : "dnd_itemproperty.name",
			'join' : "JOIN dnd_itemproperty ON dnd_item.property_id = dnd_itemproperty.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'body_slot' :
		{
			'field' : "dnd_itemslot.name",
			'join' : "JOIN dnd_itemslot ON dnd_item.body_slot_id = dnd_itemslot.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'caster_level' :
		{
			'field' : "dnd_item.caster_level",
			'join' : "",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'aura' :
		{
			'field' : "dnd_itemauratype.name",
			'join' : "JOIN dnd_itemauratype ON dnd_item.aura_id = dnd_itemauratype.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'aura_school' :
		{
			'field' : "dnd_spellschool.name",
			'join' : "JOIN dnd_item_aura_schools ON dnd_item.id = dnd_item_aura_schools.item_id JOIN dnd_spellschool ON dnd_item_aura_schools.spellschool_id = dnd_spellschool.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},
		'activation' :
		{
			'field' : "dnd_itemactivationtype.name",
			'join' : "JOIN dnd_itemactivationtype ON dnd_item.activation_id = dnd_itemactivationtype.id",
			'scheme' : "ASC",
			'limit' : None,
			'val' : None
		},		
	}
 }
