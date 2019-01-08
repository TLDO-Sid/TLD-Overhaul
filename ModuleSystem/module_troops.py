#OUTPUT troops.py
import random
 
from header_common import *
from header_items import *
from header_troops import *
from header_item_modifiers import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *
from module_constants import *

 
####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160)| wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops
#     The game will create random faces between Face code 1 and face code 2 for generated troops
####################################################################################################################
# Some constant and function declarations to be used below...
 
def wp(x):
  n = 0
#  r = 10 + int(x / 10)
  n|= wp_one_handed(x)
  n|= wp_two_handed(x)
  n|= wp_polearm(x)
  n|= wp_archery(x)
  n|= wp_crossbow(x)
  n|= wp_throwing(x)
  return n
 
def wp_melee(x):
  n = 0
#  r = 10 + int(x / 10)
  n|= wp_one_handed(x)
  n|= wp_two_handed(x)
  n|= wp_polearm(x)
  return n
 
#Skills
knows_common = knows_trade_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_dwarf = knows_riding_10|knows_horse_archery_10|knows_trade_2|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7| agi_5| int_4| cha_4
 
itm_hunting_bow = itm_short_bow
 
knows_lord_1 = knows_riding_4|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7
 
knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

#--------------------------------------|
########TLDO troops skills (Sid)#######|
#--------------------------------------|

# ELVES and DUNEDAIN
# Infantry
elf_skills_1a =   knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_3|knows_shield_1|knows_athletics_3|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_2a =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_4|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_3a =   knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_power_draw_3|knows_shield_3|knows_athletics_5|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_4a =   knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_power_draw_3|knows_shield_4|knows_athletics_6|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_5a =   knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_shield_5|knows_athletics_7|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Skirmishers
elf_skills_2b =   knows_ironflesh_1|knows_power_strike_2|knows_power_throw_3|knows_power_draw_4|               knows_athletics_4|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_3b =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_4|knows_power_draw_5|knows_shield_1|knows_athletics_5|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_4b =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_5|knows_power_draw_6|knows_shield_2|knows_athletics_6|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_5b =   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_6|knows_power_draw_7|knows_shield_3|knows_athletics_7|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Cavalry
elf_skills_2c =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_3|knows_power_draw_4|knows_shield_2|knows_athletics_4|knows_riding_4|knows_horse_archery_3|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_3c =   knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_4|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_4c =   knows_ironflesh_4|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_shield_4|knows_athletics_6|knows_riding_6|knows_horse_archery_5|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
elf_skills_5c =   knows_ironflesh_5|knows_power_strike_6|knows_power_throw_6|knows_power_draw_5|knows_shield_5|knows_athletics_7|knows_riding_7|knows_horse_archery_6|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Lords
elf_skills_lord = knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_power_draw_7|knows_shield_6|knows_athletics_7|knows_riding_7|knows_horse_archery_6|knows_tactics_3|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3|knows_persuasion_7
#--------------------------------------------

# DUNEDAIN
# Infantry
dun_skills_1a =   knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_shield_1|knows_athletics_1|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_2a =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_3|knows_power_draw_2|knows_shield_2|knows_athletics_2|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_3a =   knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_power_draw_2|knows_shield_3|knows_athletics_3|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_4a =   knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_power_draw_2|knows_shield_4|knows_athletics_4|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_5a =   knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_power_draw_2|knows_shield_5|knows_athletics_5|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Skirmishers
dun_skills_2b =   knows_ironflesh_1|knows_power_strike_2|knows_power_throw_3|knows_power_draw_3|               knows_athletics_2|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_3b =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_4|knows_power_draw_4|knows_shield_1|knows_athletics_3|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_4b =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_5|knows_power_draw_5|knows_shield_2|knows_athletics_4|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_5b =   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_6|knows_power_draw_6|knows_shield_3|knows_athletics_5|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Cavalry
dun_skills_2c =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_2|knows_riding_3|knows_horse_archery_3|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_3c =   knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_shield_3|knows_athletics_3|knows_riding_4|knows_horse_archery_4|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_4c =   knows_ironflesh_4|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_shield_4|knows_athletics_4|knows_riding_5|knows_horse_archery_5|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
dun_skills_5c =   knows_ironflesh_5|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_shield_5|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Lords
dun_skills_lord = knows_ironflesh_6|knows_power_strike_7|knows_power_throw_6|knows_power_draw_6|knows_shield_6|knows_athletics_5|knows_riding_7|knows_horse_archery_6|knows_tactics_3|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_3|knows_persuasion_7
#--------------------------------------------

# MEN
# Infantry
man_skills_1a =                     knows_power_strike_1|                                                      knows_athletics_1|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_2a =   knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|knows_shield_1|knows_athletics_2|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_3a =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_1|knows_shield_2|knows_athletics_2|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_4a =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_3|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_5a =   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_6a =   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_4|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Skirmishers
man_skills_2b =                     knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|               knows_athletics_2|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_3b =   knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_shield_1|knows_athletics_2|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_4b =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_3|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_5b =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_4|knows_power_draw_4|knows_shield_2|knows_athletics_3|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_6b =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_5|knows_power_draw_5|knows_shield_3|knows_athletics_4|knows_riding_1|                      knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Cavalry (add riding to rohan cavalrymen)
man_skills_2c =   knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|knows_shield_1|knows_athletics_2|knows_riding_2|knows_horse_archery_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_3c =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_1|knows_shield_2|knows_athletics_2|knows_riding_3|knows_horse_archery_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_4c =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_3|knows_riding_4|knows_horse_archery_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_5c =   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_5|knows_horse_archery_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_6c =   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_4|knows_riding_6|knows_horse_archery_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Mounted skirmishers
man_skills_2d =                     knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|               knows_athletics_2|knows_riding_2|knows_horse_archery_1|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_3d =   knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_shield_1|knows_athletics_2|knows_riding_3|knows_horse_archery_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_4d =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_3|knows_riding_4|knows_horse_archery_3|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_5d =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_4|knows_power_draw_4|knows_shield_2|knows_athletics_3|knows_riding_5|knows_horse_archery_4|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
man_skills_6d =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_5|knows_power_draw_5|knows_shield_3|knows_athletics_4|knows_riding_6|knows_horse_archery_5|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1|knows_trade_1
# Lords
man_skills_lord = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_shield_6|knows_athletics_4|knows_riding_6|knows_horse_archery_6|knows_trainer_3|knows_tactics_3|knows_inventory_management_2|knows_prisoner_management_2|knows_leadership_5|knows_persuasion_5
#--------------------------------------------

# DWARVES
# Infantry
dwarf_skills_1a =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|                                                    knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_2a =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|                   knows_shield_1|knows_athletics_1|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_3a =   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|                   knows_shield_2|knows_athletics_2|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_4a =   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|                   knows_shield_3|knows_athletics_3|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_5a =   knows_ironflesh_6|knows_power_strike_6|knows_power_throw_4|                   knows_shield_4|knows_athletics_4|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_6a =   knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|                   knows_shield_5|knows_athletics_4|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
# Skirmishers
dwarf_skills_2b =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_3|knows_power_draw_1|               knows_athletics_1|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_3b =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_4|knows_power_draw_2|knows_shield_1|knows_athletics_2|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_4b =   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_5|knows_power_draw_3|knows_shield_2|knows_athletics_3|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_5b =   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_6|knows_power_draw_4|knows_shield_3|knows_athletics_4|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
dwarf_skills_6b =   knows_ironflesh_6|knows_power_strike_4|knows_power_throw_7|knows_power_draw_5|knows_shield_4|knows_athletics_4|knows_riding_10|knows_horse_archery_10|knows_inventory_management_4|knows_prisoner_management_1|knows_leadership_1|knows_trade_2
# Lords
dwarf_skills_lord = knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_power_draw_6|knows_shield_6|knows_athletics_4|knows_riding_10|knows_horse_archery_10|knows_trainer_3|knows_tactics_3|knows_prisoner_management_1|knows_leadership_3|knows_persuasion_3
#--------------------------------------------

# URUK HAI
# Infantry
urukhai_skills_1a =   knows_ironflesh_2|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|               knows_athletics_1
urukhai_skills_2a =   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_shield_1|knows_athletics_2
urukhai_skills_3a =   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_shield_2|knows_athletics_3
urukhai_skills_4a =   knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_4
urukhai_skills_5a =   knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_5
urukhai_skills_6a =  knows_ironflesh_10|knows_power_strike_6|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_6 # berserkers
# Skirmishers
urukhai_skills_2b =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_shield_1|knows_athletics_2
urukhai_skills_3b =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_3
urukhai_skills_4b =   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_shield_2|knows_athletics_4
urukhai_skills_5b =   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_shield_3|knows_athletics_5
# Lords
urukhai_skills_lord = knows_ironflesh_7|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_shield_5|knows_athletics_5|knows_trainer_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7|knows_persuasion_3
#--------------------------------------------

# URUKS
# Infantry
uruk_skills_1a =   knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|               knows_athletics_1
uruk_skills_2a =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_1|knows_shield_1|knows_athletics_2
uruk_skills_3a =   knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_shield_2|knows_athletics_3
uruk_skills_4a =   knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_power_draw_1|knows_shield_3|knows_athletics_4
uruk_skills_5a =   knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_5
# Skirmishers
uruk_skills_2b =   knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|               knows_athletics_2
uruk_skills_3b =   knows_ironflesh_3|knows_power_strike_2|knows_power_throw_3|knows_power_draw_3|               knows_athletics_3
uruk_skills_4b =   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_4|knows_power_draw_4|               knows_athletics_4
uruk_skills_5b =   knows_ironflesh_4|knows_power_strike_3|knows_power_throw_5|knows_power_draw_5|               knows_athletics_5
# Lords
uruk_skills_lord = knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_shield_5|knows_athletics_5|knows_trainer_3|knows_tactics_6|knows_prisoner_management_3|knows_leadership_8|knows_persuasion_5
#--------------------------------------------

# ORCS
# Infantry
orc_skills_1a =                     knows_power_strike_1|                                                      knows_athletics_1
orc_skills_2a =                     knows_power_strike_2|knows_power_throw_1|                   knows_shield_1|knows_athletics_2
orc_skills_3a =   knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|                   knows_shield_2|knows_athletics_3
orc_skills_4a =   knows_ironflesh_2|knows_power_strike_4|knows_power_throw_2|                   knows_shield_3|knows_athletics_4
orc_skills_5a =   knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|                   knows_shield_4|knows_athletics_5
# Skirmishers
orc_skills_2b =                     knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_shield_1|knows_athletics_2
orc_skills_3b =                     knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_shield_2|knows_athletics_3
orc_skills_4b =   knows_ironflesh_1|knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_shield_3|knows_athletics_4
orc_skills_5b =   knows_ironflesh_2|knows_power_strike_3|knows_power_throw_4|knows_power_draw_4|knows_shield_3|knows_athletics_5
# Wargriders
orc_skills_2c =                     knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_shield_1|knows_athletics_2|knows_riding_3|knows_horse_archery_2
orc_skills_3c =   knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_shield_2|knows_athletics_3|knows_riding_4|knows_horse_archery_3
orc_skills_4c =   knows_ironflesh_2|knows_power_strike_4|knows_power_throw_3|knows_power_draw_3|knows_shield_3|knows_athletics_4|knows_riding_5|knows_horse_archery_4
orc_skills_5c =   knows_ironflesh_3|knows_power_strike_5|knows_power_throw_4|knows_power_draw_4|knows_shield_4|knows_athletics_5|knows_riding_5|knows_horse_archery_5
# Lords
orc_skills_lord = knows_ironflesh_4|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_shield_4|knows_athletics_5|knows_riding_4|knows_tactics_8|knows_prisoner_management_3|knows_leadership_10|knows_persuasion_3
#--------------------------------------------

#Kham Gondor Buff Test
gondor_skills_1 = knows_riding_4|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_5
gondor_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_7
gondor_skills_3 = knows_riding_4|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_8
gondor_skills_4 = knows_riding_4|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_9
gondor_skills_5 = knows_riding_4|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_10

knight_skills_1 = knows_riding_4|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_4|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_4|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_4|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
 
lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

#------------------------------------|
########TLDO troop attributes########|
#------------------------------------|

# Men
attr_tier_1 =  str_7| agi_5| int_4| cha_4|level(5)  # recruits
attr_tier_2 = str_10| agi_7| int_4| cha_4|level(10) # militia, guardsmen, tribal warriors, scouts, squires
attr_tier_3 = str_13|agi_11| int_4| cha_4|level(15) # low-tier professionals / high-tier militia
attr_tier_4 = str_15|agi_15| int_4| cha_4|level(20) # standard professionals. These are the "backbone" troops
attr_tier_5 = str_18|agi_18| int_4| cha_4|level(30) # elite or high-tier professionals
attr_tier_6 = str_20|agi_20|int_20|cha_20|level(40) # super elite, some captains
attr_tier_7 = str_22|agi_22|int_22|cha_22|level(50) # lords and captains

# Dunedain
attr_dun_tier_1 = str_12|agi_12| int_4| cha_4|level(6)
attr_dun_tier_2 = str_14|agi_14| int_4| cha_4|level(12)
attr_dun_tier_3 = str_16|agi_16| int_4| cha_4|level(20)
attr_dun_tier_4 = str_18|agi_18| int_4| cha_4|level(30)
attr_dun_tier_5 = str_22|agi_22| int_4| cha_4|level(40)
attr_dun_tier_6 = str_26|agi_26|int_20|cha_20|level(50) # lords and captains

# Elves
attr_elf_tier_1 = str_12|agi_12| int_4| cha_4|level(7)
attr_elf_tier_2 = str_14|agi_14| int_4| cha_4|level(12)
attr_elf_tier_3 = str_18|agi_18| int_4| cha_4|level(20)
attr_elf_tier_4 = str_18|agi_24| int_4| cha_4|level(30)
attr_elf_tier_5 = str_24|agi_27| int_4| cha_4|level(40)
attr_elf_tier_6 = str_30|agi_30|int_20|cha_20|level(50) # lords and captains

# Dwarves (Sid)
attr_dwarf_tier_1 = str_16| agi_6| int_4| cha_4|level(6)
attr_dwarf_tier_2 = str_18| agi_9| int_4| cha_4|level(12)
attr_dwarf_tier_3 = str_20|agi_11| int_4| cha_4|level(16)
attr_dwarf_tier_4 = str_22|agi_13| int_4| cha_4|level(21)
attr_dwarf_tier_5 = str_24|agi_18| int_4| cha_4|level(35)
attr_dwarf_tier_6 = str_26|agi_18| int_4| cha_4|level(48)
attr_dwarf_tier_7 = str_30|agi_20| int_4| cha_4|level(50)

# Uruk Hai (Sid)
attr_urukhai_tier_1 = str_10| agi_5| int_4| cha_4|level(4)
attr_urukhai_tier_2 = str_12| agi_7| int_4| cha_4|level(8)
attr_urukhai_tier_3 = str_14|agi_11| int_4| cha_4|level(13)
attr_urukhai_tier_4 = str_15|agi_15| int_4| cha_4|level(18)
attr_urukhai_tier_5 = str_18|agi_18| int_4| cha_4|level(25)
attr_urukhai_tier_6 = str_20|agi_20|int_20|cha_20|level(36)

# InVain: Not in yet, we need more tests if we can savely reduce elven and dwarf armies' size.

#attr_elf_tier_1 = str_12|agi_12| int_4| cha_4|level(11)
#attr_elf_tier_2 = str_14|agi_14| int_4| cha_4|level(16)
#attr_elf_tier_3 = str_18|agi_18| int_4| cha_4|level(23)
#attr_elf_tier_4 = str_18|agi_24| int_4| cha_4|level(34)
#attr_elf_tier_5 = str_24|agi_27| int_4| cha_4|level(47) 
#attr_elf_tier_6 = str_30|agi_30|int_20|cha_20|level(60)

#attr_dwarf_tier_1 =  str_9| agi_6| int_4| cha_4|level(9)
#attr_dwarf_tier_2 = str_12| agi_9| int_4| cha_4|level(14)
#attr_dwarf_tier_3 = str_15|agi_11| int_4| cha_4|level(21)
#attr_dwarf_tier_4 = str_18|agi_13| int_4| cha_4|level(31)
#attr_dwarf_tier_5 = str_18|agi_18| int_4| cha_4|level(43) 
#attr_dwarf_tier_6 = str_24|agi_18| int_4| cha_4|level(57)																																																		 

# InVain: ~halfed orc levels, worse in autocalc, but easier to train and cheaper.
attr_orc_tier_1 =  str_5| agi_5| int_4| cha_4|level(2)
attr_orc_tier_2 =  str_7| agi_7| int_4| cha_4|level(5)
attr_orc_tier_3 =  str_9| agi_8| int_4| cha_4|level(8)
attr_orc_tier_4 = str_11| agi_9| int_4| cha_4|level(13) #elite orcs
attr_orc_tier_5 = str_16|agi_11| int_4| cha_4|level(20) #super-elite, Moria and Gundabad only
attr_orc_tier_6 = str_17|agi_12| int_4| cha_4|level(45) #lords only

# InVain: Uruks and evil men (except black numenoreans): Middle ground between orcs and good men, their level simulating their worse equipment in autocalc, but easier to train and cheaper. Elites are good.
attr_evil_tier_1 =  str_7| agi_5| int_4| cha_4|level(3)
attr_evil_tier_2 = str_10| agi_7| int_4| cha_4|level(7)
attr_evil_tier_3 = str_13|agi_11| int_4| cha_4|level(11)
attr_evil_tier_4 = str_15|agi_15| int_4| cha_4|level(16)
attr_evil_tier_5 = str_18|agi_18| int_4| cha_4|level(25) #evil men elites are strong, Isen Uruk Champions too
attr_evil_tier_6 = str_20|agi_20|int_20|cha_20|level(40)

#----------------------------------------------|
########TLDO weapon proficiencies (Sid)########|
#----------------------------------------------|

# Men, infantry and cavalry
wp_tier_1 =                                                            wp(70) # recruits, all proficiencies are equal
wp_tier_2 =  wp_archery(80)| wp_crossbow(70)|  wp_throwing(90)| wp_melee(100)
wp_tier_3 = wp_archery(100)| wp_crossbow(70)| wp_throwing(100)| wp_melee(150)
wp_tier_4 = wp_archery(120)| wp_crossbow(70)| wp_throwing(150)| wp_melee(200)
wp_tier_5 = wp_archery(140)| wp_crossbow(70)| wp_throwing(200)| wp_melee(250)
wp_tier_6 = wp_archery(160)| wp_crossbow(70)| wp_throwing(250)| wp_melee(300)
wp_tier_7 =                  wp_crossbow(70)|                         wp(350) #lords, all proficiencies are equal

# Men, skirmishers
wp_tier_2_a = wp_archery(100)| wp_crossbow(70)| wp_throwing(100)|  wp_melee(80)
wp_tier_3_a = wp_archery(150)| wp_crossbow(70)| wp_throwing(150)| wp_melee(100)
wp_tier_4_a = wp_archery(200)| wp_crossbow(70)| wp_throwing(200)| wp_melee(120)
wp_tier_5_a = wp_archery(250)| wp_crossbow(70)| wp_throwing(250)| wp_melee(140)
wp_tier_6_a = wp_archery(300)| wp_crossbow(70)| wp_throwing(300)| wp_melee(160)
# ------------------------------------

# Gondor and Black Numenoreans, infantry and cavalry
wp_gondor_tier_1 =                                                            wp(70) # recruits, all proficiencies are equal
wp_gondor_tier_2 =  wp_archery(90)| wp_crossbow(70)| wp_throwing(90) | wp_melee(110)
wp_gondor_tier_3 = wp_archery(110)| wp_crossbow(70)| wp_throwing(110)| wp_melee(160)
wp_gondor_tier_4 = wp_archery(130)| wp_crossbow(70)| wp_throwing(160)| wp_melee(210)
wp_gondor_tier_5 = wp_archery(150)| wp_crossbow(70)| wp_throwing(210)| wp_melee(260)
wp_gondor_tier_6 = wp_archery(170)| wp_crossbow(70)| wp_throwing(260)| wp_melee(310)
wp_gondor_tier_7 =                  wp_crossbow(70)|                         wp(360) #lords, all proficiencies are equal

# Gondor and Black Numenoreans, skirmishers
wp_gondor_tier_2_a = wp_archery(110)| wp_crossbow(70)| wp_throwing(110)|  wp_melee(90)
wp_gondor_tier_3_a = wp_archery(160)| wp_crossbow(70)| wp_throwing(160)| wp_melee(110)
wp_gondor_tier_4_a = wp_archery(210)| wp_crossbow(70)| wp_throwing(210)| wp_melee(130)
wp_gondor_tier_5_a = wp_archery(260)| wp_crossbow(70)| wp_throwing(260)| wp_melee(150)
wp_gondor_tier_6_a = wp_archery(310)| wp_crossbow(70)| wp_throwing(310)| wp_melee(170)
# ------------------------------------

# Dunedain, infantry and cavalry
wp_dun_tier_1 =                  wp_crossbow(70)|                         wp(100) # recruits, all proficiencies are equal
wp_dun_tier_2 = wp_archery(120)| wp_crossbow(70)| wp_throwing(100)| wp_melee(140)
wp_dun_tier_3 = wp_archery(140)| wp_crossbow(70)| wp_throwing(140)| wp_melee(210)
wp_dun_tier_4 = wp_archery(160)| wp_crossbow(70)| wp_throwing(210)| wp_melee(280)
wp_dun_tier_5 = wp_archery(180)| wp_crossbow(70)| wp_throwing(280)| wp_melee(350)
wp_dun_tier_6 =                  wp_crossbow(70)|                         wp(420) #lords, all proficiencies are equal

# Dunedain, skirmishers
wp_dun_tier_2_a = wp_archery(140)| wp_crossbow(70)| wp_throwing(140)| wp_melee(120)
wp_dun_tier_3_a = wp_archery(210)| wp_crossbow(70)| wp_throwing(210)| wp_melee(140)
wp_dun_tier_4_a = wp_archery(280)| wp_crossbow(70)| wp_throwing(280)| wp_melee(160)
wp_dun_tier_5_a = wp_archery(350)| wp_crossbow(70)| wp_throwing(350)| wp_melee(180)
# ------------------------------------

# Elves, infantry and cavalry
wp_elf_tier_1 =                  wp_crossbow(70)|                         wp(250) # recruits, all proficiencies are equal
wp_elf_tier_2 = wp_archery(260)| wp_crossbow(70)| wp_throwing(250)| wp_melee(300)
wp_elf_tier_3 = wp_archery(280)| wp_crossbow(70)| wp_throwing(300)| wp_melee(350)
wp_elf_tier_4 = wp_archery(300)| wp_crossbow(70)| wp_throwing(350)| wp_melee(400)
wp_elf_tier_5 = wp_archery(320)| wp_crossbow(70)| wp_throwing(400)| wp_melee(450)
wp_elf_tier_6 =                  wp_crossbow(70)|                         wp(470) #lords, all proficiencies are equal

# Elves, skirmishers
wp_elf_tier_2_a = wp_archery(300)| wp_crossbow(70)| wp_throwing(300)| wp_melee(260)
wp_elf_tier_3_a = wp_archery(350)| wp_crossbow(70)| wp_throwing(350)| wp_melee(280)
wp_elf_tier_4_a = wp_archery(400)| wp_crossbow(70)| wp_throwing(400)| wp_melee(300)
wp_elf_tier_5_a = wp_archery(450)| wp_crossbow(70)| wp_throwing(450)| wp_melee(320)
# ------------------------------------

# Dwarves, infantry
wp_dwarf_tier_1 =                                                            wp(100) # recruits, all proficiencies are equal
wp_dwarf_tier_2 = wp_archery(100)| wp_crossbow(110)| wp_throwing(100)| wp_melee(130)
wp_dwarf_tier_3 = wp_archery(100)| wp_crossbow(130)| wp_throwing(130)| wp_melee(180)
wp_dwarf_tier_4 = wp_archery(100)| wp_crossbow(150)| wp_throwing(180)| wp_melee(230)
wp_dwarf_tier_5 = wp_archery(100)| wp_crossbow(170)| wp_throwing(230)| wp_melee(280)
wp_dwarf_tier_6 = wp_archery(100)| wp_crossbow(190)| wp_throwing(280)| wp_melee(330)
wp_dwarf_tier_7 =                                                            wp(380) #lords, all proficiencies are equal

# Dwarves, skirmishers
wp_dwarf_tier_2_a = wp_archery(110)| wp_crossbow(130)| wp_throwing(130)| wp_melee(110)
wp_dwarf_tier_3_a = wp_archery(130)| wp_crossbow(180)| wp_throwing(180)| wp_melee(130)
wp_dwarf_tier_4_a = wp_archery(250)| wp_crossbow(230)| wp_throwing(230)| wp_melee(150)
wp_dwarf_tier_5_a = wp_archery(170)| wp_crossbow(280)| wp_throwing(280)| wp_melee(170)
wp_dwarf_tier_6_a = wp_archery(190)| wp_crossbow(330)| wp_throwing(330)| wp_melee(190)
# ------------------------------------

# Uruks, infantry
wp_uruk_tier_1 =                                                            wp(70) # snagas, all proficiencies are equal
wp_uruk_tier_2 =  wp_archery(80)| wp_crossbow(70)|  wp_throwing(90)| wp_melee(100)
wp_uruk_tier_3 = wp_archery(100)| wp_crossbow(70)| wp_throwing(100)| wp_melee(140)
wp_uruk_tier_4 = wp_archery(110)| wp_crossbow(70)| wp_throwing(140)| wp_melee(180)
wp_uruk_tier_5 = wp_archery(120)| wp_crossbow(70)| wp_throwing(180)| wp_melee(220)
wp_uruk_tier_6 =                  wp_crossbow(70)|                         wp(240) #lords, all proficiencies are equal

# Uruks, skirmishers
wp_uruk_tier_2_a = wp_archery(100)| wp_crossbow(70)| wp_throwing(100)|  wp_melee(80)
wp_uruk_tier_3_a = wp_archery(140)| wp_crossbow(70)| wp_throwing(140)| wp_melee(100)
wp_uruk_tier_4_a = wp_archery(180)| wp_crossbow(70)| wp_throwing(180)| wp_melee(110)
wp_uruk_tier_5_a = wp_archery(220)| wp_crossbow(70)| wp_throwing(220)| wp_melee(120)
# ------------------------------------

# Orcs, infantry and wargriders
wp_orc_tier_1 =                                                            wp(70) # snagas, all proficiencies are equal
wp_orc_tier_2 =  wp_archery(70)| wp_crossbow(70)| wp_throwing(80) |  wp_melee(95)
wp_orc_tier_3 =  wp_archery(80)| wp_crossbow(70)| wp_throwing(95) | wp_melee(110)
wp_orc_tier_4 =  wp_archery(90)| wp_crossbow(70)| wp_throwing(110)| wp_melee(130)
wp_orc_tier_5 = wp_archery(100)| wp_crossbow(70)| wp_throwing(130)| wp_melee(140)
wp_orc_tier_6 =                  wp_crossbow(70)|                         wp(160) #lords, all proficiencies are equal

# Orcs, skirmishers
wp_orc_tier_2_a =  wp_archery(95)| wp_crossbow(70)| wp_throwing(95) | wp_melee(70)
wp_orc_tier_3_a = wp_archery(110)| wp_crossbow(70)| wp_throwing(110)| wp_melee(80)
wp_orc_tier_4_a = wp_archery(130)| wp_crossbow(70)| wp_throwing(130)| wp_melee(90)
wp_orc_tier_5_a = wp_archery(140)| wp_crossbow(70)| wp_throwing(140)| wp_melee(100)
# ------------------------------------

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.
 
reserved = 0
no_scene = 0
 
swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
 
vaegir_face_younger_1  = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1    = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1   = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1      = 0x0000000d00000001124000000020000000000000001c00800000000000000000 #retard face
vaegir_face_older_1    = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
 
vaegir_face_younger_2  = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2    = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2   = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2      = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000 #mongol face
vaegir_face_older_2    = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000
 
khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000
 
khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
 
nord_face_younger_1    = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1      = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1     = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1        = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1      = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
 
nord_face_younger_2    = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2      = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2     = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2        = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2      = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000
 
rhodok_face_younger_1  = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1    = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1   = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1      = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1    = 0x0000000fc9002003140000000000000000000000001c80400000000000000000
 
rhodok_face_younger_2  = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2    = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2   = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2      = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2    = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
 
man_face_younger_1     = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1       = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1      = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1         = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1       = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
 
man_face_younger_2     = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2       = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2      = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2         = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2       = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000
 
merchant_face_1        = man_face_young_1
merchant_face_2        = man_face_older_2
 
woman_face_1           = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2           = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000
 
refugee_face1  = woman_face_1
refugee_face2  = woman_face_2
girl_face1     = woman_face_1
girl_face2     = woman_face_2
 
mercenary_face_1       = 0x0000000000000000000000000000000000000000001c00000000000000000000 
mercenary_face_2       = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000
 
vaegir_face2   = vaegir_face_older_2

#TEXTUR_BIT_remind     = 0x0000000000001000000000000000000000000000000000000000000000000000 # UNUSED: but just a reminder of which one is the texture bit -- mtarini
#HAIR_BIT_remind       = 0x0000000000000001000000000000000000000000000000000000000000000000 # UNUSED: but just a reminder of which one is the hair bit -- GA
#BEARD_BIT_remind      = 0x0000000000000110000000000000000000000000000000000000000000000000 # UNUSED: but just a reminder of which one is the beard bit -- GA
#AGE_BITS_remind       = 0x0000000fc0000000000000000000000000000000000000000000000000000000 # UNUSED: but just a reminder of which one is the age bits -- GA
#HAIR_COLOR_BITS_remind= 0x000000003f000000000000000000000000000000000000000000000000000000 # UNUSED: but just a reminder of which one is the age bits -- GA
#FEATURES_VARIETY_remind_1 = 0x0000000000000000120020104220a24100000000000ca2400000000000000000 # UNUSED: but just a pattern for a good facial features' diversity -- Sid
#FEATURES_VARIETY_remind_2 = 0x00000000000000006dffb6ededb2497d00000000000e493f0000000000000000 # UNUSED: but just a pattern for a good facial features' diversity -- Sid

#-------------------------|
########TLDO faces########|
#-------------------------|

# Main faces of Gondor troops (Sid)
gondor_face_young_1    = 0x000000000000000d120020104220a24100000000001ca2400000000000000000
gondor_face_young_2    = 0x000000003f0030926dffb6ededb2497d00000000001e493f0000000000000000
gondor_face_middle_1   = 0x000000000000000f120020104220a24100000000001ca2400000000000000000
gondor_face_middle_2   = 0x000000003f0031146dffb6ededb2497d00000000001e493f0000000000000000
gondor_face_old_1      = 0x000000000000004f120020104220a24100000000001ca2400000000000000000
gondor_face_old_2      = 0x00000009bf0011146dffb6ededb2497d00000000001e493f0000000000000000

gondor_face_loss_1     = 0x000000000000010f120020104220a24100000000001ca2400000000000000000
gondor_face_loss_2     = 0x0000000b7f0032d56dffb6ededb2497d00000000001e493f0000000000000000

gondor_civil_face_1 = 0x0000000180000001120020104220a24100000000001ca2400000000000000000
gondor_civil_face_2 = 0x0000000dff0055d46dffb6ededb2497d00000000001e493f0000000000000000

# Old common Gondor faces
gondor_face1           = 0x000000017f00018122dc71b96c8cb6e300000000001d45330000000000000000
gondor_face2           = 0x00000009bf00200942ec7096e3a9b69c00000000001d47330000000000000000
gondor_face3           = 0x000000002400200942ec7096e3a9b49c00000000001d47330000000000000000

# Arnor faces
arnor_face_middle_1    = gondor_face_middle_1
arnor_face_middle_2    = gondor_face_middle_2
arnor_face_older_1     = gondor_face_old_1
arnor_face_older_2     = gondor_face_old_2

# Rohan faces
rohan_face_younger_1   = 0x0000000180000001120020104220a24100000000001ca2400000000000000000
rohan_face_younger_2   = 0x00000001800030456dffb6ededb2497d00000000001e493f0000000000000000

rohan_face_young_1     = 0x0000000180000081120020104220a24100000000001ca2400000000000000000
rohan_face_young_2     = 0x00000000000030c56dffb6ededb2497d00000000001e493f0000000000000000

rohan_face_middle_1    = 0x0000000180000102120020104220a24100000000001ca2400000000000000000
rohan_face_middle_2    = 0x00000001800031456dffb6ededb2497d00000000001e493f0000000000000000

rohan_face_old_1       = 0x0000000800000182120020104220a24100000000001ca2400000000000000000
rohan_face_old_2       = 0x00000008000031c56dffb6ededb2497d00000000001e493f0000000000000000

rohan_face_older_1     = 0x0000000a40000203120020104220a24100000000001ca2400000000000000000
rohan_face_older_2     = 0x0000000c000032436dffb6ededb2497d00000000001e493f0000000000000000

rohan_woman_face_1     = 0x0000000000000001000000000000000000000000001c00000000000000000000
rohan_woman_face_2     = 0x00000004040020087ff7fbffefff6dff00000000001f6dbf0000000000000000

# Elven faces 
rivendell_elf_face_1   = 0x000000000000200112000090c221125100000000001ca4c00000000000000000
rivendell_elf_face_2   = 0x000000003f00300a6dffd67dfefa5b6d00000000001dc73f0000000000000000

lorien_elf_face_1      = 0x000000000000200112000090c221125100000000001ca4c00000000000000000
lorien_elf_face_2      = 0x000000003f00300a6dffd67dfefa5b6d00000000001dc73f0000000000000000

mirkwood_elf_face_1    = 0x000000000000200112000090c221125100000000001ca4c00000000000000000
mirkwood_elf_face_2    = 0x000000003f00300a6dffd67dfefa5b6d00000000001dc73f0000000000000000

# Uruk-Hai faces
uruk_hai_face1         = 0x000000000000004136dfeed2596eb6fe00000000001e383b0000000000000000
uruk_hai_face2         = 0x000000000000510436dfeed2596eb6fe00000000001e383b0000000000000000
#urukhai_face_low1      = 0x0000000180000001003b6db6db6db6db00000000000000000000000000000000
#urukhai_face_low2      = 0x00000001932021c3003a8e53356a271200000000000000000000000000000000
#urukhai_face_mid1      = 0x0000000193000205003a8e53356a271a00000000000000000000000000000000
#urukhai_face_mid2      = 0x0000000193202046003a8fd31d0a2f1a00000000000000000000000000000000
#urukhai_face_high1     = 0x000000003f000084003a8ff32e6a7f0200000000000000000000000000000000
#urukhai_face_high2     = 0x0000000193202205003a8e53356a271a00000000000000000000000000000000

# Evil men faces
rhun_man1              = 0x000000003f00e004120020104220a24100000000001ca2400000000000000000
rhun_man2              = 0x0000000c3f0144cd6dffb6ededb2497d00000000001e493f0000000000000000

khand_man1             = 0x000000003f0082cc120020104220a24100000000001ca2400000000000000000
khand_man2             = 0x0000000b3f0134116dffb6ededb2497d00000000001e493f0000000000000000

mordor_man1            = 0x000000003f000000120020104220a24100000000001ca2400000000000000000
mordor_man2            = 0x0000000cff0022c86dffb6ededb2497d00000000001e493f0000000000000000

# --------------------

bandit_face1   = man_face_young_1
bandit_face2   = man_face_older_2

beorn_face1            = 0x0000000400000001124000000025120900000000001c00800000000000000000
beorn_face2            = 0x0000000cf10033054deeffffffffffff00000000001efff90000000000000000

haradrim_face_1        = 0x0000000239000008209072d1708d38ab00000000001d37240000000000000000
haradrim_face_2        = 0x0000000cff00200a6bac976dbcb6db3500000000001edb640000000000000000
far_harad_face1        = 0x0000000cf100300b209072d1708d38ab00000000001d37240000000000000000
far_harad_face2        = 0x00000001bf00400b36db6db6db6db6db00000000001db6db0000000000000000
 
dwarf_face_1           = 0x00000001a3002083375c6eddad6db6db00000000001db7230000000000000000
dwarf_face_2           = 0x0000000aff005104069d91bd2c6dbada00000000001db6e90000000000000000
dwarf_face_3           = 0x0000000180001103375c6eddad6db6db00000000001db7230000000000000000
dwarf_face_4           = 0x00000005ea001183069b926d2c6dbada00000000001d29690000000000000000
dwarf_face_5           = 0x00000005ff002204069a936d2c6dbada00000000001d29510000000000000000
dwarf_face_6           = 0x0000000fff0020c3069a936d2c6dbada00000000001d29510000000000000000
dwarf_face_7           = 0x0000000fff002004069a936d2c6dbada00000000001d29510000000000000000

dwarf_face_young_1     = 0x0000000000000041129224800900000000000000001d12590000000000000000
dwarf_face_young_2     = 0x0000000b3f00520a6dffd77ffeff7fbf00000000001e493f0000000000000000
dwarf_face_old_1       = 0x0000000000000041129224800900000000000000001d12590000000000000000
dwarf_face_old_2       = 0x0000000b3f00514a6dffd77ffeff7fbf00000000001e493f0000000000000000
 
# orc random faces.
# 0 and 1 are all extreme
# always use EVEN-number ODD-number for roops, to maximixe harcut-texture variations
orc_face_normal        = 0x000000018000000236db6db6db6db6db00000000001db6db0000000000000000
orc_face1              = 0x0000000180000000200000000000000000000000001c00800000000000000000  # extreme 0 
orc_face2              = 0x0000000fff00200f6dffffffffffffff00000000001effff0000000000000000  # extreme 1 
orc_face3              = 0x00000001b20000001b0386a58b51daaa00000000001dd7a30000000000000000
orc_face4              = 0x00000001b900200f386b6e18a3b1499d00000000001e66ab0000000000000000
orc_face5              = 0x00000001930000003b1b3a472d6ec8d200000000001de6f40000000000000000
orc_face6              = 0x000000018b00200f56dc66378c6db95d00000000001ebbab0000000000000000
orc_face7              = 0x0000000184000000481c9254b486e86c00000000001d4e940000000000000000
orc_face8              = 0x00000001a700200f4e9b7a111aa736cb00000000001dc46d0000000000000000
orc_face9              = 0x00000001be000000251b74b761cea75300000000001edd330000000000000000

troll_face1        = 0x000000018000000236db6db6db6db6db00000000001db6db0000000000000000  # no effects
troll_face2        = 0x000000018000000236db6db6db6db6db00000000001db6db0000000000000000  # no effects
 
evil_man_face1         = man_face_young_1
evil_man_face2         = man_face_older_2
dunland_face1          = 0x000000001f001001124161829880300200000000001c00800000000000000000
dunland_face2          = 0x0000000dff0062875d7fd3ffffffffff00000000001edffe0000000000000000
nord_face_younger_1    = 0x0000000000000001124000000020000000000000001c00800000000000000000

easterling_face1       = khergit_face_middle_2
easterling_face2       = khergit_face_middle_1

#Items hidden behind imod modifiers:
itm_whiterobe = (itm_free_whiterobe, imod_bent)
itm_nazgulrobe1 = (itm_nazgulrobe, imod_cheap)
itm_galadriel = (itm_free_galadriel, imod_rusty)
itm_merry_outfit = (itm_free_merry_outfit, imod_chipped)
itm_pippin_outfit = (itm_free_pippin_outfit, imod_battered)
itm_denethor_robe = (itm_free_denethor_robe, imod_well_made)
itm_black_dress = (itm_free_black_dress, imod_poor)
itm_blackwhite_dress = (itm_free_blackwhite_dress, imod_old) 
itm_white_tunic_b = (itm_free_white_tunic_b, imod_day_old)   
itm_white_tunic_c = (itm_free_white_tunic_c, imod_cheap)  
itm_blue_tunic = (itm_free_blue_tunic, imod_well_made)
itm_green_tunic = (itm_free_green_tunic, imod_sharp)
itm_red_tunic = itm_free_red_tunic
itm_leather_apron = (itm_free_leather_apron, imod_deadly)
itm_leather_jerkin = (itm_free_leather_jerkin, imod_exquisite) 
itm_green_dress = (itm_free_green_dress, imod_rough) 
itm_gondor_fine_outfit_dress = (itm_free_gondor_fine_outfit_dress, imod_large_bag) 
itm_rohan_fine_outfit_dale_dress = (itm_free_rohan_fine_outfit_dale_dress, imod_rotten) 
itm_robe_generic_dress = (itm_free_robe_generic_dress, imod_fresh)
itm_wimple_a = (itm_free_wimple_a, imod_bent)
itm_wimple_with_veil = (itm_free_wimple_with_veil, imod_cracked)
itm_fine_hat = (itm_free_fine_hat, imod_rusty)
itm_riv_helm_glorfi = (itm_free_riv_helm_glorfi, imod_rotten)
itm_troll_feet_boots = (itm_free_troll_feet_boots, imod_cracked)
itm_olog_feet_boots = (itm_free_olog_feet_boots, imod_hardened)
itm_troll_head_helm = (itm_free_troll_head_helm, imod_rotten)
itm_troll_head_helm_b = (itm_free_troll_head_helm_b, imod_day_old)
itm_troll_head_helm_c = (itm_free_troll_head_helm_c, imod_two_day_old)
itm_olog_head_helm = (itm_free_olog_head_helm, imod_hardened)
itm_olog_head_helm_b = (itm_free_olog_head_helm_b, imod_reinforced)
itm_olog_head_helm_c = (itm_free_olog_head_helm_c, imod_lordly)
itm_ent_head_helm2 = (itm_ent_head_helm2, imod_rotten)
itm_ent_head_helm3 = (itm_free_ent_head_helm3, imod_two_day_old)
itm_tree_trunk_club_b = (itm_free_tree_trunk_club_b, imod_poor)
itm_tree_trunk_invis = (itm_free_tree_trunk_invis, imod_old)
itm_giant_hammer = (itm_free_giant_hammer, imod_poor)
itm_giant_mace_b = (itm_free_giant_mace_b, imod_old)
itm_olog_body = (itm_olog_body, imod_rusty)
itm_olog_body_b = (itm_olog_body_b, imod_tattered)
itm_olog_hands = (itm_free_olog_hands, imod_rusty)
itm_ent_hands = (itm_ent_hands, imod_tattered)

#Dwarf helm variants
itm_dwarf_helm_coif_reinf = (itm_dwarf_helm_coif, imod_reinforced)
itm_dwarf_helm_coif_lordly =  (itm_dwarf_helm_coif, imod_lordly)
itm_dwarf_helm_kettle_lordly =  (itm_dwarf_helm_kettle, imod_lordly)
itm_dwarf_helm_fris_reinf = (itm_dwarf_helm_fris, imod_reinforced)
itm_dwarf_helm_fris_lordly = (itm_dwarf_helm_fris, imod_lordly)
itm_dwarf_nasal_reinf = (itm_dwarf_nasal, imod_reinforced)
itm_dwarf_nasal_lordly =  (itm_dwarf_nasal, imod_lordly)
itm_dwarf_miner_nasal = (itm_dwarf_miner, imod_thick)
itm_dwarf_miner_reinf = (itm_dwarf_miner, imod_reinforced)
itm_dwarf_helm_round_lordly = (itm_dwarf_helm_round, imod_lordly)
itm_dwarf_helm_sallet_lordly = (itm_dwarf_helm_sallet, imod_lordly)
itm_dwarf_helm_king_NPC = (itm_witchking_helmet, imod_old)

#Dwarf armour variants
itm_dwarf_armor_a_lordly = (itm_dwarf_armor_a, imod_lordly)
itm_dwarf_armor_b_lordly = (itm_dwarf_armor_b, imod_lordly)
itm_dwarf_armor_c_lordly = (itm_dwarf_armor_c, imod_lordly)
itm_dwarf_vest_lordly = (itm_dwarf_vest, imod_lordly)
itm_dwarf_vest_b_lordly = (itm_dwarf_vest_b, imod_lordly)

#Orc helm variants
itm_orc_coif_good = (itm_orc_coif, imod_reinforced)
itm_orc_coif_bad = (itm_orc_coif, imod_cracked)
itm_orc_nosehelm_good = (itm_orc_nosehelm, imod_reinforced)
itm_orc_nosehelm_bad = (itm_orc_nosehelm, imod_cracked)
itm_orc_kettlehelm_good = (itm_orc_kettlehelm, imod_reinforced)
itm_orc_kettlehelm_bad = (itm_orc_kettlehelm, imod_cracked)
itm_orc_buckethelm_good = (itm_orc_buckethelm, imod_reinforced)
itm_orc_buckethelm_bad = (itm_orc_buckethelm, imod_cracked)
itm_orc_morion_good = (itm_orc_morion, imod_reinforced)
itm_orc_morion_bad = (itm_orc_morion, imod_cracked)
itm_orc_beakhelm_good = (itm_orc_beakhelm, imod_reinforced)
itm_orc_beakhelm_bad = (itm_orc_beakhelm, imod_cracked)
itm_orc_beakhelm_lordly = (itm_orc_beakhelm, imod_lordly)
itm_orc_bughelm_good = (itm_orc_bughelm, imod_reinforced)
itm_orc_bughelm_bad = (itm_orc_bughelm, imod_cracked)
itm_orc_bughelm_lordly = (itm_orc_bughelm, imod_lordly)
itm_orc_visorhelm_good = (itm_orc_visorhelm, imod_reinforced)
itm_orc_visorhelm_bad = (itm_orc_visorhelm, imod_cracked)


#Rohan armour variants
# itm_free_rohan_armor_b = (itm_rohan_armor_a, imod_thick)
# itm_free_rohan_armor_c = (itm_rohan_armor_a, imod_hardened)
# itm_free_rohan_armor_d = (itm_rohan_armor_e, imod_crude)
# itm_free_rohan_armor_g = (itm_rohan_armor_h, imod_crude)
# itm_free_rohan_armor_i = (itm_rohan_armor_h, imod_reinforced)
# itm_free_rohan_armor_j = (itm_rohan_armor_k, imod_crude)
# itm_free_rohan_armor_l = (itm_rohan_armor_k, imod_reinforced)
# itm_free_rohan_armor_m = (itm_rohan_armor_n, imod_crude)
# itm_free_rohan_armor_o = (itm_rohan_armor_n, imod_reinforced)
# itm_free_rohan_armor_r = (itm_rohan_armor_p, imod_crude)
# itm_free_rohan_armor_q = (itm_rohan_armor_p, imod_reinforced)


# 0x000000018000004136db6db6db6db6db00000000001db6db0000000000000000  default player face
# 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000  bearded player face
 
troops = [
["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,0,0,fac_player_faction,[],      str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000004136db6db6db6db6db00000000001db6db0000000000000000],
["temp_troop","Temp_Troop","Temp_Troop",tf_hero,0,0,fac_commoners,[],0,0,knows_common|knows_inventory_management_10,0],
["game","Game","Game",tf_hero,0,0,fac_commoners, [],0,0,0,0],
["unarmed_troop","Unarmed_Troop","Unarmed_Troops",tf_hero,0,0,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],
####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
["temp_troop_2","Temp_Troop_2","Temp_Troop_2",tf_hero,0,0,fac_commoners,   [],      0,0,knows_common|knows_inventory_management_10,0],
["random_town_sequence","Random_Town_Sequence","Random_Town_Sequence",tf_hero,0,0,fac_neutral,[],0,0,0,0],
["tournament_participants","Tournament_Participants","Tournament_Participants",tf_hero,0,0,fac_commoners,[],0,0,0,0],
 
["tutorial_maceman","Maceman","Macemen",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,itm_wood_club,itm_black_tunic],
      attr_tier_1,wp_tier_1,knows_common,mercenary_face_1,mercenary_face_2],
["tutorial_archer","Archer","Archers",tfg_boots| tfg_armor| tfg_ranged,0,0,fac_commoners,
   [itm_leather_boots,itm_short_bow,itm_arrows,itm_black_tunic],
      attr_tier_1,wp_tier_1,knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
["tutorial_swordsman","Swordsman","Swordsmen",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,itm_black_tunic,itm_practice_sword],
      attr_tier_1,wp_tier_1,knows_common,mercenary_face_1,mercenary_face_2],
["novice_fighter","Novice_Fighter","Novice_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,  ],
      attr_tier_1,wp_tier_1,knows_common,mercenary_face_1,mercenary_face_2],
["regular_fighter","Regular_Fighter","Regular_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1,mercenary_face_2],
["veteran_fighter","Veteran_Fighter","Veteran_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1,mercenary_face_2],
["champion_fighter","Champion_Fighter","Champion_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_4,wp_tier_4,knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_1","Novice_Fighter","Novice_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_2","Novice_Fighter","Novice_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_3","Regular_Fighter","Regular_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_4","Regular_Fighter","Regular_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_5","Regular_Fighter","Regular_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_6","Veteran_Fighter","Veteran_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_7","Veteran_Fighter","Veteran_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_8","Veteran_Fighter","Veteran_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_9","Champion_Fighter","Champion_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["arena_training_fighter_10","Champion_Fighter","Champion_Fighters",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_boots,],
      attr_tier_3,wp_tier_3,knows_common,mercenary_face_1,mercenary_face_2],
["cattle","Cattle","Cattle",0,0,0,fac_neutral,   [],      0,0,0,0],
#soldiers:
#This troop is the troop marked as soldiers_begin
["farmer","Farmer","Farmers",tfg_armor|tfg_boots,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots, itm_practice_staff],
      attr_tier_1,wp_tier_1,knows_common,man_face_middle_1,man_face_old_2,man_face_older_2],
## In Vain Edit 
["townsman","Townsman","Townsmen",tfg_boots| tfg_armor,0,0,fac_dale,
   [itm_dale_hat,itm_leather_cap,itm_woolen_cap,itm_felt_hat_a,itm_free_fur_coat,(itm_free_fur_coat,imod_lordly),itm_blue_tunic,itm_leather_jerkin,itm_black_tunic,itm_leather_apron,itm_robe_generic_dress,itm_dale_tunic1,itm_dale_tunic2,itm_laketown_tunic1,itm_laketown_tunic2,itm_dale_boots_a,itm_rohan_shoes,],
      attr_tier_1,wp_tier_1,knows_common,mercenary_face_1,mercenary_face_2],
["watchman","Townswoman","Townswomen",tf_female| tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_gondor_ranger_hood,itm_robe_generic_dress, itm_black_dress,itm_rohan_fine_outfit_dale_dress,itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,itm_leather_boots],
      attr_tier_1,wp_tier_1,knows_common,rohan_woman_face_1,rohan_woman_face_2],
["mercenaries_end","bug","bug",0,0,0,fac_commoners,
   [],
      0,1,0,0],
#soldiers:
#######################################
#@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%
#Brigands
# ["brigand_lord","Brigand_Lord","Brigand_Lords",tf_mounted|tfg_gloves|tfg_armor|tfg_helmet|tfg_horse|tfg_boots,0,0,fac_brigands,
# [itm_leather_jerkin,itm_sword_two_handed_a,itm_sword_two_handed_a,itm_two_handed_axe,itm_wooden_shield,itm_hunter,itm_leather_gloves,itm_splinted_greaves],
# def_attrib|level(35),wp(205),knows_common|knows_tactics_2|knows_riding_5|knows_shield_2|knows_power_strike_4|knows_ironflesh_4,bandit_face1,bandit_face2],
# ["brigand_lieutenant","Brigand_Lieutenant","Brigand_Lieutenants",tf_mounted|tfg_gloves|tfg_armor|tfg_helmet|tfg_horse|tfg_boots,0,0,fac_brigands,
# [itm_leather_jerkin,itm_sword_medieval_c,itm_sword_two_handed_a,itm_sword_two_handed_a,itm_two_handed_axe,itm_wooden_shield,itm_fur_covered_shield,itm_hunter,itm_leather_gloves,itm_leather_boots],
# def_attrib|level(25),wp(165),knows_common|knows_tactics_1|knows_riding_5|knows_shield_2|knows_power_strike_3|knows_ironflesh_3,bandit_face1,bandit_face2],
# ["master_brigand","Master_Brigand","Master_Brigands",tf_mounted|tfg_gloves|tfg_armor|tfg_helmet|tfg_horse|tfg_boots,0,0,fac_brigands,
# [itm_leather_jerkin,itm_sword_medieval_c,itm_sword_medieval_c,itm_sword_two_handed_a,itm_two_handed_axe,itm_wooden_shield,itm_hunter,itm_leather_gloves,itm_leather_boots],
# def_attrib|level(23),wp(170),knows_common|knows_riding_4|knows_shield_2|knows_power_strike_3|knows_ironflesh_3,bandit_face1,bandit_face2],
# ["veteran_brigand","Veteran_Brigand","Veteran_Brigands",tf_mounted|tfg_armor|tfg_helmet|tfg_horse|tfg_boots,0,0,fac_brigands,
# [itm_sword_medieval_c,itm_two_handed_axe,itm_sword_medieval_c,itm_fur_covered_shield,itm_leather_jerkin,itm_mail_boots,itm_saddle_horse,itm_hunter,itm_leather_boots],
# def_attrib|level(20),wp(120),knows_common|knows_riding_3|knows_shield_2|knows_power_strike_2|knows_ironflesh_2,bandit_face1,bandit_face2],
# ["brigand","Brigand","Brigands",tfg_armor|tfg_boots,0,0,fac_brigands,
# [itm_arrows,itm_sword_medieval_c,itm_sword_medieval_c,itm_wooden_shield,itm_wooden_shield,itm_short_bow,itm_free_fur_coat,itm_leather_boots,itm_leather_boots,itm_sumpter_horse],
# def_attrib|level(14),wp(100),knows_common|knows_shield_2|knows_power_strike_2|knows_ironflesh_1,bandit_face1,bandit_face2],
# ["cutthroat","Cutthroat","Cutthroats",tfg_armor|tfg_boots,0,0,fac_brigands,
# [itm_arrows,itm_sword_medieval_c,itm_wooden_shield,itm_wooden_shield,itm_short_bow,itm_free_fur_coat,itm_leather_boots,itm_sumpter_horse],
# def_attrib|level(9),wp(90),knows_common|knows_shield_2|knows_power_strike_1|knows_ironflesh_1,bandit_face1,bandit_face2],
# ["thug","Thug","looters",tfg_boots,0,0,fac_brigands,
# [itm_one_handed_war_axe_a,itm_linen_tunic, itm_free_fur_coat,itm_free_fur_coat,itm_leather_boots,itm_leather_boots],
# def_attrib|level(4),wp(80),knows_common,bandit_face1,pirate_face2],
# ["master_slaver","Master_Slaver","Master_Slavers",tf_mounted|tfg_gloves|tfg_armor|tfg_horse|tfg_boots,0,0,fac_brigands,
# [itm_quarter_staff,itm_fur_covered_shield,itm_leather_jerkin,itm_hunter,itm_courser,itm_leather_gloves,itm_leather_boots],
# def_attrib|level(23),wp(165),knows_common|knows_riding_4|knows_shield_2|knows_power_strike_3|knows_ironflesh_3,bandit_face1,bandit_face2],
# ["brigand_slaver","Brigand_Slaver","Brigand_Slavers",tf_mounted|tfg_armor|tfg_helmet|tfg_boots,0,0,fac_brigands,
# [itm_quarter_staff,itm_fur_covered_shield,itm_leather_jerkin,itm_mail_boots,itm_saddle_horse,itm_hunter],
# def_attrib|level(20),wp(125),knows_common|knows_riding_3|knows_shield_2|knows_power_strike_2|knows_ironflesh_2,bandit_face1,bandit_face2],
#Woodmen
["woodmen_youth","Woodman","Woodmen",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_woodman_tunic,itm_leather_boots,itm_beorn_staff,],
      attr_tier_1,wp_tier_1,man_skills_1a,rohan_face_younger_1,rohan_face_middle_2],

["woodmen_forester","Woodmen_Forester","Woodmen_Foresters",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_woodman_tunic,itm_leather_boots,itm_beorn_axe,],
      attr_tier_2,wp_tier_2,man_skills_2a,rohan_face_young_1,rohan_face_middle_2],

["woodmen_skilled_forester","Woodmen_Skilled_Forester","Woodmen_Skilled_Foresters",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_woodman_tunic,itm_leather_boots,itm_beorn_axe,itm_beorn_battle_axe,],
      attr_tier_3,wp_tier_3,man_skills_3a,rohan_face_young_1,rohan_face_middle_2],

["woodmen_axemen","Woodmen_Axeman","Woodmen_Axemen",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_woodman_padded,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_battle_axe,],
      attr_tier_4,wp_tier_4,man_skills_4a,rohan_face_young_1,rohan_face_old_2],

["woodmen_master_axemen","Woodmen_Master_Axeman","Woodmen_Master_Axemen",tfg_armor| tfg_helm| tfg_boots| tfg_gloves,0,0,fac_beorn,
   [itm_woodman_padded,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_battle_axe,],
      attr_tier_5,wp_tier_5,man_skills_5a,rohan_face_middle_1,rohan_face_old_2],

["woodmen_tracker","Woodmen_Tracker","Woodmen_Trackers",tfg_ranged| tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_woodman_scout,itm_leather_boots,itm_rohan_shoes,itm_gondor_ranger_hood,itm_short_bow,itm_arrows,itm_beorn_axe,],
      attr_tier_2,wp_tier_2_a,man_skills_2b,rohan_face_young_1,rohan_face_old_2],

["woodmen_scout","Woodmen_Scout","Woodmen_Scouts",tfg_ranged| tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_woodman_scout,itm_leather_boots,itm_gondor_ranger_hood,itm_short_bow,itm_arrows,itm_beorn_axe,],
      attr_tier_3,wp_tier_3_a,man_skills_3b,rohan_face_young_1,rohan_face_middle_2],

["woodmen_archer","Woodmen_Archer","Woodmen_Archers",tfg_ranged| tfg_armor| tfg_helm|tfg_boots| tfg_gloves,0,0,fac_beorn,
   [itm_woodman_scout,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_gondor_ranger_hood,itm_regular_bow,itm_arrows,itm_beorn_axe,],
      attr_tier_4,wp_tier_4_a,man_skills_4b,rohan_face_young_1,rohan_face_old_2],

["fell_huntsmen_of_mirkwood","Expert_Huntsman_of_Mirkwood","Expert_Huntsmen_of_Mirkwood",tfg_ranged| tfg_gloves| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_woodman_padded,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_regular_bow,itm_arrows,itm_beorn_battle_axe,itm_beorn_axe,],
      attr_tier_5,wp_tier_5_a,man_skills_5b,rohan_face_middle_1,rohan_face_old_2],

#Beornings

["beorning_vale_man","Beorning_Man","Beorning_Men",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_beorn_tunic,itm_leather_boots,itm_gondor_ranger_hood,itm_beorn_staff,itm_beorn_axe,],
      attr_tier_1,wp_tier_1,man_skills_1a,beorn_face1,beorn_face2],

["beorning_warrior","Beorning_Warrior","Beorning_Warriors",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_beorn_padded,itm_rohan_shoes,itm_beorn_axe,itm_beorn_axe,itm_beorn_battle_axe,],
      attr_tier_2,wp_tier_2,man_skills_2a,beorn_face1,beorn_face2],

["beorning_tolltacker","Beorning_Toll-Taker","Beorning_Toll-Takers",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_beorn_padded,itm_rohan_shoes,itm_leather_gloves,itm_dale_shortsword,itm_beorn_shield,],
      attr_tier_3,wp_tier_3,man_skills_3a,beorn_face1,beorn_face2],

["beorning_sentinel","Beorning_Sentinel","Beorning_Sentinels",tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_beorn_heavy,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_shield,itm_dale_sword,itm_dale_sword1,],
      attr_tier_4,wp_tier_4,man_skills_4a,beorn_face1,beorn_face2],

["beorning_warden_of_the_ford","Beorning_Warden_of_the_Ford","Beorning_Warden_of_the_Ford",tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_beorn_chief,itm_leather_boots,itm_leather_gloves,itm_beorn_shield,itm_dale_sword,itm_dale_sword1,],
      attr_tier_5,wp_tier_5,man_skills_5a,beorn_face1,beorn_face2],

["beorning_carrock_lookout","Beorning_Carrock_Lookout","Beorning_Carrock_Lookouts",tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_beorn_tunic,itm_rohan_shoes,itm_gondor_ranger_hood,itm_beorn_axe,],
      attr_tier_3,wp_tier_3,man_skills_3a,beorn_face1,beorn_face2],

["beorning_carrock_fighter","Beorning_Carrock_Fighter","Beorning_Carrock_Fighters",tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_beorn_heavy,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_axe,itm_beorn_battle_axe,],
      attr_tier_4,wp_tier_4,man_skills_4a,beorn_face1,beorn_face2],

["beorning_carrock_berserker","Beorning_Carrock_Berserker","Beorning_Carrock_Berserkers",tfg_gloves| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_beorn_berserk,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_battle_axe,itm_dale_bastard,],
      attr_tier_5,wp_tier_5,man_skills_5a,beorn_face1,beorn_face2],

["northmen_items","BUG","_",tf_hero,0,0,fac_beorn,
   [itm_leather_gloves,itm_good_mace,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

#Dale

["dale_militia","Dalesman","Dalesmen",tfg_armor| tfg_boots,0,0,fac_dale,
   [itm_dale_hat,itm_felt_hat_a,itm_woolen_cap,itm_dale_tunic1,itm_dale_tunic2,itm_rohan_shoes,itm_dale_boots_a,itm_dale_shortsword,itm_spear,],
      attr_tier_1,wp_tier_1,man_skills_1a,vaegir_face_younger_1,vaegir_face_middle_2],

["dale_man_at_arms","Dale_Militia","Dale_Militia",tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_helm,0,0,fac_dale,
   [itm_leather_cap,itm_dale_hat,itm_dale_armor_c,itm_dale_tunic1,itm_dale_tunic2,itm_dale_boots_a,itm_dale_axe,itm_dale_sword,itm_dale_sword1,itm_dale_pike,itm_dale_shield_a,],
      attr_tier_2,wp_tier_2,man_skills_2a,vaegir_face_young_1,vaegir_face_middle_2],

["dale_scout","Dale_Bowman","Dale_Bowmen",tfg_armor| tfg_boots| tfg_helm| tfg_ranged,0,0,fac_dale,
   [itm_leather_cap,itm_dale_hat,itm_dale_armor_c,itm_dale_tunic1,itm_dale_tunic2,itm_dale_boots_a,itm_dale_axe,itm_dale_shortsword,itm_hunting_bow,itm_arrows,],
      attr_tier_2,wp_tier_2_a,man_skills_2b,vaegir_face_young_1,vaegir_face_old_2],

["dale_bowmen","Dale_Archer","Dale_Archers",tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_dale,
   [itm_dale_helmet_c,itm_dale_armor_d,itm_leather_gloves,itm_dale_boots_b,itm_dale_bow,itm_dale_arrows,itm_dale_sword_long,],
      attr_tier_3,wp_archery(170)|wp_throwing(150)|wp_melee(100),man_skills_3b,vaegir_face_young_1,vaegir_face_older_2],

["dale_archer","Dale_Veteran_Archer","Dale_Veteran_Archers",tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_dale,
   [itm_dale_helmet_c,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_bow,itm_dale_arrows,itm_dale_sword_long,],
      attr_tier_4,wp_archery(240)|wp_throwing(200)|wp_melee(120),man_skills_4b,vaegir_face_young_1,vaegir_face_older_2],

["barding_bowmen_of_dale","Bardian_Marksman","Bardian_Marksmen",tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_dale,
   [itm_dale_helmet_g,itm_dale_armor_i,itm_leather_gloves,itm_dale_boots_d,itm_dale_bow,itm_dale_arrows,itm_dale_sword_broad,],
      attr_tier_6,wp_archery(320)|wp_throwing(250)|wp_melee(160),knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_5|knows_shield_2|knows_athletics_4|knows_riding_1,vaegir_face_young_1,vaegir_face_older_2],

["dale_warrior","Dale_Swordsman","Dale_Swordsmen",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dale,
   [itm_dale_helmet_b,itm_dale_armor_d,itm_leather_gloves,itm_dale_boots_b,itm_dale_sword_long,itm_dale_shield_c,],
      attr_tier_3,wp_tier_3,man_skills_3a,vaegir_face_young_1,vaegir_face_old_2],

["dale_veteran_warrior","Dale_Veteran_Swordsman","Dale_Veteran_Swordsmen",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dale,
   [itm_dale_helmet_b,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_sword_long,itm_dale_shield_c,],
      attr_tier_4,wp_tier_4,man_skills_4a,vaegir_face_young_1,vaegir_face_older_2],

["dale_marchwarden","Dale_Swordmaster","Dale_Swordmasters",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dale,
   [itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_bastard,],
      attr_tier_5,wp_tier_5,man_skills_5a|knows_ironflesh_6|knows_power_strike_5,vaegir_face_middle_1,vaegir_face_older_2],

["dale_pikeman","Dale_Spearman","Dale_Spearmen",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dale,
   [itm_dale_helmet_b,itm_dale_armor_d,itm_leather_gloves,itm_dale_boots_b,itm_dale_pike,itm_dale_shield_c,],
      attr_tier_3,wp_tier_3,man_skills_3a,vaegir_face_young_1,vaegir_face_old_2],

["dale_billman","Dale_Veteran_Spearman","Dale_Veteran_Spearmen",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dale,
   [itm_dale_helmet_b,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_pike,itm_dale_shield_c,],
      attr_tier_4,wp_tier_4,man_skills_4a,vaegir_face_young_1,vaegir_face_older_2],

["dale_bill_master","Gadraught","Gadraughts",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dale,
   [itm_dale_helmet_b,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_pike,itm_dale_shield_c,],
      attr_tier_5,wp_tier_5,man_skills_5a,vaegir_face_middle_1,vaegir_face_older_2],

["merchant_squire_or_dale","Yeoman","Yeomen",tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_horse,0,0,fac_dale,
   [itm_dale_hat,itm_leather_cap,itm_dale_armor_c,itm_dale_tunic1,itm_dale_tunic2,itm_dale_boots_a,itm_dale_axe,itm_dale_sword,itm_dale_sword1,itm_dale_pike,itm_dale_shield_d,itm_sumpter_horse,],
      attr_tier_2,wp_tier_2,man_skills_2a,vaegir_face_young_1,vaegir_face_old_2],

["merchant_guard_of_dale","Dale_Hobelar","Dale_Hobelars",tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_dale,
   [itm_dale_helmet_d,itm_dale_armor_d,itm_leather_gloves,itm_dale_boots_b,itm_dale_sword_long,itm_dale_lance,itm_dale_shield_d,itm_dale_horse,],
      attr_tier_3,wp_tier_3,man_skills_3c,vaegir_face_young_1,vaegir_face_old_2],

["merchant_protector_of_dale","Dale_Cavalier","Dale_Cavaliers",tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_dale,
   [itm_dale_helmet_d,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_sword_long,itm_dale_lance,itm_dale_shield_d,itm_dale_horse,],
      attr_tier_4,wp_tier_4,man_skills_4c,vaegir_face_young_1,vaegir_face_older_2],

["girions_guard_of_dale","Girion's_Guard_of_Dale","Girion's_Guards_of_Dale",tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,0,fac_dale,
   [itm_dale_helmet_d,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_sword_broad,itm_dale_lance,itm_dale_shield_d,itm_dale_warhorse,],
      attr_tier_5,wp_tier_5,man_skills_5c,vaegir_face_middle_1,vaegir_face_older_2],

 # Lake-Town
["riverman","Riverman","Rivermen",tfg_armor| tfg_boots,0,subfac_laketown,fac_dale,
   [itm_dale_hat,itm_leather_cap,itm_felt_hat_a,itm_laketown_tunic1,itm_laketown_tunic2,itm_dale_armor_a,itm_dale_armor_b,itm_rohan_shoes,itm_dale_boots_a,itm_dale_shortsword,itm_spear,],
      attr_tier_1,wp_tier_1,man_skills_1a,vaegir_face_younger_1,vaegir_face_middle_2],

["laketown_militia","Lake-Town_Militia","Lake-Town_Militia",tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,subfac_laketown,fac_dale,
   [itm_leather_cap,itm_dale_hat,itm_laketown_tunic1,itm_laketown_tunic2,itm_dale_armor_a,itm_dale_armor_b,itm_dale_boots_a,itm_dale_axe,itm_dale_sword,itm_dale_sword1,itm_dale_javelin,itm_dale_shield_b,],
      attr_tier_2,wp_tier_2,man_skills_2a,vaegir_face_young_1,vaegir_face_middle_2],

["laketown_bowman","Hearth_Watchman","Hearth_Watchmen",tfg_armor| tfg_boots| tfg_helm| tfg_ranged,0,subfac_laketown,fac_dale,
   [itm_dale_hat,itm_leather_cap,itm_laketown_tunic1,itm_laketown_tunic2,itm_dale_armor_a,itm_dale_armor_b,itm_dale_boots_a,itm_dale_shortsword,itm_dale_axe,itm_short_bow,itm_arrows,],
      attr_tier_2,wp_tier_2_a,man_skills_2b,vaegir_face_young_1,vaegir_face_old_2],

["laketown_archer","Lake-Town_Archer","Lake-Town_Archers",tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_laketown,fac_dale,
   [itm_dale_helmet_a,itm_dale_armor_e,itm_leather_gloves,itm_dale_boots_a,itm_dale_bow,itm_dale_arrows,itm_dale_sword_long,],
      attr_tier_4,wp_tier_4_a,man_skills_4b,vaegir_face_young_1,vaegir_face_older_2],

["laketown_guard_archer","Lake-Town_Guard_Archer","Lake-Town_Guard_Archers",tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_laketown,fac_dale,
   [itm_dale_helmet_a,itm_dale_armor_g,itm_leather_gloves,itm_dale_boots_a,itm_dale_bow,itm_dale_arrows,itm_dale_sword_broad,],
      attr_tier_5,wp_tier_5_a,man_skills_5b,vaegir_face_young_1,vaegir_face_older_2],

["laketown_warden","Lake-Town_Warden","Lake-Town_Wardens",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm|tfg_polearm,0,subfac_laketown,fac_dale,
   [itm_dale_helmet_a,itm_dale_armor_e,itm_leather_gloves,itm_dale_boots_a,itm_dale_sword_long,itm_dale_billhook,],
      attr_tier_4,wp_tier_4,man_skills_4a,vaegir_face_young_1,vaegir_face_older_2],

["laketown_guard","Lake-Town_Guard","Lake-Town_Guard",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm|tfg_polearm,0,subfac_laketown,fac_dale,
   [itm_dale_helmet_a,itm_dale_armor_g,itm_leather_gloves,itm_dale_boots_a,itm_dale_sword_broad,itm_dale_billhook,],
      attr_tier_5,wp_tier_5,man_skills_5a,vaegir_face_middle_1,vaegir_face_older_2],

["laketown_shipman","Lake-Town_Shipman","Lake-Town_Shipmen",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_laketown,fac_dale,
   [itm_dale_helmet_e,itm_dale_armor_f,itm_leather_gloves,itm_dale_boots_a,itm_dale_sword_long,itm_dale_javelin,itm_shipmen_shield,],
      attr_tier_4,wp_tier_4,man_skills_4a|knows_power_throw_3,vaegir_face_young_1,vaegir_face_older_2],

["laketown_marine","Lake-Town_Marine","Lake-Town_Marines",tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_laketown,fac_dale,
   [itm_dale_helmet_e,itm_dale_armor_f,itm_leather_gloves,itm_dale_boots_a,itm_dale_sword_broad,itm_dale_javelin,itm_shipmen_shield,],
      attr_tier_5,wp_tier_5,man_skills_5a|knows_power_throw_3,vaegir_face_middle_1,vaegir_face_older_2],

["rhovanion_regent","Rhovanion_Regent","Rhovanion_Regents",tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,0,fac_dale,
   [itm_dale_helmet_i,itm_dale_armor_k,itm_dale_armor_l,itm_leather_gloves,itm_dale_boots_e,itm_dale_sword_broad,itm_dale_lance,itm_dale_shield_e,itm_dale_warhorse,],
      attr_tier_5,wp_tier_5,man_skills_5c,vaegir_face_young_1,vaegir_face_older_2],

["aihwothiuda_guard","Aihwothiuda_Guard","Aihwothiuda_Guard",tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,0,fac_dale,
   [itm_dale_helmet_i,itm_dale_armor_k,itm_dale_armor_l,itm_leather_gloves,itm_dale_boots_e,itm_dale_sword_broad,itm_dale_lance,itm_dale_shield_e,itm_dale_warhorse,],
      attr_tier_6,wp_tier_6,man_skills_6c,vaegir_face_middle_1,vaegir_face_older_2],

["dale_items","BUG","BUG",tf_hero,0,subfac_laketown,fac_dale,
   [itm_free_fur_coat,itm_sumpter_horse,itm_saddle_horse,itm_good_mace,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,itm_dale_armor_e,itm_dale_armor_f,itm_dale_armor_g,itm_dale_armor_j,itm_dale_armor_k,itm_dale_armor_l,
   itm_dale_helmet_a,itm_dale_helmet_e,itm_dale_helmet_f,itm_dale_helmet_h,itm_dale_helmet_i,itm_dale_boots_e,itm_dale_billhook,itm_dale_javelin,itm_dale_shield_b,itm_shipmen_shield,itm_dale_shield_e,],
      0,0,0,0],

#Rhun

["rhun_clansman","Easterling_Clansman","Easterling_Clansmen",tf_evil_man| tfg_armor| tfg_boots,0,0,fac_rhun,
   [itm_easterling_cloth,itm_rhun_shoes,itm_rhun_shortsword,itm_shortened_spear,],
      attr_evil_tier_1,wp_tier_1,man_skills_1a,rhun_man1,rhun_man2],

["rhun_militia","Easterling_Militiaman","Easterling_Militiamen",tf_evil_man| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,0,fac_rhun,
   [itm_rhun_helm_k,itm_rhun_armor_a,itm_rhun_armor_b,itm_rhun_armor_d,itm_rhun_shoes,itm_rhun_shortsword,itm_rhun_axe,itm_rhun_spear,itm_rhun_round_shield,itm_rhun_infantry_shield,],
      attr_evil_tier_2,wp_tier_2,man_skills_2a,rhun_man1,rhun_man2],

["balchoth_cavalry","Balchoth_Horse_Archer","Balchoth_Horse_Archers",tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_ranged,0,0,fac_rhun,
   [itm_rhun_helm_e,itm_rhun_armor_o,itm_leather_gloves,itm_rhun_boots_balchoth,itm_nomad_bow,itm_arrows,itm_rhun_sword,itm_rhun_round_shield,itm_rhun_horse_a,itm_rhun_horse_b,],
      attr_evil_tier_4,wp_archery(180)|wp_throwing(180)|wp_melee(130),man_skills_4d,rhun_man1,rhun_man2],

["rhun_heavy_halberdier","Rhun_Heavy_Halberdier","Rhun_Heavy_Halberdiers",tf_evil_man| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rhun,
   [itm_rhun_helm_a,itm_rhun_armor_g,itm_leather_gloves,itm_rhun_greaves,itm_rhun_halberd,itm_rhun_dragon_shield,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,rhun_man1,rhun_man2],

["loke_gamp_rim","Loke-Gamp_Rim_Warrior","Loke-Gamp_Rim_Warriors",tf_evil_man| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rhun,
   [itm_rhun_helm_a,itm_rhun_armor_g,itm_leather_gloves,itm_rhun_greaves,itm_rhun_halberd,itm_rhun_dragon_shield,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,rhun_man1,rhun_man2],

["rhun_infantry","Rhun_Footman","Rhun_Footmen",tf_evil_man| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,0,fac_rhun,
   [itm_rhun_helm_m,itm_rhun_armor_j,itm_rhun_armor_m,itm_rhun_armor_n,itm_rhun_shoes,itm_rhun_sword,itm_rhun_axe,itm_rhun_spear,itm_rhun_round_shield,itm_rhun_infantry_shield,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,rhun_man1,rhun_man2],

["rhun_heavy_infantry","Rhun_Heavy_Infantryman","Rhun_Heavy_Infantrymen",tf_evil_man| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rhun,
   [itm_rhun_helm_b,itm_rhun_armor_h,itm_leather_gloves,itm_rhun_greaves,itm_rhun_sword,itm_rhun_axe,itm_rhun_dragon_shield,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,rhun_man1,rhun_man2],

["loke_flag_rim","Loke-Flag_Rim_Warrior","Loke-Flag_Rim_Warriors",tf_evil_man| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rhun,
   [itm_rhun_helm_b,itm_rhun_armor_h,itm_leather_gloves,itm_rhun_greaves,itm_rhun_sword,itm_rhun_axe,itm_rhun_dragon_shield,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,rhun_man1,rhun_man2],

["rhun_huntsman","Easterling_Huntsman","Easterling_Huntsmen",tf_evil_man| tfg_armor| tfg_boots| tfg_helm| tfg_ranged,0,0,fac_rhun,
   [itm_rhun_helm_k,itm_rhun_armor_a,itm_rhun_armor_b,itm_rhun_armor_d,itm_rhun_shoes,itm_nomad_bow,itm_arrows,itm_rhun_shortsword,],
      attr_evil_tier_2,wp_tier_2_a,man_skills_2b,rhun_man1,rhun_man2],

["rhun_archer","Rhun_Archer","Rhun_Archers",tf_evil_man| tfg_armor| tfg_boots| tfg_helm| tfg_ranged,0,0,fac_rhun,
   [itm_rhun_helm_m,itm_rhun_armor_j,itm_rhun_armor_m,itm_rhun_armor_n,itm_rhun_shoes,itm_nomad_bow,itm_arrows,itm_rhun_shortsword,],
      attr_evil_tier_3,wp_tier_3_a,man_skills_3b,rhun_man1,rhun_man2],

["rhun_heavy_archer","Rhun_Heavy_Archer","Rhun_Heavy_Archers",tf_evil_man| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_rhun,
   [itm_rhun_helm_c,itm_rhun_armor_g,itm_leather_gloves,itm_rhun_greaves,itm_rhun_dragon_bow,itm_rhun_dragon_arrows,itm_rhun_sword,],
      attr_evil_tier_4,wp_tier_4_a,man_skills_4b,rhun_man1,rhun_man2],

["loke_nar_rim","Loke-Nar_Rim_Archer","Loke-Nar_Rim_Archers",tf_evil_man| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_rhun,
   [itm_rhun_helm_c,itm_rhun_armor_g,itm_leather_gloves,itm_rhun_greaves,itm_rhun_dragon_bow,itm_rhun_dragon_arrows,itm_rhun_sword,],
      attr_evil_tier_5,wp_tier_5_a,man_skills_5b,rhun_man1,rhun_man2],

["rhun_scout","Easterling_Scout","Easterling_Scouts",tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_rhun_helm_k,itm_rhun_armor_a,itm_rhun_armor_b,itm_rhun_armor_d,itm_rhun_shoes,itm_rhun_sword,itm_nomad_bow,itm_arrows,itm_rhun_round_shield,itm_rhun_horse_a,itm_rhun_horse_b,],
      attr_evil_tier_2,wp_archery(90)|wp_throwing(90)|wp_melee(100),man_skills_2c,rhun_man1,rhun_man2],

["rhun_cavalry","Rhun_Cavalryman","Rhun_Cavalry",tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_rhun_helm_l,itm_rhun_armor_j,itm_rhun_armor_m,itm_rhun_armor_n,itm_rhun_shoes,itm_rhun_sword,itm_nomad_bow,itm_arrows,itm_rhun_round_shield,itm_rhun_horse_a,itm_rhun_horse_b,],
      attr_evil_tier_3,wp_archery(120)|wp_throwing(120)|wp_melee(150),man_skills_3c,rhun_man1,rhun_man2],

["rhun_heavy_cavalry","Rhun_Cataphract","Rhun_Cataphracts",tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_rhun_helm_i,itm_rhun_armor_p,itm_leather_gloves,itm_rhun_greaves,itm_rhun_sword,itm_rhun_axe,itm_rhun_lance,itm_rhun_dragon_cavalry_shield,itm_rhun_horse_g,itm_rhun_horse_h,],
      attr_evil_tier_4,wp_tier_4,man_skills_4c,rhun_man1,rhun_man2],

["loke_innas_rim","Loke-Innas_Rim_Cataphract","Loke-Innas_Rim_Cataphracts",tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_rhun_helm_i,itm_rhun_armor_p,itm_leather_gloves,itm_rhun_greaves,itm_rhun_sword,itm_rhun_axe,itm_rhun_lance,itm_rhun_dragon_cavalry_shield,itm_rhun_horse_g,itm_rhun_horse_h,],
      attr_evil_tier_5,wp_tier_5,man_skills_5c,rhun_man1,rhun_man2],

["balchoth_elite_cavalry","Balchoth_Elite_Horse_Archer","Balchoth_Elite_Horse_Archers",tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_ranged,0,0,fac_rhun,
   [itm_rhun_helm_e,itm_rhun_armor_o,itm_leather_gloves,itm_rhun_boots_balchoth,itm_nomad_bow,itm_arrows,itm_rhun_sword,itm_rhun_round_shield,itm_rhun_horse_a,itm_rhun_horse_b,],
      attr_evil_tier_5,wp_archery(230)| wp_throwing(230)|wp_melee(170),man_skills_5d,rhun_man1,rhun_man2],

["rhun_items","BUG","BUG",tf_hero,0,0,fac_rhun,
   [itm_saddle_horse,itm_easterling_cloth,itm_sumpter_horse,itm_rhun_greatsword,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

########################## DWARVES #############################

["dwarven_apprentice","Erebor_Apprentice","Erebor_Apprentices",tf_dwarf| tfg_armor| tfg_boots,0,0,fac_dwarf,
   [itm_dwarf_hood,itm_dwarf_helm_coif,itm_dwarf_miner,itm_dwarf_vest,itm_dwarf_vest1,itm_dwarf_pad_boots,itm_dwarf_adz,itm_dwarf_mattock,itm_dwarf_war_pick,],
      attr_dwarf_tier_1,wp_dwarf_tier_1,dwarf_skills_1a,dwarf_face_young_1,dwarf_face_young_2],

["dwarven_warrior","Erebor_Watchman","Erebor_Watchmen",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_b,itm_dwarf_armor_a,itm_dwarf_armor_b,itm_dwarf_pad_boots,itm_dwarf_spear,itm_dwarf_sword_a,itm_dwarf_hand_axe,itm_dwarf_throwing_axe,itm_dwarf_shield_a,itm_dwarf_shield_b,],
      attr_dwarf_tier_2,wp_dwarf_tier_2,dwarf_skills_2a,dwarf_face_young_1,dwarf_face_young_2],

["dwarven_hardened_warrior","Erebor_Footman","Erebor_Footmen",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_b,itm_dwarf_armor_c,itm_leather_gloves,itm_dwarf_pad_boots,itm_dwarf_spear,itm_dwarf_sword_b,itm_dwarf_hand_axe,itm_dwarf_great_pick,itm_dwarf_throwing_axe,itm_dwarf_shield_a,itm_dwarf_shield_b,],
      attr_dwarf_tier_3,wp_dwarf_tier_3,dwarf_skills_3a,dwarf_face_young_1,dwarf_face_young_2],

["dwarven_axeman","Erebor_Warrior","Erebor_Warriors",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_j,itm_dwarf_armor_g,itm_leather_gloves,itm_dwarf_chain_boots,itm_dwarf_great_pick,itm_dwarf_great_axe,itm_dwarf_warhammer,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_4,wp_dwarf_tier_4,dwarf_skills_4a,dwarf_face_old_1,dwarf_face_old_2],

["dwarven_expert_axeman","Erebor_Veteran_Warrior","Erebor_Veteran_Warrior",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_j,itm_dwarf_armor_j,itm_dwarf_gloves,itm_dwarf_scale_boots,itm_dwarf_great_pick,itm_dwarf_great_axe,itm_dwarf_warhammer,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_5,wp_dwarf_tier_5,dwarf_skills_5a,dwarf_face_old_1,dwarf_face_old_2],

["longbeard_axeman","Thror's_Guard","Thror's_Guards",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_r,itm_dwarf_armor_l,itm_dwarf_gloves,itm_erebor_guard_boots,itm_dwarf_great_pick,itm_dwarf_great_axe,itm_dwarf_warhammer,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_6,wp_dwarf_tier_6,dwarf_skills_6a,dwarf_face_old_1,dwarf_face_old_2],

["dwarven_spearman","Erebor_Hoplite","Erebor_Hoplites",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_polearm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_j,itm_dwarf_armor_g,itm_leather_gloves,itm_dwarf_chain_boots,itm_dwarf_spear_b,itm_dwarf_sword_b,itm_dwarf_hand_axe,itm_dwarf_shield_c,],
      attr_dwarf_tier_4,wp_dwarf_tier_4,dwarf_skills_4a,dwarf_face_old_1,dwarf_face_old_2],

["dwarven_pikeman","Erebor_Veteran_Hoplite","Erebor_Veteran_Hoplites",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_polearm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_j,itm_dwarf_armor_j,itm_dwarf_gloves,itm_dwarf_scale_boots,itm_dwarf_spear_b,itm_dwarf_sword_b,itm_dwarf_hand_axe,itm_dwarf_shield_c,],
      attr_dwarf_tier_5,wp_dwarf_tier_5,dwarf_skills_5a,dwarf_face_old_1,dwarf_face_old_2],

["dwarven_halberdier","Fror's_Guard","Fror's_Guards",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_polearm,0,0,fac_dwarf,
   [itm_free_dwarf_helm_r,itm_dwarf_armor_l,itm_dwarf_gloves,itm_erebor_guard_boots,itm_dwarf_spear_b,itm_dwarf_sword_b,itm_dwarf_hand_axe,itm_dwarf_shield_f,],
      attr_dwarf_tier_6,wp_dwarf_tier_6,dwarf_skills_6a,dwarf_face_old_1,dwarf_face_old_2],

["dwarven_lookout","Erebor_Scout","Erebor_Scouts",tf_dwarf| tfg_armor| tfg_boots| tfg_helm| tfg_ranged,0,0,fac_dwarf,
   [itm_free_dwarf_helm_b,itm_dwarf_armor_a,itm_dwarf_armor_b,itm_dwarf_pad_boots,itm_dwarf_short_bow,itm_dwarf_bolts,itm_dwarf_sword_a,itm_dwarf_hand_axe,],
      attr_dwarf_tier_2,wp_dwarf_tier_2_a,dwarf_skills_2b,dwarf_face_young_1,dwarf_face_young_2],

["dwarven_scout","Erebor_Shooter","Erebor_Shooters",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_dwarf,
   [itm_free_dwarf_helm_b,itm_dwarf_armor_c,itm_leather_gloves,itm_dwarf_pad_boots,itm_dwarf_short_bow,itm_dwarf_bolts,itm_dwarf_sword_b,itm_dwarf_hand_axe,],
      attr_dwarf_tier_3,wp_dwarf_tier_3_a,dwarf_skills_3b,dwarf_face_young_1,dwarf_face_young_2],

["dwarven_bowman","Erebor_Crossbowman","Erebor_Crossbowmen",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_dwarf,
   [itm_free_dwarf_helm_j,itm_dwarf_armor_g,itm_leather_gloves,itm_dwarf_chain_boots,itm_dwarf_short_bow,itm_dwarf_bolts,itm_dwarf_sword_b,itm_dwarf_hand_axe,],
      attr_dwarf_tier_4,wp_dwarf_tier_4_a,dwarf_skills_4b,dwarf_face_old_1,dwarf_face_old_2],

["dwarven_archer","Erebor_Veteran_Crossbowman","Erebor_Veteran_Crossbowmen",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_dwarf,
   [itm_free_dwarf_helm_j,itm_dwarf_armor_j,itm_dwarf_gloves,itm_dwarf_scale_boots,(itm_dwarf_short_bow,imod_fine),itm_dwarf_heavy_bolts,itm_dwarf_sword_b,itm_dwarf_hand_axe,],
      attr_dwarf_tier_5,wp_dwarf_tier_5_a,dwarf_skills_5b,dwarf_face_old_1,dwarf_face_old_2],

["marksman_of_ravenhill","Marksman_of_Ravenhill","Marksmen_of_Ravenhill",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_dwarf,
   [itm_free_dwarf_helm_r,itm_dwarf_armor_l,itm_dwarf_gloves,itm_erebor_guard_boots,(itm_dwarf_short_bow,imod_strong),itm_dwarf_heavy_bolts,itm_dwarf_sword_b,itm_dwarf_hand_axe,],
      attr_dwarf_tier_6,wp_dwarf_tier_6_a,dwarf_skills_6b,dwarf_face_old_1,dwarf_face_old_2],

## Iron Hills ##

["iron_hills_miner","Iron_Hills_Miner","Iron_Hills_Miners",tf_dwarf| tfg_armor| tfg_boots,0,subfac_ironhills,fac_dwarf,
   [itm_dwarf_hood,itm_dwarf_helm_coif,itm_dwarf_miner,itm_dwarf_vest_a,itm_dwarf_vest_b,itm_dwarf_pad_boots,itm_dwarf_adz,itm_dwarf_mattock,itm_dwarf_war_pick,],
      attr_dwarf_tier_1,wp_dwarf_tier_1,dwarf_skills_1a,dwarf_face_young_1,dwarf_face_young_2],

["iron_hills_watchman","Iron_Hills_Watchman","Iron_Hills_Watchmen",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_c,itm_leather_dwarf_armor,itm_leather_dwarf_armor_b,itm_dwarf_pad_boots,itm_dwarf_spear,itm_dwarf_sword_a,itm_ironhills_hand_axe,itm_dwarf_throwing_axe,itm_dwarf_shield_a,itm_dwarf_shield_b,],
      attr_dwarf_tier_2,wp_dwarf_tier_2,dwarf_skills_2a,dwarf_face_young_1,dwarf_face_young_2],

["iron_hills_infantry","Iron_Hills_Footman","Iron_Hills_Footmen",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_c,itm_dwarf_armor_d,itm_dwarf_armor_e,itm_leather_gloves,itm_dwarf_pad_boots,itm_dwarf_spear,itm_dwarf_sword_c,itm_ironhills_hand_axe,itm_dwarf_great_mattock,itm_dwarf_throwing_axe,itm_dwarf_shield_a,itm_dwarf_shield_b,],
      attr_dwarf_tier_3,wp_dwarf_tier_3,dwarf_skills_3a,dwarf_face_young_1,dwarf_face_young_2],

["iron_hills_battle_infantry","Iron_Hills_Warrior","Iron_Hills_Warriors",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_o,itm_dwarf_armor_h,itm_dwarf_armor_i,itm_leather_gloves,itm_dwarf_chain_boots,itm_dwarf_great_mattock,itm_ironhills_great_axe,itm_dwarf_warhammer,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_4,wp_dwarf_tier_4,dwarf_skills_4a,dwarf_face_old_1,dwarf_face_old_2],

["iron_hills_heavy_infantry","Iron_Hills_Veteran_Warrior","Iron_Hills_Veteran_Warriors",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_o,itm_dwarf_armor_k,itm_dwarf_gloves,itm_ironhills_scale_boots,itm_dwarf_great_mattock,itm_ironhills_great_axe,itm_dwarf_warhammer,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_5,wp_dwarf_tier_5,dwarf_skills_5a,dwarf_face_old_1,dwarf_face_old_2],

["grors_guard","Gror's_Guard","Gror's_Guards",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_v,itm_dwarf_armor_m,itm_dwarf_gloves,itm_iron_guard_boots,itm_dwarf_great_mattock,itm_ironhills_great_axe,itm_dwarf_warhammer,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_6,wp_dwarf_tier_6,dwarf_skills_6a,dwarf_face_old_1,dwarf_face_old_2],

["iron_hills_spearman","Iron_Hills_Hoplite","Iron_Hills_Hoplites",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_polearm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_o,itm_dwarf_armor_h,itm_dwarf_armor_i,itm_leather_gloves,itm_dwarf_chain_boots,itm_dwarf_spear_c,itm_dwarf_sword_c,itm_ironhills_hand_axe,itm_dwarf_shield_d,],
      attr_dwarf_tier_4,wp_dwarf_tier_4,dwarf_skills_4a,dwarf_face_old_1,dwarf_face_old_2],

["iron_hills_pikeman","Iron_Hills_Veteran_Hoplite","Iron_Hills_Veteran_Hoplites",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_polearm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_o,itm_dwarf_armor_k,itm_dwarf_gloves,itm_ironhills_scale_boots,itm_dwarf_spear_c,itm_dwarf_sword_c,itm_ironhills_hand_axe,itm_dwarf_shield_d,],
      attr_dwarf_tier_5,wp_dwarf_tier_5,dwarf_skills_5a,dwarf_face_old_1,dwarf_face_old_2],

["iron_hills_halberdier","Nain's_Guard","Nain's_Guards",tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_polearm,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_v,itm_dwarf_armor_m,itm_dwarf_gloves,itm_iron_guard_boots,itm_dwarf_spear_c,itm_dwarf_sword_c,itm_ironhills_hand_axe,itm_dwarf_shield_d,],
      attr_dwarf_tier_6,wp_dwarf_tier_6,dwarf_skills_6a,dwarf_face_old_1,dwarf_face_old_2],

["iron_hills_lookout","Iron_Hills_Scout","Iron_Hills_Scouts",tf_dwarf| tfg_armor| tfg_boots| tfg_helm| tfg_ranged,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_c,itm_leather_dwarf_armor,itm_leather_dwarf_armor_b,itm_dwarf_pad_boots,itm_dwarf_short_bow,itm_dwarf_bolts,itm_dwarf_sword_a,itm_ironhills_hand_axe,],
      attr_dwarf_tier_2,wp_dwarf_tier_2_a,dwarf_skills_2b,dwarf_face_young_1,dwarf_face_young_2],

["iron_hills_scout","Iron_Hills_Shooter","Iron_Hills_Shooters",tf_dwarf| tfg_ranged| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_c,itm_dwarf_armor_d,itm_dwarf_armor_e,itm_leather_gloves,itm_dwarf_pad_boots,itm_dwarf_short_bow,itm_dwarf_bolts,itm_dwarf_sword_c,itm_ironhills_hand_axe],
      attr_dwarf_tier_3,wp_dwarf_tier_3_a,dwarf_skills_3b,dwarf_face_young_1,dwarf_face_young_2],

["iron_hills_bowman","Iron_Hills_Crossbowman","Iron_Hills_Crossbowmen",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_o,itm_dwarf_armor_h,itm_dwarf_armor_i,itm_leather_gloves,itm_dwarf_chain_boots,itm_dwarf_short_bow,itm_dwarf_bolts,itm_dwarf_sword_c,itm_ironhills_hand_axe,],
      attr_dwarf_tier_4,wp_dwarf_tier_4_a,dwarf_skills_4b,dwarf_face_old_1,dwarf_face_old_2],

["iron_hills_archer","Iron_Hills_Veteran_Crossbowman","Iron_Hills_Veteran_Crossbowmen",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_o,itm_dwarf_armor_k,itm_dwarf_gloves,itm_ironhills_scale_boots,(itm_dwarf_short_bow,imod_fine),itm_dwarf_heavy_bolts,itm_dwarf_sword_c,itm_ironhills_hand_axe,],
      attr_dwarf_tier_5,wp_dwarf_tier_5_a,dwarf_skills_5b,dwarf_face_old_1,dwarf_face_old_2],

["iron_hills_marksman","Iron_Guard_Marksman","Iron_Guard_Marksmen",tf_dwarf| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_ironhills,fac_dwarf,
   [itm_free_dwarf_helm_v,itm_dwarf_armor_m,itm_dwarf_gloves,itm_iron_guard_boots,(itm_dwarf_short_bow,imod_strong),itm_dwarf_heavy_bolts,itm_dwarf_sword_c,itm_ironhills_hand_axe,],
      attr_dwarf_tier_6,wp_dwarf_tier_6_a,dwarf_skills_6b,dwarf_face_old_1,dwarf_face_old_2],

["dwarf_items","BUG","_",tf_hero,0,0,fac_dwarf,
   [itm_pony,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,itm_mail_mittens,itm_dwarf_mace,],
      0,0,0,0],

#GONDOR

["gondor_commoner","Gondor_Levy","Gondor_Levies",tf_gondor| tfg_armor| tfg_boots,0,0,fac_gondor,
   [itm_gondor_light_helm,itm_gon_jerkin,itm_black_tunic,itm_leather_boots,itm_gondor_short_sword,itm_spear,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_young_1,gondor_face_young_2],

["gondor_militiamen","Gondor_Militia","Gondor_Militia",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_mail,itm_leather_gloves_black,itm_leather_boots,itm_gondor_short_sword,itm_spear,itm_gondor_javelin,itm_gon_tab_shield_a,],
      attr_tier_2,wp_gondor_tier_2,man_skills_2a,gondor_face_young_1,gondor_face_young_2],

["footmen_of_gondor","Footman_of_Gondor","Footmen_of_Gondor",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gondor_helm,itm_gondor_heavy_mail,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_spear,itm_gondor_sword,itm_gondor_shield_a,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3a,gondor_face_middle_1,gondor_face_middle_2],

#Gondor spearmen
["gondor_spearmen","Spearman_of_Gondor","Spearmen_of_Gondor",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_spear,itm_gondor_shield_a,],
      attr_tier_4,wp_gondor_tier_4,man_skills_4a,gondor_face_middle_1,gondor_face_middle_2],

["gondor_veteran_spearmen","Veteran_Spearman_of_Gondor","Veteran_Spearmen_of_Gondor",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_spear,itm_gondor_shield_a,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5a,gondor_face_old_1,gondor_face_old_2],

["guard_of_the_fountain_court","Guard_of_the_Fountain_Court","Guards_of_the_Fountain_Court",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_fountain_guard_helm,itm_gon_fountain_guard,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_fountain_spear,],
      attr_tier_6,wp_gondor_tier_6,knows_common|knows_ironflesh_6|knows_power_strike_6|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_4|knows_riding_1,gondor_face_old_1,gondor_face_old_2],

#Gondor swordsmen
["gondor_swordsmen","Swordsman_of_Gondor","Swordsmen_of_Gondor",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_sword,itm_gondor_shield_a,],
      attr_tier_4,wp_gondor_tier_4,man_skills_4a,gondor_face_middle_1,gondor_face_middle_2],

["gondor_veteran_swordsmen","Veteran_Swordsman_of_Gondor","Veteran_Swordsmen_of_Gondor",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_sword,itm_gondor_shield_a,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5a,gondor_face_old_1,gondor_face_old_2],

["swordsmen_of_the_tower_guard","Swordsman_of_the_Citadel","Swordsmen_of_the_Citadel",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gon_citadel_guard_helm,itm_gon_citadel_guard,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gondor_shield_c,],
      attr_tier_6,wp_gondor_tier_6,man_skills_6a,gondor_face_old_1,gondor_face_old_2],

#Gondor Noble Line
["gondor_noblemen","Gondor_Nobleman","Gondor_Noblemen",tf_gondor| tfg_armor| tfg_boots,0,0,fac_gondor,
   [itm_gon_noble_cloak,itm_leather_boots,itm_gondor_cav_sword,],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_young_1,gondor_face_young_2],

["squire_of_gondor","Squire_of_Gondor","Squires_of_Gondor",tf_gondor| tf_mounted| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_mail,itm_leather_gloves_black,itm_leather_boots,itm_gondor_cav_sword,itm_gon_tab_shield_a,itm_gondor_courser],
      attr_tier_2,wp_gondor_tier_2,man_skills_2c,gondor_face_young_1,gondor_face_young_2],

["veteran_squire_of_gondor","Horseman_of_Gondor","Horsemen_of_Gondor",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gondor_helm,itm_gondor_heavy_mail,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_cav_sword,itm_gondor_lance,itm_gondor_shield_d,itm_gondor_hunter,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3c,gondor_face_middle_2],

["knight_of_gondor","Knight_of_Gondor","Knights_of_Gondor",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_cav_sword,itm_gondor_lance,itm_gondor_shield_d,itm_gondor_hunter,],
      attr_tier_4,wp_gondor_tier_4,man_skills_4c,gondor_face_middle_1,gondor_face_middle_2],

["veteran_knight_of_gondor","Veteran_Knight_of_Gondor","Veteran_Knights_of_Gondor",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_cav_sword,itm_gondor_lance,itm_gondor_shield_d,itm_gondor_warhorse,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5c,gondor_face_old_1,gondor_face_old_2],

["knight_of_the_citadel","Knight_of_the_Citadel","Knights_of_the_Citadel",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_citadel_guard_helm,itm_gon_citadel_guard,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gondor_lance_banner,itm_gondor_shield_d,itm_gondor_guard_warhorse,],
      attr_tier_6,wp_gondor_tier_6,man_skills_6c,gondor_face_old_1,gondor_face_old_2],

#Gondor Archers
["gondor_bow_militia","Gondor_Bow_Militia","Gondor_Bow_Militia",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_mail,itm_leather_gloves_black,itm_leather_boots,itm_short_bow,itm_gondor_arrows,itm_gondor_short_sword,],
      attr_tier_2,wp_gondor_tier_2_a,man_skills_2b,gondor_face_young_1,gondor_face_young_2],

["bowmen_of_gondor","Bowman_of_Gondor","Bowmen_of_Gondor",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_gondor,
   [itm_gondor_helm,itm_gondor_heavy_mail,itm_leather_gloves_black,itm_gondor_greaves,itm_numenor_bow,itm_gondor_arrows,itm_gondor_sword,],
      attr_tier_3,wp_gondor_tier_3_a,man_skills_3b,gondor_face_middle_1,gondor_face_middle_2],

["archer_of_gondor","Archer_of_Gondor","Archers_of_Gondor",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_numenor_bow,itm_gondor_arrows,itm_gondor_sword,],
      attr_tier_4,wp_gondor_tier_4_a,man_skills_4b,gondor_face_middle_1,gondor_face_middle_2],

["veteran_archer_of_gondor","Veteran_Archer_of_Gondor","Veteran_Archers_of_Gondor",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_gondor,
   [itm_gondor_helm,itm_gon_plate,itm_leather_gloves_black,itm_gondor_greaves,itm_numenor_bow,itm_gondor_arrows,itm_gondor_sword,],
      attr_tier_5,wp_gondor_tier_5_a,man_skills_5b,gondor_face_old_1,gondor_face_old_2],

["archer_of_the_tower_guard","Archer_of_the_Tower_Guard","Archers_of_the_Tower_Guard",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_gondor,
   [itm_gon_citadel_guard_helm,itm_gon_citadel_guard,itm_leather_gloves_black,itm_gondor_greaves,itm_numenor_bow,itm_gondor_arrows,itm_gondor_guard_sword,],
      attr_tier_6,wp_gondor_tier_6_a,man_skills_6b,gondor_face_old_1,gondor_face_old_2],

# Denetor guars (Spearmen of the Citadel)
["steward_guard","Spearman_of_the_Citadel","Spearmen_of_the_Citadel",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_gondor,
   [itm_gon_citadel_guard_helm,itm_gon_citadel_guard,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_spear,itm_gondor_shield_c,],
      attr_tier_6,wp_gondor_tier_6,man_skills_6a,gondor_face_old_1,gondor_face_old_2],

#RANGERS
["ranger_of_ithilien","Ranger_of_Ithilien","Rangers_of_Ithilien",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_ranged,0,subfac_rangers,fac_gondor,
   [itm_gon_ranger_cloak,itm_leather_gloves,itm_leather_boots,itm_numenor_bow,itm_ithilien_arrows,itm_gondor_sword,],
      attr_tier_4,wp_archery(220)|wp(180),knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_6|knows_riding_1|knows_pathfinding_1,gondor_face_middle_1,gondor_face_middle_2],

["veteran_ranger_of_ithilien","Veteran_Ranger_of_Ithilien","Veteran_Rangers_of_Ithilien",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_rangers,fac_gondor,
   [itm_gondor_ranger_hood,itm_gon_ranger_cloak,itm_leather_gloves,itm_leather_boots,itm_numenor_bow,itm_ithilien_arrows,itm_gondor_bastard_sword,],
      attr_tier_5,wp_archery(270)|wp(230),knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_shield_2|knows_athletics_7|knows_riding_1|knows_pathfinding_2,gondor_face_old_1,gondor_face_old_2],

["master_ranger_of_ithilien","Master_Ranger_of_Ithilien","Master_Rangers_of_Ithilien",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_rangers,fac_gondor,
   [itm_gondor_ranger_hood_mask,itm_gon_ranger_cloak,itm_leather_gloves,itm_leather_boots,itm_numenor_bow,itm_ithilien_arrows,itm_gondor_bastard_sword,],
      attr_tier_6,wp_archery(320)|wp(280),knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_shield_3|knows_athletics_8|knows_riding_1|knows_pathfinding_3,gondor_face_old_1,gondor_face_old_2],

["ithilien_leader","Captain_of_Ithilien_Rangers","Captains_of_Ithilien_Rangers",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_rangers,fac_gondor,
   [itm_gondor_ranger_hood,itm_gon_ranger_skirt,itm_leather_gloves,itm_leather_boots,itm_numenor_bow,itm_ithilien_arrows,itm_gondor_bastard_sword,],
      attr_tier_7,wp_archery(360)|wp(320),knows_common|knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_shield_6|knows_athletics_8|knows_riding_1|knows_pathfinding_4,gondor_face_old_1,gondor_face_old_2],

#Lossarnach#######
["woodsman_of_lossarnach","Woodsman_of_Lossarnach","Woodsmen_of_Lossarnach",tf_gondor| tfg_armor| tfg_boots,0,subfac_lossarnach,fac_gondor,
   [itm_lossarnach_cloth_cap,itm_lossarnach_shirt,itm_leather_boots,itm_loss_axe,],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_loss_1,gondor_face_loss_2],

["footman_of_lossarnach","Footman_of_Lossarnach","Footmen_of_Lossarnach",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,subfac_lossarnach,fac_gondor,
   [itm_lossarnach_leather_cap,itm_lossarnach_footman,itm_leather_boots,itm_loss_axe,itm_loss_throwing_axes,itm_gon_tab_shield_a,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3a,gondor_face_loss_2,gondor_face_loss_2],

["axeman_of_lossarnach","Lossarnach_Axeman","Lossarnach_Axemen",tf_gondor| tfg_armor| tfg_boots| tfg_helm,0,subfac_lossarnach,fac_gondor,
   [itm_lossarnach_leather_cap,itm_lossarnach_warrior,itm_leather_boots,itm_loss_war_axe,itm_loss_throwing_axes,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3a,gondor_face_loss_1,gondor_face_loss_2],

["heavy_footman_of_lossarnach","Heavy_Footman_of_Lossarnach","Heavy_Footmen_of_Lossarnach",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_lossarnach,fac_gondor,
   [itm_lossarnach_scale_cap,itm_lossarnach_heavy_footman,itm_leather_gloves,itm_lossarnach_greaves,itm_loss_axe,itm_loss_throwing_axes,itm_gon_tab_shield_a,],
      attr_tier_5,wp_gondor_tier_5,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_1,gondor_face_loss_1,gondor_face_loss_2],

["heavy_axeman_of_lossarnach","Heavy_Axeman_of_Lossarnach","Heavy_Axemen_of_Lossarnach",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,subfac_lossarnach,fac_gondor,
   [itm_lossarnach_scale_cap,itm_lossarnach_heavy_warrior,itm_leather_gloves,itm_lossarnach_greaves,itm_loss_war_axe,itm_loss_throwing_axes,],
      attr_tier_5,wp_gondor_tier_5,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_1,gondor_face_loss_1,gondor_face_loss_2],

["lossarnach_leader","Captain_of_Lossarnach","Captains_of_Lossarnach",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_lossarnach,fac_gondor,
   [itm_lossarnach_scale_cap,itm_lossarnach_leader,itm_leather_gloves,itm_lossarnach_greaves,itm_gondor_cav_sword,itm_loss_axe,itm_gon_tab_shield_a,],
      attr_tier_6,wp_gondor_tier_6,knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5|knows_power_draw_1|knows_shield_5|knows_athletics_4|knows_riding_1,gondor_face_loss_1,gondor_face_loss_2],

####PELARGIR
["pelargir_watchman","Pelargir_Levy","Pelargir_Levies",tf_gondor| tfg_armor| tfg_boots,0,subfac_pelargir,fac_gondor,
   [itm_pel_jerkin,itm_leather_boots,itm_shortened_spear,itm_pelargir_eket],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_young_1,gondor_face_young_2],

["pelargir_marine","Pelargir_Marine","Pelargir_Marines",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_pelargir,fac_gondor,
   [itm_pelargir_hood,itm_pel_marine,itm_leather_gloves_black,itm_leather_boots,itm_gondor_javelin,itm_pelargir_eket,itm_gon_tab_shield_a,],
      attr_tier_3,wp_gondor_tier_3_a,man_skills_3b,gondor_face_middle_1,gondor_face_middle_2,],

["pelargir_vet_marine","Pelargir_Veteran_Marine","Pelargir_Veteran_Marine",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_pelargir,fac_gondor,
   [itm_pelargir_hood,itm_pel_marine,itm_leather_gloves_black,itm_leather_boots,itm_gondor_javelin,itm_pelargir_sword,itm_gon_tab_shield_a,],
      attr_tier_5,wp_gondor_tier_5_a,man_skills_5b,gondor_face_old_1,gondor_face_old_2,],

["pelargir_infantry","Pelargir_Infantryman","Pelargir_Infantrymen",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_pelargir,fac_gondor,
   [itm_pelargir_helmet_heavy,itm_pel_footman,itm_leather_gloves_black,itm_leather_boots,itm_pelargir_sword,itm_gondor_spear,itm_gon_tab_shield_c,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3a,gondor_face_middle_1,gondor_face_middle_2,],

["pelargir_vet_infantry","Pelargir_Veteran_Infantryman","Pelargir_Veteran_Infantrymen",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_pelargir,fac_gondor,
   [itm_pelargir_helmet_heavy,itm_pel_footman,itm_leather_gloves_black,itm_gondor_greaves,itm_pelargir_sword,itm_gondor_spear,itm_gon_tab_shield_c,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5a,gondor_face_old_1,gondor_face_old_2,],

["pelargir_leader","Captain_of_Pelargir","Captains_of_Pelargir",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_pelargir,fac_gondor,
   [itm_pelargir_helmet_heavy,itm_pel_footman,itm_leather_gloves_black,itm_gondor_greaves,itm_pelargir_sword,itm_gon_tab_shield_c,],
      attr_tier_6,wp_gondor_tier_6,man_skills_6a,gondor_face_old_1,gondor_face_old_2,],

["pelargir_marine_leader","Captain_of_Pelargir_Marines","Captains_of_Pelargir_Marines",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_pelargir,fac_gondor,
   [itm_pelargir_hood,itm_pel_marine,itm_leather_gloves_black,itm_leather_boots,itm_pelargir_sword,itm_gon_tab_shield_c,],
      attr_tier_6,wp_gondor_tier_6_a,man_skills_6b,gondor_face_old_1,gondor_face_old_2,],

#Lamedon#######
["clansman_of_lamedon","Clansman_of_Lamedon","Clansmen_of_Lamedon",tf_gondor| tfg_armor| tfg_boots,0,subfac_ethring,fac_gondor,
   [itm_lamedon_jerkin,itm_leather_boots,itm_loss_axe,itm_shortened_spear,],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_young_1,gondor_face_young_2,],

["footman_of_lamedon","Footman_of_Lamedon","Footmen_of_Lamedon",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,subfac_ethring,fac_gondor,
   [itm_lamedon_hood,itm_lamedon_jerkin,itm_leather_boots,itm_spear,itm_loss_axe,itm_gon_tab_shield_a,],
      attr_tier_2,wp_gondor_tier_2,man_skills_2a,gondor_face_young_1,gondor_face_young_2,],

["warrior_of_lamedon","Warrior_of_Lamedon","Warriors_of_Lamedon",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,subfac_ethring,fac_gondor,
   [itm_gondor_light_helm,itm_lamedon_veteran,itm_leather_boots,itm_loss_axe,itm_gondor_sword,itm_spear,itm_gon_tab_shield_a,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3a,gondor_face_middle_1,gondor_face_middle_2,],

["veteran_of_lamedon","Veteran_Warrior_of_Lamedon","Veteran_Warriors_of_Lamedon",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_ethring,fac_gondor,
   [itm_gondor_helm,itm_lamedon_warrior,itm_leather_gloves_black,itm_leather_boots,itm_loss_axe,itm_gondor_sword,itm_gondor_spear,itm_gon_tab_shield_c,],
      attr_tier_4,wp_gondor_tier_4,man_skills_4a,gondor_face_middle_1,gondor_face_middle_2,],

["champion_of_lamedon","Champion_of_Lamedon","Champions_of_Lamedon",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_ethring,fac_gondor,
   [itm_gondor_helm,itm_lamedon_heavy_mail,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_bastard_sword,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5a,gondor_face_old_1,gondor_face_old_2,],

["knight_of_lamedon","Knight_of_Lamedon","Knights_of_Lamedon",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,subfac_ethring,fac_gondor,
   [itm_gon_lord_helmet,itm_lamedon_heavy_mail,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_cav_sword,itm_gondor_lance,itm_gon_tab_shield_c,itm_gondor_lam_horse,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5c,gondor_face_old_1,gondor_face_old_2,],

["lamedon_leader","Captain_of_Lamedon","Captains_of_Lamedon",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,subfac_ethring,fac_gondor,
   [itm_gon_lord_helmet,itm_lamedon_leader,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_cav_sword,itm_gon_tab_shield_c,itm_gondor_lam_horse,],
      attr_tier_6,wp_gondor_tier_6,man_skills_6c,gondor_face_old_1,gondor_face_old_2,],

#Pinnath Gelin####
["pinnath_gelin_plainsman","Plainsman_of_Pinnath_Gelin","Plainsmen_of_Pinnath_Gelin",tf_gondor| tfg_armor| tfg_boots,0,subfac_pinnath_gelin,fac_gondor,
   [itm_pinnath_gambeson,itm_leather_boots,itm_shortened_spear,itm_short_bow,itm_arrows,],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_young_1,gondor_face_young_2,],

["pinnath_gelin_spearman","Footman_of_Pinnath_Gelin","Footmen_of_Pinnath_Gelin",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_pinnath_gelin,fac_gondor,
   [itm_gondor_light_helm,itm_pinnath_footman,itm_leather_gloves_black,itm_leather_boots,itm_spear,itm_gondor_sword,itm_gon_tab_shield_a,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3a,gondor_face_middle_1,gondor_face_middle_2,],

["warrior_of_pinnath_gelin","Warrior_of_Pinnath_Gelin","Warriors_of_Pinnath_Gelin",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_pinnath_gelin,fac_gondor,
   [itm_gondor_helm,itm_pinnath_warrior,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_spear,itm_gondor_sword,itm_gon_tab_shield_a,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5a,gondor_face_old_1,gondor_face_old_2,],

["pinnath_gelin_bowman","Bowman_of_Pinnath_Gelin","Bowmen_of_Pinnath_Gelin",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_pinnath_gelin,fac_gondor,
   [itm_gondor_ranger_hood,itm_pinnath_bowman,itm_leather_gloves_black,itm_leather_boots,itm_numenor_bow,itm_gondor_arrows,itm_gondor_short_sword,],
      attr_tier_3,wp_gondor_tier_3_a,man_skills_3b,gondor_face_middle_1,gondor_face_middle_2,],

["pinnath_gelin_archer","Archer_of_Pinnath_Gelin","Archers_of_Pinnath_Gelin",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_pinnath_gelin,fac_gondor,
   [itm_gondor_ranger_hood,itm_pinnath_archer,itm_leather_gloves_black,itm_gondor_greaves,itm_numenor_bow,itm_gondor_arrows,itm_gondor_sword,],
      attr_tier_5,wp_gondor_tier_5_a,man_skills_5b,gondor_face_old_1,gondor_face_old_2,],

["pinnath_leader","Captain_of_Pinnath_Gelin","Captains_of_Pinnath_Gelin",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,subfac_pinnath_gelin,fac_gondor,
   [itm_gon_lord_helmet,itm_pinnath_leader,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_cav_sword,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_6,wp_gondor_tier_6,man_skills_6c,gondor_face_old_1,gondor_face_old_2,],

#####Black Root Vale#####
["blackroot_vale_archer","Hunter_of_Blackroot_Vale","Hunter_of_Blackroot_Vale",tf_gondor|  tfg_armor|  tfg_boots,0,subfac_blackroot,fac_gondor,
   [itm_blackroot_jerkin,itm_leather_boots,itm_shortened_spear,itm_short_bow,itm_arrows,],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_young_1,gondor_face_young_2,],

["veteran_blackroot_vale_archer","Bowman_of_Blackroot_Vale","Bowmen_of_Blackroot_Vale",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_blackroot,fac_gondor,
   [itm_blackroot_hood,itm_blackroot_bowman,itm_leather_gloves_black,itm_leather_boots,itm_numenor_bow,itm_gondor_arrows,itm_gondor_short_sword,],
      attr_tier_3,wp_gondor_tier_3_a,man_skills_3b,gondor_face_middle_1,gondor_face_middle_2,],

["master_blackroot_vale_archer","Archer_of_Blackroot_Vale","Archers_of_Blackroot_Vale",tf_gondor| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,subfac_blackroot,fac_gondor,
   [itm_blackroot_hood,itm_blackroot_archer,itm_leather_gloves_black,itm_gondor_greaves,itm_numenor_bow,itm_gondor_arrows,itm_gondor_sword,],
      attr_tier_5,wp_gondor_tier_5_a,man_skills_5b,gondor_face_old_1,gondor_face_old_2,],

["footman_of_blackroot_vale","Footman_of_Blackroot_Vale","Footmen_of_Blackroot_Vale",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_blackroot,fac_gondor,
   [itm_gondor_light_helm,itm_blackroot_footman,itm_leather_gloves_black,itm_leather_boots,itm_spear,itm_gondor_sword,itm_gon_tab_shield_a,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3a,gondor_face_middle_1,gondor_face_middle_2,],

["spearman_of_blackroot_vale","Warrior_of_Blackroot_Vale","Warriors_of_Blackroot_Vale",tf_gondor| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,subfac_blackroot,fac_gondor,
   [itm_gondor_helm,itm_blackroot_warrior,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_spear,itm_gondor_sword,itm_gon_tab_shield_a,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5a,gondor_face_old_1,gondor_face_old_2,],

["blackroot_leader","Captain_of_Blackroot_Vale","Captains_of_Blackroot_Vale",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,subfac_blackroot,fac_gondor,
   [itm_gon_lord_helmet,itm_blackroot_leader,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_cav_sword,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_6,wp_gondor_tier_6,man_skills_6c,gondor_face_old_1,gondor_face_old_2,],

###Dol Amroth#####
["dol_amroth_youth","Dol_Amroth_Recruit","Dol_Amroth_Recruits",tf_gondor| tfg_armor| tfg_shield| tfg_boots,0,subfac_dol_amroth,fac_gondor,
   [itm_dol_shirt,itm_dol_shoes,itm_amroth_sword_a,itm_spear,itm_gon_tab_shield_a,],
      attr_tier_1,wp_gondor_tier_1,man_skills_1a,gondor_face_young_1,gondor_face_young_2,],

["squire_of_dol_amroth","Squire_of_Dol_Amroth","Squires_of_Dol_Amroth",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_horse,0,subfac_dol_amroth,fac_gondor,
   [itm_gondor_light_helm,itm_dol_padded_coat,itm_dol_shoes,itm_amroth_sword_a,itm_gon_tab_shield_c,itm_gondor_courser,],
      attr_tier_2,wp_gondor_tier_2,man_skills_2c,gondor_face_young_1,gondor_face_young_2,],

["veteran_squire_of_dol_amroth","Horseman_of_Dol_Amroth","Horsemen_of_Dol_Amroth",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,subfac_dol_amroth,fac_gondor,
   [itm_gondor_dolamroth_helm,itm_dol_padded_coat,itm_leather_gloves,itm_dol_shoes,itm_amroth_sword_a,itm_gondor_lance,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_3,wp_gondor_tier_3,man_skills_3c,gondor_face_middle_1,gondor_face_middle_2,],

["knight_of_dol_amroth","Knight_of_Dol_Amroth","Knights_of_Dol_Amroth",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,subfac_dol_amroth,fac_gondor,
   [itm_gondor_dolamroth_helm,itm_dol_hauberk,itm_mail_mittens,itm_dol_greaves,itm_amroth_sword_b,itm_gondor_lance,itm_gon_tab_shield_c,itm_dol_amroth_warhorse,],
      attr_tier_4,wp_gondor_tier_4,man_skills_4c,gondor_face_middle_1,gondor_face_middle_2,],

["veteran_knight_of_dol_amroth","Heavy_Knight_of_Dol_Amroth","Heavy_Knights_of_Dol_Amroth",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,subfac_dol_amroth,fac_gondor,
   [itm_gondor_dolamroth_helm,itm_dol_heavy_mail,itm_mail_mittens,itm_dol_greaves,itm_amroth_sword_b,itm_gondor_lance,itm_gon_tab_shield_c,itm_dol_amroth_warhorse,],
      attr_tier_5,wp_gondor_tier_5,man_skills_5c,gondor_face_middle_1,gondor_face_middle_2,],

["swan_knight_of_dol_amroth","Swan_Knight_of_Dol_Amroth","Swan_Knights_of_Dol_Amroth",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,subfac_dol_amroth,fac_gondor,
   [itm_swan_knight_helm,itm_dol_swan,itm_mail_mittens,itm_dol_greaves,itm_amroth_sword_b,itm_amroth_lance_banner,itm_gon_tab_shield_c,itm_dol_amroth_warhorse2,],
      attr_tier_6,wp_archery(230)| wp_throwing(300)| wp_melee(340),knows_common|knows_ironflesh_6|knows_power_strike_6|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_5|knows_riding_6|knows_horse_archery_1,gondor_face_middle_1,gondor_face_middle_2,],

["dol_amroth_leader","Captain_of_Dol_Amroth","Captains_of_Dol_Amroth",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse|tfg_polearm,0,subfac_dol_amroth,fac_gondor,
   [itm_swan_knight_helm,itm_dol_swan,itm_mail_mittens,itm_dol_greaves,itm_amroth_sword_b,itm_gon_tab_shield_c,itm_dol_amroth_warhorse2,],
      attr_tier_6,wp_gondor_tier_7,knows_common|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_4|knows_riding_6|knows_horse_archery_1,gondor_face_middle_1,gondor_face_middle_2,],

#Lothlorien

["lothlorien_scout","Lothlorien_Scout","Lothlorien_Scouts",tf_lorien| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_archer,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_elven_short_sword,],
      attr_elf_tier_1,wp_elf_tier_1,elf_skills_1a,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_veteran_scout","Lothlorien_Veteran_Scout","Lothlorien_Veteran_Scouts",tf_lorien| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_archer,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_2,wp_elf_tier_2_a,elf_skills_2b,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_footman","Lothlorien_Footman","Lothlorien_Footmen",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_armor_b,itm_elven_boots,itm_lorien_sword_b,itm_elven_spear,itm_lorien_round_shield,],
      attr_elf_tier_3,wp_elf_tier_3,elf_skills_3a,lorien_elf_face_1,lorien_elf_face_2],

["galadhrim_archer","Galadhrim_Archer","Galadhrim_Archers",tf_lorien| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_elven_war_sword,],
      attr_elf_tier_4,wp_elf_tier_4_a,elf_skills_4b,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_horseman","Lothlorien_Horseman","Lothlorien_Horsemen",tf_lorien| tf_mounted| tfg_armor| tfg_boots| tfg_horse| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_armor_b,itm_elven_boots,itm_lorien_sword_b,itm_elven_bow,itm_elven_arrows,itm_riv_shield_a,itm_elven_horse,],
      attr_elf_tier_3,wp_elf_tier_3,elf_skills_3c,lorien_elf_face_1,lorien_elf_face_2],

# Noldorin Swordsman
["noldorin_swordsman","Noldorin_Swordsman","Noldorin_Swordsmans",tf_imladris| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_elven_war_sword,],
      attr_elf_tier_4,wp_elf_tier_4,elf_skills_4a,rivendell_elf_face_1,rivendell_elf_face_2],
#-------------------

["galadhrim_horseman","Galadhrim_Horseman","Galadhrim_Horsemen",tf_lorien| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_elven_lance,itm_riv_shield_a,itm_elven_horse,],
      attr_elf_tier_4,wp_elf_tier_4,elf_skills_4c,lorien_elf_face_1,lorien_elf_face_2],

["galadhrim_swordsman","Galadhrim_Swordsman","Galadhrim_Swordsmen",tf_lorien| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_elven_war_sword,],
      attr_elf_tier_4,wp_elf_tier_4,elf_skills_4a,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_archer","Lothlorien_Archer","Lothlorien_Archers",tf_lorien| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_armor_b,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_3,wp_elf_tier_3_a,elf_skills_3b,lorien_elf_face_1,lorien_elf_face_2],

["galadhrim_spearman","Galadhrim_Spearman","Galadhrim_Spearmen",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_elven_spear,itm_lorien_shield_b,],
      attr_elf_tier_4,wp_elf_tier_4,elf_skills_4a,lorien_elf_face_1,lorien_elf_face_2],

["galadhrim_elite_spearman","Galadhrim_Elite_Spearman","Galadhrim_Elite_Spearmen",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_elven_spear,itm_lorien_shield_b,],
      attr_elf_tier_5,wp_elf_tier_5,elf_skills_5a,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_warden","Lothlorien_Warden","Lothlorien_Wardens",tf_lorien| tfg_armor| tfg_boots| tfg_gloves| tfg_ranged| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_armor_e,itm_leather_gloves_black,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_lorien_sword_a,],
      attr_elf_tier_4,wp_archery(400)|wp_throwing(400)|wp_melee(380),knows_common|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_5|knows_power_draw_6|knows_shield_2|knows_athletics_6|knows_riding_1,lorien_elf_face_1,lorien_elf_face_2],

["galadhrim_elite_archer","Galadhrim_Elite_Archer","Galadhrim_Elite_Archers",tf_lorien| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_elven_war_sword,],
      attr_elf_tier_5,wp_elf_tier_5_a,elf_skills_5b,lorien_elf_face_1,lorien_elf_face_2],

["galadhrim_elite_swordsman","Galadhrim_Elite_Swordsman","Galadhrim_Elite_Swordsmen",tf_lorien| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_elven_war_sword,],
      attr_elf_tier_5,wp_elf_tier_5,elf_skills_5a,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_elite_warden","Lothlorien_Elite_Warden","Lothlorien_Elite_Wardens",tf_lorien| tfg_armor| tfg_boots| tfg_gloves| tfg_ranged| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_armor_e,itm_leather_gloves_black,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_lorien_sword_a,],
      attr_elf_tier_5,wp_archery(450)|wp_throwing(450)|wp_melee(430),knows_common|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_6|knows_power_draw_7|knows_shield_3|knows_athletics_7|knows_riding_1,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_standard_bearer","Lothlorien_Standard_Bearer","Lothlorien_Standard_Bearers",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_helm_b,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_lorien_banner,],
      attr_elf_tier_5,wp_elf_tier_5,knows_common|knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_shield_5|knows_athletics_7|knows_riding_1,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_light_swordsman","Lothlorien_Watchman","Lothlorien_Watchmen",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_archer,itm_elven_boots,itm_lorien_sword_b,itm_lorien_round_shield,],
      attr_elf_tier_2,wp_elf_tier_2,elf_skills_1a,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_items","BUG","BUG",tf_hero,0,0,fac_lorien,
   [itm_good_mace,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,itm_lorien_armor_d,],
      0,0,0,0],

##MIRKWOOD#####

["greenwood_scout","Greenwood_Scout","Greenwood_Scouts",tf_woodelf| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,itm_elven_bow,itm_woodelf_arrows,itm_elven_short_sword,],
      attr_elf_tier_1,wp_elf_tier_1,elf_skills_1a,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_veteran_scout","Greenwood_Veteran_Scout","Greenwood_Veteran_Scouts",tf_woodelf| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,itm_elven_bow,itm_woodelf_arrows,itm_elven_short_sword,],
      attr_elf_tier_2,wp_elf_tier_2_a,elf_skills_2b,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_archer","Greenwood_Bowman","Greenwood_Bowmen",tf_woodelf| tfg_armor| tfg_boots| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,itm_elven_bow,itm_woodelf_arrows,itm_mirkwood_sword,],
      attr_elf_tier_3,wp_elf_tier_3_a,elf_skills_3b,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_veteran_archer","Greenwood_Archer","Greenwood_Archers",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_a,itm_mirkwood_armor_d,itm_mirkwood_boots,itm_mirkwood_bow,itm_woodelf_arrows,itm_mirkwood_sword,],
      attr_elf_tier_4,wp_elf_tier_4_a,elf_skills_4b,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_master_archer","Greenwood_Veteran_Archer","Greenwood_Veteran_Archers",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_a,itm_mirkwood_armor_d,itm_mirkwood_leather_greaves,itm_mirkwood_bow,itm_woodelf_arrows,itm_mirkwood_sword,],
      attr_elf_tier_5,wp_elf_tier_5_a,elf_skills_5b,mirkwood_elf_face_1,mirkwood_elf_face_2],

["thranduils_royal_marksman","Thranduil's_Royal_Marksman","Thranduil's_Royal_Marksmen",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_d,itm_mirkwood_armor_e,itm_mirkwood_leather_greaves,itm_mirkwood_bow,itm_woodelf_arrows,itm_mirkwood_sword,],
      attr_elf_tier_5,wp_archery(470)|wp_throwing(470)|wp_melee(340),elf_skills_5b,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_sentinel","Greenwood_Sentinel","Greenwood_Sentinels",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,itm_elven_bow,itm_woodelf_arrows,itm_mirkwood_sword,itm_mirkwood_spear_shield_b,],
      attr_elf_tier_3,wp_archery(350)|wp_throwing(350)|wp_melee(330),knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_power_draw_5|knows_shield_1|knows_athletics_6|knows_riding_1,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_vet_sentinel","Greenwood_Veteran_Sentinel","Greenwood_Veteran_Sentinels",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_ranged| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_a,itm_mirkwood_armor_a,itm_mirkwood_boots,itm_mirkwood_bow,itm_woodelf_arrows,itm_mirkwood_sword,itm_mirkwood_spear_shield_b,],
      attr_elf_tier_4,wp_archery(400)|wp_throwing(400)|wp_melee(380),knows_common|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_5|knows_power_draw_6|knows_shield_2|knows_athletics_7|knows_riding_1,mirkwood_elf_face_1,mirkwood_elf_face_2],

# Noldorin Elite Swordsman
["noldorin_elite_swordsman","Noldorin_Elite_Swordsman","Noldorin_Elite_Swordsmen",tf_imladris| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_elven_war_sword,],
      attr_elf_tier_5,wp_elf_tier_5,elf_skills_5a,rivendell_elf_face_1,rivendell_elf_face_2],
#-------------------------

["greenwood_spearman","Greenwood_Infantry","Greenwood_Infantry",tf_woodelf| tfg_armor| tfg_boots| tfg_helm| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_b,itm_mirkwood_armor_a,itm_leather_gloves,itm_mirkwood_boots,itm_mirkwood_sword,itm_mirkwood_war_spear,itm_mirkwood_short_spear,itm_mirkwood_spear_shield_a,],
      attr_elf_tier_2,wp_elf_tier_2,elf_skills_2a,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_veteran_spearman","Greenwood_Veteran_Infantry","Greenwood_Veteran_Infantry",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_b,itm_mirkwood_light_scale,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_mirkwood_sword,itm_mirkwood_war_spear,itm_mirkwood_spear_shield_a,],
      attr_elf_tier_3,wp_elf_tier_3,elf_skills_3a,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_royal_spearman","Greenwood_Elite_Infantry","Greenwood_Elite_Infantry",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_b,itm_mirkwood_armor_d,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_mirkwood_great_spear,itm_mirkwood_war_spear,itm_mirkwood_spear_shield_b,],
      attr_elf_tier_4,wp_elf_tier_4,elf_skills_4a,mirkwood_elf_face_1,mirkwood_elf_face_2],

["thranduils_royal_swordsman","Thranduil's_Royal_Swordsman","Thranduil's_Royal_Swordsmen",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_b,itm_mirkwood_armor_e,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_mirkwood_sword,itm_mirkwood_spear_shield_c,],
      attr_elf_tier_5,wp_elf_tier_5,elf_skills_5a,mirkwood_elf_face_1,mirkwood_elf_face_2],

["thranduils_spearman","Thranduil's_Royal_Spearman","Thranduil's_Royal_Spearmen",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_c,itm_mirkwood_armor_c,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_mirkwood_great_spear,itm_mirkwood_war_spear,itm_mirkwood_spear_shield_b,],
      attr_elf_tier_5,wp_elf_tier_5,elf_skills_5a,mirkwood_elf_face_1,mirkwood_elf_face_2],

["greenwood_standard_bearer","Greenwood_Standard_Bearer","Greenwood_Standard_Bearers",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_helm_a,itm_mirkwood_armor_c,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_woodelf_banner,],
      attr_elf_tier_5,wp_elf_tier_5,knows_common|knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_shield_5|knows_athletics_7|knows_riding_1,mirkwood_elf_face_1,mirkwood_elf_face_2],

["woodelf_items","BUG","_",tf_hero,0,0,fac_woodelf,
   [itm_sumpter_horse,itm_saddle_horse,itm_good_mace,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

##RIVENDELL#####

["rivendell_scout","Rivendell_Scout","Rivendell_Scouts",tf_imladris| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_armor_light,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_elven_short_sword,],
      attr_elf_tier_1,wp_elf_tier_1,elf_skills_1a,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_veteran_scout","Rivendell_Veteran_Scout","Rivendell_Veteran_Scouts",tf_imladris| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_armor_light_inf,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_2,wp_elf_tier_2_a,elf_skills_2b,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_footman","Rivendell_Footman","Rivendell_Footmen",tf_imladris| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_a,itm_riv_mail,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_elven_spear,itm_lorien_round_shield,],
      attr_elf_tier_3,wp_elf_tier_3,elf_skills_3a,rivendell_elf_face_1,rivendell_elf_face_2],

["noldorin_archer","Noldorin_Archer","Noldorin_Archers",tf_imladris| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_riv_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_4,wp_elf_tier_4_a,elf_skills_4b,rivendell_elf_face_1,rivendell_elf_face_2],

["noldorin_elite_archer","Noldorin_Elite_Archer","Noldorin_Elite_Archers",tf_imladris| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_riv_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_5,wp_elf_tier_5_a,elf_skills_5b,rivendell_elf_face_1,rivendell_elf_face_2],

["noldorin_elite_spearman","Noldorin_Elite_Spearman","Noldorin_Elite_Spearmen",tf_imladris| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_elven_spear,itm_lorien_shield_b,],
      attr_elf_tier_5,wp_elf_tier_5,elf_skills_5a,rivendell_elf_face_1,rivendell_elf_face_2],

["noldorin_spearman","Noldorin_Spearman","Noldorin_Spearmen",tf_imladris| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_elven_spear,itm_lorien_shield_b,],
      attr_elf_tier_4,wp_elf_tier_4,elf_skills_4a,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_horseman","Rivendell_Horseman","Rivendell_Horsemen",tf_imladris| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_ranged| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_a,itm_riv_mail,itm_leather_gloves,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_lorien_sword_b,itm_elven_horse,],
      attr_elf_tier_3,wp_elf_tier_3,elf_skills_3c,rivendell_elf_face_1,rivendell_elf_face_2],

["noldorin_horseman","Noldorin_Horseman","Noldorin_Horsemen",tf_imladris| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_elven_lance,itm_riv_shield_a,itm_elven_horse,],
      attr_elf_tier_4,wp_elf_tier_4,elf_skills_4c,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_knight","Rivendell_Knight","Rivendell_Knights",tf_imladris| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_c,itm_riv_guard,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_elven_lance,itm_riv_shield_b,itm_riv_warhorse,],
      attr_elf_tier_5,wp_elf_tier_5,elf_skills_5c,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_archer","Rivendell_Archer","Rivendell_Archers",tf_imladris| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_a,itm_riv_mail,itm_leather_gloves,itm_elven_boots,itm_riv_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_3,wp_elf_tier_3_a,elf_skills_3b,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_mounted_scout","Rivendell_Mounted_Scout","Rivendell_Mounted_Scouts",tf_imladris| tf_mounted| tfg_armor| tfg_boots| tfg_horse| tfg_ranged| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_armor_light_inf,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_lorien_sword_b,itm_elven_horse,],
      attr_elf_tier_2,wp_elf_tier_2,elf_skills_2c,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_standard_bearer","Rivendell_Standard_Bearer","Rivendell_Standard_Bearers",tf_imladris| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_helm_b,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_imladris_banner,],
      attr_elf_tier_5,wp_elf_tier_5,knows_common|knows_ironflesh_7|knows_power_strike_6|knows_power_throw_4|knows_power_draw_3|knows_shield_5|knows_athletics_7|knows_riding_1,rivendell_elf_face_1,rivendell_elf_face_2],

##DUNEDAIN#####

["dunedain_scout","Arnor_Militiaman","Arnor_Militiamen",tf_dunedain| tfg_armor| tfg_shield| tfg_boots,0,0,fac_imladris,
   [itm_arnor_armor_c,itm_leather_boots,itm_spear,itm_arnor_shield_b,],
      attr_dun_tier_1,wp_dun_tier_1,dun_skills_1a,arnor_face_middle_1,arnor_face_middle_2],

["dunedain_trained_scout","Arnor_Watchman","Arnor_Watchmen",tf_dunedain| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_arnor_helm_a,itm_arnor_armor_c,itm_leather_gloves,itm_leather_boots,itm_arnor_sword_f,itm_spear,itm_arnor_shield_b,],
      attr_dun_tier_2,wp_dun_tier_2,dun_skills_2a,arnor_face_middle_1,arnor_face_middle_2],

["arnor_man_at_arms","Arnor_Footman","Arnor_Footmen",tf_dunedain| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_a,itm_leather_gloves_black,itm_leather_boots,itm_arnor_sword_f,itm_arnor_spear,itm_arnor_shield_a,],
      attr_dun_tier_3,wp_dun_tier_3,dun_skills_3a,arnor_face_middle_1,arnor_face_middle_2],

["arnor_master_at_arms","Arnor_Veteran_Footman","Arnor_Veteran_Footmen",tf_dunedain| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_a,itm_leather_gloves_black,itm_arnor_greaves,itm_arnor_sword_f,itm_arnor_spear,itm_arnor_shield_a,],
      attr_dun_tier_4,wp_dun_tier_4,dun_skills_4a,arnor_face_middle_1,arnor_face_middle_2],

["high_swordsman_of_arnor","Arnor_Sergeant","Arnor_Sergeant",tf_dunedain| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_f,itm_leather_gloves_black,itm_arnor_greaves,itm_arnor_sword_f,itm_arnor_spear,itm_arnor_shield_a,],
      attr_dun_tier_5,wp_dun_tier_5,dun_skills_5a,arnor_face_older_1,arnor_face_older_2],

["arnor_horsemen","Arnor_Horseman","Arnor_Horsemen",tf_dunedain| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_a,itm_leather_gloves_black,itm_arnor_greaves,itm_arnor_sword_f,itm_arnor_lance,itm_arnor_shield_c,itm_arnor_horse,],
      attr_dun_tier_4,wp_dun_tier_4,dun_skills_4c,arnor_face_older_1,arnor_face_older_2],

["knight_of_arnor","Knight_of_Arnor","Knights_of_Arnor",tf_dunedain| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_imladris,
   [itm_dunedain_helm_b,itm_arnor_armor_f,itm_leather_gloves_black,itm_arnor_greaves,itm_arnor_sword_f,itm_arnor_lance,itm_arnor_shield_c,itm_arnor_warhorse,],
      attr_dun_tier_5,wp_dun_tier_5,dun_skills_5c,arnor_face_older_1,arnor_face_older_2],

["dunedain_ranger","Dunedain_Ranger","Dunedain_Rangers",tf_dunedain| tfg_armor| tfg_boots| tfg_gloves| tfg_ranged,0,0,fac_imladris,
   [itm_arnor_armor_d,itm_leather_gloves_black,itm_leather_boots,itm_numenor_bow,itm_arnor_arrows,itm_arnor_sword_f,],
      attr_dun_tier_3,wp_archery(230)|wp_throwing(230)|wp_melee(210),knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_shield_1|knows_athletics_6|knows_riding_1,arnor_face_middle_1,arnor_face_middle_2],

["dunedain_veteran_ranger","Dunedain_Veteran_Ranger","Dunedain_Veteran_Rangers",tf_dunedain| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_imladris,
   [itm_dunedain_helm_a,itm_arnor_armor_d,itm_leather_gloves_black,itm_leather_boots,itm_numenor_bow,itm_arnor_arrows,itm_arnor_sword_a,],
      attr_dun_tier_4,wp_archery(300)|wp_throwing(300)|wp_melee(280),knows_common|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_5|knows_power_draw_5|knows_shield_2|knows_athletics_6|knows_riding_1,arnor_face_older_1,arnor_face_older_2],

["dunedain_master_ranger","Dunedain_Master_Ranger","Dunedain_Master_Rangers",tf_dunedain| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_imladris,
   [itm_dunedain_helm_a,itm_arnor_armor_d,itm_leather_gloves_black,itm_leather_boots,itm_numenor_bow,itm_arnor_arrows,itm_arnor_sword_a,],
      attr_dun_tier_5,wp_archery(370)|wp_throwing(370)|wp_melee(350),knows_common|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_6|knows_power_draw_6|knows_shield_3|knows_athletics_7|knows_riding_1,arnor_face_older_1,arnor_face_older_2],

["imladris_items","BUG","BUG",tf_hero,0,0,fac_imladris,
   [itm_good_mace,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,itm_riv_lord,itm_arnor_armor_f,],
      0,0,0,0],

#ROHAN
["rohan_youth","Rohan_Youth","Rohan_Youths",tf_rohan| tfg_armor| tfg_boots,0,0,fac_rohan,
   [itm_rohan_armor_a,itm_free_rohan_armor_c,itm_rohan_shoes,itm_rohirrim_short_axe,itm_shortened_spear,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      attr_tier_1,wp_tier_1,man_skills_1a,rohan_face_younger_1,rohan_face_young_2],

# Infantry
["guardsman_of_rohan","Rohan_Militiaman","Rohan_Militiamen",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,0,fac_rohan,
   [itm_rohan_archer_helmet_b,itm_free_rohan_armor_g,itm_leather_boots,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_spear,itm_rohan_bow,itm_rohan_arrows,itm_rohan_javelin,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_2,wp_tier_2,man_skills_2a,rohan_face_young_1,rohan_face_young_2],

["footman_of_rohan","Footman_of_Rohan","Footmen_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_helm,0,0,fac_rohan,
   [itm_rohan_archer_helmet_a,itm_rohan_archer_helmet_b,itm_free_rohan_armor_d,itm_rohan_armor_e,itm_leather_boots,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_spear,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_3,wp_tier_3,man_skills_3a,rohan_face_young_1,rohan_face_middle_2],

["spearman_of_rohan","Spearman_of_Rohan","Spearmen_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_j,itm_leather_gloves,itm_leather_boots,itm_rohan_spear,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_4,wp_tier_4,man_skills_4a,rohan_face_young_1,rohan_face_middle_2],

["elite_spearman_of_rohan","Heavy_Spearman_of_Rohan","Heavy_Spearmen_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_m,itm_leather_gloves,itm_leather_boots,itm_rohan_spear,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_5,wp_tier_5,man_skills_5a,rohan_face_middle_1,rohan_face_old_2],

["warden_of_methuseld","Warden_of_Meduseld","Wardens_of_Meduseld",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_spear,itm_rohan_shield_e,],
      attr_tier_6,wp_tier_6,man_skills_6a,rohan_face_old_1,rohan_face_older_2],

["raider_of_rohan","Frealaf_Raider","Frealaf_Raiders",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_m,itm_leather_gloves,itm_leather_boots,itm_rohirrim_long_hafted_axe,itm_rohirrim_throwing_axe,itm_rohirrim_short_axe,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_6,wp_tier_6,man_skills_6a,rohan_face_old_1,rohan_face_older_2],

["heavy_swordsman_of_rohan","Heavy_Swordsman_of_Rohan","Heavy_Swordsmen_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_m,itm_leather_gloves,itm_leather_boots,itm_rohan_inf_sword,itm_rohan_2h_sword,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_5,wp_tier_5,man_skills_5a,rohan_face_middle_1,rohan_face_old_2],

["folcwine_guard_of_rohan","Folcwine_Guard_of_Rohan","Folcwine_Guards_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_2h_sword,itm_rohan_sword_c,itm_rohan_shield_e,],
      attr_tier_6,wp_tier_6,man_skills_6a,rohan_face_old_1,rohan_face_older_2],

# Mounted skirmishers
["skirmisher_of_rohan","Horse_Archer_of_Rohan","Horse_Archers_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_boots| tfg_helm| tfg_horse| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_archer_helmet_a,itm_rohan_archer_helmet_b,itm_free_rohan_armor_d,itm_rohan_armor_e,itm_leather_boots,itm_rohan_bow,itm_rohan_arrows,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_3,wp_tier_3_a,knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_shield_1|knows_athletics_2|knows_riding_4|knows_horse_archery_2,rohan_face_young_1,rohan_face_middle_2],

["veteran_skirmisher_of_rohan","Veteran_Horse_Archer_of_Rohan","Veteran_Horse_Archers_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_j,itm_leather_gloves,itm_leather_boots,itm_rohan_bow,itm_rohan_arrows,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_4,wp_tier_4_a,knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_3|knows_riding_5|knows_horse_archery_3,rohan_face_young_1,rohan_face_middle_2],

["elite_skirmisher_of_rohan","Heavy_Horse_Archer_of_Rohan","Heavy_Horse_Archers_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_m,itm_leather_gloves,itm_leather_boots,itm_rohan_bow,itm_rohan_arrows,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_5,wp_tier_5_a,knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_4|knows_power_draw_4|knows_shield_2|knows_athletics_3|knows_riding_6|knows_horse_archery_4,rohan_face_middle_1,rohan_face_old_2],

["brego_guard_of_rohan","Brego_Guard_of_Rohan","Brego_Guards_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_bow,itm_rohan_arrows,itm_rohan_sword_c,itm_rohan_shield_e,itm_rohan_warhorse,],
      attr_tier_6,wp_tier_6_a,knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_5|knows_power_draw_5|knows_shield_3|knows_athletics_4|knows_riding_7|knows_horse_archery_5,rohan_face_old_1,rohan_face_older_2],

# Cavalry
["lancer_of_rohan","Lancer_of_Rohan","Lancers_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_polearm,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_j,itm_leather_gloves,itm_leather_boots,itm_rohan_lance,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_4,wp_tier_4,knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_3|knows_riding_5|knows_horse_archery_1,rohan_face_young_1,rohan_face_middle_2],

["elite_lancer_of_rohan","Heavy_Lancer_of_Rohan","Heavy_Lancers_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_polearm,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_m,itm_leather_gloves,itm_leather_boots,itm_rohan_lance,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_5,wp_tier_5,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_6|knows_horse_archery_1,rohan_face_middle_1,rohan_face_old_2],

["thengel_guard_of_rohan","Thengel_Guard_of_Rohan","Thengel_Guards_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse| tfg_polearm,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_lance_banner_horse,itm_rohan_shield_e,itm_rohan_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_4|knows_riding_7|knows_horse_archery_1,rohan_face_old_1,rohan_face_older_2],

["eorl_guard_of_rohan","Eorl_Guard_of_Rohan","Eorl_Guards_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_shield_e,itm_rohan_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_5|knows_athletics_4|knows_riding_7|knows_horse_archery_1,rohan_face_old_1,rohan_face_older_2],

["squire_of_rohan","Scout_of_Rohan","Scouts_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_archer_helmet_b,itm_free_rohan_armor_g,itm_leather_boots,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_spear,itm_rohan_bow,itm_rohan_arrows,itm_rohan_javelin,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_courser,],
      attr_tier_2,wp_tier_2,knows_common|knows_ironflesh_1|knows_power_strike_1|knows_power_throw_1|knows_power_draw_1|knows_shield_1|knows_athletics_2|knows_riding_3|knows_horse_archery_1,rohan_face_young_1,rohan_face_young_2],

["rider_of_rohan","Rider_of_Rohan","Riders_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_archer_helmet_a,itm_rohan_archer_helmet_b,itm_free_rohan_armor_d,itm_rohan_armor_e,itm_leather_boots,itm_rohan_inf_sword,itm_rohan_lance,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_3,wp_tier_3,knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_1|knows_shield_2|knows_athletics_2|knows_riding_4|knows_horse_archery_1,rohan_face_young_1,rohan_face_middle_2],

["veteran_rider_of_rohan","Veteran_Rider_of_Rohan","Veteran_Riders_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_j,itm_leather_gloves,itm_leather_boots,itm_rohan_inf_sword,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_4,wp_tier_4,knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_3|knows_riding_5|knows_horse_archery_1,rohan_face_young_1,rohan_face_middle_2],

["elite_rider_of_rohan","Heavy_Rider_of_Rohan","Heavy_Riders_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_m,itm_leather_gloves,itm_leather_boots,itm_rohan_inf_sword,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,itm_rohirrim_hunter,itm_rohirrim_hunter2,],
      attr_tier_5,wp_tier_5,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_6|knows_horse_archery_1,rohan_face_middle_1,rohan_face_old_2],
# Veteran_Footman
["veteran_footman_of_rohan","Veteran_Footman_of_Rohan","Veteran_Footmen_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_j,itm_leather_gloves,itm_leather_boots,itm_rohirrim_short_axe,itm_rohan_inf_sword,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_4,wp_tier_4,man_skills_4a,rohan_face_young_1,rohan_face_middle_2],

# Skirmishers
["dismounted_skirmisher_of_rohan","Archer_of_Rohan","Archers_of_Rohan",tf_rohan| tfg_armor| tfg_boots| tfg_helm| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_archer_helmet_a,itm_rohan_archer_helmet_b,itm_free_rohan_armor_d,itm_rohan_armor_e,itm_leather_boots,itm_rohan_bow,itm_rohan_arrows,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_3,wp_tier_3_a,man_skills_3b,rohan_face_young_1,rohan_face_middle_2],

["dismounted_veteran_skirmisher_of_rohan","Veteran_Archer_of_Rohan","Veteran_Archers_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_j,itm_leather_gloves,itm_leather_boots,itm_rohan_bow,itm_rohan_arrows,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_4,wp_tier_4_a,man_skills_4b,rohan_face_young_1,rohan_face_middle_2],

["dismounted_elite_skirmisher_of_rohan","Heavy_Archer_of_Rohan","Heavy_Archers_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_light_helmet_a,itm_rohan_cav_helmet_a,itm_free_rohan_armor_m,itm_leather_gloves,itm_leather_boots,itm_rohan_bow,itm_rohan_arrows,itm_rohan_inf_sword,itm_rohirrim_short_axe,itm_rohan_shield_a,itm_rohan_shield_b,itm_rohan_shield_c,itm_rohan_shield_d,],
      attr_tier_5,wp_tier_5_a,man_skills_5b,rohan_face_middle_1,rohan_face_old_2],

["helm_guard_of_rohan","Helm_Guard_of_Rohan","Helm_Guards_of_Rohan",tf_rohan| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_bow,itm_rohan_arrows,itm_rohan_sword_c,itm_rohan_shield_e,],
      attr_tier_6,wp_tier_6_a,man_skills_6b,rohan_face_old_1,rohan_face_older_2],

["rohan_items","BUG","BUG",tf_hero,0,0,fac_rohan,
   [itm_good_mace,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,itm_rohirrim_heavy_warhorse,],
      0,0,0,0],

#HARAD

["harad_desert_warrior","Harad_Levy","Harad_Levies",tf_harad| tfg_armor,0,0,fac_harad,
   [itm_desert_boots,itm_harad_tunic,itm_harad_javelin,itm_harad_short_spear,],
      attr_evil_tier_1,wp_tier_1,man_skills_1a,haradrim_face_1,haradrim_face_2],

["harad_infantry","Harad_Light_Infantry","Harad_Light_Infantry",tf_harad| tfg_armor| tfg_boots,0,0,fac_harad,
   [itm_desert_boots,itm_harad_hauberk,itm_harad_sabre,itm_harad_short_spear,itm_harad_dagger,itm_harad_long_shield_d,itm_harad_long_shield_e,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,haradrim_face_1,haradrim_face_2],

["harad_veteran_infantry","Harad_Spearman","Harad_Spearmen",tf_harad| tfg_shield| tfg_armor| tfg_helm| tfg_boots  |tfg_polearm,0,0,fac_harad,
   [itm_harad_scale_greaves,itm_harad_scale,itm_harad_finhelm,itm_harad_long_spear,itm_harad_long_shield_d,itm_harad_long_shield_e,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,haradrim_face_1,haradrim_face_2],

["harad_tiger_guard","Tiger_Guard","Tiger_Guards",tf_harad| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tfg_gloves  |tfg_polearm,0,0,fac_harad,
   [itm_harad_scale_greaves,itm_leather_gloves,itm_harad_tiger_scale,itm_lion_helm,itm_harad_long_spear,itm_harad_long_shield_b,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,haradrim_face_1,haradrim_face_2],

["harad_swordsman","Harad_Swordsman","Harad_Swordsmen",tf_harad| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_scale_greaves,itm_harad_scale,itm_harad_finhelm,itm_harad_heavy_sword,itm_harad_khopesh,itm_harad_long_shield_d,itm_harad_long_shield_e,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,haradrim_face_1,haradrim_face_2],

["harad_lion_guard","Lion_Guard","Lion_Guards",tf_harad| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_scale_greaves,itm_leather_gloves,itm_harad_lion_scale,itm_lion_helm,itm_harad_heavy_sword,itm_harad_khopesh,itm_harad_long_shield_b,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,haradrim_face_1,haradrim_face_2],

["harad_skirmisher","Harad_Skirmisher","Harad_Skirmishers",tf_harad| tfg_ranged| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_desert_boots,itm_harad_skirmisher,itm_harad_heavy_inf_helm,itm_harad_bow,itm_harad_arrows,itm_harad_dagger,],
      attr_evil_tier_3,wp_tier_3_a,man_skills_3b,haradrim_face_1,haradrim_face_2],

["harad_archer","Harad_Archer","Harad_Archers",tf_harad| tfg_ranged| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_leather_greaves,itm_harad_archer,itm_harad_heavy_inf_helm,itm_harad_bow,itm_harad_arrows,itm_skirmisher_sword,],
      attr_evil_tier_4,wp_tier_4_a,man_skills_4b,haradrim_face_1,haradrim_face_2],

["harad_eagle_guard","Eagle_Guard","Eagle_Guards",tf_harad| tfg_ranged| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_leather_greaves,itm_leather_gloves,itm_black_snake_armor,itm_harad_eaglehelm,itm_lg_bow,itm_harad_arrows,itm_eagle_guard_spear,],
      attr_evil_tier_5,wp_tier_5_a,man_skills_5b,haradrim_face_1,haradrim_face_2],

# Harondor
["harondor_scout","Harondor_Scout","Harondor_Scouts",tf_harad| tf_mounted| tfg_armor| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_desert_boots,itm_harad_padded,itm_horandor_a,itm_harad_shield_a,itm_saddle_horse,],
      attr_evil_tier_2,wp_tier_2,man_skills_2a,haradrim_face_1,haradrim_face_2],

["harondor_rider","Harondor_Rider","Harondor_Riders",tf_harad| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_leather_greaves,itm_harad_hauberk,itm_harad_cav_helm_b,itm_horandor_a,itm_harad_shield_b,itm_harad_horse,itm_harad_shield_c,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,haradrim_face_1,haradrim_face_2],

["harondor_light_cavalry","Harondor_Light_Cavalry","Harondor_Light_Cavalry",tf_harad| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_lamellar_greaves,itm_harad_lamellar,itm_harad_wavy_helm,itm_horandor_a,itm_harad_shield_b,itm_harad_warhorse,itm_harad_shield_c,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,haradrim_face_1,haradrim_face_2],

["fang_heavy_cavalry","Fang_Heavy_Cavalry","Fang_Heavy_Cavalry",tf_harad| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_lamellar_greaves,itm_leather_gloves,itm_harad_heavy,itm_harad_dragon_helm,itm_harad_long_spear,itm_harad_yellow_shield,itm_harad_warhorse,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,haradrim_face_1,haradrim_face_2],

["harad_horse_archer","Harad_Horse_Archer","Harad_Horse_Archers",tf_harad| tfg_ranged| tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_desert_boots,itm_harad_skirmisher,itm_harad_cav_helm_a,itm_harad_bow,itm_harad_arrows,itm_harad_sabre,itm_saddle_horse,],
      attr_evil_tier_3,wp_tier_3_a,man_skills_3d,haradrim_face_1,haradrim_face_2],

["black_snake_horse_archer","Black_Snake_Horse_Archer","Black_Snake_Horse_Archers",tf_harad| tfg_ranged| tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_leather_greaves,itm_harad_archer,itm_harad_heavy_inf_helm,itm_harad_bow,itm_harad_arrows,itm_harad_sabre,itm_harad_horse,],
      attr_evil_tier_4,wp_tier_4_a,man_skills_4d,haradrim_face_1,haradrim_face_2],

["gold_serpent_horse_archer","Gold_Serpent_Horse_Archer","Gold_Serpent_Horse_Archers",tf_harad| tfg_ranged| tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_leather_greaves,itm_black_snake_armor,itm_black_snake_helm,itm_harad_bow,itm_harad_arrows,itm_black_snake_sword,itm_harad_warhorse,],
      attr_evil_tier_5,wp_tier_5_a,man_skills_5d,haradrim_face_1,haradrim_face_2],

#Far Harad
["far_harad_tribesman","Far_Harad_Tribesman","Far_Harad_Tribesmen",tf_harad| tfg_armor| tfg_boots,0,0,fac_harad,
   [itm_far_harad_2h_mace,itm_harad_javelin,itm_harad_short_spear,],
      attr_evil_tier_2,wp_tier_2,man_skills_2a,far_harad_face1,far_harad_face2],

["far_harad_champion","Far_Harad_Champion","Far_Harad_Champions",tf_harad| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_champion,itm_far_harad_2h_mace,itm_harad_javelin,itm_harad_short_spear,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,far_harad_face1,far_harad_face2],

["far_harad_panther_guard","Panther_Guard","Panther_Guards",tf_harad| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_panther_guard,itm_harad_pantherhelm,itm_harad_mace,itm_harad_javelin,itm_harad_long_shield_a,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,far_harad_face1,far_harad_face2],

["harad_items","BUG","_",tf_hero,0,0,fac_harad,
   [itm_short_bow,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

#DUNLAND
["dunnish_wildman","Dunnish_Wildman","Dunnish_Wildmen",tf_dunland| tf_randomize_face| tfg_armor| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_dunland_armor_a,itm_dunland_armor_b,itm_dunland_armor_c,itm_dunland_armor_d,itm_dunland_armor_e,itm_dunland_armor_g,itm_dunland_armor_h,itm_dunnish_axe,itm_dunland_spear,itm_wood_club,itm_dunland_javelin,itm_dunland_javelin,],
      attr_evil_tier_1,wp_tier_1,man_skills_1a,dunland_face1,dunland_face2],

["dunnish_warrior","Dunnish_Warrior","Dunnish_Warriors",tf_dunland| tf_randomize_face| tfg_armor| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_dunland_armor_a,itm_dunland_armor_b,itm_dunland_armor_c,itm_dunland_armor_d,itm_dunland_armor_e,itm_dunland_armor_g,itm_dunland_armor_h,itm_dunnish_antler_axe,itm_dunnish_axe,itm_wood_club,itm_dunland_javelin,itm_dunland_javelin,itm_dunland_javelin,],
      attr_evil_tier_2,wp_tier_2,man_skills_2a,dunland_face1,dunland_face2],

["dunnish_pikeman","Dunnish_Pikeman","Dunnish_Pikemen",tf_dunland| tf_randomize_face| tfg_shield| tfg_armor| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_leather_gloves,itm_dunland_armor_a,itm_dunland_armor_b,itm_dunland_armor_c,itm_dunland_armor_d,itm_dunland_armor_e,itm_dunland_armor_g,itm_dunland_armor_h,itm_gundabad_helm_a,itm_dun_helm_c,itm_dun_helm_e,itm_dunnish_pike,],
      attr_evil_tier_3,wp_tier_4,man_skills_4a,dunland_face1,dunland_face2],

["dunnish_veteran_pikeman","Dunnish_Veteran_Pikeman","Dunnish_Veteran_Pikemen",tf_dunland| tf_randomize_face| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_leather_gloves_black,itm_dunland_armor_i,itm_dunland_armor_j,itm_gundabad_helm_b,itm_dun_helm_c,itm_dun_helm_e,itm_dunnish_pike,],
      attr_evil_tier_4,wp_tier_5,man_skills_5a,dunland_face1,dunland_face2],

["dunnish_raven_rider","Dunnish_Raven_Rider","Dunnish_Raven_Riders",tf_dunland| tf_randomize_face| tf_mounted| tfg_armor| tfg_horse| tfg_boots| tfg_ranged,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_dunland_armor_a,itm_dunland_armor_b,itm_dunland_armor_c,itm_dunland_armor_d,itm_dunland_armor_e,itm_dunland_armor_g,itm_dunland_armor_h,itm_dunnish_antler_axe,itm_dunland_javelin,itm_dunland_javelin,itm_dunland_javelin,itm_dunland_javelin,itm_dun_shield_a,itm_dun_shield_b,itm_saddle_horse,],
      attr_evil_tier_2,wp_tier_2,man_skills_2c,dunland_face1,dunland_face2],

["dunnish_vet_warrior","Dunnish_Veteran_Warrior","Dunnish_Veteran_Warriors",tf_dunland| tf_randomize_face| tfg_shield| tfg_armor| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_leather_gloves,itm_dunland_armor_a,itm_dunland_armor_b,itm_dunland_armor_c,itm_dunland_armor_d,itm_dunland_armor_e,itm_dunland_armor_g,itm_dunland_armor_h,itm_dunland_javelin,itm_dunland_javelin,itm_dunland_javelin,itm_dun_helm_b,itm_dunnish_axe,itm_dunnish_war_axe,itm_gundabad_helm_a,itm_dun_shield_a,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,dunland_face1,dunland_face2],

["dunnish_wolf_warrior","Dunnish_Wolf_Warrior","Dunnish_Wolf_Warriors",tf_dunland| tf_randomize_face| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_leather_gloves_black,itm_dunland_armor_i,itm_dunland_armor_j,itm_dunnish_axe,itm_dunnish_war_axe,itm_dunland_javelin,itm_dunland_javelin,itm_dunland_javelin,itm_dun_shield_a,itm_dun_helm_a,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,dunland_face1,dunland_face2],

["dunnish_wolf_guard","Dunnish_Wolf_Guard","Dunnish_Wolf_Guards",tf_dunland| tf_randomize_face| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_leather_gloves_black,itm_dunland_armor_i,itm_dunland_armor_j,itm_dun_helm_a,itm_dun_helm_b,itm_dun_shield_a,itm_dunnish_axe,itm_dunnish_war_axe,itm_dunland_javelin,itm_dunland_javelin,itm_dunland_javelin,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,dunland_face1,dunland_face2],

#unused
["dunnish_chieftan","Dunnish_Chieftain","Dunnish_Chieftains",tf_dunland| tf_randomize_face| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_leather_gloves_black,itm_dunland_armor_k,itm_dun_helm_d,itm_dun_berserker,itm_dun_shield_a,itm_dun_shield_b,],
      attr_tier_5,wp_tier_5,man_skills_5a,dunland_face1,dunland_face2],

["dunland_items","BUG","_",tf_hero,0,0,fac_dunland,
   [itm_sumpter_horse,itm_saddle_horse,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

#KHAND 

["easterling_youth","Variag_Bondsman","Variag_Bondsmen",tf_evil_man| tfg_armor| tfg_boots,0,0,fac_khand,
   [itm_khand_light,itm_leather_boots,itm_shortened_spear,itm_khand_mace1,],
      attr_evil_tier_1,wp_tier_1,man_skills_1a,khand_man1,khand_man2],

["easterling_warrior","Warrior_of_Khand","Warriors_of_Khand",tf_evil_man| tfg_armor| tfg_boots,0,0,fac_khand,
   [itm_khand_light,itm_leather_boots,itm_khand_helmet_a2,itm_khand_voulge,itm_shortened_spear,itm_khand_tulwar,itm_khand_mace1,itm_tab_shield_small_round_b,],
      attr_evil_tier_2,wp_tier_2,man_skills_2a,khand_man1,khand_man2],

["easterling_axeman","Variag_Axeman","Variag_Axemen",tf_evil_man| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_foot_lam_c,itm_leather_boots,itm_khand_helmet_a2,itm_khand_axe_winged,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,khand_man1,khand_man2],

["easterling_veteran_axeman","Variag_Veteran_Axeman","Variag_Veteran_Axemen",tf_evil_man| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_foot_lam_b,itm_variag_greaves,itm_khand_helmet_c3,itm_khand_helmet_c4,itm_khand_axe_winged,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,khand_man1,khand_man2],

["easterling_axe_master","Variag_Axe_Master","Variag_Axe_Masters",tf_evil_man| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_foot_lam_a,itm_variag_greaves,itm_khand_helmet_c3,itm_khand_helmet_c4,itm_khand_axe_great,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,khand_man1,khand_man2],

["easterling_rider","Variag_Pony_Rider","Variag_Pony_Riders",tf_evil_man| tf_mounted| tfg_armor| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_light_lam,itm_leather_boots,itm_variag_pony,itm_khand_tulwar,itm_khand_mace1,],
      attr_evil_tier_2,wp_tier_2,man_skills_2c,khand_man1,khand_man2],

["easterling_horseman","Variag_Horseman","Variag_Horsemen",tf_evil_man| tf_mounted| tfg_armor| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_med_lam_b,itm_leather_boots,itm_variag_pony,itm_khand_helmet_a2,itm_khand_helmet_a3,itm_khand_helmet_b3,itm_khand_tulwar,itm_khand_mace1,itm_leather_gloves,itm_easterling_round_horseman,],
      attr_evil_tier_3,wp_tier_3,man_skills_3c,khand_man1,khand_man2],

["easterling_veteran_horseman","Variag_Heavy_Horseman","Variag_Heavy_Horsemen",tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_med_lam_c,itm_variag_greaves,itm_variag_pony,itm_khand_helmet_a2,itm_khand_helmet_a3,itm_khand_helmet_b3,itm_khand_tulwar,itm_khand_mace1,itm_khand_mace2,itm_mail_mittens,itm_easterling_round_horseman,],
      attr_evil_tier_4,wp_tier_4,man_skills_4c,khand_man1,khand_man2],

["easterling_horsemaster","Variag_Kataphrakt","Variag_Kataphrakts",tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_med_lam_d,itm_variag_greaves,itm_variag_kataphrakt,itm_khand_helmet_a1,itm_khand_helmet_b4,itm_khand_helmet_d2,itm_khand_tulwar,itm_mail_mittens,itm_easterling_round_horseman,],
      attr_evil_tier_5,wp_tier_5,man_skills_5c,khand_man1,khand_man2],

["easterling_lance_kataphract","Variag_Lance_Kataphrakt","Variag_Lance_Kataphrakts",tf_evil_man| tf_mounted| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots  |tfg_polearm,0,0,fac_khand,
   [itm_khand_heavy_lam,itm_variag_greaves,itm_variag_kataphrakt,itm_khand_helmet_b2,itm_khand_helmet_d1,itm_khand_helmet_d3,itm_khand_lance,itm_mail_mittens,],
      attr_evil_tier_5,wp_tier_5,man_skills_5c,khand_man1,khand_man2],

#Khand Variags
["khand_glaive_whirler","Khand_Blade_Whirler","Khand_Blade_Whirlers",tf_evil_man| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_foot_lam_c,itm_leather_boots,itm_khand_helmet_e1,itm_khand_helmet_e4,itm_khand_helmet_e3,itm_khand_voulge,itm_leather_gloves,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,khand_man1,khand_man2],

["variag_veteran_glaive_whirler","Khand_Veteran_Blade_Whirler","Khand_Veteran_Blade_Whirlers",tf_evil_man| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_foot_lam_b,itm_leather_boots,itm_khand_helmet_e2,itm_khand_helmet_e3,itm_khand_voulge,itm_khand_halberd,itm_mail_mittens,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,khand_man1,khand_man2],

["khand_glaive_master","Khand_Halberd_Master","Khand_Halberd_Masters",tf_evil_man| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_foot_lam_a,itm_variag_greaves,itm_khand_helmet_e2,itm_khand_halberd,itm_mail_mittens,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,khand_man1,khand_man2],

["variag_pitfighter","Variag_Pitfighter","Variag_Pitfighters",tf_evil_man| tfg_ranged| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_light,itm_javelin,itm_leather_boots,itm_khand_helmet_mask1,itm_khand_helmet_mask2,itm_khand_tulwar,itm_khand_pitsword,itm_easterling_hawk_shield,itm_variag_gladiator_shield,itm_tab_shield_small_round_b,],
      attr_evil_tier_4,wp_tier_4,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_5|knows_riding_1,khand_man1,khand_man2],

["variag_gladiator","Variag_Berserker","Variag_Berserkers",tf_evil_man| tfg_ranged| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_light,itm_javelin,itm_leather_boots,itm_khand_helmet_mask1,itm_khand_helmet_mask2,itm_khand_2h_tulwar,itm_khand_tulwar,itm_khand_pitsword,itm_khand_mace_spiked,itm_khand_2h_tulwar,itm_easterling_hawk_shield,itm_tab_shield_small_round_b,],
      attr_evil_tier_5,wp_tier_5,knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_6|knows_riding_1,khand_man1,khand_man2],

["easterling_skirmisher","Variag_Skirmisher","Variag_Skirmishers",tf_evil_man| tfg_ranged| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_light_lam,itm_javelin,itm_leather_boots,itm_variag_pony,itm_khand_helmet_a2,itm_khand_tulwar,itm_khand_mace1,itm_khand_mace2,],
      attr_evil_tier_3,wp_tier_3_a,man_skills_3b,khand_man1,khand_man2],

["easterling_veteran_skirmisher","Variag_Veteran_Skirmisher","Variag_Veteran_Skirmishers",tf_evil_man| tfg_ranged| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_med_lam_b,itm_javelin,itm_variag_greaves,itm_variag_pony,itm_khand_helmet_a2,itm_leather_gloves,itm_khand_tulwar,itm_khand_mace1,itm_khand_mace2,itm_easterling_round_horseman,],
      attr_evil_tier_4,wp_tier_4_a,man_skills_4b,khand_man1,khand_man2],

["easterling_elite_skirmisher","Variag_Heavy_Skirmisher","Variag_Heavy_Skirmishers",tf_evil_man| tfg_ranged| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_med_lam_c,itm_javelin,itm_variag_greaves,itm_variag_kataphrakt,itm_khand_helmet_a1,itm_leather_gloves,itm_khand_tulwar,itm_khand_mace1,itm_khand_mace2,itm_easterling_round_horseman,],
      attr_evil_tier_5,wp_tier_5_a,man_skills_5b,khand_man1,khand_man2],

["khand_items","BUG","_",tf_hero,0,0,fac_khand,
   [itm_leather_boots,itm_leather_gloves,itm_sumpter_horse,itm_saddle_horse,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

#UMBAR
["corsair_youth","Umbar_Sailor","Umbar_Sailors",tfg_armor,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_a,itm_umb_armor_a1,itm_umb_shield_a,itm_umb_shield_b,itm_shortened_spear,itm_corsair_sword,itm_corsair_throwing_dagger,],
      attr_evil_tier_1,wp_tier_1,man_skills_1a,bandit_face1,bandit_face2],

["corsair_warrior","Umbar_Warrior","Umbar_Warriors",tfg_armor| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_b,itm_umb_hood,itm_umb_shield_b,itm_umb_shield_d,itm_shortened_spear,itm_corsair_sword,itm_corsair_harpoon,itm_umbar_rapier,],
      attr_evil_tier_2,wp_tier_2,man_skills_2a,bandit_face1,bandit_face2],

["corsair_pikeman","Pikeman_of_Umbar","Pikemen_of_Umbar",tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_f,itm_umb_armor_h,itm_umb_helm_d,itm_corsair_sword,itm_umbar_rapier,itm_umbar_pike,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,bandit_face1,bandit_face2],

["corsair_veteran_raider","Corsair_Veteran_Raider","Corsair_Veteran_Raiders",tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_f,itm_umb_armor_h,itm_umb_helm_d,itm_umbar_rapier,itm_umbar_pike,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,bandit_face1,bandit_face2],

["corsair_night_raider","Corsair_Night_Raider","Corsair_Night_Raiders",tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_g,itm_umb_helm_e,itm_umb_helm_f,itm_umbar_rapier,itm_umbar_pike,],
      attr_evil_tier_5,wp_tier_5,man_skills_1a,bandit_face1,bandit_face2],

["militia_of_umbar","Umbar_Marine","Umbar_Marines",tfg_ranged| tfg_armor| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_b,itm_umb_hood,itm_umb_shield_a,itm_umb_shield_e,itm_corsair_bow,itm_corsair_arrows,itm_corsair_sword,itm_corsair_throwing_dagger,itm_corsair_harpoon],
      attr_evil_tier_2,wp_tier_2_a,man_skills_2b,bandit_face1,bandit_face2],

["marksman_of_umbar","Marksman_of_Umbar","Marksmen_of_Umbar",tfg_ranged| tfg_armor| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_c,itm_umb_armor_e,itm_umb_helm_c,itm_umb_helm_d,itm_corsair_bow,itm_corsair_arrows,itm_corsair_sword,],
      attr_evil_tier_3,wp_tier_3_a,man_skills_3b,bandit_face1,bandit_face2],

["veteran_marksman_of_umbar","Veteran_Marksman_of_Umbar","Veteran_Marksmen_of_Umbar",tfg_ranged| tfg_armor| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_c,itm_umb_armor_e,itm_umb_helm_c,itm_umb_helm_d,itm_corsair_bow,itm_corsair_arrows,itm_umbar_cutlass,],
      attr_evil_tier_4,wp_tier_4_a,man_skills_4b,bandit_face1,bandit_face2],

["master_marksman_of_umbar","Corsair_Master_Marksman","Corsair_Master_Marksmen",tfg_ranged| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_d,itm_umb_helm_c,itm_umb_helm_d,itm_umb_shield_a,itm_corsair_bow,itm_corsair_arrows,itm_umbar_cutlass,],
      attr_evil_tier_5,wp_tier_5_a,man_skills_5b,bandit_face1,bandit_face2],

["corsair_marauder","Swordsman_of_Umbar","Swordsmen_of_Umbar",tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_f,itm_umb_armor_h,itm_umb_helm_d,itm_umb_shield_b,itm_umb_shield_d,itm_umbar_cutlass,itm_umbar_rapier,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,bandit_face1,bandit_face2],

["corsair_veteran_marauder","Veteran_Swordsman_of_Umbar","Veteran_Swordsmen_of_Umbar",tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_f,itm_umb_armor_h,itm_umb_helm_d,itm_umb_shield_b,itm_umb_shield_d,itm_umbar_cutlass,itm_umbar_rapier,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,bandit_face1,bandit_face2],

["corsair_elite_marauder","Corsair_Swordmaster","Corsair_Swordmasters",tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_g,itm_umb_helm_a,itm_umb_helm_b,itm_umb_shield_c,itm_kraken],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,bandit_face1,bandit_face2],

["assassin_of_umbar","Assassin_of_Umbar","Assassins_of_Umbar",tfg_ranged| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_f,itm_umb_armor_d,itm_umb_helm_b,itm_umb_shield_b,itm_corsair_bow,itm_corsair_arrows,itm_umbar_cutlass,itm_kraken,],
      attr_evil_tier_4,wp_tier_4_a,man_skills_4b,bandit_face1,bandit_face2],

["master_assassin_of_umbar","Corsair_Assassin","Corsair_Assassins",tfg_ranged| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_d,itm_umb_helm_a,itm_umb_helm_b,itm_corsair_bow,itm_corsair_arrows,itm_kraken,],
      attr_evil_tier_5,wp_tier_5_a,man_skills_4b,bandit_face1,bandit_face2],

["pikeman_of_umbar","Pikeman_of_Umbar","Pikemen_of_Umbar",tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_b,itm_umb_armor_c,itm_umb_helm_c,itm_umbar_pike,itm_umb_shield_a,itm_umb_shield_b,itm_umb_shield_d,],
      attr_evil_tier_3,wp_tier_3,man_skills_3a,bandit_face1,bandit_face2],

["veteran_pikeman_of_umbar","Veteran_Pikeman_of_Umbar","Veteran_Pikemen_of_Umbar",tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_c,itm_umb_armor_d,itm_umb_helm_a,itm_umbar_pike,itm_umb_shield_a,itm_umb_shield_b,],
      attr_evil_tier_4,wp_tier_4,man_skills_4a,bandit_face1,bandit_face2],

["pike_master_of_umbar","Corsair_Pike_Master","Corsair_Pike_Masters",tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_f,itm_umb_armor_g,itm_umb_helm_a,itm_umbar_pike,itm_umb_shield_a,itm_umb_shield_b,],
      attr_evil_tier_5,wp_tier_5,man_skills_5a,bandit_face1,bandit_face2],

["umbar_items","BUG","_",tf_hero,0,0,fac_umbar,
   [itm_leather_boots,itm_leather_gloves,itm_short_bow,itm_sumpter_horse,itm_saddle_horse,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

#ISENGARD

["orc_snaga_of_isengard","Orc_Snaga_of_Isengard","Orc_Snagas_of_Isengard",tf_orc| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_armor_a,itm_orc_simple_spear,itm_wood_club,itm_orc_simple_spear,itm_orc_slasher,itm_orc_axe,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      attr_orc_tier_1,wp_orc_tier_1,orc_skills_1a,orc_face1,orc_face2],

["orc_of_isengard","Orc_of_Isengard","Orcs_of_Isengard",tf_orc| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_helm_a,itm_isen_orc_helm_b,itm_isen_orc_armor_a,itm_orc_ragwrap,itm_isen_orc_shield_a,itm_orc_slasher,itm_orc_falchion,itm_orc_machete,itm_wood_club,itm_orc_simple_spear,itm_orc_bill,itm_orc_bill,itm_orc_axe,],
      attr_orc_tier_2,wp_orc_tier_2,orc_skills_2a,orc_face2,orc_face3],

["large_orc_of_isengard","Orc_Warrior_of_Isengard","Orc_Warriors_of_Isengard",tf_orc| tfg_armor| tfg_boots| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_helm_b,itm_isen_orc_armor_e,itm_leather_gloves_black,itm_orc_ragwrap,itm_isen_orc_shield_a,itm_orc_simple_spear,itm_orc_bill,],
      attr_orc_tier_3,wp_orc_tier_3,orc_skills_3a,orc_face4,orc_face5],

["elite_uruk_hai_pikeman","Fell_Uruk_Hai_Pikeman","Fell_Uruk_Hai_Pikemen",tf_urukhai| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_b,itm_isen_uruk_light_e,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_pike,],
      attr_urukhai_tier_5,wp_uruk_tier_5,urukhai_skills_5a,uruk_hai_face1,uruk_hai_face2],

["large_orc_despoiler","Large_Orc_Despoiler","Large_Orc_Despoilers",tf_orc| tfg_armor|tfg_shield| tfg_boots| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_helm_b,itm_isen_orc_armor_e,itm_orc_greaves,itm_orc_axe,itm_orc_sledgehammer,itm_twohand_wood_club,],
      attr_orc_tier_3,wp_orc_tier_3,orc_skills_3a,orc_face8,orc_face9],

["fell_orc_despoiler","Fell_Orc_Despoiler","Fell_Orc_Despoilers",tf_orc| tfg_armor|tfg_shield| tfg_boots| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_helm_b,itm_isen_orc_armor_e,itm_orc_greaves,itm_orc_sledgehammer,itm_orc_axe,itm_isengard_hammer,itm_twohand_wood_club,],
      attr_orc_tier_4,wp_orc_tier_4,orc_skills_4a,orc_face3,orc_face6],

["wolf_rider_of_isengard","Wolf_Rider_of_Isengard","Wolf_Riders_of_Isengard",tf_orc| tf_mounted| tfg_armor| tfg_horse| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_armor_a,itm_orc_falchion,itm_orc_simple_spear,itm_warg_1b,itm_warg_1c,itm_warg_1d,],
      attr_orc_tier_2,wp_orc_tier_2,orc_skills_2c,orc_face7,orc_face4],

["warg_rider_of_isengard","Warg_Rider_of_Isengard","Warg_Riders_of_Isengard",tf_orc| tf_mounted| tfg_armor| tfg_boots| tfg_horse| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_armor_a,itm_uruk_ragwrap,itm_orc_scimitar,itm_orc_machete,itm_orc_simple_spear,itm_warg_1b,itm_warg_1c,itm_wargarmored_1b,itm_wargarmored_2c,],
      attr_orc_tier_3,wp_orc_tier_3,orc_skills_3c,orc_face5,orc_face8],

["white_hand_rider","White_Hand_Rider","White_Hand_Riders",tf_orc| tf_mounted| tfg_armor| tfg_boots| tfg_horse| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_armor_e,itm_uruk_ragwrap,itm_orc_scimitar,itm_orc_falchion,itm_orc_sabre,itm_orc_simple_spear,itm_orc_throwing_arrow,itm_wargarmored_1b,itm_wargarmored_1c,itm_wargarmored_2b,itm_wargarmored_2c,],
      attr_orc_tier_4,wp_orc_tier_4,orc_skills_4c,orc_face7,orc_face8],

# "ghost" warg riders:(invisible riders for lone wargs) number and order match warg items
["warg_ghost_1b","Warg","Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive ,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_warg_1b],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face7,orc_face2],
["warg_ghost_1c","Warg","Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_warg_1c],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face6,orc_face1],
["warg_ghost_1d","Warg","Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_warg_1d],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face1,orc_face2],
["warg_ghost_a1b","Warg","Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_wargarmored_1b],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face1,orc_face2],
["warg_ghost_a1c","Armored Warg","Armored Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_wargarmored_1c],
     str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face1,orc_face2],
["warg_ghost_a2b","Armored Warg","Armored Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_wargarmored_2b],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face1,orc_face2],
["warg_ghost_a2c","Armored Warg","Armored Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_wargarmored_2c],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face1,orc_face2],
["warg_ghost_a3a","Armored Warg","Armored Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_wargarmored_3a],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face1,orc_face2],
["warg_ghost_h","Huge Warg","Huge Wargs",tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots |tfg_polearm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_warg_reward],
      str_30| agi_7| int_4| cha_4|level(9),wp_orc_tier_2,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face1,orc_face2],

#URUK HAI OF ISENGARD
["uruk_hai_tracker","Uruk_Hai_Hunter","Uruk_Hai_Hunters",tf_urukhai| tfg_armor| tfg_boots| tfg_ranged| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,itm_isengard_large_bow,itm_isengard_arrow,itm_orc_slasher,itm_orc_falchion,itm_orc_machete,itm_orc_axe,],
      attr_urukhai_tier_2,wp_uruk_tier_2_a,urukhai_skills_2b,uruk_hai_face1,uruk_hai_face2],

["large_uruk_hai_tracker","Large_Uruk_Hai_Tracker","Large_Uruk_Hai_Trackers",tf_urukhai| tfg_armor| tfg_boots| tfg_gloves| tfg_ranged| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_orc_armor_f,itm_leather_gloves_black,itm_isen_boots,itm_isengard_large_bow,itm_isengard_arrow,itm_isengard_sword,],
      attr_urukhai_tier_3,wp_uruk_tier_3_a,urukhai_skills_2b,uruk_hai_face1,uruk_hai_face2],

["fighting_uruk_hai_tracker","Uruk_Hai_Archer","Uruk_Hai_Archers",tf_urukhai| tfg_armor| tfg_boots| tfg_gloves| tfg_ranged| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_light_d,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_large_bow,itm_isengard_arrow,itm_isengard_sword,],
      attr_urukhai_tier_4,wp_uruk_tier_4_a,urukhai_skills_2b,uruk_hai_face1,uruk_hai_face2],

["fighting_uruk_hai_berserker","Uruk_Hai_Berserker","Uruk_Hai_Berserkers",tf_urukhai| tfg_armor| tfg_boots| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_c,itm_isen_uruk_light_a,itm_isen_shoes,itm_isengard_heavy_sword,],
      attr_urukhai_tier_6,wp_uruk_tier_6,urukhai_skills_6a,uruk_hai_face1,uruk_hai_face2],

["uruk_snaga_of_isengard","Uruk_Hai_Newborn","Uruk_Hai_Newborns",tf_urukhai| tfg_boots| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_shoes,itm_orc_axe,itm_orc_simple_spear,itm_orc_slasher,itm_orc_falchion,itm_orc_machete,itm_orc_axe,],
      attr_urukhai_tier_1,wp_uruk_tier_1,urukhai_skills_1a,uruk_hai_face1,uruk_hai_face2],

["uruk_hai_of_isengard","Uruk_Hai_Scout","Uruk_Hai_Scouts",tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_urukhai_tier_2,wp_uruk_tier_2,urukhai_skills_2a,uruk_hai_face1,uruk_hai_face2],

["large_uruk_hai_of_isengard","Uruk_Hai_Raider","Uruk_Hai_Raiders",tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_a,itm_isen_orc_armor_f,itm_leather_gloves_black,itm_isen_boots,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_urukhai_tier_3,wp_uruk_tier_3,urukhai_skills_3a,uruk_hai_face1,uruk_hai_face2],

["fighting_uruk_hai_warrior","Uruk_Hai_Swordsman","Uruk_Hai_Swordsmen",tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_b,itm_isen_uruk_light_d,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_urukhai_tier_4,wp_uruk_tier_4,urukhai_skills_4a,uruk_hai_face1,uruk_hai_face2],

["fighting_uruk_hai_champion","Fell_Uruk_Hai_Swordsman","Fell_Uruk_Hai_Swordsmen",tf_urukhai|tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_b,itm_isen_uruk_light_d,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_urukhai_tier_5,wp_uruk_tier_5,urukhai_skills_5a,uruk_hai_face1,uruk_hai_face2],

["uruk_hai_pikeman","Uruk_Hai_Axeman","Uruk_Hai_Axemen",tf_urukhai| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_a,itm_isen_orc_armor_f,itm_leather_gloves_black,itm_isen_boots,itm_isengard_heavy_axe,],
      attr_urukhai_tier_3,wp_uruk_tier_3,urukhai_skills_3a,uruk_hai_face1,uruk_hai_face2],

["fighting_uruk_hai_pikeman","Uruk_Hai_Pikeman","Uruk_Hai_Pikemen",tf_urukhai| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_b,itm_isen_uruk_light_e,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_pike,],
      attr_urukhai_tier_4,wp_uruk_tier_4,urukhai_skills_4a,uruk_hai_face1,uruk_hai_face2],

["urukhai_standard_bearer","Uruk_Hai_Standard_Bearer","Uruk_Hai_Standard_Bearers",tf_urukhai| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_b,itm_isen_uruk_light_e,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_banner,],
      attr_urukhai_tier_5,wp_uruk_tier_5,knows_ironflesh_7|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_5,uruk_hai_face1,uruk_hai_face2],

["isengard_items","BUG","_",tf_hero,0,0,fac_isengard,
   [itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,itm_isen_uruk_heavy_a,itm_isen_uruk_helm_d,],
      0,0,0,0],

#MORDOR URUKS

["uruk_snaga_of_mordor","Uruk_Snaga_of_Mordor","Uruk_Snagas_of_Mordor",tf_uruk| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_ragwrap,itm_m_uruk_light_a,itm_m_uruk_light_b,itm_orc_axe,itm_orc_falchion,itm_orc_sabre,itm_orc_simple_spear,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      attr_evil_tier_1,wp_uruk_tier_1,uruk_skills_1a,uruk_hai_face1,uruk_hai_face2],

["uruk_of_mordor","Uruk_of_Mordor","Uruks_of_Mordor",tf_uruk| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_ragwrap,itm_m_uruk_heavy_c,itm_m_uruk_heavy_d,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_uruk_spear,itm_mordor_uruk_shield_a,itm_uruk_helm_a,itm_uruk_helm_b,itm_orc_coif,],
      attr_evil_tier_2,wp_uruk_tier_2,uruk_skills_2a,uruk_hai_face1,uruk_hai_face2],

["large_uruk_of_mordor","Large_Uruk_of_Mordor","Large_Uruks_of_Mordor",tf_uruk| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_ragwrap,itm_uruk_greaves,itm_leather_gloves,itm_m_uruk_heavy_e,itm_m_uruk_heavy_f,itm_m_uruk_heavy_g,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_mordor_uruk_shield_a,itm_mordor_uruk_shield_b,itm_uruk_helm_c,itm_uruk_helm_d,],
      attr_evil_tier_3,wp_uruk_tier_3,uruk_skills_3a,uruk_hai_face1,uruk_hai_face2],

["fell_uruk_of_mordor","Fell_Uruk_of_Mordor","Fell_Uruks_of_Mordor",tf_uruk| tfg_shield|tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_greaves,itm_uruk_chain_greaves,itm_evil_gauntlets_b,itm_m_uruk_heavy_h,itm_m_uruk_heavy_i,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_mordor_uruk_shield_a,itm_mordor_uruk_shield_b,itm_uruk_helm_b,itm_uruk_helm_c,itm_uruk_helm_d,],
      attr_evil_tier_4,wp_uruk_tier_4,uruk_skills_4a,uruk_hai_face1,uruk_hai_face2],

["uruk_slayer_of_mordor","Uruk_Slayer_of_Mordor","Uruk_Slayers_of_Mordor",tf_uruk| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_tracker_boots,itm_m_uruk_heavy_e,itm_m_uruk_heavy_f,itm_m_uruk_heavy_g,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_uruk_voulge,itm_uruk_skull_spear,itm_uruk_pike_b,itm_uruk_helm_b,itm_uruk_helm_c,itm_uruk_helm_d,],
      attr_evil_tier_3,wp_uruk_tier_3,uruk_skills_3a,uruk_hai_face1,uruk_hai_face2],

["fell_uruk_slayer_of_mordor","Fell_Uruk_Slayer_of_Mordor","Fell_Uruk_Slayers_of_Mordor",tf_uruk| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_greaves,itm_uruk_chain_greaves,itm_evil_gauntlets_b,itm_m_uruk_heavy_h,itm_m_uruk_heavy_i,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_uruk_voulge,itm_uruk_helm_c,itm_uruk_helm_f,itm_uruk_heavy_axe,itm_uruk_skull_spear,itm_uruk_pike_b,itm_uruk_bow,itm_orc_hook_arrow],
      attr_evil_tier_4,wp(180),knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_4|knows_shield_3|knows_athletics_4,uruk_hai_face1,uruk_hai_face2],

["black_uruk_of_barad_dur","Black_Uruk_of_Barad_Dur","Black_Uruks_of_Barad_Dur",tf_uruk| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_m_uruk_heavy_j,itm_m_uruk_heavy_k,itm_uruk_heavy_axe,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_mordor_uruk_shield_c,itm_uruk_helm_e,],
      attr_evil_tier_5,wp_uruk_tier_5,uruk_skills_5a,uruk_hai_face1,uruk_hai_face2],

["uruk_mordor_standard_bearer","Mordor_Standard_Bearer","Mordor_Standard_Bearers",tf_uruk| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_greaves,itm_uruk_chain_greaves,itm_evil_gauntlets_b,itm_m_uruk_heavy_h,itm_m_uruk_heavy_i,itm_mordor_banner,itm_uruk_helm_b,itm_uruk_helm_c,itm_uruk_helm_d,],
      attr_evil_tier_5,wp_uruk_tier_5,knows_ironflesh_7|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_5,uruk_hai_face1,uruk_hai_face2],

#Trolls  & ents
["troll_of_moria","Cave_Troll","Cave_Trolls",tf_troll| tfg_armor| tf_no_capture_alive,0,0,fac_moria,
   [itm_item_30,itm_tree_trunk_club_a,itm_tree_trunk_club_a,itm_tree_trunk_club_a,],
      str_255| agi_3| int_3| cha_3|level(58),wp(75),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],

["armoured_troll","Battle_Troll_of_Isengard","Battle_Trolls_of_Isengard",tf_troll| tfg_armor| tf_no_capture_alive,0,0,fac_isengard,
   [itm_item_31,itm_giant_hammer,],
      str_255| agi_3| int_3| cha_3|level(61),wp(100),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],

["olog_hai","Olog_Hai_of_Mordor","Olog_Hai_of_Mordor",tf_troll| tfg_armor| tf_no_capture_alive,0,0,fac_mordor,
   [itm_item_32,itm_giant_mace,itm_giant_mace_b,itm_giant_hammer,],
      str_255| agi_3| int_3| cha_3|level(61),wp(100),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],

["ent","Ent","Ents",tf_troll| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_commoners,
   [itm_tree_trunk_invis,itm_ent_body,itm_ent_hands,itm_ent_feet_boots,itm_ent_head_helm,itm_ent_water,itm_ent_head_helm2,itm_ent_head_helm3,],
      str_255| agi_3| int_3| cha_3|level(63),wp(200),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],

# Dol Guldur Orcs(duplicates of Mordor orcs!)

["orc_snaga_of_guldur","Orc_Snaga_of_Guldur","Orc_Snagas_of_Guldur",tf_orc| tf_no_capture_alive,0,0,fac_guldur,
   [itm_orc_coif_bad, itm_orc_coif,itm_m_orc_light_a,itm_m_orc_light_b,itm_m_orc_light_c,itm_wood_club,itm_orc_machete,itm_orc_simple_spear,itm_orc_axe,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      attr_orc_tier_1,wp_orc_tier_1,orc_skills_1a,orc_face5,orc_face4],

["orc_of_guldur","Orc_of_Guldur","Orcs_of_Guldur",tf_orc| tfg_armor| tf_no_capture_alive,0,0,fac_guldur,
   [itm_orc_coif, itm_orc_coif_good, itm_orc_nosehelm_bad, itm_orc_nosehelm, itm_orc_ragwrap,itm_m_orc_light_b,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_wood_club,itm_orc_club_c,itm_orc_falchion,itm_orc_sabre,itm_orc_slasher,itm_orc_bill,itm_orc_axe,itm_mordor_orc_shield_b,itm_mordor_orc_shield_c,itm_mordor_orc_shield_a,],
      attr_orc_tier_2,wp_orc_tier_2,orc_skills_2a,orc_face3,orc_face8],

#Mordor Orcs
["orc_snaga_of_mordor","Orc_Snaga_of_Mordor","Orc_Snagas_of_Mordor",tf_orc| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_coif_bad, itm_orc_coif, itm_orc_nosehelm_bad,itm_orc_ragwrap,itm_m_orc_light_a,itm_m_orc_light_b,itm_m_orc_light_c,itm_wood_club,itm_orc_machete,itm_orc_axe,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      attr_orc_tier_1,wp_orc_tier_1,orc_skills_1a,orc_face1,orc_face2],

["orc_of_mordor","Orc_of_Mordor","Orcs_of_Mordor",tf_orc| tfg_armor| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_coif_bad, itm_orc_coif, itm_orc_nosehelm, itm_orc_nosehelm_bad, itm_orc_visorhelm_bad, itm_orc_ragwrap,itm_m_orc_light_b,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_wood_club,itm_orc_falchion,itm_orc_sabre,itm_orc_slasher,itm_orc_axe,itm_mordor_orc_shield_b,itm_mordor_orc_shield_c,itm_mordor_orc_shield_a,],
      attr_orc_tier_2,wp_orc_tier_2,orc_skills_2a,orc_face7,orc_face8],

["large_orc_of_mordor","Large_Orc_of_Mordor","Large_Orcs_of_Mordor",tf_orc| tfg_shield| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_nosehelm_good,itm_orc_kettlehelm_bad, itm_orc_kettlehelm, itm_orc_morion_bad, itm_orc_morion, itm_orc_visorhelm, itm_orc_greaves,itm_m_orc_light_d,itm_m_orc_light_e,itm_m_orc_heavy_a,itm_m_orc_heavy_b,itm_orc_sabre,itm_orc_falchion,itm_orc_slasher,itm_orc_axe,itm_mordor_orc_shield_b,itm_mordor_orc_shield_c,itm_orc_throwing_axes,],
      attr_orc_tier_3,wp_orc_tier_3,orc_skills_3a,orc_face3,orc_face6],

["fell_orc_of_mordor","Fell_Orc_of_Mordor","Fell_Orcs_of_Mordor",tf_orc| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_visorhelm_good, itm_orc_buckethelm_bad, itm_orc_buckethelm, itm_orc_kettlehelm_good,itm_orc_greaves,itm_evil_gauntlets_a,itm_orc_throwing_axes,itm_m_orc_heavy_b,itm_m_orc_heavy_c,itm_m_orc_heavy_d,itm_m_orc_heavy_e,itm_orc_club_c,itm_orc_sabre,itm_orc_falchion,itm_orc_two_handed_axe,itm_twohand_wood_club,itm_orc_scimitar,itm_mordor_orc_shield_b,itm_mordor_orc_shield_c,itm_mordor_orc_shield_e,],
      attr_orc_tier_4,wp_orc_tier_4,orc_skills_4a,orc_face7,orc_face4],

["warg_rider_of_gorgoroth","Warg_Rider_of_Gorgoroth","Warg_Riders_of_Gorgoroth",tf_orc| tf_mounted| tfg_ranged| tfg_armor| tfg_horse| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_coif_bad, itm_orc_coif, itm_orc_nosehelm_bad, itm_orc_nosehelm,itm_orc_visorhelm_bad,itm_m_orc_light_a,itm_m_orc_light_b,itm_m_orc_light_c,itm_orc_falchion,itm_orc_sabre,itm_orc_machete,itm_wargarmored_1b,itm_warg_1b,itm_warg_1d,itm_warg_1c,],
      attr_orc_tier_3,wp_orc_tier_3,orc_skills_3c,orc_face5,orc_face8],

["great_warg_rider_of_mordor","Great_Warg_Rider_of_Udun","Great_Warg_Riders_of_Udun",tf_orc| tf_mounted| tfg_ranged| tfg_armor| tfg_horse| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_visorhelm, itm_orc_nosehelm, itm_orc_ragwrap,itm_leather_gloves,itm_m_orc_light_b,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_orc_falchion,itm_orc_sabre,itm_orc_machete,itm_orc_slasher,itm_wargarmored_2b,itm_wargarmored_2c,itm_warg_1d,itm_warg_1c,],
      attr_orc_tier_4,wp_orc_tier_4,orc_skills_4c,orc_face7,orc_face8],

["morgul_orc","Morgul_Orc","Morgul_Orcs",tf_orc| tfg_armor| tfg_boots|tfg_polearm| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_kettlehelm_bad,itm_orc_morion_bad,itm_orc_visorhelm_bad,itm_orc_ragwrap,itm_m_orc_light_b,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_orc_simple_spear,itm_wood_club,itm_orc_slasher,itm_orc_bill,itm_orc_axe,itm_orc_machete,itm_mordor_orc_shield_c,itm_mordor_orc_shield_d,],
      attr_orc_tier_2,wp_orc_tier_2,orc_skills_2a,orc_face5,orc_face4],

["fell_morgul_orc","Fell_Morgul_Orc","Fell_Morgul_Orcs",tf_orc| tfg_armor| tfg_helm| tfg_boots|tfg_polearm| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_kettlehelm_good, itm_orc_morion_good, itm_orc_buckethelm_good,itm_orc_ragwrap,itm_leather_gloves,itm_m_orc_heavy_b,itm_m_orc_heavy_c,itm_m_orc_heavy_d,itm_m_orc_heavy_e,itm_orc_skull_spear,itm_orc_slasher,itm_orc_machete,itm_orc_bill,itm_mordor_orc_shield_d,itm_mordor_orc_shield_e,],
      attr_orc_tier_4,wp_orc_tier_4,orc_skills_4a,orc_face5,orc_face4],

["orc_tracker_of_mordor","Orc_Tracker_of_Mordor","Orc_Trackers_of_Mordor",tf_orc| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_coif_bad, itm_orc_nosehelm_bad,itm_orc_ragwrap,itm_leather_gloves,itm_m_orc_light_b,itm_m_orc_light_c,itm_orc_bow,itm_orc_hook_arrow,itm_orc_sabre,itm_orc_falchion,],
      attr_orc_tier_3,wp_orc_tier_3_a,orc_skills_3b,orc_face9,orc_face4],

["fell_orc_tracker_of_mordor","Fell_Orc_Tracker_of_Mordor","Fell_Orc_Trackers_of_Mordor",tf_orc| tfg_ranged| tfg_helm| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_coif, itm_orc_nosehelm, itm_orc_furboots,itm_leather_gloves,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_m_orc_light_c,itm_orc_bow,itm_orc_hook_arrow,itm_orc_sabre,itm_orc_slasher,itm_orc_slasher,],
      attr_orc_tier_4,wp_orc_tier_4_a,orc_skills_4b,orc_face1,orc_face4],

["orc_archer_of_mordor","Orc_Archer_of_Mordor","Orc_Archers_of_Mordor",tf_orc| tfg_ranged| tfg_armor| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_coif_bad, itm_orc_nosehelm_bad,itm_m_orc_light_b,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_orc_bow,itm_orc_hook_arrow,itm_wood_club,],
      attr_orc_tier_2,wp_orc_tier_2_a,orc_skills_2b,orc_face7,orc_face6],

["large_orc_archer_of_mordor","Large_Orc_Archer_of_Mordor","Large_Orc_Archers_of_Mordor",tf_orc| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_kettlehelm_bad, itm_orc_coif, itm_orc_nosehelm, itm_orc_ragwrap,itm_leather_gloves,itm_m_orc_light_b,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_orc_bow,itm_orc_hook_arrow,itm_orc_sabre,itm_orc_falchion,],
      attr_orc_tier_3,wp_orc_tier_3_a,orc_skills_3b,orc_face9,orc_face4],

["fell_orc_archer_of_mordor","Fell_Orc_Archer_of_Mordor","Fell_Orc_Archers_of_Mordor",tf_orc| tfg_ranged| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_kettlehelm, itm_orc_coif_good, itm_orc_buckethelm_bad, itm_orc_greaves,itm_evil_gauntlets_b,itm_m_orc_light_d,itm_m_orc_light_e,itm_m_orc_heavy_a,itm_m_orc_heavy_b,itm_orc_bow,itm_orc_hook_arrow,itm_orc_sabre,itm_orc_slasher,itm_orc_slasher,],
      attr_orc_tier_4,wp_orc_tier_4_a,orc_skills_4b,orc_face7,orc_face6],

#MORIA

["wolf_rider_of_moria","Wolf_Rider_of_Moria","Wolf_Riders_of_Moria",tf_orc| tf_mounted| tfg_ranged| tfg_armor| tfg_horse| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_nosehelm_bad,itm_orc_sabre,itm_orc_scimitar,itm_orc_falchion,itm_orc_simple_spear,itm_wood_club,itm_moria_armor_a,itm_moria_armor_b,itm_warg_1d,itm_warg_1b,itm_warg_1c,itm_orc_shield_b,itm_orc_shield_a],
      str_7| agi_7| int_4| cha_4|level(7),wp_orc_tier_2,orc_skills_2c,orc_face5,orc_face2],

["warg_rider_of_moria","Warg_Rider_of_Moria","Warg_Riders_of_Moria",tf_orc| tf_mounted| tfg_ranged| tfg_armor| tfg_horse| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_bughelm_bad, itm_orc_nosehelm, itm_orc_beakhelm_bad, itm_orc_sabre,itm_orc_sabre,itm_orc_scimitar,itm_orc_sabre,itm_orc_simple_spear,itm_moria_armor_a,itm_moria_armor_b,itm_moria_armor_c,itm_warg_1d,itm_warg_1d,itm_warg_1b,itm_warg_1c,itm_orc_ragwrap,itm_orc_shield_b,itm_orc_shield_a],
      str_9| agi_8| int_4| cha_4|level(12),wp_orc_tier_3,orc_skills_3c,orc_face9,orc_face8],

["bolg_clan_rider","Bolg_Clan_Rider","Bolg_Clan_Riders",tf_orc| tf_mounted| tfg_ranged| tfg_shield| tfg_armor| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_bughelm, itm_orc_bughelm_good, itm_orc_beakhelm, itm_orc_sabre,itm_orc_scimitar,itm_orc_simple_spear,itm_orc_skull_spear, itm_uruk_spear,itm_orc_throwing_arrow,itm_orc_ragwrap,itm_wargarmored_2b,itm_wargarmored_2c,itm_wargarmored_3a,itm_moria_armor_c,itm_moria_armor_d,itm_gundabad_helm_e,itm_moria_orc_shield_c,],
      str_11| agi_9| int_4| cha_4|level(17),wp_orc_tier_4,orc_skills_4c,orc_face5,orc_face4],

["snaga_of_moria","Snaga_of_Moria","Snagas_of_Moria",tf_orc| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_coif_bad, itm_orc_nosehelm_bad,itm_orc_sabre,itm_moria_armor_a,itm_moria_armor_b,itm_orc_falchion,itm_orc_scimitar,itm_orc_machete,itm_orc_axe,itm_wood_club,itm_orc_shield_a],
      attr_orc_tier_1,wp_orc_tier_1,orc_skills_1a,orc_face4,orc_face9],

["goblin_of_moria","Goblin_of_Moria","Goblins_of_Moria",tf_orc| tfg_armor| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_nosehelm, itm_orc_bughelm_bad, itm_orc_beakhelm_bad,itm_orc_sabre,itm_orc_falchion,itm_orc_scimitar,itm_moria_armor_b,itm_moria_armor_c,itm_moria_armor_b,itm_orc_simple_spear,itm_moria_orc_shield_b,itm_orc_shield_b,itm_orc_shield_a,],
      attr_orc_tier_2,wp_orc_tier_2,orc_skills_2a,orc_face9,orc_face2],

["large_goblin_of_moria","Large_Goblin_of_Moria","Large_Goblins_of_Moria",tf_orc| tfg_shield| tfg_armor| tfg_helm| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_bughelm, itm_orc_beakhelm, itm_orc_throwing_axes,itm_orc_sabre,itm_orc_scimitar,itm_moria_armor_d,itm_moria_armor_c,itm_orc_simple_spear,itm_moria_orc_shield_c,itm_moria_orc_shield_b,itm_moria_armor_d,itm_orc_bill,],
      attr_orc_tier_3,wp_orc_tier_3,orc_skills_3a,orc_face3,orc_face8],

["fell_goblin_of_moria","Fell_Goblin_of_Moria","Fell_Goblins_of_Moria",tf_orc| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_bughelm_good, itm_orc_beakhelm_good, itm_orc_axe,itm_orc_slasher,itm_orc_throwing_axes,itm_moria_orc_shield_b,itm_moria_armor_e,itm_orc_greaves,itm_moria_orc_shield_c,],
      attr_orc_tier_4,wp_orc_tier_4,orc_skills_4a,orc_face1,orc_face6],

["archer_snaga_of_moria","Goblin_Archer_of_Moria","Goblin_Archers_of_Moria",tf_orc| tfg_ranged| tfg_armor| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_bughelm_bad, itm_orc_beakhelm_bad, itm_orc_slasher,itm_orc_falchion,itm_orc_bow,itm_orc_hook_arrow,itm_moria_armor_b,],
      attr_orc_tier_2,wp_orc_tier_2_a,orc_skills_2b,orc_face9,orc_face6],

["large_goblin_archer_of_moria","Large_Goblin_Archer_of_Moria","Large_Goblin_Archers_of_Moria",tf_orc| tfg_ranged| tfg_boots| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_bughelm_bad, itm_orc_bughelm, itm_orc_beakhelm, itm_orc_slasher,itm_orc_falchion,itm_orc_bow,itm_orc_hook_arrow,itm_leather_gloves,itm_moria_armor_c,itm_moria_armor_b,itm_moria_armor_c,itm_orc_ragwrap,],
      attr_orc_tier_3,wp_orc_tier_3_a,orc_skills_3b,orc_face5,orc_face6],

["fell_goblin_archer_of_moria","Fell_Goblin_Archer_of_Moria","Fell_Goblin_Archers_of_Moria",tf_orc| tfg_armor| tfg_helm| tfg_ranged| tfg_boots| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_slasher,itm_orc_falchion,itm_orc_bow,itm_orc_hook_arrow,itm_moria_armor_d,itm_moria_armor_e,itm_orc_greaves,itm_orc_visorhelm,],
      attr_orc_tier_4,wp_orc_tier_4_a,orc_skills_4b,orc_face5,orc_face4],

["moria_items","BUG","BUG",tf_hero,0,0,fac_moria,
   [itm_warg_1b,itm_warg_1c,itm_warg_1d,itm_gundabad_helm_a,itm_gundabad_helm_b,itm_gundabad_helm_c,itm_gundabad_helm_d,itm_moria_orc_shield_c,itm_orc_scimitar,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,],
      0,0,0,0],

#MT GUNDABAD + tribal orc chief below

["goblin_gundabad","Orc_Snaga_of_Gundabad","Orc_Snagas_of_Gundabad",tf_orc| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_gundabad_helm_a,itm_gundabad_armor_a,itm_orc_tribal_a,itm_wood_club,itm_orc_machete,itm_orc_slasher,itm_orc_simple_spear,itm_orc_simple_spear,itm_bone_cudgel,],
      attr_orc_tier_1,wp_orc_tier_1,knows_power_strike_2|knows_power_throw_2|knows_athletics_3,orc_face1,orc_face2],

["orc_gundabad","Gundabad_Orc","Gundabad_Orcs",tf_orc| tfg_armor| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_gundabad_helm_a,itm_gundabad_helm_b,itm_gundabad_armor_b,itm_orc_machete,itm_orc_slasher,itm_wood_club,itm_orc_simple_spear,itm_orc_skull_spear,itm_gundabad_armor_c,itm_orc_ragwrap,itm_orc_axe,itm_orc_falchion,itm_orc_shield_a,itm_orc_shield_b,],
      attr_orc_tier_2,wp_orc_tier_2,knows_ironflesh_1|knows_power_strike_3|knows_power_throw_3|knows_shield_1|knows_athletics_4,orc_face7,orc_face6],

["orc_fighter_gundabad","Gundabad_Orc_Fighter","Gundabad_Orc_Fighters",tf_orc| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_orc_javelin,itm_orc_throwing_axes,itm_orc_throwing_axes,itm_gundabad_helm_c,itm_gundabad_helm_b,itm_gundabad_armor_d,itm_gundabad_armor_c,itm_orc_falchion,itm_orc_machete,itm_orc_scimitar,itm_orc_axe,itm_orc_skull_spear,itm_leather_gloves,itm_orc_coif,itm_orc_furboots,itm_orc_shield_b,itm_orc_shield_a,],
      attr_orc_tier_3,wp_orc_tier_3,knows_ironflesh_2|knows_power_strike_4|knows_power_throw_4|knows_shield_2|knows_athletics_5,orc_face5,orc_face6],

["fell_orc_warrior_gundabad","Gundabad_Orc_Warrior","Gundabad_Orc_Warriors",tf_orc| tfg_shield| tfg_armor| tfg_helm|tfg_boots| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_orc_javelin,itm_orc_javelin,itm_orc_javelin,itm_gundabad_helm_c,itm_gundabad_helm_d,itm_gundabad_armor_d,itm_gundabad_armor_e,itm_orc_scimitar,itm_orc_throwing_axes,itm_orc_throwing_axes_reward,itm_orc_sabre,itm_orc_club_c,itm_leather_gloves,itm_orc_furboots,itm_orc_shield_b,itm_orc_shield_c,],
      attr_orc_tier_4,wp_orc_tier_4,knows_ironflesh_3|knows_power_strike_5|knows_power_throw_5|knows_shield_3|knows_athletics_6,orc_face3,orc_face8],

["skirmisher_gundabad","Orc_Shooter_of_the_North","Orc_Shooters_of_the_North",tf_orc| tfg_armor| tfg_ranged| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_gundabad_helm_a,itm_gundabad_armor_a,itm_orc_tribal_a,itm_orc_ragwrap,itm_orc_bow,itm_orc_hook_arrow,itm_orc_club_a,itm_orc_club_c,],
      attr_orc_tier_2,wp_orc_tier_2_a,knows_power_strike_2|knows_power_throw_2|knows_power_draw_2|knows_shield_1|knows_athletics_4,orc_face3,orc_face8],

["warg_skirmisher_gundabad","Keen-Eyed_Orc_Archer_of_the_North","Keen-Eyed_Orc_Archers_of_the_North",tf_orc| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_gundabad_helm_a,itm_gundabad_helm_b,itm_gundabad_armor_b,itm_gundabad_armor_c,itm_orc_ragwrap,itm_orc_furboots,itm_orc_bow,itm_orc_hook_arrow,itm_orc_club_d,itm_orc_axe,],
      attr_orc_tier_3,wp_orc_tier_3_a,knows_power_strike_3|knows_power_throw_3|knows_power_draw_3|knows_shield_2|knows_athletics_5,orc_face1,orc_face6],

["goblin_north_clan_skirmisher","Fell_Orc_Archer_of_the_North","Fell_Orc_Archers_of_the_North",tf_orc| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_gundabad_helm_c,itm_gundabad_armor_e,itm_gundabad_armor_d,itm_orc_furboots,itm_orc_bow,itm_orc_hook_arrow,itm_orc_machete,itm_orc_axe,],
      attr_orc_tier_4,wp_orc_tier_4_a,knows_ironflesh_1|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_shield_3|knows_athletics_6,orc_face3,orc_face6],

["goblin_rider_gundabad","Gundabad_Goblin_Rider","Gundabad_Goblin_Riders",tf_orc| tf_mounted| tfg_armor| tfg_horse| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_orc_throwing_arrow,itm_orc_simple_spear,itm_orc_bow,itm_orc_hook_arrow,itm_gundabad_helm_a,itm_gundabad_armor_b,itm_orc_ragwrap,itm_wood_club,itm_twohand_wood_club,itm_warg_1d,itm_warg_1b,itm_warg_1c,],
      attr_orc_tier_3,wp_orc_tier_3,knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_shield_2|knows_athletics_4|knows_riding_4|knows_horse_archery_3,orc_face9,orc_face8],

["warg_rider_gundabad","Gundabad_Warg_Rider","Gundabad_Warg_Riders",tf_orc| tf_mounted| tfg_armor| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_orc_throwing_arrow,itm_orc_simple_spear,itm_orc_bow,itm_orc_hook_arrow,itm_gundabad_helm_b,itm_gundabad_helm_c,itm_gundabad_armor_b,itm_gundabad_armor_b,itm_orc_machete,itm_orc_scimitar,itm_orc_falchion,itm_twohand_wood_club,itm_orc_club_b,itm_orc_furboots,itm_orc_ragwrap,itm_warg_1c,itm_warg_1d,itm_warg_1b,itm_warg_1d,itm_orc_shield_b,itm_orc_shield_b],
      attr_orc_tier_4,wp_orc_tier_4,knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_power_draw_3|knows_shield_3|knows_athletics_5|knows_riding_5|knows_horse_archery_4,orc_face1,orc_face6],

["goblin_north_clan_rider","Goblin_North_Clan_Rider","Goblin_North_Clan_Riders",tf_orc| tf_mounted| tfg_armor| tfg_shield| tfg_helm| tfg_horse| tfg_boots|tfg_gloves| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_orc_simple_spear,itm_orc_bow,itm_orc_hook_arrow,itm_gundabad_helm_e,itm_gundabad_helm_d,itm_gundabad_armor_d,itm_gundabad_armor_e,itm_orc_sabre,itm_orc_scimitar,itm_orc_skull_spear,itm_orc_throwing_arrow,itm_orc_club_b,itm_orc_club_b,itm_orc_club_b,itm_leather_gloves,itm_orc_furboots,itm_wargarmored_3a,itm_orc_shield_b,itm_orc_shield_a,itm_orc_shield_b],
      str_11| agi_9| int_4| cha_4|level(20),wp_orc_tier_5,knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_power_draw_4|knows_shield_4|knows_athletics_6|knows_riding_6|knows_horse_archery_5,orc_face3,orc_face6],

["gundabad_items","BUG","_",tf_hero,0,0,fac_gundabad,
   [itm_orc_javelin,itm_metal_scraps_bad,itm_metal_scraps_medium,itm_metal_scraps_good,itm_warg_1b,itm_warg_1c,itm_warg_1d,itm_angmar_shield,itm_orc_bill,itm_orc_scimitar,itm_orc_machete,itm_orc_axe,itm_orc_two_handed_axe,itm_orc_greaves,],
      0,0,0,0],

["mountain_goblin","Mountain_Goblin","Mountain_Goblins",tf_orc| tf_no_capture_alive,0,0,fac_tribal_orcs,
   [itm_orc_tribal_a,itm_orc_tribal_b,itm_orc_tribal_c,itm_orc_tribal_c,itm_orc_shield_a,itm_orc_shield_b,itm_orc_shield_c,itm_orc_ragwrap,itm_skull_club,itm_twohand_wood_club,itm_bone_cudgel,itm_wood_club,itm_orc_simple_spear,itm_orc_sledgehammer,],
      attr_orc_tier_2,wp_orc_tier_2,knows_athletics_3|knows_power_strike_2,orc_face3,orc_face4],

["tribal_orc","Tribal_Orc","Tribal_Orcs",tf_orc| tf_no_capture_alive,0,0,fac_tribal_orcs,
   [itm_orc_tribal_a,itm_orc_tribal_b,itm_orc_tribal_c,itm_orc_tribal_c,itm_skull_club,itm_bone_cudgel,itm_twohand_wood_club,itm_wood_club,itm_orc_simple_spear,itm_orc_sledgehammer,itm_wood_club,itm_orc_simple_spear,itm_orc_sledgehammer,],
      attr_orc_tier_1,wp_orc_tier_1,knows_athletics_3,orc_face1,orc_face2],

["tribal_orc_warrior","Tribal_Orc_Warrior","Tribal_Orc_Warriors",tf_orc| tfg_armor| tf_no_capture_alive,0,0,fac_tribal_orcs,
   [itm_orc_tribal_b,itm_orc_tribal_c,itm_orc_tribal_c,itm_skull_club,itm_bone_cudgel,itm_wood_club,itm_twohand_wood_club,itm_orc_simple_spear,itm_orc_sledgehammer,itm_wood_club,itm_orc_simple_spear,itm_orc_sledgehammer,],
      attr_orc_tier_2,wp_orc_tier_2,knows_athletics_4,orc_face7,orc_face6],

["tribal_orc_chief","Tribal_Orc_Chief","Tribal_Orc_Chiefs",tf_orc| tfg_armor| tfg_helm| tfg_boots| tfg_shield| tf_no_capture_alive,0,0,fac_tribal_orcs,
   [itm_orc_beakhelm,itm_orc_tribal_a,itm_orc_tribal_b,itm_orc_tribal_c,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_orc_ragwrap,itm_orc_skull_spear,itm_moria_orc_shield_a, (itm_orc_shield_c, imod_reinforced)],
      attr_orc_tier_5,wp_orc_tier_5,knows_athletics_4|knows_power_strike_4|knows_ironflesh_4,orc_face5,orc_face4],

#BLACK NUMENOREANS

["black_numenorean_renegade","Black_Numenorean_Renegade","Black_Numenorean_Renegades",tf_evil_man| tfg_armor| tfg_boots,0,0,fac_mordor,
   [itm_leather_boots,itm_leather_gloves_black,itm_evil_light_armor,itm_uruk_spear,itm_uruk_falchion_a,itm_orc_sabre,itm_umb_hood],
      attr_tier_2,wp_tier_2,knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_power_draw_1|knows_shield_1|knows_athletics_2|knows_riding_1,mordor_man1,mordor_man2],

["black_numenorean_warrior","Black_Numenorean_Warrior","Black_Numenorean_Warriors",tf_evil_man| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_leather_boots,itm_leather_gloves_black,itm_evil_light_armor,itm_m_armor_a,itm_mordor_man_shield_b,itm_mordor_sword,itm_uruk_pike_b,itm_umb_hood,itm_orc_coif],
      attr_tier_3,wp_tier_3,knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_shield_2|knows_athletics_2|knows_riding_1,mordor_man1,mordor_man2],

["black_numenorean_veteran_warrior","Black_Numenorean_Veteran_Warrior","Black_Numenorean_Veteran_Warriors",tf_evil_man| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_uruk_greaves,itm_evil_gauntlets_b,itm_m_armor_a,itm_m_armor_b,itm_mordor_helm,itm_mordor_man_shield_b,itm_mordor_longsword,itm_mordor_sword,],
      attr_tier_4,wp_tier_4,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_3|knows_riding_1|knows_tactics_1,mordor_man1,mordor_man2],

["black_numenorean_champion","Black_Numenorean_Champion","Black_Numenorean_Champions",tf_evil_man| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_black_num_armor,itm_black_num_helm,itm_mordor_man_shield_a,itm_mordor_longsword,itm_orc_club_d],
      attr_tier_5,wp_tier_5,knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_1|knows_tactics_1,mordor_man1,mordor_man2],

["black_numenorean_assassin","Black_Numenorean_Assassin","Black_Numenorean_Assassins",tf_evil_man| tfg_gloves| tfg_armor| tfg_boots,0,0,fac_mordor,
   [itm_uruk_greaves,itm_leather_gloves_black,itm_m_armor_a,itm_m_armor_b,itm_black_num_armor,itm_mordor_helm,itm_mordor_sword,itm_mordor_longsword,itm_umb_hood,itm_umb_hood, itm_umb_shield_a, itm_corsair_throwing_dagger, itm_corsair_throwing_dagger, itm_corsair_throwing_dagger],
      attr_tier_5,wp_tier_6,knows_common|knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_power_draw_1|knows_shield_5|knows_athletics_9|knows_riding_1,mordor_man1,mordor_man2],

["black_numenorean_veteran_horseman","Black_Numenorean_Horseman","Black_Numenorean_Horsemen",tf_evil_man| tf_mounted| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_leather_boots,itm_evil_gauntlets_b,itm_m_armor_a,itm_m_armor_b,itm_mordor_helm,itm_mordor_man_shield_b,itm_mordor_warhorse,itm_mordor_longsword,itm_uruk_spear],
      attr_tier_4,wp_tier_4,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_power_draw_1|knows_shield_3|knows_athletics_3|knows_riding_4|knows_horse_archery_1|knows_tactics_1,mordor_man1,mordor_man2],

["black_numenorean_horsemaster","Black_Numenorean_Horsemaster","Black_Numenorean_Horsemasters",tf_evil_man| tf_mounted| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_uruk_greaves,itm_evil_gauntlets_a,itm_black_num_armor,itm_black_num_helm,itm_mordor_man_shield_a,itm_mordor_warhorse,itm_mordor_longsword,itm_uruk_spear, itm_uruk_pike_b],
      attr_tier_5,wp_tier_5,knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_power_draw_1|knows_shield_4|knows_athletics_3|knows_riding_5|knows_horse_archery_1|knows_tactics_1,mordor_man1,mordor_man2],

#Captains and lieutenants of all factions
["noldorin_commander","Noldorin_Commander","Noldorin_Commanders",tf_imladris|tf_mounted| tfg_armor| tfg_shield| tfg_horse| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_riv_tiara,itm_riv_guard,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_riv_shield_b,itm_riv_warhorse,],
      attr_elf_tier_6,wp_elf_tier_6,knows_inventory_management_1|knows_power_draw_6|knows_tactics_6|knows_tracking_1|knows_horse_archery_6|knows_riding_5|knows_athletics_6|knows_power_strike_6|knows_ironflesh_6,rivendell_elf_face_1,rivendell_elf_face_2],

["elf_captain_of_lothlorien","Lothlorien_Captain","Lothlorien_Captains",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_lorien,
   [itm_riv_tiara,itm_lorien_armor_d,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_lorien_shield_b,],
      attr_elf_tier_6,wp_elf_tier_6,knows_inventory_management_1|knows_power_draw_6|knows_tactics_4|knows_tracking_1|knows_horse_archery_5|knows_riding_5|knows_athletics_5|knows_power_strike_5|knows_ironflesh_5,lorien_elf_face_1,lorien_elf_face_2],

["lothlorien_lieutenant","Lothlorien_Lieutenant","Lothlorien_Lieutenants",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_lorien,
   [itm_riv_tiara,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_lorien_shield_b,],
      attr_elf_tier_6,wp_elf_tier_6,knows_inventory_management_1|knows_power_draw_6|knows_tactics_3|knows_tracking_1|knows_riding_3|knows_athletics_4|knows_power_strike_4|knows_ironflesh_4,lorien_elf_face_1,lorien_elf_face_2],

["elf_captain_of_mirkwood","Greenwood_Captain","Greenwood_Captains",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_woodelf,
   [itm_riv_tiara,itm_mirkwood_armor_e,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_mirkwood_sword,itm_elven_bow,itm_elven_arrows,itm_mirkwood_spear_shield_c,],
      attr_elf_tier_6,wp_elf_tier_6,knows_riding_4|knows_athletics_5|knows_power_draw_7|knows_power_strike_5|knows_ironflesh_5,mirkwood_elf_face_1,mirkwood_elf_face_2],

["mirkwood_lieutenant","Greenwood_Lieutenant","Greenwood_Lieutenants",tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_woodelf,
   [itm_riv_tiara,itm_mirkwood_armor_c,itm_mirkwood_leather_greaves,itm_mirkwood_sword,itm_elven_bow,itm_elven_arrows,itm_mirkwood_spear_shield_c,],
      attr_elf_tier_6,wp_elf_tier_6,knows_riding_3|knows_athletics_4|knows_power_draw_6|knows_power_strike_4|knows_ironflesh_4,mirkwood_elf_face_1,mirkwood_elf_face_2],

["elf_captain_of_rivendell","Rivendell_Captain","Rivendell_Captains",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_riv_tiara,itm_riv_lord,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_lorien_shield_b,],
      attr_elf_tier_6,wp_elf_tier_6,knows_riding_5|knows_athletics_5|knows_power_strike_5|knows_power_draw_6|knows_ironflesh_5,rivendell_elf_face_1,rivendell_elf_face_2],

["rivendell_lieutenant","Rivendell_Lieutenant","Rivendell_Lieutenants",tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_riv_tiara,itm_riv_plate,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_lorien_shield_b,],
      attr_elf_tier_6,wp_elf_tier_6,knows_riding_3|knows_athletics_4|knows_power_draw_5|knows_power_strike_4|knows_ironflesh_4,rivendell_elf_face_1,rivendell_elf_face_2],

["lieutenant_of_rohan","Lieutenant_of_Rohan","Lieutenants_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_shield_e,itm_rohan_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_tactics_2|knows_riding_7|knows_athletics_2|knows_shield_1|knows_power_strike_4,rohan_face_old_1,rohan_face_older_2],

["captain_of_rohan","Captain_of_Rohan","Captains_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_shield_e,itm_rohan_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_tactics_3|knows_riding_7|knows_athletics_3|knows_shield_2|knows_power_strike_5|knows_ironflesh_6,rohan_face_old_1,rohan_face_older_2],

["high_captain_of_rohan","High_Captain_of_Rohan","High_Captains_of_Rohan",tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_shield_e,itm_rohirrim_heavy_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_tactics_4|knows_riding_7|knows_athletics_3|knows_shield_4|knows_power_strike_7|knows_ironflesh_7,rohan_face_old_1,rohan_face_older_2],

["lieutenant_of_isengard","Lieutenant_of_Isengard","Lieutenants_of_Isengard",tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves,0,0,fac_isengard,
   [itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_urukhai_tier_6,wp_uruk_tier_6,knows_common|knows_riding_3|knows_power_strike_2,uruk_hai_face1,uruk_hai_face2],

["captain_of_isengard","Captain_of_Isengard","Captains_of_Isengard",tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_helm_d,itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_urukhai_tier_6,wp_uruk_tier_6,knows_common|knows_riding_4|knows_shield_3|knows_power_strike_3|knows_ironflesh_3,uruk_hai_face1,uruk_hai_face2],

["high_captain_of_isengard","High_Captain_of_Isengard","High_Captains_of_Isengard",tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_helm_d,itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_urukhai_tier_6,wp_uruk_tier_6,knows_common|knows_riding_5|knows_shield_4|knows_power_strike_5|knows_ironflesh_3,uruk_hai_face1,uruk_hai_face2],

["lieutenant_of_mordor","Lieutenant_of_Mordor","Lieutenants_of_Mordor",tf_evil_man| tf_mounted| tfg_armor| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_mordor_cap_helm,itm_m_cap_armor,itm_leather_gloves,itm_uruk_greaves,itm_mordor_man_shield_a,itm_mordor_longsword,itm_mordor_warhorse2,],
      attr_tier_6,wp_tier_6,knows_common|knows_tactics_1|knows_athletics_2|knows_shield_1|knows_power_strike_4,mordor_man1,mordor_man2],

["captain_of_mordor","Captain_of_Mordor","Captains_of_Mordor",tf_evil_man| tf_mounted| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_mordor_cap_helm,itm_m_cap_armor,itm_evil_gauntlets_b,itm_uruk_greaves,itm_mordor_man_shield_a,itm_mordor_longsword,itm_mordor_warhorse2,],
      attr_tier_6,wp_tier_6,knows_common|knows_tactics_3|knows_riding_2|knows_athletics_3|knows_shield_3|knows_power_strike_4|knows_ironflesh_1,mordor_man1,mordor_man2],

["high_captain_of_mordor","High_Captain_of_Mordor","High_Captains_of_Mordor",tf_evil_man| tf_mounted| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_mordor_cap_helm,itm_m_cap_armor,itm_evil_gauntlets_a,itm_uruk_greaves,itm_mordor_man_shield_a,itm_mordor_longsword,itm_mordor_warhorse2,],
      attr_tier_6,wp_tier_6,knows_common|knows_tactics_4|knows_riding_6|knows_athletics_3|knows_shield_3|knows_power_strike_5|knows_ironflesh_7,mordor_man1,mordor_man2],

["easterling_chieftain","Variag_Chieftain","Variag_Chieftains",tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_khand_noble_lam,itm_variag_greaves,itm_variag_kataphrakt,itm_khand_helmet_b1,itm_mail_mittens,itm_khand_tulwar,itm_khand_2h_tulwar,itm_easterling_round_horseman,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_4|knows_athletics_3|knows_shield_2|knows_power_strike_4|knows_ironflesh_5,khand_man1,khand_man2],

["easterling_lieutenant","Variag_War_Priest","Variag_War_Priests",tf_evil_man| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_khand,
   [itm_khand_noble_lam,itm_variag_greaves,itm_khand_helmet_b1,itm_mail_mittens,itm_khand_rammace,itm_easterling_round_horseman,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_3|knows_athletics_2|knows_power_strike_3|knows_ironflesh_3,khand_man1,khand_man2],

["harad_chieftain","Harad_Chieftain","Harad_Chieftains",tf_harad| tf_mounted| tfg_gloves| tfg_shield| tfg_armor| tfg_horse| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_leather_greaves,itm_harad_heavy,itm_harad_dragon_helm,itm_harad_khopesh,itm_harad_long_shield_c,itm_harad_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_4|knows_athletics_3|knows_shield_3|knows_power_strike_4|knows_ironflesh_4,haradrim_face_1,haradrim_face_2],

["harad_lieutenant","Harad_Lieutenant","Harad_Lieutenants",tf_harad| tf_mounted| tfg_gloves| tfg_shield| tfg_armor| tfg_horse| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_leather_greaves,itm_harad_heavy,itm_harad_dragon_helm,itm_harad_khopesh,itm_harad_long_shield_c,itm_harad_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_3|knows_athletics_2|knows_power_strike_3|knows_ironflesh_3,haradrim_face_1,haradrim_face_2],

["black_numenorean_captain","Black_Numenorean_Captain","Black_Numenorean_Captains",tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_umbar,
   [itm_uruk_chain_greaves,itm_m_cap_armor,itm_evil_gauntlets_a,itm_witchking_helmet,itm_mordor_sword,itm_harad_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_5|knows_athletics_3|knows_shield_2|knows_power_strike_5|knows_ironflesh_5,mordor_man1,mordor_man2],

["black_numenorean_lieutenant","Black_Numenorean_Lieutenant","Black_Numenorean_Lieutenants",tf_evil_man| tf_mounted| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_umbar,
   [itm_umb_armor_c,itm_umb_helm_a,itm_evil_gauntlets_a,itm_harad_leather_greaves,itm_umb_shield_c,itm_umb_shield_d,itm_umbar_cutlass,itm_harad_horse,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_5|knows_athletics_2|knows_shield_3|knows_power_strike_4|knows_ironflesh_3,mordor_man1,mordor_man2],

["dunnish_chieftain","Dunnish_Chieftain","Dunnish_Chieftains",tf_dunland| tf_mounted| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_dunland_armor_e,itm_dun_berserker,itm_dun_shield_b,itm_dun_berserker,itm_hunter,itm_leather_boots,itm_evil_gauntlets_a,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_4|knows_athletics_3|knows_shield_3|knows_power_strike_5|knows_ironflesh_5,dunland_face1,dunland_face2],

["dunnish_lieutenant","Dunnish_Hetman","Dunnish_Hetmen",tf_dunland| tfg_armor| tfg_helm| tfg_boots,0,0,fac_dunland,
   [itm_dunland_wolfboots,itm_dunland_armor_e,itm_dun_berserker,itm_dun_helm_c,itm_dun_shield_b,itm_evil_gauntlets_a,],
      attr_tier_6,wp_tier_6,knows_common|knows_athletics_2|knows_shield_1|knows_power_strike_3|knows_ironflesh_3,dunland_face1,dunland_face2],

["goblin_chieftain","Orc_Chieftain","Orc_Chieftains",tf_orc| tf_mounted| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_sabre,itm_moria_orc_shield_a,itm_moria_orc_shield_b,itm_leather_gloves,itm_orc_coif,itm_orc_coif,itm_orc_ragwrap,itm_wargarmored_1b,],
      attr_orc_tier_6,wp_orc_tier_6,knows_riding_4|knows_athletics_4|knows_power_draw_1|knows_power_throw_3|knows_power_strike_5|knows_ironflesh_5,orc_face5,orc_face8],
 
["captain_of_gondor","Captain_of_Gondor","Captains_of_Gondor",tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_gon_lord,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gondor_shield_d,itm_gondor_guard_warhorse,],
      attr_tier_6,wp_tier_6,knows_common|knows_riding_4|knows_athletics_4|knows_shield_3|knows_power_strike_5|knows_ironflesh_6,gondor_face_old_1,gondor_face_old_2],

#["high_captain_of_gondor","High_Captain_of_Gondor","High_Captains_of_Gondor",tf_mounted|tfg_gloves|tfg_shield|tfg_armor|tfg_helmet|tfg_horse|tfg_boots,0,0,fac_gondor,
#   [itm_gon_lord,itm_gondor_leader_helm,itm_mail_mittens,itm_mail_mittens,itm_mail_boots,itm_gondor_shield_a,itm_sword_medieval_c,itm_sword_viking_1,itm_gondor_warhorse],
#      def_attrib|level(40),wp(255),knows_common|knows_riding_2|knows_athletics_6|knows_shield_4|knows_power_strike_6|knows_ironflesh_6,gondor_face_old_1,gondor_face_old_2],
["end_leaders","bug","bug",0,0,0,fac_gondor,   [],      0,0,0,0],
#END# Captains and lieutenants of all factions
#Agents begin
["nobleman","Nobleman","Noblemen",tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_riding_5|knows_ironflesh_3,0x110000000003395063803a],
["gondor_agent","Gondor_Agent","Gondor_Agents",tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_gondor,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common|knows_riding_5|knows_ironflesh_3,gondor_face1,gondor_face2],
["rohan_agent","Rohan_Agent","Rohan_Agents",tf_rohan| tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_rohan,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common|knows_riding_5|knows_ironflesh_3,rohan_face_middle_1,rohan_face_older_2],
["mordor_agent","Mordor_Agent","Mordor_Agents",tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common|knows_riding_5|knows_ironflesh_3,gondor_face1,gondor_face2],
["isengard_agent","Isengard_Agent","Isengard_Agents",tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_isengard,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common|knows_riding_5|knows_ironflesh_3,evil_man_face1,evil_man_face2],
#Agents end

["looter","Looter","Looters",0,0,0,fac_outlaws,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,bandit_face1,bandit_face2],
["bandit","Bandit","Bandits",tfg_armor,0,0,fac_outlaws,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_power_draw_1,bandit_face1,bandit_face2],
["brigand","Brigand","Brigands",tfg_boots| tfg_armor| tfg_horse,0,0,fac_outlaws,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_power_draw_3,bandit_face1,bandit_face2],
["mountain_bandit","Mountain_Bandit","Mountain_Bandits",tfg_armor| tfg_boots,0,0,fac_outlaws,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_power_draw_2,rhodok_face_young_1,rhodok_face_old_2],
["forest_bandit","Forest_Bandit","Forest_Bandits",tfg_armor| tfg_ranged| tfg_boots,0,0,fac_outlaws,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_power_draw_3,swadian_face_young_1,swadian_face_old_2],
["sea_raider","Sea_Raider","Sea_Raiders",tfg_boots| tfg_armor| tfg_shield,0,0,fac_outlaws,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1,nord_face_old_2],
["steppe_bandit","Steppe_Bandit","Steppe_Bandits",tfg_boots| tfg_armor| tfg_horse| tfg_ranged| tf_mounted,0,0,fac_outlaws,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1,khergit_face_old_2],
["manhunter","Manhunter","Manhunters",tfg_armor,0,0,fac_manhunters,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common,bandit_face1,bandit_face2],
 
["kidnapped_girl","Kidnapped_Girl","Kidnapped_Girls",tf_hero| tf_female| tf_randomize_face| tf_unmoveable_in_party_window,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common|knows_riding_2,woman_face_1,woman_face_2],
["refugee","Refugee","Refugees",tf_female| tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,refugee_face1,refugee_face2],
["peasant_woman","Peasant_Woman","Peasant_Women",tf_female| tf_randomize_face| tfg_armor|tfg_boots,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots, itm_practice_staff],
      attr_tier_1,wp_tier_1,knows_common,refugee_face1,refugee_face2],
["caravan_master","Caravan_Master","Caravan_Masters",tf_mounted| tfg_armor| tfg_horse| tfg_boots,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_riding_4|knows_ironflesh_3,merchant_face_1,merchant_face_2],
["caravan_guard","Caravan_Guard","Caravan_Guards",tf_mounted| tfg_armor| tfg_horse| tfg_boots,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_2,wp_tier_2,knows_common|knows_riding_2|knows_shield_1|knows_power_strike_2|knows_ironflesh_1,bandit_face1,bandit_face2],

# Messengers of different races for quests (non-heroes: can be killed or captured on purpose)
# TODO: Maybe make a messenger for each different faction. (CppCoder)

["messenger_man", "Messenger", "Messengers", tf_randomize_face| tf_unmoveable_in_party_window|tfg_armor|tfg_boots,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common|knows_riding_2,man_face_young_1,man_face_old_2],

["messenger_elf", "Messenger", "Messengers", tf_lorien| tf_randomize_face| tf_unmoveable_in_party_window|tfg_armor|tfg_boots,0,0,fac_commoners,
   [itm_lorien_archer,itm_elven_boots,],
      attr_elf_tier_1,wp_elf_tier_1,knows_common|knows_riding_2,lorien_elf_face_1,lorien_elf_face_2],

["messenger_dwarf", "Messenger", "Messengers", tf_dwarf| tf_randomize_face| tf_unmoveable_in_party_window|tfg_armor|tfg_boots,0,0,fac_commoners,
   [itm_dwarf_armor_a,itm_dwarf_pad_boots,],
      attr_dwarf_tier_1,wp_dwarf_tier_1,knows_common_dwarf|knows_riding_2,dwarf_face_2,dwarf_face_3],

["messenger_orc", "Messenger", "Messengers", tf_orc| tf_randomize_face| tf_unmoveable_in_party_window|tfg_armor|tfg_boots,0,0,fac_commoners,
   [itm_moria_armor_a,],
      attr_orc_tier_1,wp_orc_tier_1,knows_common|knows_riding_2,orc_face3,orc_face8],

# Added to fix evil factions getting gondor messengers.
["messenger_evil_man", "Messenger", "Messengers", tf_evil_man|tf_randomize_face|tf_unmoveable_in_party_window|tfg_armor|tfg_boots,0,0,fac_commoners,
   [itm_khand_foot_lam_c,itm_variag_greaves,],
      attr_tier_1,wp_tier_1,knows_common|knows_riding_2,khand_man1,khand_man2],

#This troop is the troop marked as soldiers_end
["town_walker_1","Townsman","Townsmen",tf_gondor| tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,man_face_young_1,man_face_old_2],
["town_walker_2","Townswoman","Townswomen",tf_female| tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,woman_face_1,woman_face_2],
["village_walker_1","Villager","Villagers",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,man_face_younger_1,man_face_older_2],
["village_walker_2","Villager","Villagers",tf_female| tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,woman_face_1,woman_face_2],
["spy_walker_1","Townsman","Townsmen",tfg_boots| tfg_armor| tfg_helm,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,man_face_middle_1,man_face_old_2],
["spy_walker_2","Townswoman","Townswomen",tf_female| tfg_boots| tfg_armor| tfg_helm,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,woman_face_1,woman_face_2],
# Ryan END
 
#TLD walkers - In Vain Edit
["walker_man_gondor_black","Townsman","_",tf_gondor| tfg_boots| tfg_armor,0,0,fac_gondor,
   [itm_blue_tunic,itm_white_tunic_a,itm_gon_jerkin,itm_white_tunic_a,itm_white_tunic_b,itm_white_tunic_c,itm_black_tunic,itm_leather_boots,itm_straw_hat,itm_felt_hat_b,itm_woolen_cap,],
      attr_tier_1,wp_tier_1,knows_common,gondor_civil_face_1,gondor_civil_face_2],
["walker_man_gondor_white","Townsman","_",tf_gondor| tfg_boots| tfg_armor,0,0,fac_gondor,
   [itm_white_tunic_a, itm_white_tunic_b, itm_white_tunic_c, itm_blue_tunic, itm_black_tunic,itm_leather_boots,itm_straw_hat,itm_felt_hat_b,itm_woolen_cap,],
      attr_tier_5,wp_tier_1,knows_common,gondor_civil_face_1,gondor_civil_face_2],
["walker_man_gondor_blue","Townsman","_",tf_gondor| tfg_boots| tfg_armor,0,0,fac_gondor,
   [itm_blue_tunic, itm_white_tunic_a, itm_gon_jerkin, itm_leather_jerkin, itm_black_tunic,itm_leather_apron,itm_lossarnach_shirt, itm_leather_boots,itm_straw_hat,itm_felt_hat_b,itm_woolen_cap,],
      attr_tier_1,wp_tier_1,knows_common,gondor_civil_face_1,gondor_civil_face_2],
["walker_man_gondor_green","Townsman","_",tf_gondor| tfg_boots| tfg_armor,0,0,fac_gondor,
   [itm_blue_tunic, itm_white_tunic_a, itm_leather_jerkin, itm_black_tunic, itm_leather_apron, itm_leather_boots,itm_straw_hat,itm_felt_hat_b,itm_woolen_cap,],
      attr_tier_1,wp_tier_1,knows_common,gondor_civil_face_1,gondor_civil_face_2],
["walker_man_rohan_t","Rohan_Townsman","_",tf_rohan| tfg_boots| tfg_armor,0,0,fac_rohan,
   [itm_green_tunic,itm_rohan_fine_outfit_dale_dress,itm_white_tunic_a,itm_rohan_armor_a,itm_free_rohan_armor_b,itm_free_rohan_armor_c,itm_leather_jerkin,itm_black_tunic,itm_leather_apron,itm_leather_boots,itm_rohan_shoes,itm_woolen_cap,],
      attr_tier_1,wp_tier_1,knows_common,rohan_face_younger_1,rohan_face_older_2],
["walker_man_rohan_d","Rohan_Townsman","_",tf_rohan| tfg_boots| tfg_armor,0,0,fac_rohan,
   [itm_green_tunic,itm_rohan_fine_outfit_dale_dress,itm_white_tunic_a,itm_rohan_armor_a,itm_free_rohan_armor_b,itm_free_rohan_armor_c,itm_leather_jerkin,itm_black_tunic,itm_leather_apron,itm_rohan_shoes,itm_woolen_cap,],
      attr_tier_1,wp_tier_1,knows_common,rohan_face_younger_1,rohan_face_older_2],
["walker_woman_rohan_t","Rohan_Maiden","_",tf_female| tfg_boots| tfg_armor,0,0,fac_rohan,
   [itm_robe_generic_dress,itm_green_dress, itm_black_dress,itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,itm_leather_boots],
      attr_tier_1,wp_tier_1,knows_common,rohan_woman_face_1,rohan_woman_face_2],
["walker_woman_rohan_d","Rohan_Maiden","_",tf_female| tfg_boots| tfg_armor,0,0,fac_rohan,
   [itm_robe_generic_dress,itm_rohan_fine_outfit_dale_dress, itm_green_dress, itm_black_dress, itm_green_tunic, itm_white_tunic_a, itm_rohan_armor_a, itm_free_rohan_armor_b, itm_free_rohan_armor_c,itm_leather_jerkin, itm_black_tunic, itm_leather_apron,itm_leather_boots,itm_rohan_shoes],
      attr_tier_1,wp_tier_1,knows_common,rohan_woman_face_1,rohan_woman_face_2],
["walker_woman_gondor_b","Gondor_Woman","_",tf_female| tfg_boots| tfg_armor| tfg_helm,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_robe_generic_dress,itm_rohan_fine_outfit_dale_dress,itm_black_dress, itm_wimple_a, itm_wimple_with_veil ,itm_leather_boots,],
   attr_tier_1,wp_tier_1,knows_common,woman_face_1,woman_face_2],
["walker_woman_gondor_bw","Gondor_Woman","_",tf_female| tfg_boots| tfg_armor| tfg_helm,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_robe_generic_dress,itm_black_dress,itm_black_dress, itm_blackwhite_dress,itm_wimple_a, itm_wimple_with_veil, itm_fine_hat,itm_leather_boots,],
      attr_tier_1,wp_tier_1,knows_common,woman_face_1,woman_face_2],
["walker_woman_gondor_w","Gondor_Noble","_",tf_male| tfg_boots| tfg_armor,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_free_denethor_robe,itm_leather_boots],
      attr_tier_1,wp_tier_1,knows_common,woman_face_1,woman_face_2],
# end TLD walkers

# Ryan BEGIN
["ramun_the_slave_trader","Ramun_the_slave_trader","_",tf_hero,0,0,fac_commoners,
   [],
      attr_tier_1,wp_tier_1,knows_common,merchant_face_1,merchant_face_2],
["guide","Quick_Jimmy","_",tf_hero,0,0,fac_commoners,
   [],
      attr_tier_1,wp_tier_1,knows_inventory_management_10,merchant_face_1,merchant_face_2],
# Ryan END

["galeas","Galeas","_",tf_hero,0,0,fac_commoners,
   [],
      attr_tier_1,wp_tier_1,knows_common,merchant_face_1,merchant_face_2],
["farmer_from_bandit_village","Farmer","Farmers",tfg_armor,0,0,fac_commoners,
   [],
      attr_tier_1,wp_tier_1,knows_common,merchant_face_1,merchant_face_2],
["trainer_1","Trainer","_",tf_hero, 0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["trainer_2","Trainer","_",tf_hero, 0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["trainer_3","Trainer","_",tf_hero, 0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["trainer_4","Trainer","_",tf_hero, 0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],

#TRAINERS
["trainer_gondor","Trainer","_",tf_hero| tfg_armor| tfg_boots, scn_gondor_arena|entry(1),0,fac_commoners,
   [itm_gon_citadel_guard,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,],
      0,0,0,gondor_face2],
["trainer_rohan","Trainer","_",tf_hero| tf_rohan| tfg_armor| tfg_boots, scn_rohan_arena|entry(1),0,fac_commoners,
   [itm_free_rohan_armor_j,itm_leather_gloves,itm_leather_boots,],
      0,0,0,rohan_face_old_2],
["trainer_dale","Trainer","_",tf_hero| tfg_armor| tfg_boots, scn_dale_arena|entry(1),0,fac_commoners,
   [itm_dale_armor_d,itm_dale_boots_b,itm_leather_gloves,],
      0,0,0,gondor_face2],
["trainer_elf","Trainer","_",tf_hero| tf_lorien| tfg_armor| tfg_boots, scn_elf_arena|entry(1),0,fac_commoners,
   [itm_free_whiterobe,itm_elven_boots,],
      attr_tier_5,0,0,lorien_elf_face_2],
["trainer_beorn","Trainer","_",tf_hero| tfg_armor| tfg_boots, scn_beorn_arena|entry(1),0,fac_commoners,
   [itm_beorn_padded,itm_rohan_shoes,],
      0,0,0,beorn_face2],
["trainer_dwarf","Trainer","_",tf_hero| tf_dwarf| tfg_armor| tfg_boots, scn_dwarf_arena|entry(1),0,fac_commoners,
   [itm_dwarf_armor_g,itm_dwarf_pad_boots,],
      0,0,0,dwarf_face_2],
["trainer_mordor","Trainer","_",tf_hero| tf_orc| tfg_armor| tfg_boots, scn_mordor_arena|entry(1),0,fac_commoners,
   [itm_uruk_ragwrap,itm_orc_tribal_a,],
      0,0,0,orc_face_normal],
["trainer_isengard","Trainer","_",tf_hero| tf_urukhai| tfg_armor| tfg_boots| tfg_gloves, scn_isengard_arena|entry(1),0,fac_commoners,
   [itm_isen_uruk_light_d,itm_leather_gloves_black,itm_isen_greaves,],
      0,0,0,orc_face_normal],
["trainer_khand","Trainer","_",tf_hero| tf_evil_man| tfg_armor| tfg_boots, scn_khand_arena|entry(1),0,fac_commoners,
   [itm_khand_foot_lam_c,itm_leather_boots,],
      0,0,0,khand_man2],
["trainer_rhun","Trainer","_",tf_hero| tf_randomize_face| tf_gondor| tfg_armor| tfg_boots| tfg_gloves, scn_rhun_arena|entry(1),0,fac_commoners,
   [itm_rhun_armor_g,itm_leather_gloves,itm_rhun_greaves,],
      0,0,0,gondor_civil_face_1,gondor_civil_face_2],
["trainer_harad","Trainer","_",tf_hero| tf_harad| tfg_armor| tfg_boots, scn_harad_arena|entry(1),0,fac_commoners,
   [itm_harad_scale,itm_harad_scale_greaves,],
      0,0,0,haradrim_face_2],
["trainer_umbar","Trainer","_",tf_hero| tfg_armor| tfg_boots, scn_umbar_arena|entry(1),0,fac_commoners,
   [itm_umb_armor_g,itm_corsair_boots,],
      0,0,0,bandit_face2],
      
#
# Ransom brokers.
["ransom_broker_1","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_2","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_3","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_4","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_5","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_6","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_7","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_8","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_9","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["ransom_broker_10","Ransom_Broker","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
 
# Tavern traveler.
["tavern_traveler_1","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_2","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_3","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_4","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_5","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_6","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_7","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_8","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_9","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
["tavern_traveler_10","Traveller","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
# Tavern minstrel.
["tavern_minstrel_1","Minstrel","_",tf_hero| tf_randomize_face,0,0,fac_commoners,
   [],
      0,0,0,merchant_face_1,merchant_face_2],
#Companions
["npc1","Mablung","_",tf_hero| tf_gondor| tf_unmoveable_in_party_window,0,0,fac_gondor,
   [itm_gondor_ranger_hood,itm_gon_ranger_cloak,itm_leather_gloves,itm_leather_boots,itm_numenor_bow,itm_ithilien_arrows,itm_gondor_bastard_sword,],
      str_15|agi_15|int_12|cha_9|level(20),wp_one_handed(160)|wp_two_handed(140)|wp_polearm(120)|wp_archery(140)|wp_throwing(120),knows_trade_2|knows_riding_1|knows_athletics_5|knows_power_draw_3|knows_power_strike_4|knows_shield_3|knows_ironflesh_4|knows_weapon_master_4|knows_spotting_3|knows_pathfinding_4|knows_tracking_3|knows_trainer_3|knows_tactics_2|knows_wound_treatment_2,0x000000003f0000544324d34b946a593300000000001dc9300000000000000000],

["npc2","Cirdil","_",tf_hero| tf_gondor| tf_unmoveable_in_party_window,0,0,fac_gondor,
   [itm_gondor_light_helm,itm_gon_jerkin,itm_leather_boots,itm_gondor_short_sword,itm_gon_tab_shield_a,],
      str_10|agi_7|int_4|cha_4|level(1),wp(60),knows_athletics_1|knows_power_strike_1|knows_first_aid_1,0x000000003f001010599c72556461b71b00000000001db71e0000000000000000],

["npc3","Ulfas","_",tf_rohan| tf_hero| tf_unmoveable_in_party_window,0,0,fac_rohan,
   [itm_free_rohan_armor_g,itm_leather_gloves,itm_leather_boots,itm_rohan_inf_sword,itm_rohan_spear,itm_rohan_shield_a,itm_rohirrim_courser,],
      str_14|agi_10|int_5|cha_9|level(10),wp(100),knows_riding_3|knows_shield_1|knows_power_strike_2|knows_power_throw_1|knows_ironflesh_3|knows_weapon_master_2|knows_athletics_1|knows_wound_treatment_1|knows_first_aid_2|knows_trade_2|knows_looting_2,0x00000007c00021c536db6db6db61b6db00000000001db6f30000000000000000],

["npc4","Eowyn","_",tf_female| tf_mounted| tf_hero| tf_unmoveable_in_party_window,0,0,fac_rohan,
   [itm_rohan_cav_helmet_a,itm_free_rohan_armor_g,itm_leather_boots,itm_rohan_inf_sword,itm_rohan_shield_b,itm_rohirrim_courser,],
      str_14|agi_18|int_9|cha_12|level(24),wp(200),knows_horse_archery_5|knows_riding_6|knows_power_draw_4|knows_power_strike_2|knows_power_throw_4|knows_ironflesh_3|knows_weapon_master_4|knows_shield_3|knows_athletics_1|knows_wound_treatment_4|knows_first_aid_3|knows_trade_3,0x0000000a4000400b061b6298c26e6ac700000000001d72cf0000000000000000],

["npc5","Glorfindel","_",tf_lorien| tf_hero| tf_unmoveable_in_party_window,0,0,fac_lorien,
   [itm_free_riv_helm_glorfi,itm_riv_guard,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_b,itm_riv_shield_b,itm_riv_warhorse,],
      str_30|agi_24|int_18|cha_24|level(55),wp(500),knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9|knows_power_draw_9|knows_horse_archery_9|knows_weapon_master_8|knows_trainer_6,0x000000000000100667187ab5d341249200000000001cb6d30000000000000000],

["npc6","Luevanna","_",tf_female| tfg_ranged| tf_hero| tf_unmoveable_in_party_window,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,itm_mirkwood_knife,itm_elven_bow,itm_woodelf_arrows,],
      str_8|agi_13|int_12|cha_6|level(1),wp_one_handed(70)|wp_two_handed(40)|wp_polearm(40)|wp_archery(100)|wp_throwing(60),knows_power_draw_2|knows_ironflesh_1|knows_athletics_1|knows_spotting_1|knows_pathfinding_3|knows_tracking_1|knows_wound_treatment_2,0x0000000180004009041d7566cb87608000000000001d24d30000000000000000],

["npc7","Gimli","_",tf_dwarf| tf_hero| tf_unmoveable_in_party_window,0,0,fac_dwarf,
   [itm_free_dwarf_helm_b,itm_dwarf_armor_c,itm_leather_gloves,itm_dwarf_pad_boots,itm_dwarf_great_pick,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_5,wp_dwarf_tier_5,knows_ironflesh_5|knows_power_strike_5|knows_power_throw_3|knows_athletics_3|knows_riding_10|knows_weapon_master_2|knows_trainer_1|knows_engineer_4|knows_looting_4|knows_trade_3,0x000000003c001144121c6eb7f360befb00000000001db6f30000000000000000],

["npc8","Faniul","_",tf_female| tfg_ranged| tf_hero| tf_unmoveable_in_party_window,0,0,fac_dale,
   [itm_dale_armor_c,itm_dale_boots_a,],
      str_7|agi_6|int_11|cha_5|level(1),wp(40),knows_ironflesh_1|knows_wound_treatment_2|knows_first_aid_3|knows_surgery_2|knows_trade_1,0x0000000712003004589dae38ad69a64900000000001ec6cc0000000000000000],

["npc9","Gulm","_",tf_urukhai| tf_hero| tf_unmoveable_in_party_window,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,itm_isengard_sword,],
      str_24|agi_17|int_8|cha_4|level(25),wp(185),knows_athletics_7|knows_power_strike_5|knows_ironflesh_10|knows_weapon_master_5|knows_trainer_2,0x00000001b50000c2003d7dc5a4b2195c00000000000000000000000000000000],

["npc10","Durgash","_",tf_orc| tf_mounted| tfg_ranged| tf_hero| tf_unmoveable_in_party_window,0,0,fac_isengard,
   [itm_isen_orc_armor_a,itm_wood_club,itm_orc_throwing_arrow,itm_warg_1d,],
      str_12|agi_11|int_11|cha_4|level(10),wp(90),knows_riding_3|knows_power_throw_2|knows_power_strike_2|knows_ironflesh_3|knows_weapon_master_3|knows_spotting_2|knows_pathfinding_4|knows_tracking_1,0x00000001a2000007399e8ccc9cae34e500000000001d16ad0000000000000000],

["npc11","Ufthak","_",tf_orc| tf_hero| tf_unmoveable_in_party_window,0,0,fac_mordor,
   [itm_m_orc_light_a,itm_orc_ragwrap,itm_wood_club,itm_orc_simple_spear,],
      str_13|agi_8|int_4|cha_4|level(1),wp(75),knows_athletics_2|knows_power_strike_1|knows_ironflesh_1,orc_face6],

["npc12","Gorbag","_",tf_uruk| tf_hero| tf_unmoveable_in_party_window,0,0,fac_mordor,
   [itm_m_uruk_heavy_e,itm_uruk_tracker_boots,itm_orc_two_handed_axe,itm_uruk_pike_b,itm_uruk_helm_b,],
      str_21|agi_16|int_7|cha_4|level(20),wp(175),knows_riding_1|knows_athletics_5|knows_power_strike_5|knows_ironflesh_6|knows_weapon_master_5,uruk_hai_face2],

["npc13","Lykyada","_",tf_harad| tfg_ranged| tf_mounted| tf_hero| tf_unmoveable_in_party_window,0,0,fac_harad,
   [itm_black_snake_armor,itm_harad_leather_greaves,itm_leather_gloves,itm_black_snake_helm,itm_harad_bow,itm_harad_arrows,itm_black_snake_sword,itm_harad_warhorse,],
      str_24|agi_20|int_18|cha_15|level(40),wp(300),knows_horse_archery_5|knows_riding_6|knows_power_strike_5|knows_power_draw_5|knows_ironflesh_7|knows_athletics_3|knows_weapon_master_6|knows_tactics_5|knows_trainer_6,0x000000051f00000b372571b8ed79a6ac00000000001db6360000000000000000],

["npc14","Fuldimir","_",tf_hero| tf_unmoveable_in_party_window,0,0,fac_umbar,
   [itm_umb_armor_a,itm_corsair_boots,itm_umb_shield_a,itm_corsair_throwing_dagger,itm_umbar_rapier,],
      str_10|agi_9|int_7|cha_7|level(5),wp(80),knows_athletics_1|knows_power_throw_2|knows_power_strike_1|knows_trade_2|knows_looting_2,0x00000001b70032453add7524dc76d74900000000001d35330000000000000000],

["npc15","Bolzog","_",tf_orc| tf_hero| tf_unmoveable_in_party_window,0,0,fac_moria,
   [itm_moria_armor_a,itm_orc_machete,orc_face_normal],
      str_9|agi_10|int_12|cha_4|level(7),wp(80),knows_athletics_2|knows_power_throw_1|knows_power_strike_1|knows_ironflesh_1|knows_wound_treatment_2|knows_first_aid_2|knows_surgery_1,0x00000001ab00200d35627276a42e150c00000000001dca2c0000000000000000],

["npc16","Varfang","_",tf_mounted| tf_hero| tf_unmoveable_in_party_window,0,0,fac_rhun,
   [itm_rhun_helm_k,itm_rhun_armor_a,itm_rhun_shoes,itm_rhun_sword,itm_rhun_round_shield,itm_rhun_horse_a,],
      str_15|agi_15|int_3|cha_5|level(10),wp(120),knows_riding_5|knows_power_strike_4|knows_ironflesh_1|knows_power_throw_1|knows_weapon_master_3,0x000000018700214944d468dd9bae295b00000000001cb5a40000000000000000],

["npc17","Dimborn","_",tf_hero| tf_unmoveable_in_party_window,0,0,fac_beorn,
   [itm_woodman_tunic,itm_leather_boots,itm_beorn_axe,],
      str_17|agi_13|int_3|cha_3|level(8),wp(95),knows_riding_1|knows_athletics_3|knows_power_draw_2|knows_power_strike_2|knows_ironflesh_3|knows_pathfinding_2,0x00000009f50001c97ac16e65f3ecf7de00000000001cc7080000000000000000],
#NPC system changes end
 
 
# <--- swy: heroes_begin --->
 
## Kham - New Gondor Lord
["knight_6_2","Golasgil","_",tf_hero| tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_gon_lord,itm_leather_gloves_black,itm_gondor_greaves,itm_good_mace,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_5,wp_tier_5,gondor_skills_1|knows_trainer_7,0x000000003f00611236e376e7d576473f00000000001db6ec0000000000000000],

#governors (plural contains how player refers to the guy)

["gondor_lord","Steward_Denethor","Steward",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_free_denethor_robe,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gondor_shield_d,itm_gondor_guard_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_5,0x0000000f2300300a661d6dbf917766dc00000000001da6f30000000000000000],

["rohan_lord","King_Theoden","King",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_item_9,itm_item_7,itm_leather_gloves,itm_item_10,itm_item_12,itm_rohan_shield_g,itm_item_11,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_4,0x0000000d4000210236db6db8db65b6fb00000000001e46fb0000000000000000],

["isengard_lord","Saruman","Master",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_helm| tfg_horse,0,0,fac_isengard,
   [itm_zero_head,itm_item_44,itm_leather_boots,itm_sarustaff,itm_courser,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_6,0x0000000fce003347321d61bf8b61b6db00000000001d36fa0000000000000000],

["mordor_lord","Mouth_of_Sauron","Satrap",tf_hero| tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_mordor_warhorse2,itm_m_cap_armor,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_blackroot_hood,itm_mordor_longsword,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x0000000fff00000012078077c00ff1c000000000001cf0680000000000000000],

["harad_lord","Chief_Ul-Ulcari","Chief",tf_hero| tf_harad| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_warhorse,itm_harad_heavy,itm_harad_leather_greaves,itm_evil_gauntlets_a,itm_harad_dragon_helm,itm_harad_khopesh,],
      attr_tier_6,wp_tier_6,knight_skills_4|knows_trainer_5,0x00000009ff0020071415a5f9fb60c1b700000000001d663b0000000000000000],

["rhun_lord","Loke-Khan_Borthand","Khan",tf_hero| tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_item_40,itm_item_39,itm_leather_gloves,itm_rhun_greaves,itm_rhun_greatsword,itm_item_41,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_5,0x0000000c7f01008876db6dbddb61b6dd00000000001db6f30000000000000000],

["khand_lord","Shibh_Krukmahur","Shibh",tf_hero| tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_khand,
   [itm_variag_kataphrakt,itm_khand_noble_lam,itm_variag_greaves,itm_evil_gauntlets_a,itm_khand_lance,itm_khand_tulwar,itm_variag_gladiator_shield,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_4,0x0000000f3f00b38712065fd3287f731c00000000001c53780000000000000000],

["umbar_lord","Admiral_Tulmir","Admiral",tf_hero| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_umbar,
   [itm_umb_armor_h,itm_corsair_boots,itm_leather_gloves,itm_umb_helm_f,itm_corsair_bow,itm_corsair_arrows,itm_umbar_rapier,],
      attr_tier_6,wp_tier_6,knight_skills_3|knows_trainer_3,0x0000000e3b004244365b6db99b6db7df00000000001dd6eb0000000000000000],

["lorien_lord","Lady_Galadriel","Lady",tf_hero| tf_female| tfg_armor,0,0,fac_lorien,
   [itm_free_galadriel,],
      attr_tier_6,wp(20),knows_common,0x00000000000000003e1860b88389b6c300000000001d34c30000000000000000],

["imladris_lord","Lord_Elrond","Lord",tf_hero| tf_imladris| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_riv_tiara,itm_item_20,itm_leather_gloves,itm_elven_boots,itm_item_22,itm_riv_shield_reward,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_4|knows_persuasion_5|knows_trainer_5,0x0000000c3700200a20984ddb4aae34e400000000001da6fd0000000000000000],

["woodelf_lord","King_Thranduil","King",tf_hero| tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_woodelf,
   [itm_riv_tiara,itm_mirkwood_armor_f,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_mirkwood_sword,itm_mirkwood_spear_shield_c,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_5|knows_persuasion_7|knows_trainer_5,0x0000000000002003669c54dbf3a216cb00000000001db6fa0000000000000000],

["moria_lord","Master_Bolg_the_Lesser","Master",tf_hero| tf_uruk| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_moria,
   [itm_wargarmored_3a,itm_m_uruk_heavy_i,itm_uruk_helm_e,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_orc_javelin,itm_uruk_falchion_b,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_4|knows_persuasion_3|knows_leadership_10|knows_tactics_8,0x00000000260010010038c51051df5f5800000000000000000000000000000000],

["guldur_lord","Master_Fuinur","Master",tf_hero| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_evil_man,0,0,fac_guldur,
   [itm_mordor_warhorse,itm_m_cap_armor,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_mordor_cap_helm,itm_mordor_man_shield_b,itm_mordor_longsword,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_6,0x0000000fcd0005c03586a83d4223b2c200000000001c58e00000000000000000],

["gundabad_lord","Master_Burza_Krual","Master",tf_hero| tf_uruk| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_gundabad,
   [itm_wargarmored_3a,itm_gundabad_armor_e,itm_orc_greaves,itm_evil_gauntlets_a,itm_gundabad_helm_e,itm_orc_throwing_axes,itm_orc_slasher,],
      attr_tier_6,wp_tier_6,knight_skills_4|knows_trainer_5|knows_persuasion_3|knows_leadership_10|knows_tactics_8,0x0000000026002085003f006fe95aae4000000000000000000000000000000000],

["dale_lord","King_Brand","King",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_dale,
   [itm_item_5,itm_dale_armor_reward,itm_leather_gloves,itm_dale_boots_c,itm_dale_sword_broad,itm_dale_shield_d,itm_dale_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_5,0x0000000bbf0022c756dc6db57361b6db00000000001db6eb0000000000000000],

["dwarf_lord","King_Dain_II_Ironfoot","King",tf_hero| tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dwarf,
   [itm_dain_armor,itm_mail_mittens,itm_dain_greaves,itm_dain_hammer,itm_dwarf_shield_reward,],
      attr_dwarf_tier_6,wp_dwarf_tier_6,knight_skills_5|knows_riding_10|knows_persuasion_3|knows_trainer_4,0x0000000c00001109061c6db7db60b6db00000000001db6f30000000000000000],

["dunland_lord","Chief_Daeglaf_the_Black","Chief",tf_hero| tf_dunland| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_dunland,
   [itm_saddle_horse,itm_dunland_armor_k,itm_dunland_wolfboots,itm_evil_gauntlets_a,itm_dun_helm_e,itm_dun_berserker,itm_dun_shield_b,itm_dunland_javelin,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_persuasion_5|knows_trainer_6,0x000000003f0051c721dc6c71580f36ff00000000001fd2e80000000000000000],

["beorn_lord","Chief_Grimbeorn_the_Old","Chief",tf_hero| tfg_shield| tfg_armor| tfg_helm|tfg_boots,0,0,fac_beorn,
   [itm_beorn_chief,itm_leather_boots,itm_mail_mittens,itm_beorn_helmet,itm_beorn_axe,itm_dwarf_throwing_axe,itm_beorn_shield,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_persuasion_5|knows_trainer_4,0x0000000d6a00628918d46a72d946e7ae00000000001eeeb90000000000000000],
 

 # marshalls which are not also leaders
["lorien_marshall","Celeborn","_",tf_hero| tf_lorien| tfg_armor| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_lorien,
   [itm_riv_tiara,itm_lorien_royal_armor,itm_leather_gloves,itm_elven_boots,itm_item_23,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_5|knows_persuasion_7|knows_trainer_4,0x0000000b800000042ed88db35a61cae500000000001da6eb0000000000000000],

# ["gondor_marshall","Gondor Marshall","_",tf_hero| tf_gondor| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_gondor,
   # [itm_gondor_warhorse,itm_pel_leader,itm_pelargir_greaves,itm_mail_mittens,itm_pelargir_helmet_heavy,itm_pelargir_sword,itm_numenor_bow,itm_gondor_arrows,],
      # attr_tier_6,wp_tier_6,knight_skills_4|knows_trainer_1|knows_trainer_3,0x00000006ff003004225b8ac89c62d2f400000000001ec8f90000000000000000],

## hobbits: two versions: for when you didn't meet them, and for when you did meet them (I wish there was a way to RENAME a Troop. str_set_troop_name FTW)  mtarini

["pippin_notmet","halfling","_",tf_hero| tf_mounted| tfg_armor| tfg_helm| tfg_boots,0,0,fac_commoners,
   [itm_empty_head,itm_empty_hands,itm_empty_legs,itm_free_pippin_outfit],
       attr_tier_7,wp_tier_7,knows_riding_10|knows_athletics_10|knows_power_strike_10|knows_ironflesh_10|knows_pathfinding_10,mercenary_face_2],

["merry_notmet","halfling","_",tf_hero| tf_mounted| tfg_armor| tfg_helm| tfg_boots,0,0,fac_commoners,
   [itm_empty_head,itm_empty_hands,itm_empty_legs,itm_free_merry_outfit],
       attr_tier_7,wp_tier_7,knows_riding_10|knows_athletics_10|knows_power_strike_10|knows_ironflesh_10|knows_pathfinding_10,mercenary_face_2],

["pippin","Pippin","_",tf_hero| tf_mounted| tfg_armor| tfg_helm| tfg_boots,0,0,fac_commoners,
   [itm_empty_head,itm_empty_hands,itm_empty_legs,itm_free_pippin_outfit],
       attr_tier_7,wp_tier_7,knows_riding_10|knows_athletics_10|knows_power_strike_10|knows_ironflesh_10|knows_pathfinding_10,mercenary_face_2],

["merry","Merry","_",tf_hero| tf_mounted| tfg_armor| tfg_helm| tfg_boots,0,0,fac_commoners,
   [itm_empty_head,itm_empty_hands,itm_empty_legs,itm_free_merry_outfit],
       attr_tier_7,wp_tier_7,knows_riding_10|knows_athletics_10|knows_power_strike_10|knows_ironflesh_10|knows_pathfinding_10,mercenary_face_2],

     #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
#Gondor Angbor 
["knight_1_1","Angbor_the_Fearless","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_lamedon_leader,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gon_tab_shield_c,itm_gondor_lam_horse,],
      attr_tier_6,wp_tier_6,gondor_skills_4|knows_trainer_4|knows_persuasion_3|knows_horse_archery_5|knows_power_throw_7,0x00000008ff00259436db6db6db61b4db00000000001d36fb0000000000000000],

["knight_1_2","Boromir","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_gon_lord,itm_leather_gloves_black,itm_gondor_greaves,itm_item_15,(itm_gon_tab_shield_a,imod_reinforced),itm_gondor_guard_warhorse,],
      attr_tier_6,wp_tier_6,gondor_skills_5|knows_ironflesh_6|knows_power_strike_6|knows_trainer_7|knows_leadership_10,0x000000001300258366de71b96369b4fb00000000001db6f30000000000000000],

["knight_1_3","Prince_Imrahil","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_item_2,itm_item_3,itm_mail_mittens,itm_dol_greaves,itm_amroth_sword_b,(itm_gon_tab_shield_c,imod_hardened),itm_item_4,],
      attr_tier_6,wp_tier_6,gondor_skills_5|knows_trainer_7,0x00000009ff00200777dc72b79b61b6fb00000000001d36fb0000000000000000],

["knight_1_4","Orthalion","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_pelargir_helmet_heavy,itm_pel_leader,itm_leather_gloves_black,itm_gondor_greaves,itm_pelargir_sword,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_6,wp_tier_6,gondor_skills_4|knows_trainer_7|knows_power_throw_5,0x0000000dbf002512261b69b6e341b0db00000000001d36e30000000000000000],

["knight_1_5","Duinhir","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_blackroot_leader,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_6,wp_tier_6,gondor_skills_5|knows_horse_archery_7|knows_power_draw_7,0x00000001bf002189065c6a391b61b6db00000000001d36f30000000000000000],

["knight_1_6","Hirluin_the_Fair","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_pinnath_leader,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_6,wp_tier_6,gondor_skills_3,0x000000058000200f765b69b2d36122dc00000000001d36e30000000000000000],

["knight_1_7","Faramir","_",tf_hero| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_gondor,
   [itm_gon_ranger_skirt,itm_leather_gloves,itm_leather_boots,itm_numenor_bow,itm_ithilien_arrows,itm_item_16,],
      attr_tier_6,wp(310),gondor_skills_5|knows_ironflesh_9|knows_power_strike_6|knows_power_draw_6|knows_persuasion_7,0x000000000000210336dd75b4e385b4db00000000001db6d30000000000000000],

["knight_1_8","Forlong_the_Fat","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_lossarnach_scale_cap,itm_lossarnach_leader,itm_leather_gloves,itm_lossarnach_greaves,itm_good_mace,itm_gon_tab_shield_c,itm_gondor_hunter,],
      attr_tier_6,wp_tier_6,gondor_skills_3|knows_power_throw_7,0x00000008b70052935b1b8f4ae9ee793e00000000001f4cad0000000000000000],

#Rohan
["knight_1_9","Erkenbrand","_",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_shield_g,itm_rohirrim_heavy_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_4,0x0000000e7f0001c313da5e3993abcd3400000000001da6f30000000000000000],

["knight_1_10","Prince_Theodred","_",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_item_8,itm_item_14,itm_leather_gloves,itm_item_29,itm_eorl_cavalry_sword,itm_rohan_lance_banner_sun,itm_rohan_shield_g,itm_rohirrim_heavy_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_5,0x0000000000000005771a8db75345a6db00000000001db6fb0000000000000000],

["knight_1_11","Grimbold","_",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_shield_g,itm_rohirrim_heavy_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_persuasion_3,0x0000000d8e002182211a8ce5aafd4eff00000000001cb45b0000000000000000],

["knight_1_12","Elfhelm","_",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_shield_g,itm_rohirrim_heavy_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_2,0x00000007c000220536db6db6db61b6db00000000001db6f30000000000000000],

["knight_1_13","Gamling","_",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_rohan_captain_helmet,itm_rohan_armor_p,itm_leather_gloves,itm_rohirrim_war_greaves,itm_rohan_sword_c,itm_rohan_bow,itm_rohan_arrows,itm_rohan_shield_g,itm_rohirrim_heavy_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_3,0x000000094000204336b9db32d26953ba00000000001dc6f00000000000000000],

["knight_1_14","Eomer","_",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_item_8,itm_item_6,itm_leather_gloves,itm_rohirrim_war_greaves,itm_item_13,itm_rohan_lance_banner_sun,itm_rohan_bow,itm_rohan_arrows,itm_rohan_shield_g,itm_rohirrim_heavy_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_4,0x000000000b00208536de6db8db65b6c300000000001e46fb0000000000000000],

#Isengard
["knight_1_15","Lurtz","_",tf_hero| tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_ironflesh_7|knows_trainer_3|knows_persuasion_3,0x00000000000040c436dfe2d2416eb6fe00000000001e383b0000000000000000],

["knight_1_16","Ugluk","_",tf_hero| tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_tier_6,wp_tier_6,knight_skills_3|knows_ironflesh_7|knows_persuasion_3,0x0000000a400020c336dee2d25962b4fc00000000001e382b0000000000000000],

["knight_1_17","Mauhur","_",tf_hero| tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_tier_6,wp_tier_6,knight_skills_2|knows_ironflesh_7|knows_persuasion_5,0x00000000000010c436dfe2d24162b4e600000000001e382b0000000000000000],

["knight_1_18","Hushnak_Longshanks","_",tf_hero| tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_helm_d,itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_tier_6,wp_tier_6,knight_skills_3|knows_persuasion_3|knows_trainer_4,0x0000000a400050c3361efed2416fb4ff00000000001fb82b0000000000000000],

["knight_1_19","Gridash_the_Tree-biter","_",tf_hero| tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_helm_d,itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_tier_6,wp_tier_6,knight_skills_4|knows_persuasion_3|knows_trainer_6,0x0000000a40000041361efed2417fb57f00000000001fb82b0000000000000000],

["knight_1_20","Gronk_the_Man-eater","_",tf_hero| tf_urukhai| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_isengard,
   [itm_isen_uruk_helm_d,itm_isen_uruk_heavy_a,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_persuasion_3|knows_trainer_5,0x0000000a40004082361f9d505976b57700000000001fb82b0000000000000000],

#Mordor
["knight_2_1","Captain_Mortakh","_",tf_hero| tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_mordor_warhorse2,itm_m_cap_armor,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_mordor_cap_helm,itm_mordor_longsword,itm_mordor_man_shield_b,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_trainer_3,0x0000000cff00150f21c38927434e804f00000000001d24be0000000000000000],
["knight_2_2","Berúthiel","_",tf_hero| tf_female| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_mordor_warhorse2,itm_m_cap_armor,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_mordor_cap_helm,itm_mordor_longsword,itm_mordor_man_shield_b,],
      attr_tier_6,wp_tier_6,knight_skills_2|knows_persuasion_5,0x0000000ebf0010060df26111c003815400000000001c5e380000000000000000],
["knight_2_3","Skang","_",tf_hero| tf_uruk |tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_m_uruk_heavy_k,itm_m_uruk_heavy_k,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_uruk_helm_f,itm_mordor_longsword,itm_mordor_uruk_shield_c,],
      attr_tier_6,wp_tier_6,knight_skills_3,0x000000003f002580204175274345004f00000000001d24380000000000000000],
["knight_2_4","Pharakhâd_The_Bastard","_",tf_hero| tf_evil_man| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_mordor,
   [itm_mordor_warhorse2,itm_black_num_armor,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_mordor_cap_helm,itm_mordor_longsword,itm_mordor_man_shield_b,],
      attr_tier_6,wp_tier_6,knight_skills_4,0x0000000f0d0001143586a83dc22382c600000000001cd8e00000000000000000],
["knight_2_5","Grishnakh","_",tf_hero| tf_uruk |tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_m_uruk_heavy_k,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_uruk_helm_f,itm_mordor_longsword,itm_mordor_uruk_shield_c,],
      attr_tier_6,wp_tier_6,knight_skills_5,0x00000000260000870038a005c03c5f7000000000000000000000000000000000],
["knight_2_51","Gothmog","Lieutenant",tf_hero| tf_uruk| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_m_uruk_heavy_k,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_uruk_helm_f,itm_mordor_uruk_shield_c,itm_mordor_longsword,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_persuasion_5|knows_trainer_4,0x000000002c000104003fb3f407b83d0d00000000000000000000000000000000],
#Harad
["knight_2_6","Chieftain_Karna_the_Lion","_",tf_hero| tf_harad| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_warhorse,itm_harad_lion_scale,itm_harad_leather_greaves,itm_evil_gauntlets_a,itm_harad_dragon_helm,itm_harad_khopesh,itm_harad_long_shield_c,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_persuasion_3|knows_trainer_3,0x00000009ff00300b1415a5f77872f7b700000000001d663b0000000000000000],
["knight_2_7","Chieftain_Na’man","_",tf_hero| tf_harad| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_warhorse,itm_harad_heavy,itm_harad_leather_greaves,itm_evil_gauntlets_a,itm_harad_dragon_helm,itm_harad_khopesh,itm_harad_long_shield_c,],
      attr_tier_6,wp_tier_6,knight_skills_2|knows_persuasion_3|knows_trainer_4,0x000000003f00000f20a8b7f9e87ff1b700000000001c3ab80000000000000000],
["knight_2_8","Chieftain_Haarith","_",tf_hero| tf_harad| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_harad,
   [itm_harad_warhorse,itm_harad_tiger_scale,itm_harad_leather_greaves,itm_evil_gauntlets_a,itm_harad_dragon_helm,itm_harad_khopesh,itm_harad_long_shield_c,],
      attr_tier_6,wp_tier_6,knight_skills_2|knows_persuasion_3|knows_trainer_4,0x000000003f00100421526ff7708d22f700000000001fea200000000000000000],
# ["knight_2_9","Harad_Chieftain","_",tf_hero,0,reserved,fac_harad,[itm_saddle_horse,itm_rich_outfit,itm_mail_hauberk,itm_leather_boots,itm_mail_boots,itm_mail_mittens,itm_two_handed_axe,itm_shield_heater_c],knight_attrib_4,wp(230),knight_skills_4,0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000,vaegir_face_older_2],
# ["knight_2_10","Harad_Lieutenant","_",tf_hero,0,reserved,fac_harad,[itm_warhorse,itm_free_fur_coat,itm_mail_hauberk,itm_leather_boots,itm_mail_boots,itm_mail_mittens,itm_shield_heater_c],knight_attrib_5,wp(260),knight_skills_5|knows_trainer_6,0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000,vaegir_face_older_2],
#Rhun
["knight_2_11","Margoz","_",tf_hero| tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_rhun_helm_n,itm_rhun_armor_k,itm_leather_gloves,itm_rhun_greaves,itm_rhun_greatsword,itm_rhun_horse_g,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x0000000cbf0130d536db6dbddb61b6eb00000000001db6f30000000000000000],

["knight_2_12","Ulwarth_the_Balchoth","_",tf_hero| tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_rhun_helm_n,itm_rhun_armor_k,itm_leather_gloves,itm_rhun_greaves,itm_rhun_greatsword,itm_rhun_horse_g,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x00000009bf0123c0121d6db5132df56900000000001db6fb0000000000000000],

["knight_2_13","Ulfang","_",tf_hero| tf_evil_man| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rhun,
   [itm_rhun_helm_n,itm_rhun_armor_k,itm_leather_gloves,itm_rhun_greaves,itm_rhun_greatsword,itm_rhun_horse_g,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x0000000bbf01024424db6dbd9b61b4e500000000001db6fb0000000000000000],

#Khand
["knight_2_16","Torask","_",tf_hero| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_evil_man,0,0,fac_khand,
   [itm_variag_kataphrakt,itm_khand_noble_lam,itm_variag_greaves,itm_evil_gauntlets_a,itm_khand_tulwar,itm_easterling_round_horseman,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x0000000ac800d5400bf7d3f5fb9179ff00000000001f62fc0000000000000000],
["knight_2_17","Lurmsakun","_",tf_hero| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_evil_man,0,0,fac_khand,
   [itm_variag_kataphrakt,itm_khand_noble_lam,itm_variag_greaves,itm_evil_gauntlets_a,itm_khand_tulwar,itm_easterling_round_horseman,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x0000000d3f00c40812065fd328ff7bfc00000000001ce6b80000000000000000],
#Umbar
["knight_3_1","Captain_Morbir","_",tf_hero| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_umbar,
   [itm_umb_armor_h,itm_umb_armor_h,itm_corsair_boots,itm_corsair_boots,itm_leather_gloves,itm_umb_helm_e,itm_corsair_bow,itm_corsair_arrows,itm_umbar_rapier,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_power_draw_4,0x0000000eb10063c8365369b99b6f77df00000000001d5aeb0000000000000000],
["knight_3_2","Captain_Angamaitë","_",tf_hero| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_umbar,
   [itm_umb_armor_h,itm_umb_armor_h,itm_corsair_boots,itm_corsair_boots,itm_leather_gloves,itm_umb_helm_a,itm_corsair_bow,itm_corsair_arrows,itm_umbar_rapier,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_power_draw_4,0x000000093f0035c5300251e9b3e041df00000000001cfaeb0000000000000000],
["knight_3_3","Captain_Sangahyando","_",tf_hero| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_umbar,
   [itm_umb_armor_h,itm_umb_armor_h,itm_corsair_boots,itm_corsair_boots,itm_leather_gloves,itm_umb_helm_b,itm_corsair_bow,itm_corsair_arrows,itm_umbar_rapier,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_power_draw_4,0x000000093f004045300251e9b3e2f7df00000000001dbaab0000000000000000],
#Lothlorien
["knight_3_6","Haldir","_",tf_hero| tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_lorien,
   [itm_lorien_armor_d,itm_leather_gloves,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_lorien_sword_a,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_1|knows_persuasion_7|knows_power_draw_4,0x00000000000000025adc4db9da95e6a500000000001d26ab0000000000000000],
["knight_3_7","Orophin","_",tf_hero| tf_lorien| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_lorien,
   [itm_lorien_armor_d,itm_leather_gloves,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_elven_war_sword,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_1|knows_power_draw_4|knows_persuasion_7,0x000000000000000216dd6634e36170fa00000000001db4e40000000000000000],
#Imladris
["knight_3_11","Elladan","_",tf_hero| tf_imladris| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_imladris,
   [itm_riv_tiara,itm_riv_lord,itm_leather_gloves,itm_elven_boots,itm_riv_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_1|knows_persuasion_5|knows_power_draw_4,0x0000000037002007519c4ddb4a8234e300000000001db6f50000000000000000],
["knight_3_12","Elrohir","_",tf_hero| tf_imladris| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_riv_tiara,itm_riv_lord,itm_leather_gloves,itm_elven_boots,itm_lorien_sword_a,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_2|knows_persuasion_5|knows_power_draw_4,0x0000000037002002255c56594b85b4e200000000001db6f50000000000000000],
["knight_3_13","Aragorn","_",tf_hero| tf_dunedain| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_imladris,
   [itm_zero_head,itm_item_45,itm_leather_gloves_black,itm_arnor_greaves,itm_item_35,],
      attr_elf_tier_6,wp(450),knight_skills_2|knows_power_draw_4|knows_persuasion_7,0x000000003c003189355d8dc95348b4f400000000001ca6eb0000000000000000],
#Woodelves
["knight_3_16","Prince_Legolas","_",tf_hero| tf_woodelf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_woodelf,
   [itm_mirkwood_armor_f,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_elven_bow,itm_woodelf_arrows,itm_mirkwood_sword,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_1|knows_power_draw_8|knows_persuasion_7,0x000000000000000247db65b5bb4174fb00000000001db6cb0000000000000000],
["knight_3_17","Tauriel","_",tf_hero| tf_female| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_woodelf,
   [itm_mirkwood_armor_f,itm_leather_gloves,itm_mirkwood_leather_greaves,itm_elven_bow,itm_woodelf_arrows,itm_mirkwood_sword,],
      attr_elf_tier_6,wp_elf_tier_6,knight_skills_1|knows_power_draw_6|knows_persuasion_7,0x00000001b500400d379b69b7026e375200000000001cb6c30000000000000000],
#Moria
["knight_4_1","Whip_Snog","_",tf_hero| tf_orc| tf_mounted| tfg_ranged| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_moria,
   [itm_wargarmored_3a,itm_moria_armor_e,itm_orc_beakhelm_lordly,itm_orc_greaves,itm_evil_gauntlets_a,itm_orc_throwing_axes,itm_orc_slasher,],
      attr_orc_tier_6,wp_orc_tier_6,knight_skills_1|knows_persuasion_3|knows_leadership_10|knows_tactics_8,0x0000000fff00100936db6db6db6db6db00000000001db6db0000000000000000],
["knight_4_2","Whip_Snotgor","_",tf_hero| tf_orc| tf_mounted| tfg_ranged| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_moria,
   [itm_wargarmored_3a,itm_moria_armor_e,itm_orc_bughelm_lordly,itm_orc_greaves,itm_evil_gauntlets_a,itm_orc_javelin,itm_orc_slasher,],
      attr_orc_tier_6,wp_orc_tier_6,knight_skills_1|knows_leadership_10|knows_persuasion_3|knows_tactics_8,0x000000087f00000e36db6db6db6db6db00000000001db6db0000000000000000],
#Dol Guldur
["knight_4_6","General_Tuskim","_",tf_hero| tf_uruk |tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_guldur,
   [itm_m_uruk_heavy_k,itm_m_uruk_heavy_k,itm_uruk_chain_greaves,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_uruk_helm_f,itm_mordor_uruk_shield_c,itm_mordor_longsword,],
      attr_tier_6,wp_tier_6,knight_skills_2|knows_trainer_4|knows_leadership_10,0x000000018000210700389ff43fdbff4500000000000000000000000000000000],
["knight_4_7","General_Mugslag","_",tf_hero| tf_uruk |tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_guldur,
   [itm_m_uruk_heavy_k,itm_m_uruk_heavy_k,itm_uruk_chain_greaves,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_uruk_helm_f,itm_mordor_uruk_shield_c,itm_mordor_longsword,],
      attr_tier_6,wp_tier_6,knight_skills_2|knows_trainer_4|knows_persuasion_3|knows_leadership_10,0x00000001800011c4003f1c65b8cdb6db00000000000000000000000000000000],
#Northmen
["knight_4_11","Beranhelm","_",tf_hero |tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_beorn_chief,itm_beorn_chief,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_axe,itm_dwarf_throwing_axe,itm_beorn_shield,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x0000000b260022493f596db9df7b7e7f00000000001f47530000000000000000],
["knight_4_12","Beranor_Blackfur","_",tf_hero |tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_beorn_chief,itm_beorn_chief,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_axe,itm_dwarf_throwing_axe,itm_beorn_shield,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_persuasion_5,0x0000000bbf0052894dd95757a55accff00000000001d29190000000000000000],
#Mt. Gundabad
["knight_4_16","Whip_Brolgukhsh","_",tf_hero| tf_orc| tf_mounted| tfg_ranged| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_gundabad,
   [itm_wargarmored_3a,itm_gundabad_armor_e,itm_orc_greaves,itm_orc_ragwrap,itm_evil_gauntlets_a,itm_gundabad_helm_e,itm_orc_throwing_axes,itm_orc_slasher,],
      attr_orc_tier_6,wp_orc_tier_6,knight_skills_1|knows_leadership_10|knows_persuasion_3|knows_tactics_8,0x0000000fc000000536db6db6db6db6db00000000001db6db0000000000000000],
["knight_4_17","Whip_Grumrunt","_",tf_hero| tf_orc| tf_mounted| tfg_ranged| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_gundabad,
   [itm_wargarmored_3a,itm_gundabad_armor_e,itm_orc_greaves,itm_orc_ragwrap,itm_evil_gauntlets_a,itm_gundabad_helm_e,itm_orc_throwing_axes,itm_orc_slasher,],
      attr_orc_tier_6,wp_orc_tier_6,knight_skills_1|knows_leadership_10|knows_persuasion_3|knows_tactics_8,0x00000009bf00000736db6db6db6db6db00000000001db6db0000000000000000],
["knight_4_18","Whip_Grimsob","_",tf_hero| tf_orc| tf_mounted| tfg_ranged| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_gundabad,
   [itm_wargarmored_3a,itm_gundabad_armor_e,itm_orc_greaves,itm_orc_ragwrap,itm_evil_gauntlets_a,itm_gundabad_helm_e,itm_orc_throwing_axes,itm_orc_slasher,],
      attr_orc_tier_6,wp_orc_tier_6,knight_skills_1|knows_leadership_10|knows_persuasion_3|knows_tactics_8,0x000000083f00200a36db6db6db6db6db00000000001db6db0000000000000000],
#Dale
["knight_5_1","Lord_Halward","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_dale,
   [itm_dale_helmet_h,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_sword_broad,itm_dale_shield_d,itm_dale_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_trainer_3,0x0000000c7f00310836db6db6db6db6db00000000001db6eb0000000000000000],
["knight_5_2","Lord_Bard","_",tf_hero| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_dale,
   [itm_dale_helmet_h,itm_dale_armor_h,itm_leather_gloves,itm_dale_boots_c,itm_dale_sword_broad,itm_dale_shield_d,itm_dale_warhorse,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_trainer_3,0x00000003c000050e379b7635db41b6dd00000000001db6fb0000000000000000],
["knight_5_3","Lord_Esgarain","_",tf_hero| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dale,
   [itm_dale_helmet_f,itm_dale_armor_j,itm_leather_gloves,itm_dale_boots_a,itm_dale_sword_broad,itm_shipmen_shield,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_trainer_3,0x0000000c2d0014cf369c6d7b53a5b6fc00000000001db6fc0000000000000000],
#Dwarven
["knight_5_6","Dwalin","_",tf_hero| tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dwarf,
   [itm_dwalin_armor,itm_mail_mittens,itm_dwalin_greaves,itm_obsidian_warhammer,],
      attr_dwarf_tier_6,wp_dwarf_tier_6,knows_riding_10|knows_persuasion_3|knight_skills_1,0x0000000b7f005140069c6db7fb6036db00000000001db73b0000000000000000],
["knight_5_7","Thorin_Stonehelm","_",tf_hero| tf_dwarf| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm,0,0,fac_dwarf,
   [itm_stonehelm_helmet,itm_stonehelm_armor,itm_dwarf_gloves,itm_stonehelm_greaves,itm_dwarf_greatsword,],
      attr_dwarf_tier_6,wp_dwarf_tier_6,knows_riding_10|knows_persuasion_3|knight_skills_1,0x0000000000001207475c6db7d362b6db00000000001e36eb0000000000000000],
#Dunland
["knight_5_11","Chief_Fudreim","_",tf_hero| tf_dunland| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_dunland,
   [itm_saddle_horse,itm_dunland_armor_k,itm_dunland_armor_k,itm_dunland_wolfboots,itm_dunland_wolfboots,itm_evil_gauntlets_a,itm_dun_helm_e,itm_dun_berserker,itm_dun_shield_b,itm_dunland_javelin,],
      attr_tier_6,wp_tier_6,knight_skills_1,0x0000000cbf00528736db6db71b6db6db00000000001fd6db0000000000000000],
["knight_5_12","Chief_Wulf","_",tf_hero| tf_dunland| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_dunland,
   [itm_saddle_horse,itm_dunland_armor_k,itm_dunland_armor_k,itm_dunland_wolfboots,itm_dunland_wolfboots,itm_evil_gauntlets_a,itm_dun_helm_e,itm_dun_berserker,itm_dun_shield_b,itm_dunland_javelin,],
      attr_tier_6,wp_tier_6,knight_skills_1|knows_persuasion_5,0x0000000e3b00324305f858f1606bbfff00000000001f7ce80000000000000000],

## Kham - New Gondor Lord
["knight_6_1","Dervorin","_",tf_hero| tf_gondor| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_gondor,
   [itm_gon_lord_helmet,itm_gon_lord,itm_leather_gloves_black,itm_gondor_greaves,itm_gondor_guard_sword,itm_gon_tab_shield_c,itm_gondor_warhorse,],
      attr_tier_5,wp_tier_5,gondor_skills_1|knows_power_throw_5|knows_persuasion_5|knows_shield_9,0x00000001bf002050375b6db7eb7138dd00000000001db6e30000000000000000],

# <--- swy: heroes_end --->
      
# Kham - move commented out healers to the end

# Weapon merchants
["smith_mtirith","Berethor_the_Smith","Steward's_smiths",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_pelargir","Hallatan_Metalmaster","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,subfac_pelargir,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_linhir","Bor_the_Armorer","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_dolamroth","Haldad_the_Smith","Amroth_smiths",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,subfac_dol_amroth,fac_gondor,
   [itm_leather_apron,itm_dol_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_edhellond","Ryis_Ironbender","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_lossarnach","Berin_Axemaker","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,subfac_lossarnach,fac_gondor,
   [itm_leather_apron,itm_lossarnach_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_tarnost","Harandil_Steelhammer","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_erech","Lorne_the_Black","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_pinnath","Tarandil_Swordmaker","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,subfac_blackroot,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_eosgiliath","Bzurg_the_Looter","smithy",tf_hero| tf_orc| tf_randomize_face| tf_is_merchant,0,0,fac_mordor,
   [itm_m_orc_light_e,itm_orc_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,orc_face_normal,orc_face2],
["smith_wosgiliath","Gardil","makeshift_smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_calembel","Agronom","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,subfac_ethring,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_hannun","Fal_the_Ranger_Smith","ranger_gear_stash",tf_hero| tf_is_merchant,0,subfac_rangers,fac_gondor,
   [itm_gon_ranger_cloak,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x000000018000218936db6db6db65b4db00000000001d36eb0000000000000000],
["smith_candros","Kalimdor","smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_gon_mail,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_1|knows_power_strike_1|knows_persuasion_1|knows_horse_archery_1|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_edoras","Eaoden_Steelmaster","King's_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x00000008c80002c219248896a4b96b6300000000001e1af30000000000000000],
["smith_aldburg","Fulm_Ironhoof","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000a22002341375b72ab4c6aba6500000000001f24e20000000000000000],
["smith_hornburg","Aldhelm","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000a35003183479c6e12548f451400000000001f355e0000000000000000],
["smith_eastemnet","Eadfrid","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000a10002282392cc9172d8dbb1b00000000001caa9d0000000000000000],
["smith_westfold","Deor_Helmmaker","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000a100011c4444395aaec92c4c400000000001db6cd0000000000000000],
["smith_westemnet","Armourer","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000a3b000281451d364924d5571400000000001e46a30000000000000000],
["smith_eastfold","Eaderan_Ironcarver","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000a170000c12b1b8f499892995b00000000001e68e90000000000000000],
["smith_morannon","Hurbag_Gateforger","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_uruk_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,orc_face_normal,orc_face2],
["smith_mmorgul","Orgurz_Firebelcher","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_uruk_ragwrap,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,orc_face_normal,orc_face2],
["town_24_smith","Boz_Ironspoiler","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_orc_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,orc_face_normal,orc_face2],
["smith_orc_patrol","Glugz_Ironfinger","camp_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_uruk_tracker_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,orc_face_normal,orc_face2],
["smith_oscamp","Kugash_Ironlover","camp_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_uruk_tracker_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,orc_face_normal,orc_face2],
["smith_isengard","Burz_Ironbasher","underground_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_orc_armor_f,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,uruk_hai_face1,uruk_hai_face2],
["smith_uoutpost","Gurzuk_Irontooth","outpost_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_orc_armor_f,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,uruk_hai_face1,uruk_hai_face2],
["smith_uhcamp","Rabzug_Rusteater","camp_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_orc_armor_f,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,uruk_hai_face1,uruk_hai_face2],
["smith_urcamp","Glurk","camp_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_orc_armor_f,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,uruk_hai_face1,uruk_hai_face2],
["smith_cgaladhon","Dirufin the Bowyer","elven_weaponmakers",tf_hero| tf_randomize_face| tf_is_merchant| tf_lorien,0,0,fac_lorien,
   [itm_lorien_armor_b,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,lorien_elf_face_1,lorien_elf_face_2],
["smith_cdolen","Dimirian the Fletcher","elven_weaponmakers",tf_hero| tf_randomize_face| tf_is_merchant| tf_lorien,0,0,fac_lorien,
   [itm_lorien_armor_b,itm_elven_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,lorien_elf_face_1,lorien_elf_face_2],
["smith_camroth","Getasistan","elven_weaponmakers",tf_hero| tf_randomize_face| tf_is_merchant| tf_lorien,0,0,fac_lorien,
   [itm_lorien_armor_b,itm_elven_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,lorien_elf_face_1,lorien_elf_face_2],
["smith_thranduils_halls","Thurinor","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_woodelf,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,lorien_elf_face_1,lorien_elf_face_2],
["smith_woodelf_camp","Calechir","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_woodelf,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,lorien_elf_face_1,lorien_elf_face_2],
["smith_beorn","Beornalaf_Axemaker","smithy",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_beorn,
   [itm_beorn_tunic,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_moria","Burgak_Forger","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_moria,
   [itm_moria_armor_b,itm_orc_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_dale","Ardel_Firehand","smithy",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_dale,
   [itm_free_leather_apron,itm_dale_boots_a,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_esgaroth","Kelegarn_The_Bowyer","smithy",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_dale,
   [itm_dale_armor_b,itm_dale_boots_a,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_erebor","Thror_the_Hammerer","praised_Dwarven_smiths",tf_hero| tf_randomize_face| tf_is_merchant| tf_dwarf,0,0,fac_dwarf,
   [itm_dwarf_miner,itm_dwarf_vest1,itm_dwarf_pad_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_first_aid_2|knows_surgery_2|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,dwarf_face_3,dwarf_face_4],
["smith_dunland","Dorrowuld_Ironpike","smithy",tf_hero| tf_dunland| tf_is_merchant,0,0,fac_dunland,
   [itm_dunland_armor_h,itm_dunland_wolfboots,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000cbf00624636db6db71b6db6db00000000001ec2db0000000000000000],
["smith_harad","Har_Steelbender","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_harad,0,0,fac_harad,
   [itm_harad_padded,itm_harad_scale_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_khand","Pushurt_The_Haggler","smithy",tf_hero| tf_is_merchant| tf_evil_man,0,0,fac_khand,
   [itm_khand_light_lam,itm_variag_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000fff00d45213f7e6f1636172fb00000000001dc22a0000000000000000],
["smith_umbar","Fuinir_the_Forger","smithy",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_umbar,
   [itm_umb_armor_e,itm_corsair_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_imladris","Duifirian","elven_weaponmakers",tf_hero| tf_randomize_face| tf_is_merchant| tf_imladris,0,0,fac_imladris,
   [itm_leather_apron,itm_elven_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,rivendell_elf_face_1,rivendell_elf_face_2],
["smith_dolguldur","Shtazg_Dulbash","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_uruk_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_north_rhun","Blacksmith","makeshift_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_gondor,0,0,fac_rhun,
   [itm_rhun_armor_j,itm_rhun_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,gondor_civil_face_1,gondor_civil_face_2],
["smith_gundabad","Blurg_Snowseller","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_c,itm_orc_furboots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_ironhill","Ironhill_Smith","Dwarven_camp_smiths",tf_hero| tf_randomize_face| tf_is_merchant| tf_dwarf,0,0,fac_dwarf,
   [itm_dwarf_miner,itm_dwarf_armor_e,itm_dwarf_pad_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_first_aid_2|knows_surgery_2|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,dwarf_face_3,dwarf_face_4],
["town_50_weaponsmith","Shruklug_Knife_Grinder","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_c,itm_orc_furboots,itm_gundabad_helm_a],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],

["smith_gondor_ac","Bor_the_Armorer","camp_smithy",tf_hero| tf_gondor| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_leather_apron,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_rohan_ac","Deor_Helmmaker","camp_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_rohan,0,0,fac_rohan,
   [itm_free_rohan_armor_c,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_mordor_ac","Hurbag_Gateforger","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_uruk_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,orc_face_normal,orc_face2],
["smith_isengard_ac","Burz_Ironbasher","underground_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_orc_armor_f,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,uruk_hai_face1,uruk_hai_face2],
["smith_lorien_ac","Dimirian the Fletcher","elven_weaponmakers",tf_hero| tf_randomize_face| tf_is_merchant| tf_lorien,0,0,fac_lorien,
   [itm_lorien_armor_b,itm_elven_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,lorien_elf_face_1,lorien_elf_face_2],
["smith_woodelf_ac","Dhoelath","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_woodelf,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,lorien_elf_face_1,lorien_elf_face_2],
["smith_dwarf_ac","Ironhill_Smith","Dwarven_camp_smiths",tf_hero| tf_randomize_face| tf_is_merchant| tf_dwarf,0,0,fac_dwarf,
   [itm_dwarf_miner,itm_dwarf_armor_e,itm_dwarf_pad_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_first_aid_2|knows_surgery_2|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,dwarf_face_3,dwarf_face_4],
["smith_gundabad_ac","Blurg_Snowseller","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_c,itm_orc_furboots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_rhun_ac","Branikar","makeshift_smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_gondor,0,0,fac_rhun,
   [itm_rhun_armor_j,itm_rhun_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,gondor_civil_face_1,gondor_civil_face_2],
["smith_guldur_ac","Shtazg_Dulbash","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_uruk_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_imladris_ac","Duifirian","elven_weaponmakers",tf_hero| tf_randomize_face| tf_is_merchant| tf_imladris,0,0,fac_imladris,
   [itm_leather_apron,itm_elven_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,rivendell_elf_face_1,rivendell_elf_face_2],
["smith_dunland_ac","Dorrowuld_Ironpike","smithy",tf_hero| tf_dunland| tf_is_merchant,0,0,fac_dunland,
   [itm_dunland_armor_h,itm_dunland_wolfboots,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000cbf00624636db6db71b6db6db00000000001ec2db0000000000000000],
["smith_harad_ac","Har_Steelbender","smithy",tf_hero| tf_randomize_face| tf_is_merchant| tf_harad,0,0,fac_harad,
   [itm_harad_padded,itm_harad_scale_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],
["smith_khand_ac","Pushurt_The_Haggler","smithy",tf_hero| tf_is_merchant| tf_evil_man,0,0,fac_khand,
   [itm_khand_light_lam,itm_variag_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,0x0000000fff00d45213f7e6f1636172fb00000000001dc22a0000000000000000],
["smith_umbar_ac","Fuinir_the_Forger","smithy",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_umbar,
   [itm_umb_armor_e,itm_corsair_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_leadership_2|knows_power_strike_2|knows_persuasion_2|knows_horse_archery_2|knows_shield_4|knows_power_draw_2|knows_power_throw_2|knows_trade_4|knows_tactics_4|knows_ironflesh_4|knows_athletics_2|knows_looting_1,mercenary_face_1,mercenary_face_2],

#Tavern keepers   # in TLD, their plular name serves as city "Castle" name.
["barman_mtirith","Tavern_Keeper","the_Citadel",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_pelargir","Tavern_Keeper","the_Castle",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_linhir","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_dolamroth","Tavern_Keeper","the_Castle",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_edhellond","Tavern_Keeper","the_Castle",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_commoners, [],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_lossarnach","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_tarnost","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,   [],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_erech","Tavern_Keeper","the_Castle",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_commoners,   [],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_pinnath","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,   [],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_hannun","Tavern_Keeper","the_Secret_Cave",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,   [],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_calembel","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners, [],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_edoras","Tavern_Keeper","Meduseld,_the_Golden_Hall",tf_hero| tf_randomize_face,0,0,fac_commoners, [],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_aldburg","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners, [],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_hornburg","Tavern_Keeper","the_Lord_Halls",tf_hero| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_eastemnet","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_westfold","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_westemnet","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_eastfold","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_baraddur","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_morannon","Tavern_Keeper","the_Leader's_Cave",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_mmorgul","Tavern_Keeper","the_Tower",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_cungol","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_isengard","Tavern_Keeper","the_tower_of_Orthanc",tf_hero| tf_randomize_face| tf_urukhai,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,uruk_hai_face1,uruk_hai_face2],
["barman_cgaladhon","Tavern_Keeper","the_Tree_castle",tf_hero| tf_randomize_face| tf_lorien,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_cdolen","Tavern_Keeper","the_Tree_castle",tf_hero| tf_randomize_face| tf_lorien,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_camroth","Tavern_Keeper","the_Tree_castle",tf_hero| tf_randomize_face| tf_lorien,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_thalls","Tavern_Keeper","the_Throne_Room",tf_hero| tf_randomize_face| tf_woodelf,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_beorn","Tavern_Keeper","Beorn_House",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_moria","Tavern_Keeper","the_Chief's_Chamber",tf_hero| tf_randomize_face| tf_orc,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_dale","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["barman_esgaroth","Tavern_Keeper","the_Hall",tf_hero| tf_randomize_face| tf_female,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_erebor","Tavern_Keeper","the_Lord's_Chamber",tf_hero| tf_randomize_face| tf_dwarf,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
["barman_dolguldur","Tavern_Keeper","the_Castle",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_commoners,[],
      def_attrib|level(2),wp(20),knows_common,woman_face_1,woman_face_2],
#Goods Merchants
#["town_1_merchant","Merchant","bug",tf_hero|tf_randomize_face|tf_is_merchant,scn_town_store|entry(9),0,fac_commoners,[itm_short_tunic,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
#["town_2_merchant","Merchant","bug",tf_hero|tf_randomize_face|tf_is_merchant,scn_town_2_store|entry(9),0,fac_commoners,[itm_leather_apron,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
#["salt_mine_merchant","Barezan","Barezan",tf_hero|tf_is_merchant,scn_salt_mine|entry(1),0,fac_commoners,[itm_leather_apron,itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,0x00000000000c528601ea69b6e46dbdb6],
# Horse Merchants
["merchant_mtirith","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_gon_jerkin,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_riding_6,woman_face_1,woman_face_2],
["merchant_pelargir","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,subfac_pelargir,fac_gondor,
   [itm_pel_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_3,man_face_young_1,man_face_older_2],
["merchant_linhir","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_gon_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,man_face_young_1,man_face_older_2],
["merchant_dolamroth","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,subfac_dol_amroth,fac_gondor,
   [itm_dol_shirt,itm_dol_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_3,man_face_young_1,man_face_older_2],
["merchant_edhellond","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_gon_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,man_face_young_1,man_face_older_2],
["merchant_lossarnach","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,subfac_lossarnach,fac_gondor,
   [itm_lossarnach_shirt,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,man_face_young_1,man_face_older_2],
["merchant_tarnost","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_gon_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_5,man_face_young_1,man_face_older_2],
["merchant_erech","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,subfac_blackroot,fac_gondor,
   [itm_blackroot_bowman,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,man_face_young_1,man_face_older_2],
["merchant_pinnath","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,subfac_pinnath_gelin,fac_gondor,
   [itm_pinnath_gambeson,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,0x0000000c2900555235d36db7536db6db00000000001db6dd0000000000000000],
["merchant_eosgiliath","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_mordor,
   [itm_m_orc_heavy_a,itm_orc_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_1,man_face_young_1,man_face_older_2],
["merchant_wosgiliath","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_gon_mail,itm_gondor_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
["town_12_horse_merchant","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_gon_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
["town_13_horse_merchant","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_gondor,
   [itm_lamedon_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
["merchant_edoras","Supply_Maiden","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_female,0,0,fac_rohan,
   [itm_green_dress,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,woman_face_1,woman_face_2],
["merchant_aldburg","Supply_Master","King's_stable_and_warehouse",tf_hero| tf_rohan| tf_is_merchant,0,0,fac_rohan,
   [itm_green_tunic,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,0x0000000a31000301449bfb13a1ae451d00000000001e2ce30000000000000000],
["merchant_hornburg","Supply_Master","stable_and_warehouse",tf_hero| tf_rohan| tf_is_merchant,0,0,fac_rohan,
   [itm_green_tunic,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,0x0000000a3c00424434944a656429591300000000001d38440000000000000000],
["merchant_eastemnet","Supply_Master","stable_and_warehouse",tf_hero| tf_rohan| tf_is_merchant,0,0,fac_rohan,
   [itm_green_tunic,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,0x0000000a220012456aaca2575d5692ab00000000001e48ec0000000000000000],
["merchant_westfold","Supply_Maiden","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_female,0,0,fac_rohan,
   [itm_green_dress,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,woman_face_1,woman_face_2],
["merchant_westemnet","Supply_Maiden","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_female,0,0,fac_rohan,
   [itm_green_dress,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,woman_face_1,woman_face_2],
["merchant_eastfold","Supply_Maiden","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_female,0,0,fac_rohan,
   [itm_green_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_riding_6,woman_face_1,woman_face_2],
["town_21_horse_merchant","Supply_Master","pit_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_orc_ragwrap,],
      def_attrib|level(2),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
["merchant_morannon","Supply_Master","pit_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_orc_ragwrap,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
["merchant_mmorgul","Supply_Master","pit_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_orc_ragwrap,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
["town_24_horse_merchant","Supply_Master","pit_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_a,itm_orc_ragwrap,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
["merchant_orc_patrol","Supply_Master","camp_stash",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_orc_ragwrap,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,man_face_young_1,man_face_older_2],
["merchant_isengard","Supply_Master","camp_stash",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,uruk_hai_face1,uruk_hai_face2],
["town_27_horse_merchant","Supply_Master","warg_pit_and_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,uruk_hai_face1,uruk_hai_face2],
["merchant_uoutpost","Supply_Master","warg_pit_and_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_3,uruk_hai_face1,uruk_hai_face2],
["merchant_uhcamp","Supply_Master","warg_pit_and_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_3,uruk_hai_face1,uruk_hai_face2],
["merchant_urcamp","Supply_Master","warg_pit_and_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_urukhai,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,uruk_hai_face1,uruk_hai_face2],
["merchant_cgaladhon","Supply_Master","elven_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_lorien,0,0,fac_lorien,
   [itm_lorien_archer,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_riding_3,lorien_elf_face_1,lorien_elf_face_2],
["merchant_cdolen","Supply_Master","elven_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_lorien,0,0,fac_lorien,
   [itm_lorien_archer,itm_elven_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_1,lorien_elf_face_1,lorien_elf_face_2],
["merchant_camroth","Supply_Master","elven_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_lorien,0,0,fac_lorien,
   [itm_lorien_archer,itm_elven_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,lorien_elf_face_1,lorien_elf_face_2],
["merchant_thranduils_halls","Supply_Master","elven_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_woodelf,0,0,fac_woodelf,
   [itm_mirkwood_armor_d,itm_mirkwood_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,lorien_elf_face_1,lorien_elf_face_2],
["merchant_woodelf_camp","Supply_Master","elven_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_woodelf,0,0,fac_woodelf,
   [itm_mirkwood_armor_d,itm_mirkwood_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_1,lorien_elf_face_1,lorien_elf_face_2],
["merchant_woodmen","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_beorn,
   [itm_beorn_tunic,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
["merchant_beorn","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_beorn,
   [itm_beorn_tunic,itm_rohan_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10,man_face_young_1,man_face_older_2],
["merchant_moria","Supply_Master","warg_pit_and_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_moria,
   [itm_moria_armor_c,itm_orc_ragwrap,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
["merchant_dale","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_dale,
   [(itm_free_fur_coat,imod_lordly),itm_dale_boots_a,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
["merchant_esgaroth","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_dale,
   [itm_free_fur_coat,itm_dale_boots_a,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
["merchant_erebor","Supply_Master","Dwarven_supplies",tf_hero| tf_is_merchant| tf_dwarf,0,0,fac_dwarf,
   [itm_dwarf_hood,itm_dwarf_vest,itm_dwarf_pad_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_1,0x00000001c000110336db6db6db6db6db00000000001db6db0000000000000000],
["merchant_dunland","Dun_Stash_Master","camp_stash",tf_hero| tf_dunland| tf_is_merchant,0,0,fac_dunland,
   [itm_dunland_armor_h,itm_dunland_wolfboots,],
      def_attrib|level(2),wp(20),knows_inventory_management_10|knows_riding_2,0x000000003f00520137da6c7bd86f36db00000000001e42f80000000000000000],
["merchant_harad","Harad_Stash_Master","camp_stash",tf_hero| tf_randomize_face| tf_is_merchant| tf_harad,0,0,fac_harad,
   [itm_harad_padded,itm_harad_scale_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_4,man_face_young_1,man_face_older_2],
["merchant_khand","Khand_Stash_Master","camp_stash",tf_hero| tf_is_merchant| tf_evil_man,0,0,fac_khand,
   [itm_khand_foot_lam_c,itm_variag_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_3,0x0000000fff0093c213f746f5e363f35b00000000001de22a0000000000000000],
["merchant_umbar","Supply_Master","camp_stash",tf_hero| tf_randomize_face| tf_is_merchant,0,0,fac_umbar,
   [itm_umb_armor_a,itm_corsair_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_1,man_face_young_1,man_face_older_2],
["merchant_imladris","Supply_Master","camp_supplies",tf_hero| tf_is_merchant,0,0,fac_imladris,
   [itm_arnor_armor_d,itm_leather_gloves_black,itm_leather_boots],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,0x0000000af700414719da9135148aa8d300000000001db9110000000000000000],
["merchant_dolguldur","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant| tf_uruk,0,0,fac_guldur,
   [itm_m_uruk_heavy_c,itm_orc_greaves,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,man_face_young_1,man_face_older_2],
["merchant_north_rhun","Supply_Master","camp_stash",tf_hero| tf_randomize_face| tf_is_merchant| tf_gondor,0,0,fac_rhun,
   [itm_easterling_cloth,itm_rhun_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,gondor_civil_face_1,gondor_civil_face_2],
["merchant_south_rhun","Supply_Master","camp_stash",tf_hero| tf_randomize_face| tf_is_merchant| tf_gondor,0,0,fac_rhun,
   [itm_easterling_cloth,itm_rhun_shoes,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,gondor_civil_face_1,gondor_civil_face_2],
["merchant_gundabad","Supply_Master","camp_stash",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_d,itm_orc_furboots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
["merchant_ironhill","Supply_Master","Dwarven_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_dwarf,0,0,fac_dwarf,
   [itm_dwarf_helm_coif,itm_dwarf_vest_a,itm_dwarf_pad_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_1,dwarf_face_3,dwarf_face_4],
["town_50_horse_merchant","Gobrip_Yellowtooth","warg_pit_and_supplies",tf_hero| tf_randomize_face| tf_is_merchant| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_c,itm_orc_furboots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_2,man_face_young_1,man_face_older_2],
["merchant_calembel","Supply_Master","stable_and_warehouse",tf_hero| tf_randomize_face| tf_is_merchant,0,subfac_ethring,fac_gondor,
   [itm_lamedon_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(20),knows_inventory_management_10|knows_riding_6,man_face_young_1,man_face_older_2],
#
["elder_mtirith","Tirith_Guildmaster","the_White_City",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_pelargir","Sailor_Guildmaster","the_city",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_linhir","Linhir_Guildmaster","the_city",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_dolamroth","Dol_Amroth_Guildmaster","the_city",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_dol_shoes,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_edhellond","Edhellond_Guildmaster","the_city",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_lossarnach","Lossarnach_Guildmaster","the_town",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_tarnost","Tarnost_Guildmaster","the_town",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_erech","Erech_Guildmaster","the_town",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_pinnath","Pinnath_Tribe_Elder","the_town",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_ethring","Calembel_Guildmaster","the_city",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_henneth","Ranger_Guildmaster","the_hideout",tf_hero,0,0,fac_gondor,
   [itm_gon_ranger_skirt,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,0x00000001bf00210336db6db6db65b4db00000000001d36eb0000000000000000],
["elder_cairandros","Cair_Andros_Guildmaster","the_island_fortress",tf_hero,0,0,fac_gondor,
   [itm_gon_ranger_skirt,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,0x00000001bf00210336db6db6db65b4db00000000001d36eb0000000000000000],
["elder_edoras","Edoras_Thain","the_city",tf_hero| tf_rohan,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000a0e00330226db69d9abb6271300000000001c45130000000000000000],
["elder_aldburg","Aldburg_Thain","the_town",tf_hero| tf_rohan,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000a2a0002c326c66a695e8e74f300000000001eeb230000000000000000],
["elder_hornburg","Hornburg_Thain","the_fortress",tf_hero| tf_rohan,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000a040021414ce3915792b2ab2200000000001ce7150000000000000000],
["elder_eastemnet","East_Emnet_Thain","the_town",tf_hero| tf_rohan,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000a10000341472366aae58ed89400000000001caccb0000000000000000],
["elder_westfold","Westfold_Thain","the_town",tf_hero| tf_rohan,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000a3d00410526cbb1c71269cadb00000000001d368a0000000000000000],
["elder_westemnet","West_Emnet_Thain","the_town",tf_hero| tf_rohan,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000a1d0021c546cb672932eea69e00000000001eb95b0000000000000000],
["elder_eastfold","Eastfold_Thain","the_town",tf_hero| tf_rohan,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000a0d0042c1556a8547648b34e400000000001d56d50000000000000000],
["elder_morannon","Morannon_Chief","the_caves_overlooking_the_Great_Gate",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_uruk_greaves,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_mmorgul","Morgul_Chief","the_sinister_city",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_uruk_greaves,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_cungol","Camp_Chief","the_camp",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_uruk_greaves,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_isengard","Grima_Wormtongue","the_city",tf_hero| tf_evil_man,0,0,fac_isengard,
   [itm_evil_light_armor,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,0x000000077f0010044bff71fd836a38e400000000001db6e40000000000000000],
["elder_cgaladhon","Lorien Loremaster","the_elven_forest_fortress",tf_hero| tf_randomize_face| tf_lorien,0,0,fac_lorien,
   [itm_whiterobe,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_cdolen","Lorien Loremaster","the_encampment",tf_hero| tf_randomize_face| tf_lorien,0,0,fac_lorien,
   [itm_whiterobe,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_camroth","Lorien Loremaster","the_encampment",tf_hero| tf_randomize_face| tf_lorien,0,0,fac_lorien,
   [itm_whiterobe,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_thalls","Mirkwood_Elder","the_elven_caves",tf_hero| tf_randomize_face| tf_woodelf,0,0,fac_woodelf,
   [itm_mirkwood_armor_d,itm_mirkwood_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_imladris","Rivendell_Campmaster","the_camp",tf_hero| tf_randomize_face| tf_imladris,0,0,fac_imladris,
   [itm_riv_armor_light,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_wvillage","Pierre_Woodman","the_village",tf_hero,0,0,fac_beorn,
   [itm_beorn_tunic,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x000000052300000036db6db75eedf6ed00000000001f2adb0000000000000000],
["elder_beorn","Beorn_Elder","the_hamlet",tf_hero| tf_randomize_face,0,0,fac_beorn,
   [itm_beorn_tunic,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_harad","Harad_Camp_chief","the_camp",tf_hero| tf_randomize_face| tf_harad,0,0,fac_harad,
   [itm_harad_padded,itm_harad_scale_greaves,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_rhun","Rhun_Camp_Chief","the_camp",tf_hero| tf_randomize_face| tf_gondor,0,0,fac_rhun,
   [itm_rhun_armor_b,itm_rhun_shoes,],
      def_attrib|level(2),wp(20),knows_common,gondor_civil_face_1,gondor_civil_face_2],
["elder_khand","Khand_Camp_Chief","the_camp",tf_hero| tf_randomize_face,0,0,fac_khand,
   [itm_khand_foot_lam_c,itm_variag_greaves,],
      def_attrib|level(2),wp(20),knows_common,khand_man1,khand_man2],
["elder_dunland","Dun_Camp_Chief","the_camp",tf_hero |tf_dunland,0,0,fac_dunland,
   [itm_dunland_armor_h,itm_dunland_wolfboots,],
      def_attrib|level(2),wp(20),knows_common,0x000000003f0061c720996c7bd86f36db00000000001e42e80000000000000000],
["elder_umbar","Umbar_Quartermaster","the_fortified_camp",tf_hero| tf_randomize_face,0,0,fac_umbar,
   [itm_umb_armor_a,itm_corsair_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_moria","Moria_Chief","the_Mines",tf_hero| tf_randomize_face| tf_orc,0,0,fac_moria,
   [itm_moria_armor_c,itm_orc_ragwrap,],
      def_attrib|level(2),wp(20),knows_common,khand_man1,khand_man2],
["elder_gunda","Master_of_the_Caves","the_caves",tf_hero| tf_randomize_face| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_d,itm_orc_furboots,],
      def_attrib|level(2),wp(20),knows_common,khand_man1,khand_man2],
["elder_dale","Dale_Quartermaster","the_city",tf_hero| tf_randomize_face,0,0,fac_dale,
   [(itm_free_fur_coat,imod_lordly),itm_dale_boots_a,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_esgaroth","Esgaroth_Quartermaster","the_lake_town",tf_hero| tf_randomize_face,0,0,fac_dale,
   [(itm_free_fur_coat,imod_lordly),itm_dale_boots_a,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_erebor","Gloin","the_Halls",tf_hero| tf_dwarf,0,0,fac_dwarf,
   [itm_leather_dwarf_armor_b,itm_dwarf_pad_boots,],
      def_attrib|level(2),wp(20),knows_common_dwarf,0x0000000b7c00108372dc6db7fb713efb00000000001db6fb0000000000000000],
["elder_dolguldur","Guldur_Chief","the_black_castle",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_guldur,
   [itm_m_uruk_light_b,itm_uruk_greaves,],
      def_attrib|level(2),wp(20),knows_common,mordor_man1,mordor_man2],

["elder_gondor_ac","Campmaster","the_camp",tf_hero| tf_gondor| tf_randomize_face,0,0,fac_gondor,
   [itm_gondor_fine_outfit_dress,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_rohan_ac","Campmaster","the_camp",tf_hero| tf_rohan| tf_randomize_face,0,0,fac_rohan,
   [itm_rohan_fine_outfit_dale_dress,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,0x0000000f00001184574a6934eb6ed2d700000000001eb86e0000000000000000],
["elder_mordor_ac","Campmaster","the_camp",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_mordor,
   [itm_m_uruk_light_b,itm_uruk_greaves,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_isengard_ac","Campmaster","the_camp",tf_hero| tf_randomize_face| tf_urukhai,0,0,fac_isengard,
   [itm_isen_uruk_light_b,itm_isen_boots,],
      def_attrib|level(2),wp(20),knows_common,uruk_hai_face1,uruk_hai_face2],
["elder_lorien_ac","Campmaster","the_camp",tf_hero| tf_randomize_face| tf_lorien,0,0,fac_lorien,
   [itm_whiterobe,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_woodelf_ac","Campmaster","the_camp",tf_hero| tf_randomize_face| tf_woodelf,0,0,fac_woodelf,
   [itm_mirkwood_armor_d,itm_mirkwood_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_imladris_ac","Campmaster","the_camp",tf_hero| tf_randomize_face| tf_imladris,0,0,fac_imladris,
   [itm_riv_armor_light,itm_elven_boots,],
      def_attrib|level(2),wp(20),knows_common,lorien_elf_face_1,lorien_elf_face_2],
["elder_beorn_ac","Campmaster","the_camp",tf_hero| tf_randomize_face,0,0,fac_beorn,
   [itm_beorn_tunic,itm_rohan_shoes,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_harad_ac","Harad_Camp_Chief","the_camp",tf_hero| tf_randomize_face| tf_harad,0,0,fac_harad,
   [itm_harad_padded,itm_harad_scale_greaves,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_rhun_ac","Rhun_Camp_Chief","the_camp",tf_hero| tf_randomize_face| tf_gondor,0,0,fac_rhun,
   [itm_rhun_armor_b,itm_rhun_shoes,],
      def_attrib|level(2),wp(20),knows_common,gondor_civil_face_1,gondor_civil_face_2],
["elder_khand_ac","Khand_Camp_Chief","the_camp",tf_hero| tf_randomize_face,0,0,fac_khand,
   [itm_khand_foot_lam_c,itm_variag_greaves,],
      def_attrib|level(2),wp(20),knows_common,khand_man1,khand_man2],
["elder_dunland_ac","Dun_Camp_Chief","the_camp",tf_hero |tf_dunland,0,0,fac_dunland,
   [itm_dunland_armor_h,itm_dunland_wolfboots,],
      def_attrib|level(2),wp(20),knows_common,0x000000003f0061c720996c7bd86f36db00000000001e42e80000000000000000],
["elder_umbar_ac","Umbar_Quartermaster","the_camp",tf_hero| tf_randomize_face,0,0,fac_umbar,
   [itm_umb_armor_a,itm_corsair_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_moria_ac","Moria_Camp_Chief","the_camp",tf_hero| tf_randomize_face| tf_orc,0,0,fac_moria,
   [itm_moria_armor_c,itm_orc_ragwrap,],
      def_attrib|level(2),wp(20),knows_common,khand_man1,khand_man2],
["elder_gunda_ac","Gundabad_Camp_Chief","the_camp",tf_hero| tf_randomize_face| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_d,itm_orc_furboots,],
      def_attrib|level(2),wp(20),knows_common,khand_man1,khand_man2],
["elder_dale_ac","Dale_Quartermaster","the_camp",tf_hero| tf_randomize_face,0,0,fac_dale,
   [(itm_free_fur_coat,imod_lordly),itm_dale_boots_a,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder_guldur_ac","Guldur_Camp_Chief","the_camp",tf_hero| tf_randomize_face| tf_uruk,0,0,fac_guldur,
   [itm_m_uruk_light_b,itm_uruk_greaves,],
      def_attrib|level(2),wp(20),knows_common,mordor_man1,mordor_man2],   
["elder_dwarf_ac","Dwarven_Campmaster","the_camp",tf_hero| tf_randomize_face| tf_dwarf,0,0,fac_dwarf,
   [itm_leather_dwarf_armor_b,itm_dwarf_pad_boots,],
      def_attrib|level(2),wp(20),knows_common_dwarf,dwarf_face_3,dwarf_face_4],
    
    
#Village stores
["village_1_elder","Lord_of_the_Lash","the_caves",tf_hero| tf_randomize_face| tf_orc,0,0,fac_gundabad,
   [itm_gundabad_armor_d,itm_orc_furboots,],
      def_attrib|level(2),wp(20),knows_common,khand_man1,khand_man2],
["merchants_end","bug","bug",tf_hero,0,0,fac_commoners,   [],      0,0,0,0],
 
# Chests
#["zendar_chest","Zendar_Chest","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      def_attrib,0,0,0],
["tutorial_chest_1","Melee_Weapons_Chest","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      def_attrib,0,0,0],
["tutorial_chest_2","Ranged_Weapons_Chest","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      def_attrib,0,0,0],
["bonus_chest_1","Bonus_Chest","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      def_attrib,0,0,0],
["bonus_chest_2","Bonus_Chest","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      def_attrib,0,0,0],
["bonus_chest_3","Bonus_Chest","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      def_attrib,0,0,0],
["camp_chest_faction","Faction_Chest","bug",tf_hero|tf_inactive|tf_is_merchant,0,0,fac_neutral,   [],      def_attrib,0,knows_inventory_management_10,0],
["camp_chest_none","Chest_for_nones","bug",tf_hero|tf_inactive|tf_is_merchant,0,0,fac_neutral,   [],      def_attrib,0,0,0],
["player_chest","Your_Chest","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      def_attrib,0,0,0],
# These are used as arrays in the scripts.
["temp_array_a","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["temp_array_b","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["temp_array_c","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["stack_selection_amounts","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["stack_selection_ids","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["notification_menu_types","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["notification_menu_var1","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["notification_menu_var2","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
["banner_background_color_array","bug","bug",tf_hero|tf_inactive,0,0,fac_neutral,   [],      0,0,0,0],
# Add Extra Quest NPCs below this point  
["local_merchant","Local_Merchant","Local_Merchants",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(5),wp(40),knows_power_strike_1,mercenary_face_1,mercenary_face_2],
["tax_rebel","Peasant_Rebel","Peasant_Rebels",tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
["trainee_peasant","Peasant","Peasants",tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
["fugitive_man","Suspicious_Man","Suspicious_Men",tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_jerkin,itm_leather_boots,itm_arnor_sword_f,],
      attr_tier_4,wp_tier_4,knows_common|knows_athletics_6|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,mercenary_face_1,mercenary_face_2],
["fugitive_elf","Suspicious_Elf","Suspicious_Elves",tf_lorien| tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_lorien_armor_b,itm_elven_boots,itm_lorien_sword_b,],
      attr_elf_tier_4,wp_elf_tier_4,knows_common|knows_athletics_6|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,lorien_elf_face_1,lorien_elf_face_2],
["fugitive_dwarf","Suspicious_Dwarf","Suspicious_Dwarves",tf_dwarf| tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_leather_dwarf_armor,itm_dwarf_pad_boots,itm_dwarf_sword_a,itm_dwarf_throwing_axe,],
      attr_dwarf_tier_4,wp_dwarf_tier_4,knows_common_dwarf|knows_athletics_6|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,dwarf_face_2,dwarf_face_3],
["fugitive_orc","Suspicious_Orc","Suspicious_Orcs",tf_orc| tfg_boots| tfg_armor,0,0,fac_commoners,
   [itm_moria_armor_a,itm_orc_slasher,itm_orc_throwing_arrow,],
      attr_orc_tier_4,wp_orc_tier_4,knows_common|knows_athletics_6|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,mercenary_face_1,mercenary_face_2],
["spy","Shifty-eyed_Corsair","Shifty-eyed_Corsairs",tf_mounted| tfg_boots| tfg_armor| tfg_gloves| tfg_horse,0,0,fac_neutral,
   [itm_umb_armor_f,itm_umb_armor_h,itm_corsair_boots,itm_umb_shield_b,itm_umb_shield_d,itm_umbar_cutlass,itm_umbar_rapier,itm_steppe_horse,],
      attr_tier_4,wp_tier_4,knows_common|knows_riding_3|knows_power_strike_3,bandit_face1,bandit_face2],
["spy_evil","Shifty-eyed_Southerner","Shifty-eyed_Southerners",tf_mounted| tfg_boots| tfg_armor| tfg_gloves| tfg_horse,0,0,fac_neutral,
   [itm_leather_jerkin,itm_leather_gloves,itm_leather_boots,itm_arnor_sword_f,itm_steppe_horse,],
      attr_tier_4,wp_tier_4,knows_common|knows_riding_3|knows_power_strike_3,bandit_face1,bandit_face2],
["spy_partner","Spy_Handler","Spy_Handlers", tf_mounted| tfg_boots| tfg_armor| tfg_gloves| tfg_horse,0,0,fac_neutral,
   [itm_gon_mail,itm_gondor_greaves,itm_gondor_cav_sword,itm_gon_tab_shield_a,itm_gondor_courser,],
      attr_tier_4,wp_tier_4,knows_common|knows_riding_3|knows_athletics_2|knows_power_strike_3|knows_ironflesh_3,gondor_face1,gondor_face2],
["spy_partner_evil","Spy_Handler","Spy_Handlers",tf_mounted| tfg_boots| tfg_armor| tfg_gloves| tfg_horse,0,0,fac_neutral,
   [itm_evil_light_armor,itm_leather_boots,itm_mordor_sword,itm_mordor_longsword,itm_mordor_man_shield_b,itm_mordor_warhorse,],
      attr_tier_4,wp_tier_4,knows_common|knows_riding_3|knows_athletics_2|knows_power_strike_3|knows_ironflesh_3,bandit_face1,bandit_face2],
#MV: Easter Egg Troll in Troll Cave
["easter_egg_troll","The Troll","_",tf_troll| tfg_helm| tfg_boots| tf_no_capture_alive| tf_hero,scn_troll_cave_center|entry(8),0,fac_moria,
   [itm_tree_trunk_club_a,itm_item_30,],
      str_255| agi_3| int_30| cha_18|level(30),wp(200),knows_power_strike_10|knows_ironflesh_10,troll_face1],
["treebeard","Treebeard","_",tf_troll| tfg_helm| tfg_boots| tfg_armor| tfg_gloves| tf_no_capture_alive| tf_hero,scn_fangorn|entry(16),0,fac_commoners,
   [itm_tree_trunk_invis,itm_ent_body,itm_ent_hands,itm_ent_feet_boots,itm_ent_head_helm,itm_ent_water,],
      str_255| agi_3| int_30| cha_30|level(30),wp(200),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],
["ent_1","Bregalad","_",tf_troll| tfg_helm| tfg_boots| tfg_armor| tfg_gloves| tf_no_capture_alive| tf_hero,scn_fangorn|entry(17),0,fac_commoners,
   [itm_tree_trunk_invis,itm_ent_body,itm_ent_hands,itm_ent_feet_boots,itm_ent_head_helm2,itm_ent_water,],
      str_255| agi_3| int_30| cha_30|level(30),wp(200),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],
["ent_2","Finglas","_",tf_troll| tfg_helm| tfg_boots| tfg_armor| tfg_gloves| tf_no_capture_alive| tf_hero,scn_fangorn|entry(18),0,fac_commoners,
   [itm_tree_trunk_invis,itm_ent_body,itm_ent_hands,itm_ent_feet_boots,itm_ent_head_helm3,itm_ent_water,],
      str_255| agi_3| int_30| cha_30|level(30),wp(200),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],
["ent_3","Fladrif","_",tf_troll| tfg_helm| tfg_boots| tfg_armor| tfg_gloves| tf_no_capture_alive| tf_hero,scn_fangorn|entry(19),0,fac_commoners,
   [itm_tree_trunk_invis,itm_ent_body,itm_ent_hands,itm_ent_feet_boots,itm_ent_head_helm2,itm_ent_water,],
      str_255| agi_3| int_30| cha_30|level(30),wp(200),knows_power_strike_10|knows_ironflesh_10,troll_face1,troll_face2],

# Gandalf and Nazgul for conversations
["gandalf","Gandalf","Home-grown Gandalves",tf_hero| tf_mounted| tfg_armor| tfg_boots|tfg_helm| tfg_horse,0,0,fac_commoners,
   [itm_item_36,itm_item_37,itm_leather_boots,itm_gandstaff,itm_mearas_reward,],
      attr_tier_7,wp_tier_7,knows_riding_10|knows_athletics_10|knows_power_strike_10|knows_ironflesh_10|knows_pathfinding_10,0x0000000fc000234721419ab9eeafbeff00000000001d89110000000000000000],
["nazgul","Nazgul","Domesticated Nazgul",tf_hero| tf_mounted| tfg_armor| tfg_helm| tfg_horse| tfg_boots,0,0,fac_commoners,
   [itm_empty_head,itm_nazgulrobe,itm_evil_gauntlets_a,itm_uruk_greaves,itm_nazgul_sword,itm_mordor_warhorse2,],
       attr_tier_7,wp_tier_7,knows_riding_10|knows_athletics_10|knows_power_strike_10|knows_ironflesh_10|knows_pathfinding_10,mercenary_face_2],

["quick_battle_6_player","quick_battle_6_player","_",tf_hero,0,0,fac_player_faction,
   [itm_leather_jerkin,itm_leather_boots,itm_short_bow,itm_arrows,],
      knight_attrib_1,wp(130),knight_skills_1,0x000000000008010b01f041a9249f65fd],
# GA scene stub NPCs
["barman","Barman","_",tf_hero| tf_randomize_face,0,0,fac_neutral,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["elder","Center_Elder","_",tf_hero| tf_randomize_face,0,0,fac_neutral,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["gear_merchant","Gear_Merchant","_",tf_hero| tf_randomize_face,0,0,fac_neutral,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["goods_merchant","Goods_Merchant","_",tf_hero| tf_randomize_face,0,0,fac_neutral,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["start_quest_caravaneer","Torbal_the_Caravaneer","_",tf_hero| tf_randomize_face,0,0,fac_neutral,
   [itm_leather_jerkin,itm_leather_boots,],
      def_attrib|level(50),wp(400),knows_common|knows_power_strike_10|knows_ironflesh_10,mercenary_face_1,mercenary_face_2],
# ["brigand_arena_master","Tournament_Master","_",tf_hero| tf_randomize_face,scn_zendar_arena|entry(52),0,fac_commoners,
   # [itm_leather_jerkin,itm_leather_boots,],
      # def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
# ["gondor_arena_master","Tournament_Master","_",tf_hero| tf_randomize_face,scn_gondor_arena|entry(52),0,fac_commoners,
   # [itm_leather_jerkin,itm_leather_boots,],
      # def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
# ["rohan_arena_master","Tournament_Master","_",tf_hero| tf_randomize_face,scn_rohan_arena|entry(52),0,fac_commoners,
   # [itm_leather_jerkin,itm_leather_boots,],
      # def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
# ["mordor_arena_master","Pit_Master","_",tf_hero| tf_randomize_face,scn_mordor_arena|entry(52),0,fac_commoners,
   # [itm_leather_jerkin,itm_leather_boots,],
      # def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
# ["elf_arena_master","Tournament_Master","_",tf_hero| tf_randomize_face,scn_elf_arena|entry(52),0,fac_commoners,
   # [itm_leather_jerkin,itm_leather_boots,],
      # def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
#Kolba additions
#["androg","Androg","_",tf_hero,scn_zendar_center|entry(7),0,fac_commoners,
#   [itm_leather_jerkin,itm_leather_boots,],
#      def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["dorwinion_bandit","Easterling_Bandit","Easterling_Bandits",tfg_armor| tfg_boots,0,0,fac_outlaws,
   [itm_rhun_helm_k,itm_rhun_armor_b,itm_rhun_shoes,itm_rhun_shortsword,itm_rhun_axe,itm_rhun_sword,itm_javelin,itm_rhun_round_shield,],
         def_attrib|level(12),wp(100),knows_common,rhun_man1,rhun_man2],
["dorwinion_raider","Easterling_Raider","Easterling_Raiders",tfg_armor|tfg_shield|tfg_boots|tfg_helm,0,0,fac_outlaws,
   [itm_rhun_helm_l,itm_rhun_armor_m,itm_rhun_shoes,itm_rhun_shortsword,itm_rhun_axe,itm_rhun_sword,itm_javelin,itm_rhun_round_shield,],
              def_attrib|level(17),wp(120),knows_common,rhun_man1,rhun_man2],

# Troops for scripting purpose. Make sure these are the last troops. (by foxyman)
["troops_end","troops_end","troops_end",tf_hero,no_scene,reserved,fac_commoners,[],0,0,0,0,0],
["no_troop","_","the place",tf_hero,0,0,fac_commoners,[],0,0,0,0,0],
["skill2item_type","_","_",tf_hero,0,0,fac_commoners,[],0,0,0,0,0], # array for working with merchant skills as indicator of quantity of items in shop
["traits","_","_",tf_hero,0,0,fac_commoners,[],0,0,0,0,0], # array of traits (0/1)
#Player history array
["log_array_entry_type","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_entry_time","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_actor","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_center_object","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_center_object_lord","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_center_object_faction","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_troop_object","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_troop_object_faction","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
["log_array_faction_object","_","_",0,0,0,fac_commoners,   [],      0,0,0,0],
##############################
#MV: what are these - future quest troops? not used anywhere
["city_guard","City_Guard","city_guard",tfg_armor| tfg_boots,0,0,fac_gondor,
   [itm_leather_jerkin,itm_leather_boots,itm_gon_tab_shield_a,],
      def_attrib|level(9),wp(90),knows_common|knows_athletics_1|knows_power_strike_1|knows_riding_1,mercenary_face_1,mercenary_face_2],
["orc_sentry","Orc_Sentry","orc_sentry",tf_orc| tfg_shield| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_mordor_orc_shield_d,itm_orc_coif,itm_orc_ragwrap,itm_orc_slasher,],
      def_attrib|level(12),wp(90),knows_prisoner_management_1|knows_inventory_management_1|knows_pathfinding_1|knows_athletics_3|knows_power_strike_2|knows_ironflesh_2,orc_face1,orc_face2],
["uruk_hai_sentry","Uruk-hai_Sentry","uruk_hai_sentry",tf_urukhai|tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_a,itm_isen_orc_armor_f,itm_isen_boots,itm_isengard_sword,itm_isen_uruk_shield_a,],
      def_attrib|level(12),wp(90),knows_prisoner_management_1|knows_inventory_management_1|knows_pathfinding_1|knows_athletics_2|knows_power_strike_2|knows_ironflesh_3,uruk_hai_face1,uruk_hai_face2],
["black_numenorean_sorcerer","Black_Numenorean_Sorcerer","Black_numenorean_sorcerer", tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_m_cap_armor,itm_mordor_helm,itm_mordor_sword,itm_leather_boots,],
      def_attrib|level(45),wp(400),knows_common|knows_athletics_10|knows_power_strike_6|knows_ironflesh_10|knows_riding_1,mercenary_face_1,mercenary_face_2],
["black_numenorean_acolyte","Black_Numenorean_Acolyte","Black_Numenorean_Acolytes",tf_evil_man| tfg_armor| tfg_boots,0,0,fac_mordor,
   [itm_leather_boots,itm_leather_gloves,itm_evil_light_armor,itm_uruk_spear,],
      attr_tier_2,wp_tier_2,knows_common|knows_athletics_1|knows_power_strike_1|knows_riding_1,mordor_man1,mordor_man2],
["wolf_rider_of_mirkwood","Wolf_Rider_of_Mirkwood","Wolf_Riders_of_Mirkwood",tf_orc| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_isengard,
   [itm_orc_bow,itm_arrows,itm_orc_sabre,itm_orc_sabre,itm_isen_orc_armor_a,itm_isen_orc_armor_e,itm_orc_coif,itm_wargarmored_2c,itm_orc_ragwrap,],
      def_attrib|level(15),wp(110),knows_pathfinding_1|knows_horse_archery_2|knows_riding_4|knows_power_throw_2|knows_power_strike_2|knows_ironflesh_2,orc_face3,orc_face6],
["warg_rider_of_mirkwood","Warg_Rider_of_Mirkwood","Warg_Riders_of_Mirkwood",tf_orc| tf_mounted| tfg_shield| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_isengard,
   [itm_orc_bow,itm_arrows,itm_orc_sabre,itm_orc_sabre,itm_isen_orc_armor_a,itm_isen_orc_armor_e,itm_orc_coif,itm_wargarmored_1c,itm_orc_ragwrap,],
      def_attrib|level(22),wp(135),knows_pathfinding_1|knows_horse_archery_3|knows_riding_4|knows_power_throw_3|knows_power_strike_4|knows_ironflesh_4,orc_face3,orc_face8],
["gate_aggravator","Gate_is_holding","_", tfg_armor| tfg_boots| tfg_helm|tfg_gloves,0,0,fac_neutral,
   [itm_warg_ghost_armour,itm_empty_hands,itm_empty_legs,itm_empty_head],
      str_255|level(80),wp(5),knows_shield_10|knows_ironflesh_10,0,0],
["orc_pretender","Orc_Pretender","_",tf_orc| tfg_shield| tfg_armor| tfg_helm| tf_no_capture_alive,0,0,fac_neutral,
   [itm_orc_slasher,itm_orc_sabre,itm_moria_orc_shield_b,itm_moria_orc_shield_a,itm_moria_armor_e,itm_orc_greaves,],
      attr_orc_tier_6,wp_tier_6,knows_athletics_5|knows_power_strike_4|knows_ironflesh_10,orc_face5,orc_face8],
["human_prisoner","Human_Prisoner","_",tf_hero| tfg_helm,0,0,fac_neutral,
   [itm_prisoner_coll_chain,],
      attr_orc_tier_4,wp_tier_6,knows_athletics_5|knows_power_strike_4,0x000000063f00004336db75b7ab6eb6b400000000001db6eb0000000000000000],
 
# CC: Ambush troops here...

["spider","Mirkwood Spider","Mirkwood Spiders", tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
[itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_spider],
str_30| agi_7| int_4| cha_4|level(20),0,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face7,orc_face2],

["bear","Bear","Bears", tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_outlaws,
[itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_bear],
str_127|agi_7|int_4|cha_4|level(35),0,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face7,orc_face2], #0x7D = str_127

["wolf","Wolf","Wolves", tf_orc| tfg_gloves| tfg_armor| tfg_helm| tfg_horse| tfg_boots| tf_no_capture_alive,0,0,fac_outlaws,
[itm_warg_ghost_lance,itm_warg_ghost_armour,itm_empty_legs,itm_empty_hands,itm_empty_head,itm_wolf],
str_30| agi_7| int_4| cha_4|level(15),0,knows_riding_10|knows_ironflesh_10|knows_power_strike_2,orc_face7,orc_face2],

#kham Spears Quest
["dorwinion_sack","Dorwinion_Sack","bug",tf_hero|tfg_helm|tf_inactive|tf_is_merchant,0,0,fac_neutral,   [itm_cram,itm_metal_scraps_good,itm_metal_scraps_good,itm_metal_scraps_good, itm_rhun_helm_c],      def_attrib,0,knows_inventory_management_10,0],
#end Kham Spears quest

#kham Ring Hunters Start ####

["ring_hunter_captain","Ring_Hunter_Captain","bug",tf_evil_man|tf_hero| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_black_num_armor,itm_black_num_helm,itm_mordor_man_shield_b,itm_mordor_longsword,],
      attr_tier_6,wp_tier_5,knows_common|knows_leadership_10|knows_tactics_1|knows_athletics_8|knows_shield_7|knows_power_strike_7|knows_ironflesh_7|knows_riding_1,mordor_man1,mordor_man2],

["ring_hunter_lt","Ring_Hunter_Captain","bug",tf_evil_man| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_black_num_armor,itm_black_num_helm,itm_mordor_man_shield_b,itm_mordor_longsword,],
      attr_tier_6,wp_tier_5,knows_common|knows_leadership_10|knows_tactics_1|knows_athletics_8|knows_shield_7|knows_power_strike_7|knows_ironflesh_7|knows_riding_1,mordor_man1,mordor_man2],


["ring_hunter_one","Ring_Hunter","Ring_Hunters",tf_harad| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_harad,
   [itm_harad_scale_greaves,itm_leather_gloves,itm_harad_lion_scale,itm_lion_helm,itm_harad_heavy_sword,itm_harad_khopesh,itm_harad_long_shield_b,],
      attr_tier_5,wp_tier_5,knows_common|knows_athletics_6|knows_power_strike_5|knows_ironflesh_6|knows_riding_1,haradrim_face_1,haradrim_face_2],

["ring_hunter_two","Ring_Hunter","Ring_Hunters",tfg_ranged| tfg_armor| tfg_helm| tfg_boots,0,0,fac_umbar,
   [itm_corsair_boots,itm_umb_armor_d,itm_umb_helm_d,itm_umb_helm_c,itm_corsair_bow,itm_corsair_arrows,itm_corsair_sword,],
      attr_tier_5,wp_tier_5,knows_common|knows_athletics_5|knows_power_draw_3|knows_power_strike_4|knows_ironflesh_4|knows_riding_1,bandit_face1,bandit_face2],

["ring_hunter_three","Ring_Hunter","Ring_Hunters",tf_urukhai| tfg_armor| tfg_shield| tfg_boots|tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_isengard,
   [itm_isen_uruk_helm_b,itm_isen_uruk_light_d,itm_leather_gloves_black,itm_isen_greaves,itm_isengard_sword,itm_isen_uruk_shield_a,],
      attr_tier_5,wp_tier_5,knows_athletics_6|knows_power_strike_6|knows_ironflesh_6,uruk_hai_face1,uruk_hai_face2],

["ring_hunter_four","Ring_Hunter","Ring_Hunters",tf_orc| tfg_ranged| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_greaves,itm_evil_gauntlets_b,itm_m_orc_light_d,itm_m_orc_light_e,itm_m_orc_heavy_a,itm_m_orc_heavy_b,itm_orc_bow,itm_orc_hook_arrow,itm_orc_sabre,itm_orc_slasher,itm_orc_slasher,],
      attr_orc_tier_4,wp_orc_tier_4,knows_athletics_4|knows_power_draw_4|knows_power_strike_2,orc_face7,orc_face6],
### Kham Ring Hunters End ###

#Kham Start Quest Troops
["start_quest_uruk","Mordor_Uruk_Captain","bug",tf_uruk| tfg_shield| tfg_ranged|tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_greaves,itm_uruk_chain_greaves,itm_evil_gauntlets_b,itm_orc_throwing_arrow,itm_uruk_bow,itm_orc_hook_arrow,itm_m_uruk_heavy_h,itm_m_uruk_heavy_i,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_uruk_skull_spear,itm_mordor_uruk_shield_a,itm_mordor_uruk_shield_b,itm_uruk_helm_b,itm_uruk_helm_c,itm_uruk_helm_d,],
      attr_tier_4,wp_tier_4,knows_athletics_6|knows_power_strike_5|knows_power_draw_4|knows_power_throw_3|knows_ironflesh_4|knows_shield_2,uruk_hai_face1,uruk_hai_face2],

["start_quest_orc","Mordor_Orc_Lieutenant","Large_Orcs_of_Mordor",tf_orc| tfg_shield| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_greaves,itm_orc_coif, itm_orc_nosehelm, itm_orc_kettlehelm, itm_m_orc_light_d,itm_m_orc_light_e,itm_m_orc_heavy_a,itm_m_orc_heavy_b,itm_orc_sabre,itm_orc_falchion,itm_orc_two_handed_axe,itm_orc_skull_spear,itm_orc_slasher,itm_orc_bill,itm_orc_axe,itm_mordor_orc_shield_b,itm_mordor_orc_shield_c,itm_orc_throwing_axes,itm_mordor_orc_shield_d,],
      attr_orc_tier_3,wp_orc_tier_3,knows_athletics_5|knows_power_strike_3|knows_power_throw_3,orc_face3,orc_face6],

["start_quest_woodelf","Galadhrim_Royal_Marksman","Galadhrim_Royal_Marksmen",tf_lorien| tfg_ranged| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_helm_a,itm_lorien_armor_c,itm_leather_gloves,itm_elven_boots,itm_lorien_bow,itm_elven_arrows,itm_elven_war_sword,],
      attr_elf_tier_6,wp_elf_tier_6,knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_draw_6|knows_shield_1|knows_athletics_7|knows_riding_1,lorien_elf_face_1,lorien_elf_face_2],

["start_quest_mordor_scout","Mordor_Guide","Mordor_Guides",tf_orc| tfg_ranged| tfg_helm| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_furboots,itm_orc_coif, itm_orc_nosehelm, itm_orc_kettlehelm_bad,itm_leather_gloves,itm_m_orc_light_c,itm_m_orc_light_d,itm_m_orc_light_e,itm_m_orc_light_c,itm_orc_bow,itm_orc_hook_arrow,itm_orc_sabre,itm_orc_slasher,itm_orc_slasher,],
      attr_orc_tier_4,wp_archery(135)| wp(110),knows_power_strike_2|knows_power_draw_5|knows_athletics_6|knows_riding_1,orc_face1,orc_face4],

["start_quest_beorning","Beorning_Carrock_Berserker","Beorning_Carrock_Berserkers",tfg_gloves| tfg_armor| tfg_helm| tfg_boots,0,0,fac_beorn,
   [itm_beorn_berserk,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,itm_beorn_battle_axe,itm_dale_bastard,],
      attr_tier_5,wp_tier_5,knows_common|knows_ironflesh_6|knows_power_strike_3|knows_athletics_6|knows_riding_1,beorn_face1,beorn_face2],

## Kham Amath Dollen's Troops

["black_shield","Amath_Dollen","-",tf_hero| tf_evil_man| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_rhun,
   [itm_furry_boots,itm_evil_gauntlets_a,itm_m_uruk_heavy_j,itm_rhun_sword,itm_mordor_uruk_shield_a,],
      attr_tier_5,wp_tier_6,knows_common|knows_athletics_7|knows_shield_7|knows_power_strike_7|knows_ironflesh_7|knows_riding_1,0x000000003f00b30d2d2ea72ac902553500000000001d42300000000000000000],

["black_shield_bandit","Amath_Dollen's_Bandit","Amath_Dollen's_Bandits",tf_evil_man| tf_randomize_face| tfg_shield| tfg_armor| tfg_boots,0,0,fac_rhun,
   [itm_furry_boots,itm_leather_gloves,itm_dunland_armor_a,itm_dunland_armor_b,itm_dunland_armor_c,itm_dunland_armor_d,itm_dunland_armor_e,itm_dunland_armor_g,itm_dunland_armor_h,itm_orc_throwing_axes,itm_umb_hood,itm_orc_shield_a,itm_orc_shield_b,itm_wood_club,itm_orc_axe,],
      attr_tier_3,wp_tier_3,knows_common|knows_athletics_3|knows_shield_3|knows_power_strike_3|knows_ironflesh_3|knows_power_throw_3|knows_riding_1,rhun_man1,rhun_man2],

["black_shield_scout","Amath_Dollen's_Scout","Amath_Dollen's_Scouts",tf_evil_man| tf_randomize_face|tfg_helm|tfg_armor| tfg_boots|tfg_ranged,0,0,fac_rhun,
   [itm_furry_boots,itm_leather_gloves,itm_dunland_armor_a,itm_dunland_armor_b,itm_dunland_armor_c,itm_dunland_armor_d,itm_dunland_armor_e,itm_dunland_armor_g,itm_dunland_armor_h,itm_umb_hood,itm_wood_club,itm_arrows,itm_orc_bow,],
      attr_tier_3,wp_tier_3,knows_common|knows_athletics_3|knows_shield_3|knows_power_strike_3|knows_ironflesh_3|knows_power_draw_5|knows_riding_1,rhun_man1,rhun_man2],

["black_shield_guard","Amath_Dollen's_Guard","Amath_Dollen's_Guards",tf_evil_man| tf_randomize_face|tfg_helm| tfg_shield| tfg_armor| tfg_boots,0,0,fac_rhun,
   [itm_furry_boots,itm_leather_gloves,itm_dunland_armor_i,itm_dunland_armor_j,itm_corsair_harpoon,itm_dun_helm_e,itm_mordor_uruk_shield_a,itm_rhun_shortsword,itm_rhun_sword,],
      attr_tier_4,wp_tier_4,knows_common|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5|knows_power_throw_5|knows_riding_1,rhun_man1,rhun_man2],

["dorwinion_spirit_leader","Spirit","_", tf_urukhai|tfg_armor| tfg_boots| tfg_helm|tfg_gloves,0,0,fac_neutral,
  [(itm_dunland_armor_k,imod_old),(itm_leather_gloves,imod_poor),itm_dunland_wolfboots,(itm_empty_head,imod_old)],
    def_attrib|level(45),wp(255),knows_common|knows_athletics_6|knows_power_strike_6|knows_ironflesh_6|knows_riding_1,0,0],

["dorwinion_spirit","Lesser Spirit","_", tf_uruk|tfg_armor| tfg_boots| tfg_helm|tfg_gloves,0,0,fac_neutral,
  [(itm_dunland_armor_k,imod_poor),(itm_leather_gloves,imod_poor),itm_dunland_wolfboots,(itm_empty_head,imod_poor)],
    def_attrib|level(45),wp(255),knows_common|knows_athletics_6|knows_power_strike_6|knows_ironflesh_6|knows_riding_1,0,0],

["dummy_troop",  "bug","_", tf_hero, 0, 0, fac_gondor, [], lord_attrib,0,0,0],
["dummy_troop_b","bug","_", tf_hero, 0, 0, fac_gondor, [], lord_attrib,0,0,0],
    
["beorning_shield_bear","Beorning_Shield_Bear","Beorning_Shield_Bears",tfg_gloves| tfg_shield| tfg_armor| tfg_boots,0,0,fac_beorn,
   [itm_beorn_chief,itm_beorn_heavy,itm_leather_boots,itm_leather_gloves,itm_beorn_helmet,(itm_beorn_shield_reward,imod_reinforced), (itm_dale_sword_broad,imod_fine), (itm_good_mace,imod_masterwork)],
      attr_tier_6,wp_tier_6,knows_common|knows_ironflesh_7|knows_power_strike_5|knows_shield_7|knows_athletics_6|knows_riding_1,beorn_face1,beorn_face2],

["test_vet_archer","Test_Vet_Archer","Test_Vet_Archer",tf_woodelf| tfg_ranged| tfg_gloves| tfg_shield| tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_armor_e,itm_mirkwood_leather_greaves,itm_mirkwood_helm_d],
      attr_elf_tier_6,wp_elf_tier_6|wp_throwing(300), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_draw_7|knows_athletics_8|knows_riding_1,mirkwood_elf_face_1,mirkwood_elf_face_2],

## Kham - Volunteers

["volunteers","--- Reserves ---:","_", tfg_armor| tfg_boots| tfg_helm|tfg_gloves,0,0,fac_neutral,
   [itm_warg_ghost_armour,itm_empty_hands,itm_empty_legs,itm_empty_head],
      str_255|level(80),wp(5),knows_shield_10|knows_ironflesh_10,0,0],

## Kham - Dormant Troop

["dormant","Dormant","_", tfg_armor| tfg_boots| tfg_helm|tfg_gloves,0,0,fac_neutral,
   [itm_warg_ghost_armour,itm_empty_hands,itm_empty_legs,itm_empty_head],
      str_255|level(80),wp(5),knows_shield_10|knows_ironflesh_10,0,0],


## Kham - Test AI
["badass_theo","Badass_King_Theo","King",tf_hero| tf_rohan| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_rohan,
   [itm_item_9,itm_item_7,itm_leather_gloves,itm_item_10,itm_item_12,itm_rohan_shield_g,itm_item_11,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_4,0x0000000d4000210236db6db8db65b6fb00000000001e46fb0000000000000000],

["killer_witcher","Ugly Mogly","Lieutenant",tf_hero| tf_uruk| tfg_shield| tfg_armor| tfg_helm| tfg_boots,0,0,fac_mordor,
   [itm_m_uruk_heavy_k,itm_uruk_chain_greaves,itm_evil_gauntlets_a,itm_uruk_helm_f,itm_mordor_uruk_shield_c,itm_mordor_longsword,],
      attr_tier_6,wp_tier_6,knight_skills_5|knows_trainer_4,0x000000002c000104003fb3f407b83d0d00000000000000000000000000000000],

## Kham - Healers

["morannon_healer","Okstuk_the_Healer","_",tf_hero|tf_orc,scn_morannon_center|entry(13),0,fac_mordor,
   [itm_moria_armor_b,itm_orc_greaves,itm_orc_coif],
      str_15|agi_5|int_4|cha_4|level(2),wp(20),knows_common,orc_face1],

["minas_tirith_healer","Ioreth","_",tf_female|tf_hero,scn_minas_tirith_center|entry(13),0,fac_gondor,
   [itm_free_whiterobe,itm_leather_boots],
      str_15|level(2),wp(20),knows_common,0x0000000fff0030064b3152c34d27231100000000001c986d0000000000000000],

["edoras_healer","Freya_the_Healer","_",tf_female|tf_hero,scn_edoras_center|entry(13),0,fac_rohan,
   [itm_free_whiterobe,itm_leather_boots],
      str_15|level(2),wp(20),knows_common,0x00000005070010045a9569a16d724adc00000000001db95a0000000000000000],

["isengard_healer","Nurgal_the_Patcher","_",tf_hero|tf_urukhai,scn_isengard_center|entry(13),0,fac_isengard,
   [itm_isen_uruk_light_a,itm_isen_shoes,],
      str_15|agi_5|int_4|cha_4|level(2),wp(20),knows_common,0x0000000a400020c336dee2d25962b4fc00000000001e382b0000000000000000],

["guldur_healer","Mornagar_the_Gramaryer","_",tf_hero|tf_evil_man,scn_dol_guldur_center|entry(13),0,fac_guldur,
   [itm_leather_boots, itm_evil_light_armor,],
      str_15|agi_5|int_4|cha_4|level(2),wp(20),knows_common,0x000000047f0024d212014ac90032e05200000000001c84880000000000000000],

["gundabad_healer","Lurgakh_Third_Eye","_",tf_orc|tf_hero,scn_gundabad_camp_center|entry(13),0,fac_gundabad,
   [itm_gundabad_armor_d,itm_orc_furboots],
      def_attrib|level(2),wp(20),knows_common,0x0000000fc000200b5ff83e35e4f8ed8900000000001f6d470000000000000000],

["mirkwood_healer","Corwiel_the_Soft-Handed","_",tf_woodelf|tf_woodelf|tf_hero,scn_thranduils_halls_center|entry(13),0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,],
      str_15|level(2),wp(20),knows_common,0x000000000000014148ed6e47238dd70d00000000001d36f30000000000000000],

#Kham Morale Troops

["hungry_uruk","Hungry_Uruk","bug",tf_uruk| tfg_shield| tfg_ranged|tfg_armor| tfg_helm| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_uruk_greaves,itm_uruk_chain_greaves,itm_evil_gauntlets_b,itm_orc_throwing_arrow,itm_uruk_bow,itm_orc_hook_arrow,itm_m_uruk_heavy_h,itm_m_uruk_heavy_i,itm_uruk_falchion_a,itm_uruk_falchion_b,itm_uruk_skull_spear,itm_mordor_uruk_shield_a,itm_mordor_uruk_shield_b,itm_uruk_helm_b,itm_uruk_helm_c,itm_uruk_helm_d,],
      attr_tier_4,wp_tier_4,knows_athletics_6|knows_power_strike_5|knows_power_draw_4|knows_power_throw_3|knows_ironflesh_4|knows_shield_2,uruk_hai_face1,uruk_hai_face2],

["hungry_orc","Hungry_Orc","Large_Orcs_of_Mordor",tf_orc| tfg_shield| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_mordor,
   [itm_orc_greaves,itm_orc_coif, itm_orc_nosehelm_bad, itm_orc_nosehelm, itm_m_orc_light_d,itm_m_orc_light_e,itm_m_orc_heavy_a,itm_m_orc_heavy_b,itm_orc_sabre,itm_orc_falchion,itm_orc_two_handed_axe,itm_orc_skull_spear,itm_orc_slasher,itm_orc_bill,itm_orc_axe,itm_mordor_orc_shield_b,itm_mordor_orc_shield_c,itm_orc_throwing_axes,itm_mordor_orc_shield_d,],
      attr_orc_tier_3,wp_orc_tier_3,knows_athletics_5|knows_power_strike_3|knows_power_throw_3,orc_face3,orc_face6],

["longing_lorien","Longing_Elf","Lothlorien_Scouts",tf_lorien| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_lorien,
   [itm_lorien_archer,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_1,wp_elf_tier_1,knows_common|knows_power_draw_3|knows_power_strike_2|knows_ironflesh_1|knows_riding_1,lorien_elf_face_1,lorien_elf_face_2],

["longing_woodelf","Longing_Elf","Greenwood_Scouts",tf_woodelf| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_woodelf,
   [itm_mirkwood_armor_a,itm_mirkwood_boots,itm_elven_bow,itm_woodelf_arrows,itm_mirkwood_sword,],
      attr_elf_tier_1,wp_elf_tier_1,knows_common|knows_power_draw_3|knows_power_strike_2|knows_ironflesh_1|knows_riding_1,mirkwood_elf_face_1,mirkwood_elf_face_2],

["longing_imladris","Longing_Elf","Rivendell_Scouts",tf_imladris| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_imladris,
   [itm_riv_armor_light,itm_elven_boots,itm_elven_bow,itm_elven_arrows,itm_lorien_sword_b,],
      attr_elf_tier_1,wp_elf_tier_1,knows_common|knows_power_draw_3|knows_power_strike_2|knows_ironflesh_1|knows_riding_1,rivendell_elf_face_1,rivendell_elf_face_2],

["last","BUG","BUG",tf_hero,0,0,fac_commoners,[],0,0,0,0],

["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero, 0, 0,fac_commoners,[itm_leather_jerkin, itm_leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female, 0, 0,fac_commoners,[itm_leather_jerkin, itm_leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],

["future_troop_6", "Compatibility","_", tf_randomize_face,0,0,fac_neutral,[], def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["future_troop_7", "Compatibility","_", tf_randomize_face,0,0,fac_neutral,[], def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["future_troop_8", "Compatibility","_", tf_randomize_face,0,0,fac_neutral,[], def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["future_troop_9", "Compatibility","_", tf_randomize_face,0,0,fac_neutral,[], def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
["future_troop_10","Compatibility","_", tf_randomize_face,0,0,fac_neutral,[], def_attrib|level(2),wp(20),knows_common,mercenary_face_1,mercenary_face_2],
  ########TLD_Overhaul#########

#Dunedain_overhaul#   
#This troop is the troop marked as new_soldiers_begin
["dunedain_bowman","Arnor_Scout","Arnor_Scouts",tf_dunedain| tfg_armor| tfg_boots| tfg_gloves| tfg_ranged| tfg_helm,0,0,fac_imladris,
   [itm_arnor_helm_a,itm_arnor_armor_c,itm_leather_gloves,itm_leather_boots,itm_regular_bow,itm_arrows,itm_arnor_sword_f,],
      attr_dun_tier_2,wp_dun_tier_2_a,dun_skills_2b,arnor_face_middle_1,arnor_face_middle_2],

["arnor_squire","Arnor_Squire","Arnor_Squires",tf_dunedain| tf_mounted| tfg_armor| tfg_shield| tfg_boots| tfg_gloves| tfg_helm| tfg_horse,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_a,itm_leather_gloves_black,itm_leather_boots,itm_arnor_sword_f,itm_arnor_shield_c,itm_arnor_horse,],
      attr_dun_tier_3,wp_dun_tier_3,dun_skills_3c,arnor_face_older_1,arnor_face_older_2],   

["arnor_archer","Arnor_Archer","Arnor_Archers",tf_dunedain| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_a,itm_leather_gloves_black,itm_leather_boots,itm_numenor_bow,itm_arnor_arrows,itm_arnor_sword_f,],
      attr_dun_tier_3,wp_dun_tier_3_a,dun_skills_3b,arnor_face_middle_1,arnor_face_middle_2],

["arnor_veteran_archer","Arnor_Veteran_Archer","Arnor_Veteran_Archers",tf_dunedain| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_a,itm_leather_gloves_black,itm_arnor_greaves,itm_numenor_bow,itm_arnor_arrows,itm_arnor_sword_f,],
      attr_dun_tier_4,wp_dun_tier_4_a,dun_skills_4b,arnor_face_middle_1,arnor_face_middle_2],

["arnor_elite_archer","Arnor_Elite_Archer","Arnor_Elite_Archers",tf_dunedain| tfg_armor| tfg_boots| tfg_gloves| tfg_helm| tfg_ranged,0,0,fac_imladris,
   [itm_arnor_helm_b,itm_arnor_armor_f,itm_leather_gloves_black,itm_arnor_greaves,itm_numenor_bow,itm_arnor_arrows,itm_arnor_sword_f,],
      attr_dun_tier_5,wp_dun_tier_5_a,dun_skills_5b,arnor_face_middle_1,arnor_face_middle_2], 

#orcs_Overhaul"
["deep_dweller_of_moria","Deep-Dweller_of_Moria","Deep-Dwellers_of_Moria",tf_orc| tfg_armor| tfg_helm| tfg_boots| tfg_shield| tf_no_capture_alive,0,0,fac_moria,
   [itm_orc_club_d,itm_uruk_heavy_axe,itm_uruk_voulge,itm_orc_javelin,itm_orc_javelin,itm_orc_greaves,itm_orc_bughelm_lordly,itm_orc_bughelm_lordly,itm_uruk_helm_e,itm_uruk_helm_f,itm_moria_armor_e,itm_moria_orc_shield_a,itm_moria_orc_shield_b,itm_moria_orc_shield_c],
      attr_orc_tier_5,wp_orc_tier_5,knows_ironflesh_5|knows_power_strike_5|knows_power_throw_5|knows_shield_4|knows_athletics_5,orc_face5,orc_face4],

 ["orc_beserker_gundabad","Gundabad_Orc_Berserker","Gundabad_Orc_Berserkers",tf_orc| tfg_armor|tfg_boots| tf_no_capture_alive,0,0,fac_gundabad,
   [itm_gundabad_helm_a,itm_gundabad_helm_b,itm_gundabad_helm_c,itm_gundabad_helm_d,itm_gundabad_armor_d,itm_gundabad_armor_e,itm_leather_gloves,itm_orc_furboots,itm_orc_throwing_axes,itm_orc_throwing_axes_reward,itm_orc_two_handed_axe,itm_orc_two_handed_axe,itm_uruk_falchion_b, itm_uruk_skull_spear, itm_orc_club_b,itm_twohand_wood_club ],
      attr_orc_tier_5,wp_orc_tier_5,knows_ironflesh_5|knows_power_strike_6|knows_power_throw_6|knows_shield_4|knows_athletics_7,orc_face3,orc_face8],



#This troop is the troop marked as new_soldiers_end
["void_overhaul","_","_",tf_imladris| tf_hero| tfg_ranged| tfg_armor| tfg_boots| tf_no_capture_alive,0,0,fac_imladris,
   [itm_elven_boots,],
      attr_elf_tier_1,wp_elf_tier_1,elf_skills_1a,rivendell_elf_face_1,rivendell_elf_face_2],
   
]
 
#
#upgrade(troops,"veteran_brigand","master_brigand")
#upgrade2(troops,"brigand","veteran_brigand","brigand_slaver")
#upgrade(troops,"cutthroat","brigand")
#upgrade(troops,"thug","cutthroat")
#upgrade(troops,"brigand_slaver","master_slaver")
#WOODMEN
upgrade2(troops,"woodmen_youth","woodmen_forester","woodmen_tracker")
upgrade(troops,"woodmen_forester","woodmen_skilled_forester")
upgrade(troops,"woodmen_skilled_forester","woodmen_axemen")
upgrade(troops,"woodmen_axemen","woodmen_master_axemen")
upgrade(troops,"woodmen_tracker","woodmen_scout")
upgrade(troops,"woodmen_scout","woodmen_archer")
upgrade(troops,"woodmen_archer","fell_huntsmen_of_mirkwood")
#BEORNINGS
upgrade(troops,"beorning_vale_man","beorning_warrior")
upgrade2(troops,"beorning_warrior","beorning_tolltacker","beorning_carrock_lookout")
upgrade(troops,"beorning_tolltacker","beorning_sentinel")
upgrade(troops,"beorning_sentinel","beorning_warden_of_the_ford")
upgrade(troops,"beorning_warden_of_the_ford","beorning_shield_bear")
upgrade(troops,"beorning_carrock_lookout","beorning_carrock_fighter")
upgrade(troops,"beorning_carrock_fighter","beorning_carrock_berserker")
##LOSSARNACH
upgrade2(troops,"woodsman_of_lossarnach","footman_of_lossarnach","axeman_of_lossarnach")
upgrade(troops,"footman_of_lossarnach","heavy_footman_of_lossarnach")
upgrade(troops,"axeman_of_lossarnach","heavy_axeman_of_lossarnach")
##LAMEDON
upgrade(troops,"clansman_of_lamedon","footman_of_lamedon")
upgrade(troops,"footman_of_lamedon","warrior_of_lamedon")
upgrade(troops,"warrior_of_lamedon","veteran_of_lamedon")
upgrade2(troops,"veteran_of_lamedon","champion_of_lamedon","knight_of_lamedon")
##PINNATH GELIN
upgrade2(troops,"pinnath_gelin_plainsman","pinnath_gelin_spearman","pinnath_gelin_bowman")
upgrade(troops,"pinnath_gelin_spearman","warrior_of_pinnath_gelin")
upgrade(troops,"pinnath_gelin_bowman","pinnath_gelin_archer")
##BLACK ROOT VALE
upgrade2(troops,"blackroot_vale_archer","veteran_blackroot_vale_archer","footman_of_blackroot_vale")
upgrade(troops,"veteran_blackroot_vale_archer","master_blackroot_vale_archer")
upgrade(troops,"footman_of_blackroot_vale","spearman_of_blackroot_vale")
###PELARGIR
upgrade2(troops,"pelargir_watchman","pelargir_marine","pelargir_infantry")
upgrade(troops,"pelargir_infantry","pelargir_vet_infantry")
upgrade(troops,"pelargir_marine","pelargir_vet_marine")
##DOL AMROTH
upgrade(troops,"dol_amroth_youth","squire_of_dol_amroth")
upgrade(troops,"squire_of_dol_amroth","veteran_squire_of_dol_amroth")
upgrade(troops,"veteran_squire_of_dol_amroth","knight_of_dol_amroth")
upgrade(troops,"knight_of_dol_amroth","veteran_knight_of_dol_amroth")
upgrade(troops,"veteran_knight_of_dol_amroth","swan_knight_of_dol_amroth")
#LORIEN
upgrade2(troops,"lothlorien_scout","lothlorien_veteran_scout","lothlorien_light_swordsman")
upgrade(troops,"lothlorien_veteran_scout","lothlorien_archer")
upgrade2(troops,"lothlorien_archer","lothlorien_warden","galadhrim_archer")
upgrade(troops,"lothlorien_warden","lothlorien_elite_warden")
upgrade(troops,"galadhrim_archer","galadhrim_elite_archer")
upgrade2(troops,"lothlorien_light_swordsman","lothlorien_footman","lothlorien_horseman")
upgrade2(troops,"lothlorien_footman","galadhrim_spearman","galadhrim_swordsman")
upgrade(troops,"galadhrim_spearman","galadhrim_elite_spearman")
upgrade(troops,"galadhrim_swordsman","galadhrim_elite_swordsman")
upgrade(troops,"lothlorien_horseman","galadhrim_horseman")
#MIRKWOOD
upgrade2(troops,"greenwood_scout","greenwood_veteran_scout","greenwood_spearman")
upgrade2(troops,"greenwood_veteran_scout","greenwood_archer","greenwood_sentinel")
upgrade(troops,"greenwood_archer","greenwood_veteran_archer")
upgrade(troops,"greenwood_veteran_archer","greenwood_master_archer")
upgrade(troops,"greenwood_master_archer","thranduils_royal_marksman")
upgrade(troops,"greenwood_spearman","greenwood_veteran_spearman")
upgrade(troops,"greenwood_veteran_spearman","greenwood_royal_spearman")
upgrade2(troops,"greenwood_royal_spearman","thranduils_spearman","thranduils_royal_swordsman")
upgrade(troops,"greenwood_sentinel","greenwood_vet_sentinel")
#RIVENDELL
upgrade2(troops,"rivendell_scout","rivendell_mounted_scout","rivendell_veteran_scout")
upgrade(troops,"rivendell_mounted_scout","rivendell_horseman")
upgrade(troops,"rivendell_horseman","noldorin_horseman")
upgrade(troops,"noldorin_horseman","rivendell_knight")
upgrade2(troops,"rivendell_veteran_scout","rivendell_footman","rivendell_archer")
upgrade2(troops,"rivendell_footman","noldorin_swordsman","noldorin_spearman")
upgrade(troops,"noldorin_swordsman","noldorin_elite_swordsman")
upgrade(troops,"noldorin_spearman","noldorin_elite_spearman")
upgrade(troops,"rivendell_archer","noldorin_archer")
upgrade(troops,"noldorin_archer","noldorin_elite_archer")
#DUNEADAIN
upgrade2(troops,"dunedain_scout","dunedain_bowman","dunedain_trained_scout")
upgrade2(troops,"dunedain_bowman","dunedain_ranger","arnor_archer")
upgrade(troops,"dunedain_ranger","dunedain_veteran_ranger")
upgrade(troops,"dunedain_veteran_ranger","dunedain_master_ranger")
upgrade(troops,"arnor_archer","arnor_veteran_archer")
upgrade(troops,"arnor_veteran_archer","arnor_elite_archer")
upgrade2(troops,"dunedain_trained_scout","arnor_squire","arnor_man_at_arms")
upgrade(troops,"arnor_squire","arnor_horsemen")
upgrade(troops,"arnor_horsemen","knight_of_arnor")
upgrade(troops,"arnor_man_at_arms","arnor_master_at_arms")
upgrade(troops,"arnor_master_at_arms","high_swordsman_of_arnor")

#Gondor infantry
upgrade2(troops,"gondor_commoner","gondor_militiamen","gondor_bow_militia")
upgrade(troops,"gondor_militiamen","footmen_of_gondor")
upgrade2(troops,"footmen_of_gondor","gondor_swordsmen","gondor_spearmen" )
upgrade(troops,"gondor_swordsmen","gondor_veteran_swordsmen" )
upgrade(troops,"gondor_veteran_swordsmen","swordsmen_of_the_tower_guard" )
upgrade(troops,"gondor_spearmen","gondor_veteran_spearmen" )
upgrade2(troops,"gondor_veteran_spearmen","guard_of_the_fountain_court","steward_guard" )
#Gondor Noble Line
upgrade(troops,"gondor_noblemen","squire_of_gondor" )
upgrade(troops,"squire_of_gondor","veteran_squire_of_gondor" )
upgrade(troops,"veteran_squire_of_gondor","knight_of_gondor" )
upgrade(troops,"knight_of_gondor","veteran_knight_of_gondor" )
upgrade(troops,"veteran_knight_of_gondor","knight_of_the_citadel" )
#Gondor archers
upgrade(troops,"gondor_bow_militia","bowmen_of_gondor")
upgrade(troops,"bowmen_of_gondor","archer_of_gondor")
upgrade(troops,"archer_of_gondor","veteran_archer_of_gondor" )
upgrade(troops,"veteran_archer_of_gondor","archer_of_the_tower_guard" )
upgrade(troops,"ranger_of_ithilien","veteran_ranger_of_ithilien" )
upgrade(troops,"veteran_ranger_of_ithilien","master_ranger_of_ithilien" )
#ROHAN
upgrade2(troops,"rohan_youth","squire_of_rohan","guardsman_of_rohan")
upgrade2(troops,"guardsman_of_rohan","footman_of_rohan","dismounted_skirmisher_of_rohan")
upgrade2(troops,"footman_of_rohan","spearman_of_rohan","veteran_footman_of_rohan")
upgrade(troops,"spearman_of_rohan","elite_spearman_of_rohan")
upgrade(troops,"elite_spearman_of_rohan","warden_of_methuseld")
upgrade2(troops,"veteran_footman_of_rohan","raider_of_rohan","heavy_swordsman_of_rohan")
upgrade(troops,"heavy_swordsman_of_rohan","folcwine_guard_of_rohan")
upgrade(troops,"skirmisher_of_rohan","veteran_skirmisher_of_rohan")
upgrade(troops,"veteran_skirmisher_of_rohan","elite_skirmisher_of_rohan")
upgrade(troops,"elite_skirmisher_of_rohan","brego_guard_of_rohan")
upgrade(troops,"lancer_of_rohan","elite_lancer_of_rohan")
upgrade(troops,"elite_lancer_of_rohan","thengel_guard_of_rohan")
upgrade2(troops,"squire_of_rohan","rider_of_rohan","skirmisher_of_rohan")
upgrade2(troops,"rider_of_rohan","veteran_rider_of_rohan","lancer_of_rohan")
upgrade(troops,"veteran_rider_of_rohan","elite_rider_of_rohan")
upgrade(troops,"elite_rider_of_rohan","eorl_guard_of_rohan")
upgrade(troops,"dismounted_skirmisher_of_rohan","dismounted_veteran_skirmisher_of_rohan")
upgrade(troops,"dismounted_veteran_skirmisher_of_rohan","dismounted_elite_skirmisher_of_rohan")
upgrade(troops,"dismounted_elite_skirmisher_of_rohan","helm_guard_of_rohan")
#HARAD
upgrade2(troops,"harad_desert_warrior","harad_infantry","harad_skirmisher")
upgrade2(troops,"harondor_scout","harondor_rider","harad_horse_archer")
upgrade2(troops,"harad_infantry","harad_veteran_infantry","harad_swordsman")
upgrade(troops,"harad_swordsman","harad_lion_guard")
upgrade(troops,"harad_veteran_infantry","harad_tiger_guard")
upgrade(troops,"harondor_rider","harondor_light_cavalry")
upgrade(troops,"harondor_light_cavalry","fang_heavy_cavalry")
upgrade(troops,"harad_skirmisher","harad_archer")
upgrade(troops,"harad_archer","harad_eagle_guard")
upgrade(troops,"harad_horse_archer","black_snake_horse_archer")
upgrade(troops,"black_snake_horse_archer","gold_serpent_horse_archer")
upgrade(troops,"far_harad_tribesman","far_harad_champion")
upgrade(troops,"far_harad_champion","far_harad_panther_guard")
#DUNLAND
upgrade2(troops,"dunnish_wildman","dunnish_warrior","dunnish_raven_rider")
upgrade2(troops,"dunnish_warrior","dunnish_vet_warrior","dunnish_pikeman")
upgrade(troops,"dunnish_pikeman","dunnish_veteran_pikeman")
#upgrade(troops,"dunnish_veteran_spearman","dunnish_spear_master")
#upgrade(troops,"dunnish_long_spearman","dunnish_pike_master")
#upgrade(troops,"dunnish_horseman","dunnish_wolf_guard")
upgrade(troops,"dunnish_vet_warrior","dunnish_wolf_warrior")
upgrade(troops,"dunnish_wolf_warrior","dunnish_wolf_guard")
#upgrade2(troops,"dunnish_axeman","dunnish_veteran_axeman","dunnish_wolf_warrior")
#upgrade(troops,"dunnish_veteran_axeman","dunnish_axe_master")
#upgrade2(troops,"dunnish_wolf_warrior","dunnish_berserker","dunnish_crebain_raider")
#EASTERLINGS
upgrade2(troops,"easterling_youth","easterling_warrior","easterling_rider")
upgrade2(troops,"easterling_warrior","easterling_axeman","khand_glaive_whirler")
upgrade2(troops,"easterling_axeman","easterling_veteran_axeman","variag_pitfighter")
upgrade(troops,"easterling_veteran_axeman","easterling_axe_master")
upgrade2(troops,"easterling_rider","easterling_horseman","easterling_skirmisher")
upgrade(troops,"easterling_horseman","easterling_veteran_horseman")
upgrade2(troops,"easterling_veteran_horseman","easterling_horsemaster","easterling_lance_kataphract")
upgrade(troops,"khand_glaive_whirler","variag_veteran_glaive_whirler")
upgrade(troops,"variag_veteran_glaive_whirler","khand_glaive_master")
upgrade(troops,"variag_pitfighter","variag_gladiator")
upgrade(troops,"easterling_skirmisher","easterling_veteran_skirmisher")
upgrade(troops,"easterling_veteran_skirmisher","easterling_elite_skirmisher")
#CORSAIRS
upgrade2(troops,"corsair_youth","corsair_warrior","militia_of_umbar")
upgrade2(troops,"corsair_warrior","corsair_pikeman","corsair_marauder")
upgrade(troops,"corsair_pikeman","corsair_veteran_raider")
upgrade(troops,"corsair_veteran_raider","corsair_night_raider")
upgrade(troops,"militia_of_umbar","marksman_of_umbar")
upgrade(troops,"marksman_of_umbar","veteran_marksman_of_umbar")
upgrade2(troops,"veteran_marksman_of_umbar","master_marksman_of_umbar","master_assassin_of_umbar")
upgrade(troops,"corsair_marauder","corsair_veteran_marauder")
upgrade(troops,"corsair_veteran_marauder","corsair_elite_marauder")
#upgrade(troops,"assassin_of_umbar","master_assassin_of_umbar")
#upgrade(troops,"pikeman_of_umbar","veteran_pikeman_of_umbar")
#upgrade(troops,"veteran_pikeman_of_umbar","pike_master_of_umbar")
#ISENGARD ORCS
upgrade2(troops,"orc_snaga_of_isengard","orc_of_isengard","wolf_rider_of_isengard")
upgrade2(troops,"orc_of_isengard","large_orc_of_isengard","large_orc_despoiler")
upgrade(troops,"large_orc_despoiler","fell_orc_despoiler")
upgrade(troops,"wolf_rider_of_isengard","warg_rider_of_isengard")
upgrade(troops,"warg_rider_of_isengard","white_hand_rider")
#ISENGARD URUK-HAIS
upgrade2(troops,"uruk_snaga_of_isengard","uruk_hai_of_isengard","uruk_hai_tracker")
upgrade2(troops,"uruk_hai_of_isengard","large_uruk_hai_of_isengard","uruk_hai_pikeman")
upgrade(troops,"large_uruk_hai_of_isengard","fighting_uruk_hai_warrior")
upgrade(troops,"fighting_uruk_hai_warrior","fighting_uruk_hai_champion")
upgrade(troops,"fighting_uruk_hai_champion","fighting_uruk_hai_berserker")
upgrade(troops,"uruk_hai_pikeman","fighting_uruk_hai_pikeman")
upgrade(troops,"fighting_uruk_hai_pikeman","elite_uruk_hai_pikeman")
upgrade(troops,"uruk_hai_tracker","large_uruk_hai_tracker")
upgrade(troops,"large_uruk_hai_tracker","fighting_uruk_hai_tracker")
#MORDOR ORCS
upgrade2(troops,"orc_snaga_of_mordor","orc_of_mordor","orc_archer_of_mordor")
upgrade2(troops,"orc_of_mordor","large_orc_of_mordor","warg_rider_of_gorgoroth")
upgrade2(troops,"large_orc_of_mordor","fell_orc_of_mordor","fell_morgul_orc")
upgrade(troops,"orc_tracker_of_mordor","fell_orc_tracker_of_mordor")
upgrade2(troops,"orc_archer_of_mordor","large_orc_archer_of_mordor","orc_tracker_of_mordor")
upgrade(troops,"large_orc_archer_of_mordor","fell_orc_archer_of_mordor")
upgrade(troops,"warg_rider_of_gorgoroth","great_warg_rider_of_mordor")
upgrade(troops,"morgul_orc","fell_morgul_orc")
#MORDOR URUKS
upgrade(troops,"uruk_snaga_of_mordor","uruk_of_mordor")
upgrade2(troops,"uruk_of_mordor","large_uruk_of_mordor","uruk_slayer_of_mordor")
upgrade(troops,"large_uruk_of_mordor","fell_uruk_of_mordor")
upgrade(troops,"uruk_slayer_of_mordor","fell_uruk_slayer_of_mordor")
#GULDUR ORCS
upgrade2(troops,"orc_snaga_of_guldur","orc_of_guldur","orc_archer_of_mordor")
upgrade2(troops,"orc_of_guldur","large_orc_of_mordor","warg_rider_of_gorgoroth")
#MORIA ORCS
upgrade(troops,"wolf_rider_of_moria","warg_rider_of_moria")
upgrade(troops,"warg_rider_of_moria","bolg_clan_rider")
upgrade2(troops,"snaga_of_moria","goblin_of_moria","archer_snaga_of_moria")
upgrade2(troops,"goblin_of_moria","large_goblin_of_moria","wolf_rider_of_moria")
upgrade(troops,"archer_snaga_of_moria","large_goblin_archer_of_moria")
upgrade(troops,"large_goblin_archer_of_moria","fell_goblin_archer_of_moria")
upgrade(troops,"large_goblin_of_moria","fell_goblin_of_moria")
upgrade(troops,"fell_goblin_of_moria","deep_dweller_of_moria")
#GUNDABAD ORCS
upgrade2(troops,"goblin_gundabad","orc_gundabad","skirmisher_gundabad")
upgrade2(troops,"orc_gundabad","orc_fighter_gundabad","goblin_rider_gundabad")
upgrade(troops,"orc_fighter_gundabad","fell_orc_warrior_gundabad")
upgrade(troops,"fell_orc_warrior_gundabad","orc_beserker_gundabad")
upgrade(troops,"goblin_rider_gundabad","warg_rider_gundabad")
upgrade(troops,"warg_rider_gundabad","goblin_north_clan_rider")
upgrade(troops,"skirmisher_gundabad","warg_skirmisher_gundabad")
upgrade(troops,"warg_skirmisher_gundabad","goblin_north_clan_skirmisher")

#BLACK NUMENORIANS
upgrade(troops,"black_numenorean_renegade","black_numenorean_warrior")
upgrade2(troops,"black_numenorean_warrior","black_numenorean_veteran_warrior","black_numenorean_veteran_horseman")
upgrade2(troops,"black_numenorean_veteran_warrior","black_numenorean_champion","black_numenorean_assassin")
upgrade(troops,"black_numenorean_veteran_horseman","black_numenorean_horsemaster")
#DWARVES
upgrade2(troops,"dwarven_apprentice","dwarven_warrior","dwarven_lookout")
upgrade(troops,"dwarven_warrior","dwarven_hardened_warrior")
upgrade2(troops,"dwarven_hardened_warrior","dwarven_axeman","dwarven_spearman")
upgrade(troops,"dwarven_axeman","dwarven_expert_axeman")
upgrade(troops,"dwarven_expert_axeman","longbeard_axeman")
upgrade(troops,"dwarven_spearman","dwarven_pikeman")
upgrade(troops,"dwarven_pikeman","dwarven_halberdier")
upgrade(troops,"dwarven_lookout","dwarven_scout")
upgrade(troops,"dwarven_scout","dwarven_bowman")
upgrade(troops,"dwarven_bowman","dwarven_archer")
upgrade(troops,"dwarven_archer","marksman_of_ravenhill")
#IRON HILLS
upgrade2(troops,"iron_hills_miner","iron_hills_watchman","iron_hills_lookout")
upgrade(troops,"iron_hills_watchman","iron_hills_infantry")
upgrade2(troops,"iron_hills_infantry","iron_hills_battle_infantry","iron_hills_spearman")
upgrade(troops,"iron_hills_battle_infantry","iron_hills_heavy_infantry")
upgrade(troops,"iron_hills_heavy_infantry","grors_guard")
upgrade(troops,"iron_hills_spearman","iron_hills_pikeman")
upgrade(troops,"iron_hills_pikeman","iron_hills_halberdier")
upgrade(troops,"iron_hills_lookout","iron_hills_scout")
upgrade(troops,"iron_hills_scout","iron_hills_bowman")
upgrade(troops,"iron_hills_bowman","iron_hills_archer")
upgrade(troops,"iron_hills_archer","iron_hills_marksman")
#DALE
upgrade2(troops,"dale_militia","dale_man_at_arms","dale_scout")
upgrade2(troops,"dale_man_at_arms","dale_warrior","dale_pikeman")
upgrade(troops,"dale_warrior","dale_veteran_warrior")
upgrade(troops,"dale_veteran_warrior","dale_marchwarden")
upgrade(troops,"dale_pikeman","dale_billman")
upgrade(troops,"dale_billman","dale_bill_master")
upgrade(troops,"merchant_squire_or_dale","merchant_guard_of_dale")
upgrade(troops,"merchant_guard_of_dale","merchant_protector_of_dale")
upgrade(troops,"merchant_protector_of_dale","girions_guard_of_dale")
upgrade(troops,"dale_scout","dale_bowmen")
upgrade(troops,"dale_bowmen","dale_archer")
upgrade(troops,"dale_archer","barding_bowmen_of_dale")
upgrade(troops,"rhovanion_regent","aihwothiuda_guard")
upgrade2(troops,"riverman","laketown_militia","laketown_bowman")
upgrade2(troops,"laketown_militia","laketown_shipman","laketown_warden")
upgrade(troops,"laketown_shipman","laketown_marine")
upgrade(troops,"laketown_warden","laketown_guard")
upgrade(troops,"laketown_bowman","laketown_archer")
upgrade(troops,"laketown_archer","laketown_guard_archer")
#RHUN
upgrade2(troops,"rhun_clansman","rhun_huntsman","rhun_militia")
upgrade(troops,"rhun_huntsman","rhun_archer")
upgrade(troops,"rhun_archer","rhun_heavy_archer")
upgrade(troops,"rhun_heavy_archer","loke_nar_rim")
upgrade(troops,"rhun_militia","rhun_infantry")
upgrade2(troops,"rhun_infantry","rhun_heavy_infantry","rhun_heavy_halberdier")
upgrade(troops,"rhun_heavy_infantry","loke_flag_rim")
upgrade(troops,"rhun_heavy_halberdier","loke_gamp_rim")
upgrade(troops,"rhun_scout","rhun_cavalry")
upgrade2(troops,"rhun_cavalry","balchoth_cavalry","rhun_heavy_cavalry")
upgrade(troops,"balchoth_cavalry","balchoth_elite_cavalry")
upgrade(troops,"rhun_heavy_cavalry","loke_innas_rim")
#BANDITS
upgrade(troops,"tribal_orc","tribal_orc_warrior")
upgrade(troops,"tribal_orc_warrior","tribal_orc_chief")


