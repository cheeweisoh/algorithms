#!/usr/bin/env python3

from pathlib import Path
import re

words_to_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def getCalibrationValues(calibration_doc):
    ans = 0
    
    for i in calibration_doc:
        digits = []
        for j in range(len(i)):
            if i[j].isdigit():
                digits.append(i[j])
            else:
                for k in range(j+1, len(i)+1):
                    word = i[j:k]
                    if word in words_to_digits.keys():
                        digits.append(words_to_digits[word])
        
        ans += int(digits[0] + digits[-1])
        
    return ans

def main():
    here = Path(__file__).parent
    with open(here/'test02.txt') as file:
        test_values = [i for i in file]
    
    print(f'Test Answer: {getCalibrationValues(test_values)}')
    
    with open(here/'calibration_document.txt') as file:
        calibration_values = [i for i in file]
    
    print(f'Final Answer: {getCalibrationValues(calibration_values)}')
    
    return

if __name__ == '__main__':
    main()