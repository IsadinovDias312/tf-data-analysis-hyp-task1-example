import pandas as pd
import numpy as np

chat_id = 1182463770
def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    tmp = ((x_success+y_success) * y_cnt)/(x_cnt+y_cnt)    
    sqr = (y_success - tmp)**2/tmp
    if sqr < 3.5:
      return False
    else:
      return True
