import util
import sys, getopt

data = util.get_data()

def port_by_state(state):
  return [(data[element]['Port Code'], data[element]['Port Name'], data[element]['State']) for element in data if data[element]['State'] == state]

def port_by_name(pname):
  return [(data[element]['Port Code'], data[element]['Port Name'], data[element]['State']) for element in data if data[element]['Port Name'] == pname]


if __name__ == '__main__':
  argvs = sys.argv[1:]
  np = []
  sp = []
  
  try:
    opts, args = getopt.getopt(argvs, "n:s:")
  except:
    print("Error")

  for opt, arg in opts:
    if opt in ['-s']:
      sp = port_by_state(arg) 
    elif opt in ['-n']:
      np = port_by_name(arg)

  if sp != [] and np != []:
    for i in list(set(sp) & set(np)):
      print(f"{i[0]} : {i[1]}, {i[2]}")
  elif sp != []:
    for i in sp:
      print(f"{i[0]} : {i[1]}, {i[2]}")
  elif np != []:
    for i in np:
      print(f"{i[0]} : {i[1]}, {i[2]}")
