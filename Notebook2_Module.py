def create_bohr_model(atom):
  try:
    atom = element(atom)
  except Exception as e:
    print(f"Error: {e}")
    return
  num_proton = atom.atomic_number
  fig, ax = plt.subplots()

  ax.set_axis_off()
  ax.set_xlim(-3.1,3.1)
  ax.set_ylim(-3.1,3.1)
  ax.autoscale(False)
  ax.set_aspect('equal')

  fp = fm.FontProperties(size='20') # Atomic symbol size
  t = txt.Text(text=atom.symbol, fontproperties=fp, verticalalignment='center', horizontalalignment='center', bbox = dict( visible=False, color='grey')) # Atomic symbol code
  ax.add_artist(t)

  coord_list = [ (0,-1),(0,1),(1,0),(-1,0),(.707,.707),(-.707,.707),(-.707,-.707),(.707,-.707),(.5,.866),(-.5,-.866),
  (-.5,.866),(.5,-.866),(.866,.5),(-.866,.5),(.866,-.5),(-.866,-.5),(.966,-.259),(-.966,.259)]
  coord_list_2 = [tuple(item * 1.5 for item in t) for t in coord_list]
  coord_list_3 = [tuple(item * 2 for item in t) for t in coord_list]
  coord_list_4 = [tuple(item * 2.5 for item in t) for t in coord_list]

  #if num_proton > 20:
    #print("Error: Element is out of range (atomic number must be 1-20).")
    #return
  if num_proton > 0 :
    circle = Circle((0, 0), radius=0.5, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton, 2)):
      circle = Circle((0,-.5 +  i ), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 2:
    circle = Circle((0, 0), radius=1, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-2, 8)):
      circle = Circle(((coord_list[i])), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 10:
    circle = Circle((0, 0), radius=1.5, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-10, 8)):
      circle = Circle(((coord_list_2[i])), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 18:
    circle = Circle((0, 0), radius=2, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-18, 2)):
      circle = Circle((0,-2 + i*4 ), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 20:
    for i in range(min(num_proton-20,10)):
      circle = Circle(((coord_list_2[i+8])), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 30:
    for i in range(min(num_proton-30,6)):
      circle = Circle(((coord_list_3[i+2])), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 36:
    circle = Circle((0, 0), radius=2.5, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-36,2)):
      circle = Circle((0,-2.5 + i*5 ), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 38:
    for i in range(min(num_proton-38,10)):
      circle = Circle(((coord_list_3[i+8])), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 48:
    for i in range(min(num_proton-48,6)):
      circle = Circle(((coord_list_4[i+2])), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)
  if num_proton > 54:
    circle = Circle((0, 0), radius=3, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-54,2)):
      circle = Circle((0,-3 + i*6 ), radius=0.04, fill=True, color='blue')
      ax.add_patch(circle)

  plt.show()
atom = 'Cs'#@param
create_bohr_model(atom)


def determine_functional_group(smiles):
  found_groups = []
  for string, group_name in functional_group_dict.items():
    if string in smiles:
      found_groups.append(group_name)
  if found_groups:
    return found_groups
  else:
    return 'No functional groups detected'
  # Corrected by Gemini


def create_atomic_model(atom):
  try:
    atom = element(atom)
  except Exception as e:
    print(f"Error: {e}")
    return
  num_proton = atom.atomic_number
  num_neutron = round(atom.atomic_weight - atom.atomic_number) # check accuracy here**
  atom.atomic_number = num_proton

  fig, ax = plt.subplots()

  ax.set_axis_off()
  ax.set_xlim(-2.5,2.2)
  ax.set_ylim(-2.5,2.5)
  ax.autoscale(False)
  ax.set_aspect('equal')

  coord_list = [ (0,1),(1,0),(0,-1),(-1,0),(.707,.707),(-.707,.707),(-.707,-.707),(.707,-.707)]
  coord_list_2 = [tuple(item * 1.5 for item in t) for t in coord_list]

  #proton_coords = [(0,.025),(0,-.025),(0,0),]
  #neutron_coords = [(-.025,0),(.025,0),(.035,.025),(-.035,-.075)]

  proton_coords = [(0,.05),(0,-.045),(.085,.015),(-.09,.005),(-.1,.09),(-.01,.14),(.08,.1),(-.11,.19),(-.025,.24),(.075,.2),(.11,-.09),(.17,-.03),(.16,.08),(.05,.285),(-.11,.275),(-.18,.13),
  (-.085,-.1),(.2,-.12),(-.17,-.075),(-.2,.22)]
  neutron_coords = [(-.035,0),(.035,0),(.05,.05),(-.06,.05),(-.045,.1),(.025,.1),(-.08,.15),(-.05,.19),(.05,.15),(.018,.19),(.07,-.05),(.12,-.035),(.11,.065),(.03,.24),(-.08,.24),(-.13,.13),
  (-.065,-.055),(.16,-.08),(-.17,.18),(-.12,-.055),(-.15,-.01),(.1,.25)]

  if num_proton > 20:
    print("Error: Element is out of range (atomic number must be 1-20).")
    return
  for i in range(num_proton):
    #circle = Circle((random.uniform(-.35, .35), random.uniform(-.35, .35)), radius=0.03, fill=True, edgecolor='purple',  alpha = 0.75 ,  )
    #ax.add_patch(circle)
    circle = Circle((proton_coords[i]), radius=0.03, fill=True, facecolor='red', edgecolor = 'black', alpha = .75)
    ax.add_patch(circle)

  for i in range(num_neutron):
    #circle = Circle((random.uniform(-.35, .35), random.uniform(-.35, .35)), radius=0.03, fill=True, edgecolor='blue', alpha = 0.5)
    #ax.add_patch(circle)
    circle = Circle((neutron_coords[i]), radius=0.03, fill=True, facecolor='blue', edgecolor = 'black', alpha = .75)
    ax.add_patch(circle)

  if num_proton > 0 :
    circle = Circle((0, 0), radius=0.5, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton, 2)):
      circle = Circle((0,-.5 +  i ), radius=0.04, fill=True, color='green')
      ax.add_patch(circle)
  if num_proton > 2:
    circle = Circle((0, 0), radius=1, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-2, 8)):
      circle = Circle(((coord_list[i])), radius=0.04, fill=True, color='green')
      ax.add_patch(circle)
  if num_proton > 10:
    circle = Circle((0, 0), radius=1.5, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-10, 8)):
      circle = Circle(((coord_list_2[i])), radius=0.04, fill=True, color='green')
      ax.add_patch(circle)
  if num_proton > 18:
    circle = Circle((0, 0), radius=2, fill=False, color='black')
    ax.add_patch(circle)
    for i in range(min(num_proton-18, 2)):
      circle = Circle((0,-2 + i*4 ), radius=0.04, fill=True, color='green')
      ax.add_patch(circle)

  plt.show()
atom = 'Ar'
create_atomic_model(atom)