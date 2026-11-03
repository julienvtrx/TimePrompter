import time
import sys


def load_timestamps_and_text(timestamps_and_text):
    timestamps_and_text_list = []

    #open and reads the file and closes it to not cause memory leak
    with open(timestamps_and_text, "r", encoding="utf-8") as file:

        for line in file:

            # strips file from useless spaces(also tabs) and \n for lines
            line = line.strip()
            
            # skips empty line or comments
            if not line or line.startswith("#"):
                continue
                
            # separetes timestamps from the text
            parts = line.split(":")
            if len(parts) == 2:
                timestamps = int(parts[0].strip())
                text = parts[1].strip()
                timestamps_and_text_list.append((timestamps, text))

            #error message for the user
            else:
                sys.exit("Formating of timestamps_and_text.txt is not correct")
    return timestamps_and_text_list




def prompter():
    timestamps_and_text = load_timestamps_and_text("timestamps_and_text.txt")

    start_time = time.time()

    last_printed_text = None
    
    while True:
        elapsed_time = time.time() - start_time
        
        # if no timestamps is given for the current time it will show as loading
        current_text = "Loading..." 
        
        # finds the correct text to its timestamp
        for timestamp, text in timestamps_and_text:
            if elapsed_time <= timestamp:
                current_text = text

                # break when found
                break  

        #checks if text is the same, so that it doesnt output the same thing several times
        if current_text != last_printed_text:
            print(current_text)
            #new text is moved into last+printed_text for the next check
            last_printed_text = current_text

        time.sleep(1)






def main():
    prompter()

if __name__ == "__main__":
    main()
