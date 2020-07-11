# Gem Sorting Machine 
### Based on Image Processing and powered by Artificial Intelligence.

**Aim -** To replicate a small scale machine that can differentiate similar objects using image recognition. In this particular case, colour detection.

# DESCRIPTION
Colour sorters are highly usable in big industries for separating items according to their colour and in filtering the things which do not fall within the acceptable criteria or which are desired by the user. Similarly, gem sorting machine is highly functional on a smaller scale. Using image recognition, the particular colour of multi-coloured gems can be detected with a great user interface.

# WORKING
The main software which is a Python application clicks a picture and crops it to the specific size of a gem as per it’s needs. The colour of the gem is extracted and is converted into the RGB format. After sending the information to the neural network, the exact colour is determined which is provided to the GUI. The main loop informs the Arduino through serial communication, ultimately dropping the gem in the assigned box according to the output of the software.

# Running the Application
1. Clone the whole repository.
2. Set up Oracle's MySQL -> Run all the SQL Scripts In MySQL Workbench from the folder "MySQL Scripts" in order to get the database for the application.
3. Set up JetBrain's PyCharm -> Open the project in PyCharm and create a Virtual Python Environment with all dependencies.
4. Trigger the main function of file "\_Main\_.py".

# Technical Dependencies
- Operating System – RedHat Fedora 30 (Linux).
- Languages – Python3, C/C++, SQL.
- Database – MySQL.
- Software used – JetBrain’s PyCharm, Oracle’s MySQL, PAGE.
- Dependencies – OpenCV, SerialCommunication, SciPy, NumPy, Tkinter, MySQL.

# For more details, refer to
1. [Project Report](https://github.com/AvGeekGupta/Gems-Seperator/blob/master/Documents/Project%20Report.pdf)
2. [Project Architecture](https://github.com/AvGeekGupta/Gems-Seperator/blob/master/Documents/Project%20Architecture.pdf)
3. [Project Presentation](https://github.com/AvGeekGupta/Gems-Seperator/blob/master/Documents/Presentation.pdf)
4. [Project Poster](https://github.com/AvGeekGupta/Gems-Seperator/blob/master/Documents/Poster.png)

# OWNERS
- [Utkarsh Gupta](https://www.linkedin.com/in/avgeekgupta/)
- [Vanshaj Goel](https://www.linkedin.com/in/vanshaj-goel-593833163/)
- [Tanya Malhotra](https://www.linkedin.com/in/tanya-malhotra-0999001a9/)
