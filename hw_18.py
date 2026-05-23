from datetime import datetime
from pathlib import Path

filename = Path(__file__).parent / "hblog"
log_output = Path(__file__).parent / "hb_test.log"  

history = {}


with open(filename, mode="r", encoding="utf-8") as f, open(log_output, mode="w", encoding="utf-8") as out_f:
    for line in f:
        words = line.split()
        
        time_str = words[10]
        key_val = words[12]
        
        current_time = datetime.strptime(time_str, "%H:%M:%S")
        
        if key_val in history:
            previous_time = history[key_val]
            delta_seconds = (previous_time - current_time).total_seconds()
            
            
            if 31 < delta_seconds <= 33:
                
                out_f.write(f"WARNING: Процес {key_val} має затримку {delta_seconds} сек.\n")
                
            elif delta_seconds > 33:
                out_f.write(f"ERROR: Процес {key_val} має затримку {delta_seconds} сек.\n")
                
        history[key_val] = current_time

print("Аналіз завершено! Перевір файл hb_test.log.")