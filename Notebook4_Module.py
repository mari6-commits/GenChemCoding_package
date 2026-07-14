def get_limiting_reactant(equation, grams_comp1, grams_comp2):
  reactants_str, products_str = equation.split('->', 1)
  # Split by '+' and remove leading/trailing spaces
  reactants_list = [r.strip() for r in reactants_str.split('+')]
  products_list = [p.strip() for p in products_str.split('+')]

  all_compounds_with_coeffs = reactants_list + products_list

  compound_formulas = []
  coefficients = []

  # Regex to find coefficient and compound formula
  # It matches an optional number at the beginning, followed by the compound formula
  compound_regex = re.compile(r'^(\d*)\s*(.*)$')

  for full_compound_str in all_compounds_with_coeffs:
      match = compound_regex.match(full_compound_str)
      if match:
          coeff_str, formula = match.groups()
          coefficient = int(coeff_str) if coeff_str else 1 # Default to 1 if no coefficient is given
          coefficients.append(coefficient)
          compound_formulas.append(formula.strip())

  print(f"Original compounds with coefficients: {all_compounds_with_coeffs}")
  print(f"Extracted coefficients: {coefficients}")
  print(f"Extracted compound formulas: {compound_formulas}")

  molecular_weights = {}
  for compound_name in compound_formulas:
    if compound_name:
      parsed_data = chemparse.parse_formula(compound_name)
      molecular_weight = 0.0
      print(f"\nCompound: {compound_name}")
      for el_symbol, count in parsed_data.items():
        element_obj = mendeleev.element(el_symbol)
        atomic_weight = element_obj.atomic_weight
        molecular_weight += atomic_weight * count
        print(f"  Element: {el_symbol}, Count: {count}, Atomic Weight: {atomic_weight}")
      molecular_weights[compound_name] = molecular_weight
      print(f"  Molecular Weight: {molecular_weight:.3f}")

  # Calculate moles for the given grams
  # Assuming grams_comp1 corresponds to the first reactant in compound_formulas
  # and grams_comp2 corresponds to the second reactant
  mols_comp1_input = grams_comp1 / molecular_weights[compound_formulas[0]]
  mols_comp2_input = grams_comp2 / molecular_weights[compound_formulas[1]]

  print(f"\n{grams_comp1} grams of {compound_formulas[0]} is {mols_comp1_input:.3f} moles")
  print(f"{grams_comp2} grams of {compound_formulas[1]} is {mols_comp2_input:.3f} moles")

  # Determine limiting reactant
  # Moles / Coefficient Ratio
  ratio1 = mols_comp1_input / coefficients[0]
  ratio2 = mols_comp2_input / coefficients[1]

  if ratio1 < ratio2:
      limiting_reactant = compound_formulas[0]
      print(f"\nThe limiting reactant is {limiting_reactant}")
  else:
      limiting_reactant = compound_formulas[1]
      print(f"\nThe limiting reactant is {limiting_reactant}")


equation = '2 NH3 + H2SO4 -> (NH4)2SO4'
get_limiting_reactant(equation, 10, 11)


def solve_stoichiometry(equation):
  reactants_str, products_str = equation.split('->', 1)
  all_compounds = [c.strip() for c in equation.replace("->", "+").split("+")]
  
  elements_present = set()
  for compound in all_compounds:
      if compound:
          parsed_data = chemparse.parse_formula(compound)
          elements_present.update(parsed_data.keys())
  
  sorted_elements = sorted(list(elements_present))
  element_to_index = {element: i for i, element in enumerate(sorted_elements)}
  
  compound_coefficient_vectors = []

  for compound_full in all_compounds:
      compound = compound_full.strip()
      if compound:
          parsed_data = chemparse.parse_formula(compound)
          
          # Create a vector for the current compound based on sorted_elements
          coefficient_vector = np.zeros(len(sorted_elements))
          for element, count in parsed_data.items():
              coefficient_vector[element_to_index[element]] = count

          # Check if the compound is a product and apply scaling
          if compound_full.strip() in [c.strip() for c in products_str.split('+')]:
              scaled_vector = coefficient_vector * -1
              compound_coefficient_vectors.append(scaled_vector) 
          else:
              compound_coefficient_vectors.append(coefficient_vector)
          
  large_matrix = np.vstack(compound_coefficient_vectors).T # Transpose to get elements as rows, compounds as columns
  print()
  print(f"Elements in rows (sorted alphabetically): {sorted_elements}")
  print(f"Compounds in columns: {all_compounds}")
  print("Initial large matrix (elements as rows, compounds as columns):")
  print(large_matrix)
  
  rref_matrix = sp.Matrix(large_matrix).rref()[0]
  np_rref = np.array(rref_matrix).astype(np.float64)
  print()
  print("RREF of the large matrix:")
  print(np_rref)

  # Extract the last column (which represents the dependence on the free variable)
  last_col_rref_np = np_rref[:, -1]

  # Construct the vector of coefficients (including the free variable coefficient of 1)
  # The signs are flipped because of the RREF interpretation for Ax = 0 solutions
  stoich_raw_np = np.append(-last_col_rref_np, 1.0)
  
  # Convert to sympy Rational for precise fraction handling
  stoich_raw_sympy = [sp.Rational(x) for x in stoich_raw_np]

  # Get denominators
  denominators = [x.q for x in stoich_raw_sympy] 

  # Calculate LCM of denominators
  scaling_factor = sp.lcm(denominators)

  # Scale the raw coefficients to get integer coefficients
  final_coefficients_sympy = [x * scaling_factor for x in stoich_raw_sympy]
  
  # Convert back to numpy array of integers
  final_coefficients_np = np.array([int(x) for x in final_coefficients_sympy])

  # Reshape to a column vector (Nx1 matrix)
  stoichiometric_matrix = final_coefficients_np.reshape(-1, 1)
  
  print()
  print("Stoichiometric coefficients (scaled to whole numbers):")
  # Create a DataFrame to display compounds next to their coefficients
  balanced_equation_df = pd.DataFrame({
      'Compound': all_compounds,
      'Coefficient': stoichiometric_matrix.flatten()
  })
  display(balanced_equation_df)

solve_stoichiometry('Fe + O2 -> Fe2O3')