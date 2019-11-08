import argparse
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def GetArgs():
   """
   Supports the command-line arguments listed below.
   """
   parser = argparse.ArgumentParser(
       description='Process args for report options')
   parser.add_argument('-t', '--type', required=True, action='store',
                       help='Type of the report, allowed types for example: cpu, hdd, ram, swp')
   parser.add_argument('-f', '--file', required=True, action='store',
                       help='Filename of the *.csv data file')
   
   args = parser.parse_args()
   return args

def main():
   """
   Simple command-line program for generating resource graphs from data files.
   """

   args = GetArgs()

   #data = pd.read_csv('./' + args.file)
   data = pd.read_csv(args.file)
    
   filename = args.file[:-3] + 'png'

   data['date_time'] = pd.to_datetime(data.date_time, format='%d/%m/%Y %H:%M:%S')
   time = data.date_time.sort_values()

   if args.type == "cpu":
      cpu = data.value
      cpu_max = data.value.max()
      cpu_avg = data.value.mean()

      print(cpu_max)
      print(cpu_avg)

      title_font = {'fontname':'Arial', 'size':'18', 'color':'black', 'weight':'normal', 'verticalalignment':'bottom'}
      axis_font = {'fontname':'Arial', 'size':'16'}
      #ax1.plot(x,y, c='r', label='the data')
      plt.figure(figsize=(15, 5))
      plt.subplots_adjust(hspace=0.2, wspace=0.2, bottom=0.12, left=0.05, top=0.90, right=0.98)
      plt.plot(time, cpu, color='b', label='CPU utilizace v %')
      #plt.gcf().autofmt_xdate()
      plt.title("CPU utilizace v %", **title_font)    
      plt.xlabel('datum', **axis_font)
      plt.ylabel('CPU %', **axis_font)

      plt.savefig(filename)

   elif args.type == "ram":
      ram = data.value
      ram_max = data.value.max()
      ram_avg = data.value.mean()

      print(ram_max)
      print(ram_avg)

      title_font = {'fontname':'Arial', 'size':'12', 'color':'black', 'weight':'normal', 'verticalalignment':'bottom'}
      axis_font = {'fontname':'Arial', 'size':'10'}
      plt.figure(figsize=(7.5, 2.5))
      plt.subplots_adjust(hspace=0.2, wspace=0.2, bottom=0.18, left=0.09, top=0.88, right=0.98)
      plt.ylim([0,100])
      plt.plot(time, ram, color='g', label='RAM utilizace v %')
      #plt.gcf().autofmt_xdate()
      plt.title("RAM utilizace v %", **title_font)    
      plt.xlabel('datum', **axis_font)
      plt.ylabel('RAM %', **axis_font)

      plt.savefig(filename)

   elif args.type == "hdd":
      hdd = data.value
      hdd_max = data.value.max()
      hdd_avg = data.value.mean()

      print(hdd_max)
      print(hdd_avg)

      title_font = {'fontname':'Arial', 'size':'12', 'color':'black', 'weight':'normal', 'verticalalignment':'bottom'}
      axis_font = {'fontname':'Arial', 'size':'10'}
      plt.figure(figsize=(7.5, 2.5))
      plt.subplots_adjust(hspace=0.2, wspace=0.2, bottom=0.18, left=0.09, top=0.88, right=0.98)
      plt.ylim([0,500000])
      plt.plot(time, hdd, color='sienna', label='HDD utilizace v KB/s')
      #plt.gcf().autofmt_xdate()
      plt.title("HDD utilizace v KB/s", **title_font)    
      plt.xlabel('datum', **axis_font)
      plt.ylabel('HDD KB/s', **axis_font)

      plt.savefig(filename)

   elif args.type == "swp":
      swp = data.value
      swp_max = data.value.max()
      swp_avg = data.value.mean()

      print(swp_max)
      print(swp_avg)

      title_font = {'fontname':'Arial', 'size':'12', 'color':'black', 'weight':'normal', 'verticalalignment':'bottom'}
      axis_font = {'fontname':'Arial', 'size':'10'}
      plt.figure(figsize=(7.5, 2.5))
      plt.subplots_adjust(hspace=0.2, wspace=0.2, bottom=0.18, left=0.09, top=0.88, right=0.98)
      plt.ylim([0,500])
      plt.plot(time, swp, color='r', label='SWAP utilizace v KB/s')
      #plt.gcf().autofmt_xdate()
      plt.title("SWAP utilizace v KB/s", **title_font)    
      plt.xlabel('datum', **axis_font)
      plt.ylabel('SWP KB/s', **axis_font)

      plt.savefig(filename)

   else:
      print('You must specify the correct type of the report: cpu, mem, hdd, swp supported')

# Start program
if __name__ == "__main__":
   main()