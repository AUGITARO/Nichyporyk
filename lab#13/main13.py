# -*- coding: cp1251 -*-
import re
def replace_time_with_tbd(text):
    time_pattern = r'\b(2[0-3]|[01]?[0-9]):([0-5][0-9])(:([0-5][0-9]))?\b'
    result = re.sub(time_pattern, '(TBD)', text)
    return result
input_text = "Встреча в 14:30, а потом в 16:45:30. Не забудьте о встрече в 09:00."
output_text = replace_time_with_tbd(input_text)
print(output_text)