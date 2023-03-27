# 63102230 Chitsanupong Paenyoi
'''
  ot ชั่วโมงละ 60
  แต่ทำได้ไม่เกิน 3
  ot วันนึงได้ไม่เกิน 180

  และหากในเดือนนึงไม่มาสายเลยจะได้เพิ่มเดือนละ 1000

  input => จำนวนวันทำงาน, จำนวน ot รวม, จำนวนวันมาสาย
  output => ค่าตอบแทนรายเดือน
'''

def validate_input(working_day, total_ot, late_day):
  # if total ot more than working hour
  if working_day > 31 or working_day < 0:
    return "invalid day"
  elif total_ot < 0:
    return "invalid total ot"
  elif late_day < 0 or late_day > 31:
    return "invalid late day"
  elif total_ot > working_day * 3:
    return "number of OTs above threshold per day"
  elif working_day == 0 and total_ot == 0:
    return "invalid all inputs"
  else:
    return True

def calculate_salary(working_day, total_ot, late_day):
  # validate input
  validated = validate_input(working_day, total_ot, late_day)
  if type(validated) is not str:
    PAYMENT = 340
    normal_paymeny = PAYMENT * working_day
    sum_ot = total_ot * 60
    if late_day == 0 and working_day >= 30:
      return normal_paymeny + sum_ot + 1000
    else:
      return normal_paymeny + sum_ot
  else:
    return validated