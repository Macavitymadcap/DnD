"""A calculator like gui for rolling dice.

The main entry point for the calculator is the roll_query StringVar, which is 
updated to provide a string that can be evaluated to by a roll function from
the dice module to return a die or dice roll.

The interface has an entry widget for roll_query; button widgets for adding
a string to the roll query; button widgets for evaluating the roll query and
returning different types of die roll (advantage/disadvantage, array of die rolls 
with modifier applied to each roll, critical damage of 2 roll multiplied plus or
minus a modifier and an array of ability scores rollled 4d6 minus the lowest die);
and a button widget to clear the roll query."""

from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import Tk

from dice import roll_ability_scores
from dice import roll_advantage
from dice import roll_array
from dice import roll_crit
from dice import roll_disadvantage
from dice import roll_string

def main():
    """Run main loop of GUI to file as script."""
    root.mainloop()


class DiceRoller:
    """Class containing the dice roller GUI."""

    def __init__(self, master):
        """Initialise a DiceRoller instance.

        Args:
            master (func): Tk function to initialise the GUI
        
        Atrributes:
            expression (str): Empty string updated to get roll_query
            roll_query (func): StringVar updated to get expression_field
            expression_field (widget): Entry used to generate roll
            button_1 (widget): Button to add 1 to expression_field
            button_2 (widget): Button to add 2 to expression_field
            button_3 (widget): Button to add 3 to expression_field
            button_4 (widget): Button to add 4 to expression_field
            button_5 (widget): Button to add 5 to expression_field
            button_6 (widget): Button to add 6 to expression_field
            button_7 (widget): Button to add 7 to expression_field
            button_8 (widget): Button to add 8 to expression_field
            button_9 (widget): Button to add 9 to expression_field
            button_0 (widget): Button to add 0 to expression_field
            button_plus (widget): Button to add + to expression_field
            button_divide  (widget): Button to add / to expression_field
            button_minus (widget): Button to add - to expression_field
            button_multiply (widget): Button to add * to expression_field
            button_d4 (widget): Button to add d4 to expression_field
            button_d6 (widget): Button to add d6 to expression_field
            button_d8 (widget): Button to add d8 to expression_field
            button_d10 (widget): Button to add d10 to expression_field
            button_d12 (widget): Button to add d12 to expression_field
            button_d20 (widget): Button to add d20 to expression_field
            button_d100 (widget): Button to add d100 to expression_field
            button_roll (widget): Button to roll expression_field
            button_roll_advan (widget): Button to roll_advantage expression_field
            button_roll_disad (widget): Button to roll_disadvantage expression_field 
            button_roll_array (widget): Button to roll_array expression_field
            button_roll_crit (widget): Button to roll_crit expression_field
            button_roll_scores (widget): Button to roll_ability_scores expresion field
            button_clear (widget): Button to clear expression_field"""
        self.master = master
        self.expression = ""
        self.master.configure(background="#1C2350")
        self.master.title("Dice Roller")
        self.master.geometry("410x383")

        # GUI widgets.
        self.roll_query = StringVar()
        self.expression_field = Entry(self.master, font="piboto 20", justify="right",
                                      textvariable=self.roll_query, fg="white", bg="#1C2350", width=17)
        self.button_1 = Button(self.master, font="piboto 10", text="1", fg="white",
                               bg="#14668C", command=lambda: self.press(1), height=2, width=4)
        self.button_2 = Button(self.master, font="piboto 10", text="2", fg="white",
                               bg="#14668C", command=lambda: self.press(2), height=2, width=4)
        self.button_3 = Button(self.master, font="piboto 10", text="3", fg="white",
                               bg="#14668C", command=lambda: self.press(3), height=2, width=4)
        self.button_4 = Button(self.master, font="piboto 10", text="4", fg="white",
                               bg="#14668C", command=lambda: self.press(4), height=2, width=4)
        self.button_5 = Button(self.master, font="piboto 10", text="5", fg="white",
                               bg="#14668C", command=lambda: self.press(5), height=2, width=4)
        self.button_6 = Button(self.master, font="piboto 10", text="6", fg="white",
                               bg="#14668C", command=lambda: self.press(6), height=2, width=4)
        self.button_7 = Button(self.master, font="piboto 10", text="7", fg="white",
                               bg="#14668C", command=lambda: self.press(7), height=2, width=4)
        self.button_8 = Button(self.master, font="piboto 10", text="8", fg="white",
                               bg="#14668C", command=lambda: self.press(8), height=2, width=4)
        self.button_9 = Button(self.master, font="piboto 10", text="9", fg="white",
                               bg="#14668C", command=lambda: self.press(9), height=2, width=4)
        self.button_0 = Button(self.master, font="piboto 10", text="0", fg="white",
                               bg="#14668C", command=lambda: self.press(0), height=2, width=4)
        self.button_plus = Button(self.master, font="piboto 10", text="+", fg="white",
                                  bg="#62A3B2", command=lambda: self.press("+"), height=2,
                                  width=4)
        self.button_divide = Button(self.master, font="piboto 10", text="/", fg="white",
                                    bg="#62A3B2", command=lambda: self.press("/"), height=2,
                                    width=4)
        self.button_minus = Button(self.master, font="piboto 10", text="-", fg="white",
                                   bg="#62A3B2", command=lambda: self.press("-"), height=2,
                                   width=4)
        self.button_multiply = Button(self.master, font="piboto 10", text="*", fg="white",
                                   bg="#62A3B2", command=lambda: self.press("*"), height=2,
                                   width=4)
        self.button_d4 = Button(self.master, font="piboto 10", text="d4", fg="white",
                                bg="#20819C", command=lambda: self.press("d4"), height=2,
                                width=4)
        self.button_d6 = Button(self.master, font="piboto 10", text="d6", fg="white",
                                bg="#20819C", command=lambda: self.press("d6"), height=2,
                                width=4)
        self.button_d8 = Button(self.master, font="piboto 10", text="d8", fg="white",
                                bg="#20819C", command=lambda: self.press("d8"), height=2,
                                width=4)
        self.button_d10 = Button(self.master, font="piboto 10", text="d10", fg="white",
                                 bg="#20819C", command=lambda: self.press("d10"), height=2,
                                 width=4)
        self.button_d12 = Button(self.master, font="piboto 10", text="d12", fg="white",
                                 bg="#20819C", command=lambda: self.press("d12"), height=2,
                                 width=4)
        self.button_d20 = Button(self.master, font="piboto 10", text="d20", fg="white",
                                 bg="#20819C", command=lambda: self.press("d20"), height=2,
                                 width=4)
        self.button_d100 = Button(self.master, font="piboto 10", text="d100", fg="white",
                                  bg="#20819C", command=lambda: self.press("d100"), height=2,
                                  width=4)
        self.button_roll = Button(self.master, font="piboto 10", text="Roll", fg="white",
                                  bg="#2D3B6B", command=self.roll_press, height=2, width=4)
        self.button_roll_advan = Button(self.master, font="piboto 10", text="Advan",
                                        fg="white", bg="#2D3B6B", command=self.roll_advan_press,
                                        height=2, width=4)
        self.button_roll_disad = Button(self.master, font="piboto 10", text="Disad",
                                        fg="white", bg="#2D3B6B", command=self.roll_disad_press,
                                        height=2, width=4)
        self.button_roll_array = Button(self.master, font="piboto 10", text="Array",
                                        fg="white", bg="#2D3B6B",
                                        command=self.roll_array_press, height=2,
                                        width=4)
        self.button_roll_crit =Button(self.master, font="piboto 10", text="Crit",
                                      fg="white", bg="#2D3B6B", 
                                      command=self.roll_crit_press, height=2,
                                      width=4)
        self.button_roll_scores =Button(self.master, font="piboto 10", text="Scores",
                                      fg="white", bg="#2D3B6B", 
                                      command=self.roll_scores_press, height=2,
                                      width=4)
        self.button_clear = Button(self.master, font="piboto 10", text="Clear", fg="white",
                                   bg="#1C2350", command=self.clear_press, height=2, 
                                   width=20)

        # Position all widgets in GUI.
        self.expression_field.grid(row=0, columnspan=5)
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=2, column=0)
        self.button_4.grid(row=2, column=1)
        self.button_5.grid(row=3, column=0)
        self.button_6.grid(row=3, column=1)
        self.button_7.grid(row=4, column=0)
        self.button_8.grid(row=4, column=1)
        self.button_9.grid(row=5, column=0)
        self.button_0.grid(row=5, column=1)
        self.button_plus.grid(row=4, column=3)
        self.button_divide.grid(row=5, column=2)
        self.button_minus.grid(row=5, column=3)
        self.button_multiply.grid(row=6, column=3)
        self.button_d4.grid(row=1, column=2)
        self.button_d6.grid(row=1, column=3)
        self.button_d8.grid(row=2, column=2)
        self.button_d10.grid(row=2, column=3)
        self.button_d12.grid(row=3, column=2)
        self.button_d20.grid(row=3, column=3)
        self.button_d100.grid(row=4, column=2)
        self.button_roll.grid(row=1, column=4)
        self.button_roll_advan.grid(row=2, column=4)
        self.button_roll_disad.grid(row=3, column=4)
        self.button_roll_array.grid(row=4, column=4)
        self.button_roll_crit.grid(row=5, column=4)
        self.button_roll_scores.grid(row=6, column=4)
        self.button_clear.grid(row=6, column=0, columnspan=3)

    def press(self, but):
        """Add a string to the expression_field.

        Args:
            but(str): String to be added to the expression_field
        
        Returns:
            expression_field: Updatied with added string
        """
        self.expression += str(but)
        self.roll_query.set(self.expression)


    def roll_press(self):
        """Set expression_field passed as string to dice.roll."""
        try:
            total = roll_string(self.expression)
            self.roll_query.set(total)
            self.expression = ""

        except:
            self.roll_query.set("Roll: dx|xdx +|/|-|* x")
            self.expression = ""


    def roll_advan_press(self):
        """Set expression_field passed as string to dice.roll_advantage."""
        try:
            total = roll_advantage(self.expression)
            self.roll_query.set(total)
            self.expression = ""

        except:
            self.roll_query.set("Roll: dx|xdx +|- x")
            self.expression = ""


    def roll_disad_press(self):
        """Set expression_field passed as string to dice.roll_disadvantage."""
        try:
            total = roll_disadvantage(self.expression)
            self.roll_query.set(total)
            self.expression = ""

        except:
            self.roll_query.set("Roll: dx|xdx +|- x")
            self.expression = ""


    def roll_array_press(self):
        """Set expression_field passed as string to dice.roll_array."""
        try:
            total = roll_array(self.expression)
            self.roll_query.set(total)
            self.expression = ""

        except:
            self.roll_query.set("Roll: xdx +|- x")
            self.expression = ""


    def roll_crit_press(self):
        """Set expression_field passed as string to dice.roll_crit."""
        try:
            if "+" in self.expression:
                dice = self.expression[:self.expression.index("+")]
                modifier = self.expression[self.expression.index("+"):]
                total = roll_crit(dice, modifier)
                self.roll_query.set(total)
                self.expression = ""
            
            elif "-" in self.expression:
                dice = self.expression[:self.expression.index("-")]
                modifier = self.expression[self.expression.index("-"):]
                total = roll_crit(dice, modifier)
                self.roll_query.set(total)
                self.expression = ""
            
            else:
                total = roll_crit(self.expression, "+0")
                self.roll_query.set(total)
                self.expression = ""
        
        except:
            self.roll_query.set("Roll: xdx +|- x")
            self.expression = ""


    def roll_scores_press(self):
        """Set expresion field to call to roll_ability_scores."""
        self.roll_query.set(roll_ability_scores())
        self.expression = ""


    def clear_press(self):
        """Set expression_field as empty string."""
        self.expression = ""
        self.roll_query.set("")


# Run script.
if __name__ == "__main__":
    root = Tk()
    calculator = DiceRoller(root)
    main()