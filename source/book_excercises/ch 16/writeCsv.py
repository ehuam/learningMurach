#! /usr/bin/env python3

#Write a 3-D list [Title, Price, Discount]
import csv

dvds = [
            ['Die Hard', 4.75, 30],
            ['Read Player One', 8.97, 20],
            ['Inception', 6.50, 15],            
         ]

with open("products.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dvds)