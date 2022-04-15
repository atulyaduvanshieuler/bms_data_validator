"""
This module will validate the bms output.
"""


def bms_validation_function(bms_output_list ):

    """This function will take bms_output as string and will parse it 
        and will match it to the expected ouput

    Args:
        bms_output (_str_): bms output as string
    """    
    test_resp = {}
    test_resp["test_errors"]=[]
    
    

    try:
        #CAN_ID = 110
        if float(bms_output_list[52]) < 0 or float(bms_output_list[52]) > 4200:
            error_string = "The value of BMS data Balancing limit is {} should be between 0-4200".format(bms_output_list[5])
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[53]) != 0 and float(bms_output_list[53]) != 1:
            print(bms_output_list[53])
            error_string = "The value of BMS Data Pre Charge Limit is {} should be between 0-1".format(bms_output_list[53])
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[54]) != 0 and float(bms_output_list[54]) != 1:
            print(bms_output_list[54])
            error_string = "The value of BMS Data Balancing Active is {} should be between 0-1".format(bms_output_list[54])
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[3]) < -4294967296 or float(bms_output_list[3]) > 4294967296 :
            error_string = "The value of BMS Data Pack I Master is {} should be between -4294967296-4294967296".format(bms_output_list[3])
            
            test_resp["test_errors"].append(error_string)
            
        #CAN_ID = 111 
        if float(bms_output_list[4]) < 0 or float(bms_output_list[4]) > 100:
            print(bms_output_list[4])
            error_string = "The value of Pack Q SoC Trimmed is {} should be between 0-100".format(bms_output_list[4])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[5]) < float(0) or float(bms_output_list[5]) > float(100):
            error_string = "The value of SOH is {} should be between 0-100".format(bms_output_list[5])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[7]) < 0 or float(bms_output_list[7]) > 4:
            error_string = "The value of BMS Status is {} should be between 0-4".format(bms_output_list[7])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[51]) != float(0) and float(bms_output_list[51]) != float(1):
            error_string = "The value of Fully Charge Flag is {} should be between 0-1".format(bms_output_list[51])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[6]) < 61.5 or float(bms_output_list[6]) > 83:
            error_string = "The value of Pack V Sum of Cells is {} should be between 63-83".format(bms_output_list[6])
            
            test_resp["test_errors"].append(error_string)
            
        #Aux_T temperatures CAN_ID = 112
        if float(bms_output_list[8]) < 0 or float(bms_output_list[8]) > 40:
            error_string = "The value of Aux Temperature_1 is {} should be between 0-40".format(bms_output_list[8])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[9]) < 0 or float(bms_output_list[9]) > 40:
            error_string = "The value of Aux Temperature_2 is {} should be between 0-40".format(bms_output_list[9])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[10]) < 0 or float(bms_output_list[10]) > 40:
            error_string = "The value of Aux Temperature_3 is {} should be between 0-40".format(bms_output_list[10])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[11]) < 0 or float(bms_output_list[11]) > 40:
            error_string = "The value of Aux Temperature_4 is {} should be between 0-40".format(bms_output_list[11])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[12]) < 0 or float(bms_output_list[12]) > 40:
            error_string = "The value of Aux Temperature_5 is {} should be between 0-40".format(bms_output_list[12])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[13]) < 0 or float(bms_output_list[13]) > 40:
            error_string = "The value of Aux Temperature_6 {} should be between 0-40".format(bms_output_list[13])
            
            test_resp["test_errors"].append(error_string)
            

        #CMU1 Cell VOltages CAN_ID = 113
        if float(bms_output_list[15]) < 3100 or float(bms_output_list[15]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_1 is {} should be between 3100-4200".format(bms_output_list[15])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[16]) < 3100 or float(bms_output_list[16]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_2 is {} should be between 3100-4200".format(bms_output_list[16])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[17]) < 3100 or float(bms_output_list[17]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_3 is {} should be between 3100-4200".format(bms_output_list[17])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[18]) < 3100 or float(bms_output_list[18]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_4 is {} should be between 3100-4200".format(bms_output_list[18])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[19]) < 3100 or float(bms_output_list[19]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_5 is {} should be between 3100-4200".format(bms_output_list[19])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[20]) < 3100 or float(bms_output_list[20]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_6 is {} should be between 3100-4200".format(bms_output_list[20])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[21]) < 3100 or float(bms_output_list[21]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_7 is {} should be between 3100-4200".format(bms_output_list[21])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[22]) < 3100 or float(bms_output_list[22]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_8 is {} should be between 3100-4200".format(bms_output_list[22])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[23]) < 3100 or float(bms_output_list[23]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_9 is {} should be between 3100-4200".format(bms_output_list[23])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[24]) < 3100 or float(bms_output_list[24]) > 4200:
            error_string = "The value of CMU1 Cell Voltage_10 is {} should be between 3100-4200".format(bms_output_list[24])
            
            test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[25]) < 3100 or float(bms_output_list[25]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_11 is {} should be between 3100-4200".format(bms_output_list[25])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[26]) < 3100 or float(bms_output_list[26]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_12 is {} should be between 3100-4200".format(bms_output_list[26])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[27]) < 3100 or float(bms_output_list[27]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_13 is {} should be between 3100-4200".format(bms_output_list[27])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[28]) < 3100 or float(bms_output_list[28]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_14 is {} should be between 3100-4200".format(bms_output_list[28])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[29]) < 3100 or float(bms_output_list[29]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_15 is {} should be between 3100-4200".format(bms_output_list[29])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[30]) < 3100 or float(bms_output_list[30]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_16 is {} should be between 3100-4200".format(bms_output_list[30])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[31]) < 3100 or float(bms_output_list[31]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_17 is {} should be between 3100-4200".format(bms_output_list[31])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[32]) < 3100 or float(bms_output_list[32]) > 4200:
        #     error_string = "The value of CMU1 Cell Voltage_18 is {} should be between 3100-4200".format(bms_output_list[32])
            
        #     test_resp["test_errors"].append(error_string)
            

        
        #CMU2 Cell VOltages CAN_ID = 114
        if float(bms_output_list[33]) < 3100 or float(bms_output_list[33]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_1 is {} should be between 3100-4200".format(bms_output_list[33])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[34]) < 3100 or float(bms_output_list[34]) > 4200:
            error_string = "The value of 310CMU2 Cell Voltages_2 is {} should be between 3100-4200".format(bms_output_list[34])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[35]) < 3100 or float(bms_output_list[35]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_3 is {} should be between 3100-4200".format(bms_output_list[35])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[36]) < 3100 or float(bms_output_list[36]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_4 is {} should be between 3100-4200".format(bms_output_list[36])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[37]) < 3100 or float(bms_output_list[37]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_5 is {} should be between 3100-4200".format(bms_output_list[37])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[38]) < 3100 or float(bms_output_list[38]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_6 is {} should be between 3100-4200".format(bms_output_list[38])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[39]) < 3100 or float(bms_output_list[39]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_7 is {} should be between 3100-4200".format(bms_output_list[39])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[40]) < 3100 or float(bms_output_list[40]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_8 is {} should be between 3100-4200".format(bms_output_list[40])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[41]) < 3100 or float(bms_output_list[41]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_9 is {} should be between 3100-4200".format(bms_output_list[41])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[42]) < 3100 or float(bms_output_list[42]) > 4200:
            error_string = "The value of CMU2 Cell Voltages_10 is {} should be between 3100-4200".format(bms_output_list[42])
            
            test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[43]) < 3100 or float(bms_output_list[43]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_11 is {} should be between 3100-4200".format(bms_output_list[43])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[44]) < 3100 or float(bms_output_list[44]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_12 is {} should be between 3100-4200".format(bms_output_list[44])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[45]) < 3100 or float(bms_output_list[45]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_13 is {} should be between 3100-4200".format(bms_output_list[45])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[46]) < 3100 or float(bms_output_list[46]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_14 is {} should be between 3100-4200".format(bms_output_list[46])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[47]) < 3100 or float(bms_output_list[47]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_15 is {} should be between 3100-4200".format(bms_output_list[47])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[48]) < 3100 or float(bms_output_list[48]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_16 is {} should be between 3100-4200".format(bms_output_list[48])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[49]) < 3100 or float(bms_output_list[49]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_17 is {} should be between 3100-4200".format(bms_output_list[49])
            
        #     test_resp["test_errors"].append(error_string)
            
        # if float(bms_output_list[50]) < 3100 or float(bms_output_list[50]) > 4200:
        #     error_string = "The value of CMU2 Cell Voltages_18 is {} should be between 3100-4200".format(bms_output_list[50])
            
        #     test_resp["test_errors"].append(error_string)
            
        
        #CAN_ID = 12A DYNAMIC_LIMITS
        if float(bms_output_list[60]) < 0 or float(bms_output_list[60]) > 200:
            error_string = "The value of Dynamic In Limit is {} should be between 0-200".format(bms_output_list[60])
            
            test_resp["test_errors"].append(error_string)
            
        if float(bms_output_list[61]) < 0 or float(bms_output_list[61]) > 250:
            error_string = "The value of Dynamic Out Limit is {} should be between 0-250".format(bms_output_list[61])
            
            test_resp["test_errors"].append(error_string)
            

        #CAN_ID = 11C  TODO: need to decide indices here , haven't been added in the output by dharmanshu
        # if float(bms_output_list[60]) < 0 or float(bms_output_list[60]) > 200:
        #     error_string = "The value of Dynamic In Limit is {}".format(bms_output_list[60])
        #     
        #     test_resp["test_errors"].append(error_string)
        #     
        # if float(bms_output_list[61]) < 0 or float(bms_output_list[61]) > 200:
        #     error_string = "The value of Dynamic Out Limit is {}".format(bms_output_list[61])
        #     
        #     test_resp["test_errors"].append(error_string)
        #     
        # if float(bms_output_list[60]) < 0 or float(bms_output_list[60]) > 200:
        #     error_string = "The value of Dynamic In Limit is {}".format(bms_output_list[60])
        #     
        #     test_resp["test_errors"].append(error_string)
        #     
        # if float(bms_output_list[61]) < 0 or float(bms_output_list[61]) > 200:
        #     error_string = "The value of Dynamic Out Limit is {}".format(bms_output_list[61])
        #     
        #     test_resp["test_errors"].append(error_string)
        #     
        
        return test_resp["test_errors"]

    except Exception as e:
        print(e)
        return False





