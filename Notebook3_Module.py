def create_bohr_model():
  atom = mendeleev.element(random.randint(1,56))
  rand_ion = random.randint(-1,1)
  num_proton = atom.atomic_number + rand_ion
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

  if num_proton > 56:
    print("Error: Element is out of range (atomic number must be 1-56).")
    return
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
  if rand_ion != 0:
    print("This is an ion")
    print("It has",rand_ion,"extra electrons")
  else:
    print("This is not an ion")
  plt.show()


def determine_ion():
  atom = mendeleev.element(random.randint(1,56))
  rand_ion = random.randint(-1,1)
  num_proton = atom.atomic_number + rand_ion
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

  if num_proton > 56:
    print("Error: Element is out of range (atomic number must be 1-56).")
    return
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
  #if rand_ion != 0:
    #print("This is an ion")
    #print("It has",rand_ion,"extra electrons")
  #else:
    #print("This is not an ion")
  plt.show()

determine_ion()

