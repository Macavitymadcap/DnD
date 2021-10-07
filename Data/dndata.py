# Imports
import pandas as pd

# modifiers - Dictionary of ability score modifiers
modifiers = {
    1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5,
    22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10
}

# xp_df - DataFrame of xp thresholds for calculating encounter difficulty
xp_thresholds = {
    "easy": [25, 50, 75, 125, 250, 300, 350, 450, 550, 600, 800, 1000, 1100, 1250, 1400, 1600, 2000, 2100, 2400, 2800],
    "medium": [50, 100, 150, 250, 500, 600, 750, 900, 1100, 1200, 1600, 2000, 2200, 2500, 2800, 3200, 3900, 4200, 4900, 5700],
    "hard": [75, 150, 225, 375, 750, 900, 1100, 1400, 1600, 1900, 2400, 3000, 3400, 3800, 4300, 4800, 5900, 6300, 7300, 8500],
    "deadly": [100, 200, 400, 500, 1100, 1400, 1700, 2100, 2400, 2800, 3600, 4500, 5100, 5700, 6400, 7200, 8800, 9500, 10900, 12700]
}
xp_df = pd.DataFrame(xp_thresholds, index=[num + 1 for num in range(20)])
xp_df.index.name = "Level"

# stats_by_cr_df - DataFrame containing average stats for monsters by challenge rating
stats_by_cr_df = pd.read_csv('Data/Monster Statistics by CR.csv', index_col='CR', header=0)

# encounter_multipliers_df = DataFrame of encounter multipliers for determining the adjusted xp value of an encounter.
mult_fewer_three = [1.5, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4, 4, 4, 4, 5]
mult_three_five = [1, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4]
mult_six_plus = [0.5, 1, 1.5, 1.5, 1.5, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3]
encounter_multipliers_df = pd.DataFrame(list(zip(mult_fewer_three, mult_three_five, mult_six_plus)), 
                                                 index=[num + 1 for num in range(15)], 
                                                 columns=['<3', '3-5', '>=6'])
encounter_multipliers_df.index.name = 'num'

# exchange_rates_df - DataFame of exchange rates for coinage
exchange_rates_df = pd.read_csv('Data/Exchange Rates.csv', index_col='Coin', header=0)

# beyond_1st_level_df - DataFrame of experience points and proficiency bonuses by level
beyond_1st_level_df = pd.read_csv('Data/Beyond 1st Level.csv', index_col='Level', header=0)

# names_df - From Xanathar's Guide to Everything
names_df = pd.read_csv('Data/Xanathar Names.csv', index_col='d100', header=0)

# wild_magic_df - From Player's Handbook
wild_magic_df = pd.read_csv('Wild Magic Surge.csv', index_col='d100', header=0)

#magic item tables from Dungeon Master's Gude
magic_items_a = pd.read_csv('Data/Magic Item Table A.csv', index_col='d100', header=0)
magic_items_b = pd.read_csv('Data/Magic Item Table B.csv', index_col='d100', header=0)
magic_items_c = pd.read_csv('Data/Magic Item Table C.csv', index_col='d100', header=0)
magic_items_d = pd.read_csv('Data/Magic Item Table D.csv', index_col='d100', header=0)
magic_items_e = pd.read_csv('Data/Magic Item Table E.csv', index_col='d100', header=0)
magic_items_f = pd.read_csv('Data/Magic Item Table F.csv', index_col='d100', header=0)
magic_items_g = pd.read_csv('Data/Magic Item Table G.csv', index_col='d100', header=0)
magic_items_h = pd.read_csv('Data/Magic Item Table H.csv', index_col='d100', header=0)
magic_items_i = pd.read_csv('Data/Magic Item Table I.csv', index_col='d100', header=0)
magic_items_figurines = pd.read_csv('Data/Magic Item Table Figurines.csv', index_col='d8', header=0)
magic_items_armour = pd.read_csv('Data/Magic Item Table Armour.csv', index_col='d12', header=0)

#art object tables, from Dungeon Masters Guide
art_objects_25gp = pd.read_csv('Data/Treasure - 25 gp Art Objects.csv', index_col='d10', header=0)
art_objects_250gp = pd.read_csv('Data/Treasure - 250 gp Art Objects.csv', index_col='d10', header=0)
art_objects_750gp = pd.read_csv('Data/Treasure - 750 gp Art Objects.csv', index_col='d10', header=0)
art_objects_2500gp = pd.read_csv('Data/Treasure - 2500 gp Art Objects.csv', index_col='d10', header=0)
art_objects_7500gp = pd.read_csv('Data/Treasure - 7500 gp Art Objects.csv', index_col='d8', header=0)

#gemstone tables, from Dungeon Master's Guide
gemstones_10gp = pd.read_csv('Data/Treasure - 10 gp Gemstones.csv', index_col='d12', header=0)
gemstones_50gp = pd.read_csv('Data/Treasure - 50 gp Gemstones.csv', index_col='d12', header=0)
gemstones_100gp = pd.read_csv('Data/Treasure - 100 gp Gemstones.csv', index_col='d10', header=0)
gemstones_500gp = pd.read_csv('Data/Treasure - 500 gp Gemstones.csv', index_col='d6', header=0)
gemstones_1000gp = pd.read_csv('Data/Treasure - 1000 gp Gemstones.csv', index_col='d8', header=0)
gemstones_5000gp = pd.read_csv('Data/Treasure - 5000 gp Gemstones.csv', index_col='d4', header=0)

#background tables, from the Player's Handbook
backgrounds_personality_traits = pd.read_csv('Data/Backgrounds - Personality Trait.csv', index_col='d8', header=0)
backgrounds_bonds = pd.read_csv('Data/Backgrounds - Bond.csv', index_col='d6', header=0)
backgrounds_flaws = pd.read_csv('Data/Backgrounds - Flaw.csv', index_col='d6', header=0)
backgrounds_ideals = pd.read_csv('Data/Backgrounds - Ideal.csv', index_col='d6', header=0)
scams = ["I cheat at games of chance.", "I shave coins or forge documents.", 
         "I insinuate myself into people's lives to prey on their weakness and secure their fortunes.", 
         "I put on new identities like clothes.", 
         "I run sleight-of-hand cons on street corners.", 
         "I convince people that worthless junk is worth their hard-earned money."]
charlatan_schemes = pd.DataFrame(scams, index=[num + 1 for num in range(6)])
charlatan_schemes.index.name = "d6"
charlatan_schemes.rename(columns={0: "Schemes"}, inplace=True)

#Class tables, from Player's Handbook
warlock_table = pd.read_csv('Data/Warlock.csv', index_col='Level')
warlock_expanded_spell_list = pd.read_csv('Data/Warlock - Expanded Spell List.csv', index_col='Spell Level', header=0)