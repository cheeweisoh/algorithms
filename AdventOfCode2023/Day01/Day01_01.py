#!/usr/bin/env python3

from pathlib import Path
import re

def getCalibrationValues(calibration_doc):
    ans = 0
    
    for i in calibration_doc:
        digits = [l for l in i if l.isdigit()]
        ans += int(digits[0] + digits[-1])        
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test01.txt') as file:
        test_values = [i for i in file]
    
    print(f"Test Answer: {getCalibrationValues(test_values)}")
    
    with open(here/'calibration_document.txt') as file:
        calibration_values = [i for i in file]
    
    print(f"Final Answer: {getCalibrationValues(calibration_values)}")
    
    return

if __name__ == "__main__":
    main()