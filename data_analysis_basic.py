import json
from dateutil import parser


"""
More info at the end
God knows how this shit works
"""

class Unit():
   def __init__ (self,unit_name):
      self.unit_name = unit_name  # unit name -> obtained from json file
      self.test_results = list()  # [(date,result),(date,result)]
      self.status = False

def read_json_files(json_list):
   # json_list = list of json file names
   unit_list = list()
   # unit_list = list of Unit objects
   for json_file in json_list:
      with open(json_file,"r") as j_file:
         j_data = json.load(j_file)
         unit_name = j_data['test_report']['head']['product']['-name']
         unit = Unit(unit_name)
         for unit_obj in unit_list:
            if unit_obj.unit_name == unit_name: # in case current unit is in the unit_list 
               unit = unit_obj
               break
   
         test_result = j_data['test_report']['head']['result']['-value']
         test_time = j_data['test_report']['head']['timestamp']['-value']
         unit.test_results.append((test_time,test_result))

         if unit not in unit_list:
            unit_list.append(unit)
   return unit_list

def comp_prod_test(start_date,end_date,unit_list):
   # compares list of units 
   # returns dictionary {Unit obj. : num. of tests if provided time frame, ...}

   prod_test_count = {}
   start_date = parser.parse(start_date)
   end_date = parser.parse(end_date)
   for product in unit_list:
      test_count = 0
      for date in product.test_results:
         local_date = parser.parse(date[0])
         if local_date >= start_date and local_date <= end_date:
            test_count += 1
      prod_test_count[product] = test_count
   return prod_test_count



def error_rate(start_date = 'YY-MM-DD HH:MM:SS',end_date = 'YY-MM-DD HH:MM:SS',unit_test_results = list):
   # returns None if no testes were concluded in provided time period
   # return tuple (passed tests, failed tests)

   start_date = parser.parse(start_date)
   end_date = parser.parse(end_date)
   fail_count = pass_count = 0
   for date in unit_test_results:
      local_date = parser.parse(date[0])
      if local_date >= start_date and local_date <= end_date:
         if date[1] == 'PASS': pass_count += 1
         else: fail_count += 1

   else: return (pass_count,fail_count)

if __name__ in "__main__":
   # Date format example'2020-02-10 14:38:12.0'
   t_time = '2020-02-10 14:38:12.0' # start of time period
   e_time = '2023-02-10 14:38:12.0' # end  of time perdiod
   j_list = ['data.json','data2.json','data3.json']
   unit_list = read_json_files(j_list) # list of unit objects
   res = comp_prod_test(t_time,e_time,unit_list)
   print(res)
   exit()
   for ele in res:
      print(ele.unit_name,res[ele])
   print()
   for unit in unit_list:
      print(unit.unit_name,error_rate(t_time,e_time,unit.test_results))
   