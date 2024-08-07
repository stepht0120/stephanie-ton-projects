from tkinter import Tk, Frame, simpledialog, messagebox, Label, Button
from button import ImageButtonApp  
from PIL import ImageTk, Image

class WaterCalculator:
    """
    Water Calculator Class: calculates the user's suggested daily water intake by finding the BMR (Basal Metabolic Rate)
    and the TDEE (Total Daily Energy Expenditure)
    """
    def __init__(self):
        self.bmr = None
        self.TDEE = None
        self.water_goal = None
        self.get_user_input()

    def get_user_input(self):
        """
        gets the user inputs on age, sex, weight, height, and activity level
        """
        self.age = simpledialog.askinteger("Input", "Enter your age:")
        self.sex = simpledialog.askstring("Input", "Enter your sex (m/f):").lower()
        self.weight = simpledialog.askfloat("Input", "Enter your weight in pounds:")
        self.height = simpledialog.askfloat("Input", "Enter your height in inches:")
        self.activity_level = simpledialog.askinteger("Input", "Enter your activity level from 1-5. 5 is very active. 1 is inactive:")
        self.calculate_goals()

    def calculate_goals(self):
        """
        calculates the BMR (Basal Metabolic Rate) and the TDEE (Total Daily Energy Expenditure)
        based on the BMR and the TDEE, it sets the suggested daily amount of water the user should drink in ounces
        shows a message box with how much the suggested daily water intake is for the user
        """
        self.calc_BMR()  # Calculate BMR
        self.adjust_for_activity_level()  # Adjust BMR based on activity level
        self.water_goal = self.final_intake()  # Now set the water goal
        messagebox.showinfo("Daily Water Goal", f"Your daily water intake goal is {self.water_goal:.2f} ounces.")

    def calc_BMR(self):
        """
        calculates the BMR (Basal Metabolic Rate) based on weight, height, and age
        the if statements differenate the formula based on sex

        returns:
            bmr (int): the result of the Basal Metabolic Rate formula based on the sex

        raises:
            ValueError: for invalid input for sex (has to be "m" or "f")
        """

        # conditionals to differenate the BMR (Basal Metabolic Rate) based on the user's sex
        # if the user input is "m" for male
        if self.sex == "m":
            self.bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        # if the user input is "f" for female
        elif self.sex == "f":
            self.bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        # if the user input is invalid
        else:
            raise ValueError("Invalid value for 'sex'. Please use 'm' or 'f'.")
        
        return self.bmr

    def adjust_for_activity_level(self):
        """
        adjusts the TDEE (Total Daily Energy Expenditure) based on the daily activity level entered

        returns:
            TDEE (int): Total Daily Energy Expenditure based on BMR (Basal Metabolic Rate) and activity level
        
        raises:
            ValueError: for invalid input for activity level (has to be an integer in between 1 to 5)

        """
        # the dictionary of activity level multiplers based on user's input from 1 to 5
        activity_multipliers = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}

        # if statement to multiply the TDEE (Total Daily Energy Expenditure) based on user's activty level input 
        if self.activity_level in activity_multipliers:
            self.TDEE = self.bmr * activity_multipliers[self.activity_level]
        # if the user input is invalid
        else:
            raise ValueError("Invalid value for 'activity_level'. Please use values 1-5.")
        
        return self.TDEE

    def final_intake(self):
        """
        calculates the user's suggested daily water intake in ounces based on the TDEE (Total Daily Energy Expenditure)

        returns:
            water_intake_goal_oz (int): the user's suggested daily water intake in ounces

        """
        water_intake_goal_oz = self.TDEE * 0.03
        return water_intake_goal_oz

class WaterTracker(WaterCalculator):
    """ Class tracking the water intake of the user"""
    def __init__(self):
        """Initializing the Water Tracker Class"""
        super().__init__()
        self.user_water_intake = 0

    def check_water_intake(self, user_water_intake):
        """Method tracking the user's water intake, calculating the percentage, and returning it
            Args:
                user_water_intake: the amount of water the user has drunk so far
            Returns:
                the percentage of the user's water intake goal that they have drunk so far"""
        self.user_water_intake += user_water_intake
        percentage = (self.user_water_intake / self.water_goal) * 100
        return percentage

class BenchmarkFrame(Frame):
    """Class representing a frame in the benchmarks"""
    def __init__(self, parent, water_tracker, index):
        """Initializes the Benchmark Frame Class
            Args:
                parent: represents the parent widget
                water_tracker: instance of water tracker class
                index: index of the benchmark # """
        super().__init__(parent)
        self.parent = parent
        self.water_tracker = water_tracker
        self.index = index

        # Button to record water intake
        self.drink_button = Button(self, text="I Drank Water", command=self.drink_water)
        self.drink_button.pack()

    def drink_water(self):
        """Provides pop up for user water intake input, and gets the appropriate frame"""
        user_water_intake = simpledialog.askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        if user_water_intake:
            percentage = self.water_tracker.check_water_intake(user_water_intake)
            self.parent.update_image(percentage)


class MainPage(Tk):
    """Main Page for the Water Tracker"""
    def __init__(self, *args, **kwargs):
        """inititalizes the Main page Class
            Args:
                *args: any number of positional arguments
                **kwargs: any number of keyword arguments
            """
        super().__init__(*args, **kwargs)
        self.title("Water Intake Tracker")
        self.water_tracker = WaterTracker()
        #creates instance of ImageButtonApp with image paths
        self.image_paths = ['0%.png', '10%.png', '20%.png', '30%.png', '40%.png', '50%.png', '60%.png', '70%.png', '80%.png', '90%.png', '100%.png']
        self.image_button_app = ImageButtonApp(self, self.image_paths, self.drink_water)
        self.image_button_app.grid(row=0, column=0, sticky="nsew")
       
        #creates BenchmarkFrame instances and stores them in a dictionary
        self.frames = {}
        for i in range(11):
            frame = BenchmarkFrame(self, self.water_tracker, i)
            self.frames[f"Benchmark{i}"] = frame
            frame.grid(row=1, column=0, sticky="nsew")
        
        #initializes label with first image
        self.initial_image = ImageTk.PhotoImage(file=self.image_paths[0])
        self.label = Label(self, image=self.initial_image)
        self.label.grid(row=2, column=0, sticky="nsew")
        self.label.image = self.initial_image

    def drink_water(self):
        """handles the I drank button 
            prompts the user to enter the amount of water they have drunk 
            and updates percentage"""
        user_water_intake = simpledialog.askfloat("Enter Water Intake", "Enter the amount of water you drank (in ounces):")
        if user_water_intake:
            percentage = self.water_tracker.check_water_intake(user_water_intake)
            self.update_image(percentage)

    def update_image(self, percentage):
        """Updates image based on percentage
            Args: 
                percentage: the percentage of water the user has drunk towards their goal"""
        index = min(int(percentage // 10), len(self.image_paths) - 1)
        new_image = ImageTk.PhotoImage(file=self.image_paths[index])
        self.label.configure(image=new_image)
        self.label.image = new_image

if __name__ == "__main__":
    main = MainPage()
    main.mainloop()
