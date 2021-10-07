"""A class for calculating encounter difficulty.

The class is initialised with two lists; one representing party levels 
as numbers and the other for monster challenge ratings as strings. 

The class has four methods; get_thresholds; get_xp; modifiy_xp; calculate 
difficulty and calculate. The first three are used by the fourth to 
calculate an encounter's difficulty.

The class's __str__ method returns passing the instance's party and monster
attributes through calculate_difficulty. 
"""

from Data import encounter_multipliers_df, stats_by_cr_df, xp_df

class CRCalculator:
    """Class that calculates encounter difficulty for given levels and CRs.
    
    Attributes:
        party (lst): List of ints of the party's character levels
        monsters (lst): List of strings of monster's challenge ratings"""

    def __init__(self, party, monsters):
        """Initialise the CRCalc instance.

        Args:
            party (lst): List of ints of the party's character levels
            monsters (lst): List of strings of monster's challenge ratings"""

        self.party = party
        self.monsters = monsters


    def __str__(self):
        """Return calculate_difficulty called on the instance's attributes."""
        return self.calculate_difficulty(self.party, self.monsters)


    def get_thresholds(self, levels):
        """Return a list of xp thresholds from easy to deadly from list of levels.

        Args:
            levels (lst): A list of numbers for a party and their character levels
        
        Returns:
            list:  Total easy, medium, hard and deadly xp thresholds for party
        """
        easy = 0
        medium = 0
        hard = 0
        deadly = 0

        for level in levels:

            easy += xp_df.at[level, "easy"]
            medium += xp_df.at[level, "medium"]
            hard += xp_df.at[level, "hard"]
            deadly += xp_df.at[level, "deadly"]
        
        return [easy, medium, hard, deadly]


    def get_xp(self, challenge_ratings):
        """Return the total xp value of given list of challenge ratings.
        
        Args:
            challenge_ratings (lst): List of strings of monster challenge ratings
        
        Returns:
            total: Int of combined experience point value of challenge ratings
        """
        total = 0

        for challenge_rating in challenge_ratings:
            total += stats_by_cr_df.at[challenge_rating, 'XP']
        
        return total


    def modify_xp(self, experience_points, party, monsters):
        """Return modified xp value for given nimber of monsters and party.
        
        Args:
            experience_points (int): Combined xp value of each monster's cr
            party (int): Total number of player characters
            monsters (int): Total number of monsters and npcs
        
        Returns:
            int: xp multiplied by a value based on the number of combatants
        """

        if monsters < 15:

            if party < 3:
                return int(experience_points * encounter_multipliers_df.at[monsters, '<3'])
            
            elif party in range(3, 5):
                return int(experience_points * encounter_multipliers_df.at[monsters, '3-5'])
            
            else:
                return int(experience_points * encounter_multipliers_df.at[monsters, '>=6'])
        
        else:

            if party < 3:
                return int(experience_points * encounter_multipliers_df.at[15, '<3'])
            
            elif party in range(3, 5):
                return int(experience_points * encounter_multipliers_df.at[15, '3-5'])
            
            else:
                return int(experience_points * encounter_multipliers_df.at[15, '>=6'])


    def calculate_difficulty(self, party, monsters):
        """Return a string outling xp values and cr of an encounter.
        
        Args:
            party (lst): A list of player character levels for a party as ints
            monster (lst): A list of monster challenge ratings as strings
        
        Attributes:
            party (lst): get_thresholds and len are called on the list
            monsters (lst): get_xp and len are called on the list

        Returns:
            string: Encounter difficulty summarised with xp totals and thresholds
        """
        levels = self.get_thresholds(party)
        challenge_ratings = self.get_xp(monsters)
        num_party = len(party)
        num_monsters = len(monsters)
        modded_xp = self.modify_xp(challenge_ratings, num_party, num_monsters)
        difficulty = ""

        if modded_xp < levels[1]:
            difficulty = "Easy"
        
        elif modded_xp < levels[2]:
            difficulty = "Medium"
        
        elif modded_xp < levels[3]:
            difficulty = "Hard"
        
        else:
            difficulty = "Deadly"

        thresholds_string = f"Easy: {levels[0]}\tMedium: {levels[1]}\tHard: {levels[2]}\tDeadly: {levels[3]}"
        xp_string = f"Total XP: {challenge_ratings}\tPer PC: {int(challenge_ratings / num_party)}\tModified XP: {modded_xp} ({difficulty})"

        return thresholds_string + "\n" + xp_string


