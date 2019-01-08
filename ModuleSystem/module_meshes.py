from header_meshes import *
from module_info import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [#(set_background_mesh, "mesh_ui_default_menu_window"),
  ("ui_default_menu_window", 0, "ui_default_menu_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
# ("pic_bandits",            0, "pic_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("pic_mb_warrior_1",       0, "pic_mb_warrior_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("relief01",               0, "relief01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_tribal_orcs",       0, "draw_tribal_orcs", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_orc_raiders",       0, "draw_orc_raiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_wild_troll",        0, "draw_wild_troll", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_fangorn",           0, "draw_fangorn", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_fangorn_orc",       0, "draw_fangorn_orc", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_ent_attack",        0, "draw_ent_attack", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_ent_attack_orc",    0, "draw_ent_attack_orc", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_entdrink_human",    0, "draw_entdrink_human", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_orc",       0, "draw_victory_orc", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_uruk",      0, "draw_victory_uruk", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_dwarf",     0, "draw_victory_dwarf", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_defeat_human",      0, "draw_defeat_human", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_defeat_orc",        0, "draw_defeat_orc", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_gondor",    0, "draw_victory_gondor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_rohan",     0, "draw_victory_rohan", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_orc_orc",   0, "draw_victory_orc_orc", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_lorien_arrows",     0, "draw_lorien_arrows", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_spiders",           0, "draw_spiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("town_west_emnet"    , 0, "town_west_emnet", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_dol_guldur"    , 0, "town_dol_guldur", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_isengard"      , 0, "town_isengard", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_minas_tirith"  , 0, "town_minas_tirith", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_morannon"      , 0, "town_morannon", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_edoras"        , 0, "town_edoras", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_pelargir"      , 0, "town_pelargir", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_dol_amroth"    , 0, "town_dol_amroth", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_minas_morgul"  , 0, "town_minas_morgul", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_osgilliath"    , 0, "town_osgilliath", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_thranduils"    , 0, "town_thranduils", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_rivendell_camp", 0, "town_rivendell_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_moria"         , 0, "town_moria", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_hornburg"      , 0, "town_hornburg", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_esgaroth"      , 0, "town_esgaroth", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_caras_galadhon", 0, "town_caras_galadhon", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_beorns_house"  , 0, "town_beorns_house", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_edhellond"     , 0, "town_edhellond", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_erebor"        , 0, "town_erebor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_erech"         , 0, "town_erech", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_calembel"      , 0, "town_ethring", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_harad"         , 0, "town_harad", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_lossarnach"    , 0, "town_lossarnach", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_rhun_north"    , 0, "town_rhun_north", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_henneth_annun" , 0, "town_henneth_annun", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_khand"         , 0, "town_khand", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_rhun"          , 0, "town_rhun", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_goodcamp"      , 0, "town_goodcamp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_evilcamp"      , 0, "town_evilcamp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_cair_andros"   , 0, "town_cair_andros", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("town_gundabad"      , 0, "town_gundabad", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  #("pic_prisoner_man", 0, "pic_prisoner_man", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_prisoner_fem", 0, "pic_prisoner_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_prisoner_wilderness", 0, "pic_prisoner_wilderness", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_siege_sighted", 0, "pic_siege_sighted", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_siege_sighted_fem", 0, "pic_siege_sighted_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_camp", 0, "pic_camp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_payment", 0, "pic_payment", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_escape_1", 0, "pic_escape_1", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_escape_1_fem", 0, "pic_escape_1_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_victory", 0, "pic_victory", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_defeat", 0, "pic_defeat", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_wounded", 0, "pic_wounded", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_wounded_fem", 0, "pic_wounded_fem", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_steppe_bandits", 0, "pic_steppe_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_mountain_bandits", 0, "pic_mountain_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_sea_raiders", 0, "pic_sea_raiders", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_deserters", 0, "pic_deserters", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_forest_bandits", 0, "pic_forest_bandits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_cattle", 0, "pic_cattle", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_looted_village", 0, "pic_looted_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_village_p", 0, "pic_village_p", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_village_s", 0, "pic_village_s", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_village_w", 0, "pic_village_w", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_recruits", 0, "pic_recruits", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_arms_swadian", 0, "pic_arms_swadian", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_arms_vaegir", 0, "pic_arms_vaegir", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_arms_khergit", 0, "pic_arms_khergit", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_arms_nord", 0, "pic_arms_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("pic_arms_rhodok", 0, "pic_arms_rhodok", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("portrait_blend_out", 0, "portrait_blend_out", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_infantry", 0, "flag_infantry", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_archers", 0, "flag_archers", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_cavalry", 0, "flag_cavalry", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("color_picker", 0, "color_picker",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("custom_map_banner_01", 0, "custom_map_banner_01",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_map_banner_02", 0, "custom_map_banner_02",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_map_banner_03", 0, "custom_map_banner_03",  0, 0, 0, -90, 0, 90, 1, 1, 1),
  ("custom_banner_01", 0, "custom_banner_01",  0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("custom_banner_02", 0, "custom_banner_02",  0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("custom_banner_bg", 0, "custom_banner_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg01", 0, "custom_banner_fg01",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg02", 0, "custom_banner_fg02",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg03", 0, "custom_banner_fg03",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg04", 0, "custom_banner_fg04",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg05", 0, "custom_banner_fg05",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg06", 0, "custom_banner_fg06",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg07", 0, "custom_banner_fg07",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg08", 0, "custom_banner_fg08",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg09", 0, "custom_banner_fg09",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg10", 0, "custom_banner_fg10",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg11", 0, "custom_banner_fg11",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg12", 0, "custom_banner_fg12",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg13", 0, "custom_banner_fg13",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg14", 0, "custom_banner_fg14",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg15", 0, "custom_banner_fg15",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg16", 0, "custom_banner_fg16",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg17", 0, "custom_banner_fg17",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg18", 0, "custom_banner_fg18",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg19", 0, "custom_banner_fg19",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg20", 0, "custom_banner_fg20",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg21", 0, "custom_banner_fg21",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg22", 0, "custom_banner_fg22",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_fg23", 0, "custom_banner_fg23",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_01", 0, "custom_banner_charge_01",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_02", 0, "custom_banner_charge_02",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_03", 0, "custom_banner_charge_03",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_04", 0, "custom_banner_charge_04",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_05", 0, "custom_banner_charge_05",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_06", 0, "custom_banner_charge_06",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_07", 0, "custom_banner_charge_07",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_08", 0, "custom_banner_charge_08",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_09", 0, "custom_banner_charge_09",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_10", 0, "custom_banner_charge_10",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_11", 0, "custom_banner_charge_11",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_12", 0, "custom_banner_charge_12",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_13", 0, "custom_banner_charge_13",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_14", 0, "custom_banner_charge_14",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_15", 0, "custom_banner_charge_15",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_16", 0, "custom_banner_charge_16",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_17", 0, "custom_banner_charge_17",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_18", 0, "custom_banner_charge_18",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_19", 0, "custom_banner_charge_19",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_20", 0, "custom_banner_charge_20",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_21", 0, "custom_banner_charge_21",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_22", 0, "custom_banner_charge_22",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_23", 0, "custom_banner_charge_23",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_24", 0, "custom_banner_charge_24",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_25", 0, "custom_banner_charge_25",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_26", 0, "custom_banner_charge_26",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_27", 0, "custom_banner_charge_27",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_28", 0, "custom_banner_charge_28",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_29", 0, "custom_banner_charge_29",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_30", 0, "custom_banner_charge_30",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_31", 0, "custom_banner_charge_31",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_32", 0, "custom_banner_charge_32",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_33", 0, "custom_banner_charge_33",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_34", 0, "custom_banner_charge_34",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_35", 0, "custom_banner_charge_35",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_36", 0, "custom_banner_charge_36",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_37", 0, "custom_banner_charge_37",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_38", 0, "custom_banner_charge_38",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_39", 0, "custom_banner_charge_39",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_40", 0, "custom_banner_charge_40",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_41", 0, "custom_banner_charge_41",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_42", 0, "custom_banner_charge_42",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_43", 0, "custom_banner_charge_43",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_44", 0, "custom_banner_charge_44",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_45", 0, "custom_banner_charge_45",  0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("custom_banner_charge_46", 0, "custom_banner_charge_46",  0, 0, 0, 0, 0, 0, 10, 10, 10),

#TLD begin
  ("tableau_mesh_shield_kite"  , 0, "tableau_mesh_shield_kite"  , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_tower" , 0, "tableau_mesh_shield_tower" , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_square", 0, "tableau_mesh_shield_square", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round" , 0, "tableau_mesh_shield_round" , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_harad" , 0, "tableau_mesh_shield_harad" , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_rohan" , 0, "tableau_mesh_shield_rohan" , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  #TLD end

  ("tableau_mesh_custom_banner", 0, "tableau_mesh_custom_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_square", 0, "tableau_mesh_custom_banner_square", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_tall", 0, "tableau_mesh_custom_banner_tall", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_custom_banner_short", 0, "tableau_mesh_custom_banner_short", 0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("tableau_mesh_shield_round_1",  0, "tableau_mesh_shield_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_2",  0, "tableau_mesh_shield_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_3",  0, "tableau_mesh_shield_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_4",  0, "tableau_mesh_shield_round_4", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_round_5",  0, "tableau_mesh_shield_round_5", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_1",  0, "tableau_mesh_shield_small_round_1", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_2",  0, "tableau_mesh_shield_small_round_2", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_shield_small_round_3",  0, "tableau_mesh_shield_small_round_3", 0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_kite_1",   0, "tableau_mesh_shield_kite_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_kite_2",   0, "tableau_mesh_shield_kite_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_kite_3",   0, "tableau_mesh_shield_kite_3",  0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_kite_4",   0, "tableau_mesh_shield_kite_4",  0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_heater_1", 0, "tableau_mesh_shield_heater_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_heater_2", 0, "tableau_mesh_shield_heater_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_pavise_1", 0, "tableau_mesh_shield_pavise_1",  0, 0, 0, 0, 0, 0, 10, 10, 10),
#  ("tableau_mesh_shield_pavise_2", 0, "tableau_mesh_shield_pavise_2",  0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("heraldic_armor_bg", 0, "heraldic_armor_bg",  0, 0, 0, 0, 0, 0, 10, 10, 10),

#  ("tableau_mesh_heraldic_armor_a", 0, "tableau_mesh_heraldic_armor_a",  0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("tableau_mesh_heraldic_armor_b", 0, "tableau_mesh_heraldic_armor_b",  0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("tableau_mesh_heraldic_armor_c", 0, "tableau_mesh_heraldic_armor_c",  0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("tableau_mesh_heraldic_armor_d", 0, "tableau_mesh_heraldic_armor_d",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("tableau_mesh_heraldic_rohan_armor", 0, "tableau_mesh_heraldic_rohan_armor",  0, 0, 0, 0, 0, 0, 1, 1, 1),

#  ("outer_terrain_plain_1", 0, "ter_border_a", -90, 0, 0, 0, 0, 0, 1, 1, 1),
  ("banner_gondor"  , 0, "b_arms_gondor", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_rohan"   , 0, "b_arms_rohan", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_mordor"  , 0, "b_mordor", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_harad"   , 0, "b_harad", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_khand"   , 0, "b_arms_khand", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_rhun"    , 0, "b_rhun", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_umbar"   , 0, "b_arms_umbar", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_lorien"  , 0, "b_arms_lorien", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_imladris", 0, "b_arms_imladris", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_woodelf" , 0, "b_arms_woodelf", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_moria"   , 0, "b_moria", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_guldur"  , 0, "b_guldur", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_beorn"   , 0, "b_beorn", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_gundabad", 0, "b_gundabad", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_dale"    , 0, "b_arms_dale", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_erebor"  , 0, "b_arms_erebor", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_dunland" , 0, "b_dunland", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_isengard", 0, "b_isengard", 0, 0, 0, -90, 0, 0, 1, 1, 1),

# BCD banners are not used

  ("banner_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
#  ("banner_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),#bad banner. others are better and enough for Rohan lords
  ("banner_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f21", 0, "b_arms_los", 0, 0, 0, -90, 0, 0, 1, 1, 1), # lossarnach
  ("banner_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_esgaroth", 0, "b_arms_esgaroth", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f_end", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),


  ("arms_a01", 0, "b_arms_gondor", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a02", 0, "b_arms_rohan", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a03", 0, "b_mordor", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a04", 0, "b_harad", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a05", 0, "b_arms_khand", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a06", 0, "b_rhun", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a07", 0, "b_arms_umbar", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a08", 0, "b_arms_lorien", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a09", 0, "b_arms_imladris", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a10", 0, "b_arms_woodelf", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a11", 0, "b_moria", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a12", 0, "b_guldur", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a13", 0, "b_beorn", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a14", 0, "b_gundabad", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a15", 0, "b_arms_dale", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a16", 0, "b_arms_erebor", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a17", 0, "b_dunland", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_a19", 0, "b_isengard", 0, 0, 0, -90, 0, 0, 1, 1, 1),

# BCD banners are not used
  ("arms_e01", 0, "banner_e01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e02", 0, "banner_e02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e03", 0, "banner_e03", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e04", 0, "banner_e04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e05", 0, "banner_e05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e06", 0, "banner_e06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e07", 0, "banner_e07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e08", 0, "banner_e08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e09", 0, "banner_e09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e10", 0, "banner_e10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e11", 0, "banner_e11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e12", 0, "banner_e12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e13", 0, "banner_e13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e14", 0, "banner_e14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e15", 0, "banner_e15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e16", 0, "banner_e16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e17", 0, "banner_e17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e18", 0, "banner_e18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e19", 0, "banner_e19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e20", 0, "banner_e20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_e21", 0, "banner_e21", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("arms_f01", 0, "banner_f01", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f02", 0, "banner_f02", 0, 0, 0, -90, 0, 0, 1, 1, 1),
 # ("arms_f03", 0, "banner_f03", 0, 0, 0, -90, 0, 0, 1, 1, 1),#bad banner. others are better and enough for Rohan lords
  ("arms_f04", 0, "banner_f04", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f05", 0, "banner_f05", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f06", 0, "banner_f06", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f07", 0, "banner_f07", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f08", 0, "banner_f08", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f09", 0, "banner_f09", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f10", 0, "banner_f10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f11", 0, "banner_f11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f12", 0, "banner_f12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f13", 0, "banner_f13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f14", 0, "banner_f14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f15", 0, "banner_f15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f16", 0, "banner_f16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f17", 0, "banner_f17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f18", 0, "banner_f18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f19", 0, "banner_f19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f21", 0, "b_arms_los", 0, 0, 0, -90, 0, 0, 1, 1, 1), # lossarnach
  ("arms_f20", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_esgaroth", 0, "b_arms_esgaroth", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("arms_f_end", 0, "banner_f20", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banners_default_a", 0, "banners_default_a", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_b", 0, "banners_default_b", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_c", 0, "banners_default_c", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_d", 0, "banners_default_d", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_e", 0, "banners_default_e", 0, 0, 0, -90, 0, 0, 1, 1, 1),
#### TLD Rhun circular patterns
  ("circular_8mosaic1", 0, "circular_8mosaic1", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic2", 0, "circular_8mosaic2", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic3", 0, "circular_8mosaic3", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic4", 0, "circular_8mosaic4", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic5", 0, "circular_8mosaic5", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic6", 0, "circular_8mosaic6", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic7", 0, "circular_8mosaic7", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic8", 0, "circular_8mosaic8", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic9", 0, "circular_8mosaic9", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("circular_8mosaic10",0, "circular_8mosaic10",0, 0, 0, -90, 0, 0, 1, 1, 1),
#### Far Harad shield paint
  ("far_harad_shield_paint", 0, "harad_tableau_paint_mesh", 0, 0, 0, 0, 0, 0, 10, 10, 10),
#### Civilian clothes tableau
  ("tableau_mesh_gondor_tunic_a",0, "tableau_mesh_gondor_tunic_a", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_gondor_tunic_b",0, "tableau_mesh_gondor_tunic_b", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_rohan_tunic"   ,0, "tableau_mesh_rohan_tunic"   , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_dale_tunic"    ,0, "tableau_mesh_dale_tunic"    , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("tableau_mesh_woodman_tunic" ,0, "tableau_mesh_woodman_tunic" , 0, 0, 0, 0, 0, 0, 10, 10, 10),
#### TLD rohan shield paintings
  ("rohan_paint_1",0, "rohan_paint_mesh_a", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("rohan_paint_2",0, "rohan_paint_mesh_b", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("rohan_paint_3",0, "rohan_paint_mesh_f", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("rohan_paint_4",0, "rohan_paint_mesh_g", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("rohan_paint_5",0, "rohan_paint_mesh_c", 0, 0, 0, 0, 0, 0, 10, 10, 10), # here start paitings suitable for bulb-centered shields
  ("rohan_paint_6",0, "rohan_paint_mesh_d", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("rohan_paint_7",0, "rohan_paint_mesh_e", 0, 0, 0, 0, 0, 0, 10, 10, 10),
### burned map icons
  ("icon_burn_pattern",0, "tableau_mesh_burn_pattern", 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("icon_gondor_town" ,0, "tableau_mesh_gondortown"  , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("icon_castle1"     ,0, "tableau_mesh_iconcastle1" , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("icon_minastirith" ,0, "tableau_mesh_mt"          , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("icon_helmsdeep"   ,0, "tableau_mesh_hd"          , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("icon_dolamroth"   ,0, "tableau_mesh_dolamroth"   , 0, 0, 0, 0, 0, 0, 10, 10, 10),
  ("icon_edoras"      ,0, "tableau_mesh_edoras"      , 0, 0, 0, 0, 0, 0, 10, 10, 10),

### TLD defiled presentation meshes
  ("defiled_customize_bg", 0, "defile_ui_background", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_customize_overlay", 0, "defile_ui_overlay", 0, 0, 0, 0, 0, 0, 1, 1, 1),
### TLD defiled armor backgrounds
  ("defiled_gondor_bg" ,0, "tableau_mesh_gondor" ,  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_rohan_bg" ,0, "tableau_mesh_rohan" ,    0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_dale_bg" ,0, "tableau_mesh_dale" ,      0, 0, 0, 0, 0, 0, 1, 1, 1),
### TLD defiled armor decals
### GONDOR
  ("defiled_gondor_chest1" ,0, "gondor_chest_tear_aa" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_chest2" ,0, "gondor_chest_tear_ab" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_chest3" ,0, "gondor_chest_tear_ac" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_chest4" ,0, "gondor_chest_sauron_eye_a" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_chest5" ,0, "gondor_chest_saruman_hand_a" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_chest6" ,0, "gondor_chest_saruman_rune" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_thigh1" ,0, "gondor_thigh_tear_aa" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_thigh2" ,0, "gondor_thigh_tear_ab" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("defiled_gondor_thigh3" ,0, "gondor_thigh_tear_ac" , 0, 0, 0, 0, 0, 0, 1, 1, 1),
### ROHAN
### DALE

  ]

if wb_compile_switch==1:
  meshes+=[
    #swy-- for the main menu
    ("loading_background",                    0, "ui_default_menu_window",    0, 0, 0, 0, 0, 0, 1, 1, 1),
    ("main_menu_background",                  0, "meeting_window",            0, 0, 0, 0, 0, 0, 1, 1, 1),
    ("main_menu_statue",    render_order_plus_1, "pic_mercenary",             0, 0, 0, 0, 0, 0, 1, 1, 1),

    #swy-- for the escape menu
    ("pic_mb_warrior_1",    render_order_plus_1, "pic_mb_warrior_1",          0, 0, 0, 0, 0, 0, 1, 1, 1),
    ("pic_mb_warrior_2",    render_order_plus_1, "pic_mb_warrior_2",          0, 0, 0, 0, 0, 0, 1, 1, 1),
    ("pic_mb_warrior_3",    render_order_plus_1, "pic_mb_warrior_3",          0, 0, 0, 0, 0, 0, 1, 1, 1),
    ("pic_mb_warrior_4",    render_order_plus_1, "pic_mb_warrior_4",          0, 0, 0, 0, 0, 0, 1, 1, 1),
  ]

#swy-- these ones were missing and we don't want to break the indexing, do we?
meshes+=[
  ("draw_lorien_magic",      0, "draw_lorien_magic",      0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_war_starts",        0, "draw_war_starts",        0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_bear",              0, "draw_bear",              0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_wolf",              0, "draw_wolf",              0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_victory_dunland",   0, "draw_victory_dunland",   0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_khand",     0, "draw_victory_khand",     0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_mountain_goblins",  0, "draw_mountain_goblins",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_corsair_renegades", 0, "draw_corsair_renegades", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_dunland_outcasts",  0, "draw_dunland_outcasts",  0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_entdrink_dwarf",    0, "draw_entdrink_dwarf",    0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_entdrink_orc",      0, "draw_entdrink_orc",      0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_victory_harad",     0, "draw_victory_harad",     0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_rhun",      0, "draw_victory_rhun",      0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_evilman",   0, "draw_victory_evilman",   0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_victory_mirkwood",  0, "draw_victory_mirkwood",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_rivendell", 0, "draw_victory_rivendell", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_victory_beornings", 0, "draw_victory_beornings", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_corsairs",  0, "draw_victory_corsairs",  0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_funeral_pyre",      0, "draw_funeral_pyre",      0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_mound_desecrated",  0, "draw_mound_desecrated",  0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_mound_visit",       0, "draw_mound_visit",       0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_troublesome_goblins", 0, "draw_troublesome_goblins", 0, 0, 0, 0, 0, 0, 1, 1, 1),

# Kham - Troop Presentation dupes
  ("tp_victory_gondor",      0, "draw_victory_gondor",    0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_dwarf",       0, "draw_victory_dwarf",     0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_rohan",       0, "draw_victory_rohan",     0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_evilman",     0, "draw_victory_evilman",   0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_uruk",        0, "draw_victory_uruk",      0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_lorien_arrows",       0, "draw_victory_lorien",    0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_rivendell",   0, "draw_victory_rivendell", 0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_mirkwood",    0, "draw_victory_mirkwood",  0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_war_starts",          0, "draw_victory_dale",      0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_harad",       0, "draw_victory_harad",     0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_rhun",        0, "draw_victory_rhun",      0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_khand",       0, "draw_victory_khand",     0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_corsairs",    0, "draw_victory_corsairs",  0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_orc_orc",     0, "draw_victory_orc_orc",   0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_tribal_orcs",         0, "draw_tribal_orcs",       0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_orc_raiders",         0, "draw_orc_raiders",       0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_dunland",     0, "draw_victory_dunland",   0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("tp_victory_beornings",   0, "draw_victory_beornings", 0, 0, 0, 0, 0, 0, 3, 3, 3),
  ("mp_inventory_choose",    0, "mp_inventory_choose",    0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("inv_slot",               0, "inv_slot",               0, 0, 0, 0, 0, 0, 1, 1, 1),
# Kham - Troop Presentation dupes end
# Add new meshes here
  ("draw_lumberjack_orcs",   0, "draw_lumberjack_orcs",   0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_mound_kneel",       0, "draw_mound_kneel",       0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_ring_hunters_army", 0, "draw_ring_hunters_army", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_ring_hunters_lair", 0, "draw_ring_hunters_lair", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("draw_victory_dale",      0, "draw_victory_dale",      0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("draw_victory_lorien",    0, "draw_victory_lorien",    0, 0, 0, 0, 0, 0, 1, 1, 1),
  
###VC presentations
    ("pic_troop_trees", 0, "town_goodcamp", 0, 0, 0, 0, 0, 0, 1, 1, 1),
    ("pic_units_details", 0, "town_goodcamp", 0, 0, 0, 0, 0, 0, 1, 1, 1),

("cb_ui_main", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),
("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
]
