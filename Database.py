# File Name - Database.py
# Created by Vanshaj Goel
#########################


import numpy as numpy
import mysql.connector
from mysql.connector import Error
from datetime import datetime


class Database:
    def __init__(self):
        self.username = ''
        decision = 'y'
        while decision == 'y':
            decision = 'n'
            try:
                self.connection = mysql.connector.connect(host='localhost',
                                                          port='3306',
                                                          database='synaptic_weights',
                                                          user='application',
                                                          password='PyApp@3RGB')

            except Error as error_message:
                print("Error while connecting to MySQL", error_message, "\n")
                decision = input("Do you want to retry? [y/n] : ")
        self.cursor = self.connection.cursor()

    def get_synaptic_weights(self, colour):
        self.cursor.execute("USE `synaptic_weights`;")
        self.cursor.execute("SELECT `red_component` FROM `" + colour + "` " +
                            "WHERE `S_No` = (SELECT MAX(S_No) FROM `" + colour + "`);")
        red_component = self.cursor.fetchone()
        self.cursor.execute("SELECT `green_component` FROM `" + colour + "` " +
                            "WHERE `S_No` = (SELECT MAX(S_No) FROM `" + colour + "`);")
        green_component = self.cursor.fetchone()
        self.cursor.execute("SELECT `blue_component` FROM `" + colour + "` " +
                            "WHERE `S_No` = (SELECT MAX(S_No) FROM `" + colour + "`);")
        blue_component = self.cursor.fetchone()
        return numpy.array([red_component[0], green_component[0], blue_component[0]])

    def user_login_verification(self, user_name, password):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='synaptic_weights',
                                                  user='application',
                                                  password='PyApp@3RGB')
        self.cursor = self.connection.cursor()
        self.cursor.execute("USE `users`;")
        self.cursor.execute("SELECT `s_no`, `name` FROM `user_details` WHERE '" + user_name +
                            "' = `username` " + "AND '" + password + "' = `password`;")
        result = self.cursor.fetchone()
        if result:
            self.username = result[1]
            return 1
        else:
            return 0

    def get_name(self):
        return self.username

    def writecolor(self, colour_code, colour):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='colour_data',
                                                  user='application',
                                                  password='PyApp@3RGB')
        self.cursor = self.connection.cursor()
        if colour == 1:
            self.cursor.execute("INSERT INTO `colour_data`.`blue` (`red_component`, `blue_component`," +
                                " `green_component`) VALUES ('" + str(colour_code[0][0]) + "', '" +
                                str(colour_code[1][0]) + "', '" + str(colour_code[2][0]) + "');")
        elif colour == 2:
            self.cursor.execute("INSERT INTO `colour_data`.`brown` (`red_component`, `blue_component`," +
                                " `green_component`) VALUES ('" + str(colour_code[0][0]) + "', '" +
                                str(colour_code[1][0]) + "', '" + str(colour_code[2][0]) + "');")
        elif colour == 3:
            self.cursor.execute("INSERT INTO `colour_data`.`green` (`red_component`, `blue_component`," +
                                " `green_component`) VALUES ('" + str(colour_code[0][0]) + "', '" +
                                str(colour_code[1][0]) + "', '" + str(colour_code[2][0]) + "');")
        elif colour == 4:
            self.cursor.execute("INSERT INTO `colour_data`.`pink` (`red_component`, `blue_component`," +
                                " `green_component`) VALUES ('" + str(colour_code[0][0]) + "', '" +
                                str(colour_code[1][0]) + "', '" + str(colour_code[2][0]) + "');")
        elif colour == 5:
            self.cursor.execute("INSERT INTO `colour_data`.`red` (`red_component`, `blue_component`," +
                                " `green_component`) VALUES ('" + str(colour_code[0][0]) + "', '" +
                                str(colour_code[1][0]) + "', '" + str(colour_code[2][0]) + "');")
        else:
            self.cursor.execute("INSERT INTO `colour_data`.`yellow` (`red_component`, `blue_component`," +
                                " `green_component`) VALUES ('" + str(colour_code[0][0]) + "', '" +
                                str(colour_code[1][0]) + "', '" + str(colour_code[2][0]) + "');")
        self.connection.commit()

    def getcolor(self, colour):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='colour_data',
                                                  user='application',
                                                  password='PyApp@3RGB')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT `red_component`, `blue_component`, `green_component` FROM `colour_data`.`"
                            + colour + "`;")
        return self.cursor.fetchall()

    def writeerror(self, error):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='run_results',
                                                  user='application',
                                                  password='PyApp@3RGB')
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO `run_results`.`errors`(`error`) VALUES('" + str(error) + "');")
        self.connection.commit()

    def write_synaptic_weights(self, rgbcomponent, colour):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='run_results',
                                                  user='application',
                                                  password='PyApp@3RGB')
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO `synaptic_weights`.`" + colour +
                            "` (`red_component`, `blue_component`, `green_component`) VALUES ('" + str(rgbcomponent[0][0])
                            + "', '" + str(rgbcomponent[0][1]) + "', '" + str(rgbcomponent[0][2]) + "');")
        self.connection.commit()

    def write_run_result(self, ColourCount):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='run_results',
                                                  user='application',
                                                  password='PyApp@3RGB')
        self.cursor = self.connection.cursor()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y - %H:%M:%S")
        self.cursor.execute("INSERT INTO `run_results`.`sorting_result` (`datetime`, `blue`, `brown`, `green`, `pink" +
                            "`, `red`, `yellow`, `Total`) VALUES ('" + dt_string + "', '" + str(ColourCount[0]) + "', '"
                            + str(ColourCount[1]) + "', '" + str(ColourCount[2]) + "', '" + str(ColourCount[3]) + "', '"
                            + str(ColourCount[4]) + "', '" + str(ColourCount[5]) + "', '" + str(sum(ColourCount)) +
                            "');")
        self.connection.commit()

    def get_error(self):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='run_results',
                                                  user='application',
                                                  password='PyApp@3RGB')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT `error` FROM `run_results`.`errors`;")
        return self.cursor.fetchall()