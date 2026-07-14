def convert_to_k(temp, unit):
  if unit == 'C':
    temp_k = temp + 273.15
  elif unit == 'F':
    temp_k = (temp - 32) * 5/9 + 273.15
  temp_k = round(temp_k, 2)
  return temp_k


def ideal_gas_constant(volume_unit, pressure_unit):
  if volume_unit == 'c^3' or pressure_unit == 'kPa':
    return 8.3145
  elif volume_unit == 'L':
    if pressure_unit == 'atm':
      return 0.08206
    else:
      return 62.363


def ideal_gas_law(unknown='', P=0, V=0, n=0, R=0, T=0):
  match unknown:
    case 'P':
      return n*R*T/V
    case 'V':
      return n*R*T/P
    case 'n':
      return P*V/(R*T)
    case 'R':
      return P*V/(n*T)
    case 'T':
      return P*V/(n*R)
    case _:
      return 'Invalid input'