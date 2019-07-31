import numpy
import math
import random
import sys


class MakeScaleFreePlugin:
   def input(self, filename):
      myfile = open(filename, 'r')
      self.N = int(myfile.readline())

   def run(self):
      self.DG = networkx.scale_free_graph(self.N)

   def output(self, filename):
      networkx.write_gml(self.DG, filename)

class TriadCounterPlugin:
   def input(self, filename):
      ###########################################################
      # Read the file
      # Put results in filestuff
      filestuff = open(filename, 'r')
      firstline = filestuff.readline()
      bacteria = firstline.split(',')
      if ('\"\"' in bacteria):
         bacteria.remove('\"\"')
      self.n = len(bacteria)
      inf = float("infinity")
      ###########################################################
     
      ###########################################################
      # Populate the adjacency matrix, self.ADJ
      self.ADJ = []
      for line in filestuff:
        self.ADJC = []
        contents = line.split(',')
        for i in range(1, self.n+1):
           value = float(contents[i])
           self.ADJC.append(value)
        self.ADJ.append(self.ADJC)
     
      # Check to make sure all entries (i, i) are 0
      for i in range(self.n):
        self.ADJ[i][i] = 0
      ##########################################################

   def run(self):
      self.threegreen = 0
      self.twogreen = 0
      self.onegreen = 0
      self.zerogreen = 0
     
      # Remove edges that are 'redundant' (triangles)
      for i in range(self.n):
        for j in range(i+1, self.n):
           for k in range(j+1, self.n):
              # All green triangle
              if (self.ADJ[i][j] > 0 and self.ADJ[i][k] > 0 and self.ADJ[j][k] > 0):
                 self.threegreen += 1
              # Two (but not three) are green
              if (self.ADJ[i][j] > 0 and self.ADJ[i][k] > 0 and self.ADJ[j][k] < 0):
                 self.twogreen += 1
              elif (self.ADJ[i][k] > 0 and self.ADJ[j][k] > 0 and self.ADJ[i][j] < 0):
                 self.twogreen += 1
              elif (self.ADJ[j][k] > 0 and self.ADJ[i][j] > 0 and self.ADJ[i][k] < 0):
                 self.twogreen += 1
              # Two (but not three) are red
              if (self.ADJ[i][j] < 0 and self.ADJ[i][k] < 0 and self.ADJ[j][k] > 0):
                 self.onegreen += 1
              elif (self.ADJ[i][k] < 0 and self.ADJ[j][k] < 0 and self.ADJ[i][j] > 0):
                 self.onegreen += 1
              elif (self.ADJ[j][k] < 0 and self.ADJ[i][j] < 0 and self.ADJ[i][k] > 0):
                 self.onegreen += 1
      	      # All three are red
              if (self.ADJ[i][j] < 0 and self.ADJ[i][k] < 0 and self.ADJ[j][k] < 0):
                 self.zerogreen += 1

   def output(self, filename):
      # Display the counts
      print("*********************************************")
      print("Stable triads:" , self.threegreen+self.onegreen)
      print("Unstable triads: ", self.twogreen+self.zerogreen)
      print()
      print("Counts of green triads:")
      print("3: ", self.threegreen)
      print("2: ", self.twogreen)
      print("1: ", self.onegreen)
      print("0: ", self.zerogreen)
      print("********************************************")


