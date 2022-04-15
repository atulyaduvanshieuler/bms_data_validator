import csv
import pickle
import json
from bms_validator import bms_validation_function

bms_output_list = [1]*62
count=0
csv_files_list = ['1868_BMS_258_12_02Mar22.csv', '0011210516TTN_BMS Log_020322.csv','1871_BMS_258_12_02Mar22.csv' ]
all_errors=[]
for file in csv_files_list:
    errors_map={}
    count=0
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter = ",")
        for index,row in enumerate(reader):
            if index==1 or index==0:
                continue
            if row[1]=="LOSS OF SIGNAL":
                continue
            try:
                bms_output_list[8] = float(row[12])
                bms_output_list[9] = float(row[13])
                bms_output_list[10] = float(row[14])
                bms_output_list[11] = float(row[15])
                bms_output_list[12] = float(row[16])
                
                bms_output_list[13] = float(row[17])
                bms_output_list[60] = float(row[20])
                bms_output_list[61] = float(row[21])
                
                if row[28]!="2000 - SYS_LIM_CELL_V_MIN" and row[28]!="2009 - SYS_LIM_PACK_I_OUT":
                    
                    bms_output_list[15] = float(row[35])
                    bms_output_list[16] = float(row[36])

                    bms_output_list[17] = float(row[37])
                    bms_output_list[18] = float(row[38])
                    bms_output_list[19] = float(row[39])
                    bms_output_list[20] = float(row[40])
                    bms_output_list[21] = float(row[41])

                    bms_output_list[22] = float(row[42])
                    bms_output_list[23] = float(row[43])
                    bms_output_list[24] = float(row[44])
                    

                    bms_output_list[33] = float(row[53])
                    bms_output_list[34] = float(row[54])
                    bms_output_list[35] = float(row[55])
                    bms_output_list[36] = float(row[56])
                    bms_output_list[37] = float(row[57])

                    bms_output_list[38] = float(row[58])
                    bms_output_list[39] = float(row[59])
                    bms_output_list[40] = float(row[60])
                    bms_output_list[41] = float(row[61])
                    bms_output_list[42] = float(row[62])

                    bms_output_list[43] = float(row[63])
                    bms_output_list[44] = float(row[64])
                else:
                    
                    bms_output_list[15] = float(3200)
                    bms_output_list[16] = float(3200)

                    bms_output_list[17] = float(3200)
                    bms_output_list[18] = float(3200)
                    bms_output_list[19] = float(3200)
                    bms_output_list[20] = float(3200)
                    bms_output_list[21] = float(3200)

                    bms_output_list[22] = float(3200)
                    bms_output_list[23] = float(3200)
                    bms_output_list[24] = float(3200)

                    bms_output_list[33] = float(3200)
                    bms_output_list[34] = float(3200)
                    bms_output_list[35] = float(3200)
                    bms_output_list[36] = float(3200)
                    bms_output_list[37] = float(3200)

                    bms_output_list[38] = float(3200)
                    bms_output_list[39] = float(3200)
                    bms_output_list[40] = float(3200)
                    bms_output_list[41] = float(3200)
                    bms_output_list[42] = float(3200)


                bms_output_list[52] = float(row[75])
                bms_output_list[54] = float(row[76])
                bms_output_list[5] = float(row[77])

                bms_output_list[4] = float(row[79])
                bms_output_list[6] = float(row[6])
                if row[23]=="FALSE":
                    bms_output_list[51] = float(0)
                elif row[23]=="TRUE":
                    bms_output_list[51]=float(1)


                res = bms_validation_function(bms_output_list)
                if res!=[]:
                    errors_map[index]=[file,res]

            except Exception as e:
                count+=1
                print(e)
                print(row)
    #print(count)        

            #print(index,bms_validation_function(bms_output_list))
    all_errors.append(errors_map)

with open("validation_errors.txt","w") as error_file:
    for index,file_errors in enumerate(all_errors):
        error_file.write(csv_files_list[index])
        error_file.write("\n")
        for line_errors in file_errors.keys():
            error_file.write("   ")
            error_file.write(json.dumps(line_errors))
            error_file.write("   ")
            error_file.write(json.dumps(file_errors[line_errors]))
            error_file.write("\n")

       



    #error_file.write(all_errors)
#
# print(all_errors)

        
#['The value of BMS Data Pre Charge Limit is 1 should be between 0-1', 'The value of BMS Data Balancing Active is 1.0 should be between 0-1', 'The value of SOH is 100.0 should be between 0-100', 'The value of Fully Charge Flag is 0.0 should be between 0-1']