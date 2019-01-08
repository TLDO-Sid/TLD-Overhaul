from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.1),("deserters", -0.1),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], [], 0x474745),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], [], 0x474745),
  ("outlaws","Savages and Bandits", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x474745),
# Factions before this point are hardwired into the game end their order should not be changed.
#
##TLD FACTIONS BEGIN##########
  ("gondor",    "Gondor",                0,0.5,[                ("rohan", 0.2),("lorien", 0.5),("imladris", 0.5),("woodelf", 0.5),("mordor",-0.5),("harad",-0.5),("rhun",-0.5),("khand",-0.5),("dunland",-0.5),("umbar",-0.5),("isengard",-0.5),("moria",-0.5),("guldur",-0.5),("gundabad",-0.5),("dale", 0.2),("dwarf", 0.2),("beorn", 0.2),("tribal_orcs",-0.5),("outlaws",-0.15),("player_faction", 0.20)], [], 0xEEF7ED),
  ("dwarf",     "Erebor",                0,0.5,[("gondor", 0.2),("rohan", 0.2),("lorien", 0.1),("imladris", 0.1),("woodelf", 0.1),("mordor",-0.2),("harad",-0.1),("rhun",-0.1),("khand",-0.1),("dunland",-0.1),("umbar",-0.1),("isengard",-0.1),("moria",-0.5),("guldur",-0.5),("gundabad",-0.5),("dale", 0.5),               ("beorn", 0.2),("tribal_orcs",-0.5),("outlaws",-0.05)                         ], [], 0xEBF0DD),
  ("rohan",     "Rohan",                 0,0.5,[("gondor", 0.2),               ("lorien", 0.1),("imladris", 0.1),("woodelf", 0.1),("mordor",-0.5),("harad",-0.5),("rhun",-0.5),("khand",-0.5),("dunland",-0.5),("umbar",-0.5),("isengard",-0.5),("moria",-0.5),("guldur",-0.5),("gundabad",-0.5),("dale", 0.5),("dwarf", 0.2),("beorn", 0.2),("tribal_orcs",-0.5),("outlaws",-0.15),("player_faction", 0.20)], [], 0x67B938),
  ("mordor",    "Mordor",                0,0.5,[("gondor",-0.5),("rohan",-0.2),("lorien",-0.2),("imladris",-0.2),("woodelf",-0.2),                ("harad", 0.5),("rhun", 0.2),("khand", 0.2),("dunland", 0.2),("umbar", 0.5),("isengard", 0.2),("moria", 0.5),("guldur", 0.5),("gundabad", 0.5),("dale",-0.2),("dwarf",-0.2),("beorn",-0.2),("tribal_orcs",-0.5),                  ("player_faction",-0.15)], [], 0xDE0000),
  ("isengard",  "Isengard",              0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.1),("imladris",-0.1),("woodelf",-0.1),("mordor", 0.2),("harad", 0.1),("rhun", 0.5),("khand", 0.5),("dunland", 0.5),("umbar", 0.5),                  ("moria", 0.5),("guldur", 0.5),("gundabad", 0.5),("dale",-0.2),("dwarf",-0.2),("beorn",-0.2),("tribal_orcs",-0.5),                  ("player_faction",-0.15)], [], 0x808080),
  ("lorien",    "Lothlorien",            0,0.5,[("gondor", 0.5),("rohan", 0.2),                ("imladris", 0.5),("woodelf", 0.5),("mordor",-0.2),("harad",-0.1),("rhun",-0.5),("khand",-0.1),("dunland",-0.1),("umbar",-0.1),("isengard",-0.1),("moria",-0.5),("guldur",-0.5),("gundabad",-0.5),("dale", 0.2),("dwarf", 0.1),("beorn", 0.2),("tribal_orcs",-0.5)                                           ], [], 0xA5F24D),
  ("imladris",  "Imladris",              0,0.5,[("gondor", 0.5),("rohan", 0.2),("lorien", 0.5),                  ("woodelf", 0.5),("mordor",-0.2),("harad",-0.1),("rhun",-0.1),("khand",-0.1),("dunland",-0.1),("umbar",-0.1),("isengard",-0.1),("moria",-0.5),("guldur",-0.5),("gundabad",-0.5),("dale", 0.2),("dwarf", 0.1),("beorn", 0.2),("tribal_orcs",-0.5),("outlaws",-0.05)                         ], [], 0x4A4AC6),
  ("woodelf",   "Woodland Realm",        0,0.5,[("gondor", 0.5),("rohan", 0.2),("lorien", 0.5),("imladris", 0.5),                 ("mordor",-0.2),("harad",-0.1),("rhun",-0.1),("khand",-0.1),("dunland",-0.1),("umbar",-0.1),("isengard",-0.1),("moria",-0.5),("guldur",-0.9),("gundabad",-0.5),("dale", 0.1),("dwarf", 0.1),("beorn", 0.2),("tribal_orcs",-0.5),("outlaws",-0.05)                         ], [], 0x168C11),
  ("dale",      "Dale",                  0,0.5,[("gondor", 0.2),("rohan", 0.5),("lorien", 0.5),("imladris", 0.5),("woodelf", 0.5),("mordor",-0.5),("harad",-0.5),("rhun",-0.5),("khand",-0.5),("dunland",-0.5),("umbar",-0.5),("isengard",-0.5),("moria",-0.5),("guldur",-0.5),("gundabad",-0.5),              ("dwarf", 0.5),("beorn", 0.2),("tribal_orcs",-0.5),("outlaws",-0.05)                         ], [], 0x4973D7),
  ("harad",     "Harad",                 0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.1),("imladris",-0.1),("woodelf",-0.1),("mordor", 0.5),               ("rhun", 0.5),("khand", 0.5),("dunland", 0.5),("umbar", 0.5),("isengard", 0.5),("moria", 0.5),("guldur", 0.5),("gundabad", 0.5),("dale",-0.2),("dwarf",-0.2),("beorn",-0.2),("tribal_orcs",-0.5)                                           ], [], 0xE73C1E),
  ("rhun",      "Rhun",                  0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.1),("imladris",-0.1),("woodelf",-0.1),("mordor", 0.2),("harad", 0.1),              ("khand", 0.5),("dunland", 0.1),("umbar", 0.5),("isengard", 0.5),("moria", 0.5),("guldur", 0.5),("gundabad", 0.5),("dale",-0.7),("dwarf",-0.7),("beorn",-0.2),("tribal_orcs",-0.5)                                           ], [], 0xFF7521),
  ("khand",     "Khand",                 0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.1),("imladris",-0.1),("woodelf",-0.1),("mordor", 0.2),("harad", 0.1),("rhun", 0.5),               ("dunland", 0.1),("umbar", 0.5),("isengard", 0.5),("moria", 0.5),("guldur", 0.5),("gundabad", 0.5),("dale",-0.5),("dwarf",-0.5),("beorn",-0.5),("tribal_orcs",-0.5)                                           ], [], 0xF081C2),
  ("umbar",     "Umbar",                 0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.5),("imladris",-0.5),("woodelf",-0.5),("mordor", 0.5),("harad", 0.5),("rhun", 0.5),("khand", 0.5),("dunland", 0.5),               ("isengard", 0.5),("moria", 0.5),("guldur", 0.5),("gundabad", 0.5),("dale",-0.2),("dwarf",-0.2),("beorn",-0.2),("tribal_orcs",-0.5)                                           ], [], 0x9B42BA),
  ("moria","Orcs of the Misty Mountains",0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.5),("imladris",-0.5),("woodelf",-0.5),("mordor", 0.5),("harad", 0.5),("rhun", 0.5),("khand", 0.5),("dunland", 0.5),("umbar", 0.5),("isengard", 0.5),               ("guldur", 0.5),("gundabad", 0.5),("dale",-0.2),("dwarf",-0.2),("beorn",-0.2),("tribal_orcs",-0.5)                                           ], [], 0x865E39),
  ("guldur",    "Dol Guldur",            0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.5),("imladris",-0.5),("woodelf",-0.5),("mordor", 0.5),("harad", 0.5),("rhun", 0.5),("khand", 0.5),("dunland", 0.5),("umbar", 0.5),("isengard", 0.5),("moria", 0.5),                ("gundabad", 0.5),("dale",-0.5),("dwarf",-0.5),("beorn",-0.5),("tribal_orcs",-0.5)                                           ], [], 0xDE0000),
  ("gundabad",  "Orcs of Gundabad",      0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.5),("imladris",-0.5),("woodelf",-0.5),("mordor", 0.5),("harad", 0.5),("rhun", 0.5),("khand", 0.5),("dunland", 0.5),("umbar", 0.5),("isengard", 0.5),("moria", 0.5),("guldur", 0.5),                  ("dale",-0.5),("dwarf",-0.5),("beorn",-0.5),("tribal_orcs",-0.5)                                           ], [], 0x71813C),
  ("dunland",   "Dunland",               0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.1),("imladris",-0.1),("woodelf",-0.1),("mordor", 0.5),("harad", 0.5),("rhun", 0.5),("khand", 0.5),                 ("umbar", 0.5),("isengard", 0.5),("moria", 0.5),("guldur", 0.5),("gundabad", 0.5),("dale",-0.2),("dwarf",-0.2),("beorn",-0.2),("tribal_orcs",-0.5)                                           ], [], 0x99544A),
  ("beorn",     "Anduin Vale",           0,0.5,[("gondor", 0.2),("rohan", 0.2),("lorien", 0.5),("imladris", 0.5),("woodelf", 0.5),("mordor",-0.2),("harad",-0.5),("rhun",-0.5),("khand",-0.5),("dunland",-0.5),("umbar",-0.5),("isengard",-0.5),("moria",-0.5),("guldur",-0.5),("gundabad",-0.5),("dale", 0.5),("dwarf", 0.5),               ("tribal_orcs",-0.5),("outlaws",-0.05)                         ], [], 0x00A16B),
  
  ("kingdoms_end","kingdoms_end",0,0,[],[], 0x474745),
  ("player_supporters_faction","Player Faction",0, 0.9, [("player_faction",1.00),("outlaws",-0.1),("deserters", -0.02),("mountain_bandits", -0.1),("forest_bandits", -0.05)], [], 0x474745),
  ("player_faction","Player Faction",0, 0.9, [("mordor",-0.6),("gondor",0.1)], [], 0x474745),
  ("brigands",   "Brigands",   0,0.5,[("gondor", 0  ),("rohan", 0  ),("lorien", 0  ),("imladris", 0  ),                 ("mordor", 0  ),("harad", 0  ),("rhun", 0  ),("khand", 0  ),("dunland", 0   ),("umbar", 0 ),("isengard", 0  ),("moria", 0  ),("guldur", 0  ),("gundabad", 0),("dale", 0  ),("tribal_orcs",-0.5)], [], 0x474745),
  ("tribal_orcs","Tribal Orcs",0,0.5,[("gondor",-0.5),("rohan",-0.5),("lorien",-0.5),("imladris",-0.5),("woodelf",-0.5),("mordor",-0.5),("harad",-0.5),("rhun",-0.5),("khand",-0.5),("dunland",-0.5),("umbar",-0.5),("isengard",-0.5),("moria",-0.5),("guldur",-0.5),                ("dale",-0.5),], [], 0x474745),
##TLD FACTIONS END##########

  ("neutral","ruins",ff_always_hide_label, 0.1,[("player_faction",0.0)], [], 0x474745),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], [], 0x474745),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], [], 0x474745),
#########################
#TLD UNCOMMENTED
##########################
  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], [], 0x474745),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x474745),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x474745),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x474745),

#  ("noble_refugees","Noble Refugees", 0, 0.5,[], []),

  ("mission_companion_1" ,"_", 0, 0.5,[], [], 0x474745), # mission companion arrays
  ("mission_companion_2" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_3" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_4" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_5" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_6" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_7" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_8" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_9" ,"_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_10","_", 0, 0.5,[], [], 0x474745),
  ("mission_companion_11","_", 0, 0.5,[], [], 0x474745),
]
